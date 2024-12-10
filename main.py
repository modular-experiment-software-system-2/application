
from datetime import datetime
import os
import sys
from typing import List
import yaml

from modules.common import *
from modules.settings import Settings
from modules.device import (
    Device,
    WorkerDevicesROS2LocalStart,
    WorkerDevicesROS2LocalStop,
    WorkerDevicesSSHConnect,
    WorkerDevicesSSHDisconnect,
    WorkerDevicesROS2RemoteStart,
    WorkerDevicesROS2RemoteStop,
    WorkerDeviceUi,
    WorkerROS2Ui,

)
from modules.ui import Ui_MainWindow
from modules.other.ui_tileDiagnosticsPage import Ui_tileDiagnosticsPage
from widgets import custom_grips as Ui_Grips
os.environ["QT_FONT_DPI"] = "96"

GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True
WIDGETS = None


class MainWindow(QMainWindow):
    """
    
    """
    def __init__(self):
        """
        """
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global WIDGETS
        WIDGETS = self.ui

        # SETTINGS
        title = "mess2"
        description = "Modular Experiment Software System 2"
        version = "v0.2.2"
        self.setWindowTitle(title)
        WIDGETS.titleRightInfo.setText(description)
        WIDGETS.version.setText(version)

        Ui_Functions.uiDefinitions(self)

        WIDGETS.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # UI THREADPOOL
        self.Ui_Threadpool = QThreadPool.globalInstance()
        self.Ui_Threadpool.maxThreadCount = 5

        # MAIN THREADPOOL
        self.threadpool = QThreadPool.globalInstance()
        self.threadpool.maxThreadCount = 8

        # BUTTON CONNECTIONS
        WIDGETS.buttonExperimentSelect.clicked.connect(self.clickExperimentSelect)
        WIDGETS.buttonExperimentLoad.clicked.connect(self.clickExperimentLoad)
        WIDGETS.buttonROS2LocalLaunchShutdown.clicked.connect(self.clickROS2LocalLaunchShutdown)
        WIDGETS.buttonNetworkRemoteConnectDisconnect.clicked.connect(self.clickNetworkRemoteConnectDisconnect)
        WIDGETS.buttonROS2RemoteLaunchShutdown.clicked.connect(self.clickROS2RemoteLaunchShutdown)



        # EXPERIMENT STATE ATTRIBUTES
        self.ros2_local_status: int = 0             # 0: not active; 1: active
        self.remote_network_status: int = 0         # 0: not connected; 1: connected
        self.ros2_remote_status: int = 0            # 0: not active; 1: active
        self.is_experiment_running: bool = False

        # EXPERIMENT FILE ATTRIBUTES
        self.experiment_file_extensions: str = ".yaml (*.yaml)"     # valid experiment file types
        self.experiment_file_path: str = None       # absolute path to the experiment file
        self.experiment_file_content: str = None    # content of the experiment file
        self.experiment_name: str = None            # name of the experiment

        # EXPERIMENT BACKEND
        self.experiment_section: List[Ui_Content] = []
        self.devices_offline: List[Device] = []
        self.devices_local: List[Device] = []
        self.devices_remote: List[Device] = []


        # UI TIMERS
        self.experiment_timer_tiles_network_and_ssh = QTimer()
        self.experiment_timer_tiles_network_and_ssh.timeout.connect(self.updateExperimentDiagnosticsTiles)
        self.experiment_timer_tiles_network_and_ssh.start(7000)

        self.experiment_timer_tiles_ros2 = QTimer()
        self.experiment_timer_tiles_ros2.timeout.connect(self.updateExperimentDiagnosticsROS2)
        self.experiment_timer_tiles_ros2.start(7000)




        # SHOW WINDOW
        self.show()
        Ui_Functions.diagnosticsConsoleLog(self, "launched mess2")


    def resizeEvent(self, event):
        """
        """
        Ui_Functions.resize_grips(self)

    def mousePressEvent(self, event):
        """
        """
        self.dragPos = event.globalPos()
    

    def clickExperimentSelect(self):
        """
        Opens a dialogue to select a .yaml experiment file and assigns selected file path to experiment_file_path attribute; does not validate whether the contents of the file are compatible with mess2.
        """
        if self.is_experiment_running == True:
            Ui_Functions.diagnosticsConsoleLog(self, "unable to select experiment file while experiment is running")
        elif self.is_experiment_running == False:
            dir = os.getcwd()
            if self.experiment_file_path != None:
                dir = os.path.dirname(os.path.realpath(self.experiment_file_path))
            response = QFileDialog.getOpenFileName(
                parent=self,
                caption="Select a .yaml experiment file",
                dir=dir,
                filter=self.experiment_file_extensions
            )
            experiment_file_path, _ = response
            if experiment_file_path:
                self.experiment_file_path = experiment_file_path
                Ui_Functions.diagnosticsConsoleLog(self, f"selected experiment file {self.experiment_file_path}")
                WIDGETS.diagnosticsMenu1ExperimentFileText.setText(self.experiment_file_path)


    def validateExperimentFile(self, file):
        """
        """
        Ui_Functions.diagnosticsConsoleLog(self, "todo: experiment file validation")
        # Ui_Functions.diagnosticsConsoleLog(self, "selected experiment file is invalid")
        self.experiment_file_content
        return True


    def unloadExperimentFile(self):
        """
        Unloads a loaded experiment file.
        """
        if self.experiment_file_content != None:
            return
        else:
            for content in self.experiment_section:
                WIDGETS.diagnosticsTilesDefaultPage.removeWidget(content.page)
                content.page.deleteLater()
                WIDGETS.diagnosticsTilesMenu1Buttons.removeWidget(content.button)
                content.button.deleteLater()
            self.experiment_section.clear()
            self.devices_offline.clear()
            self.devices_local.clear()
            self.devices_remote.clear()
            Ui_Functions.diagnosticsConsoleLog(self, f"unloaded experiment {self.experiment_name}")


    def loadExperimentFile(self, file):
        """
        Loads an experiment file assuming 1. it is valid; 2. it is not already loaded.
        """
        exp = file.get("experiment", "")
        exp_name = exp.get("name", "")
        exp_categories = exp.get("categories", "")

        if file != None and exp_name == self.experiment_name:
            Ui_Functions.diagnosticsConsoleLog(self, "selected experiment file is already loaded")
            return

        if file != None and exp_name != self.experiment_name:
            self.unloadExperimentFile()

        counter = 0
        self.experiment_name = exp_name
        for cat in exp_categories:
            content = Ui_Content(self, cat)
            self.experiment_section.append(content)
            devices = file.get(cat, "")
            for device in devices:
                device_type = device.get("type", "")
                device_name = device.get("name", "")
                device_ip = device.get("ip", "")
                device_username = device.get("username", "ubuntu")
                device_password = device.get("password", "1234")
                enable_network = device.get("enable_network", False)
                enable_ssh = device.get("enable_ssh", False)
                enable_battery = device.get("enable_battery", False)
                commands1 = device.get("commands1", [])
                commands2 = device.get("commands2", [])
                nodes = device.get("nodes", [])

                device_ = Device(
                    type=device_type,
                    name=device_name,
                    ip=device_ip,
                    username=device_username,
                    password=device_password,
                    logger=self.ui.diagnosticsConsoleDisplay,
                    threadpool=self.threadpool,
                    enable_network=enable_network,
                    enable_ssh=enable_ssh,
                    enable_battery=enable_battery,
                    commands1=commands1,
                    commands2=commands2,
                    nodes=nodes,
                )

                if enable_network == False:
                    self.devices_offline.append(device_)
                elif enable_ssh == False:
                    self.devices_local.append(device_)
                elif enable_ssh == True:
                    self.devices_remote.append(device_)

                index_row = content.grid.get_index_row()
                index_col = content.grid.get_index_col()
                content.layout.addWidget(device_.widget, index_row, index_col)

            counter += 1
            if counter == 1:
                content.select()
        
        Ui_Functions.diagnosticsConsoleLog(self, f"loaded experiment {self.experiment_name}")


    def clickExperimentLoad(self):
        """
        """
        if self.is_experiment_running == True:
            Ui_Functions.diagnosticsConsoleLog(self, "unable to load experiment file while experiment is running")
        elif self.is_experiment_running == False:
            if self.experiment_file_path == None:
                Ui_Functions.diagnosticsConsoleLog(self, "unable to load experiment file because no experiment is selected")
            else:
                with open(self.experiment_file_path, "r") as file:
                    experiment_file_content = yaml.safe_load(file)
                if self.validateExperimentFile(experiment_file_content) == False:
                    return
                self.loadExperimentFile(experiment_file_content)


    def checkDevicesNetworkStatus(self, devices: List[Device]):
        """
        Checks a list of devices to determine whether all devices are connected to the network; assumes that worker checks/updates device statuses frequently enough that pinging the devices here is not necessary.
        """
        result = True
        for device in devices:
            if device.network.status_network == False or device.network.status_network == None:
                result = False
        return result


    def checkDevicesSSHStatus(self, devices: List[Device]):
        """
        Checks a list of devices to determine whether all devices are connected to the application via ssh; assumes that worker checks/updates device statuses frequently enough that testing the device transports is not necessary.
        """
        result = True
        for device in devices:
            if device.network.status_ssh == False or device.network.status_ssh == None:
                result = False
        return result


    def clickROS2LocalLaunchShutdown(self):
        """
        """
        if not self.devices_local:
            Ui_Functions.diagnosticsConsoleLog(self, "unable to start local ros2 nodes because no local devices are loaded")
            return
        if not self.checkDevicesNetworkStatus(self.devices_local):
            Ui_Functions.diagnosticsConsoleLog(self, "unable to start local ros2 nodes because not all local devices are connected to the network")
            return
        if self.ros2_local_status == 0:
            Ui_Functions.diagnosticsConsoleLog(self, "launching local ROS2 nodes")
            worker = WorkerDevicesROS2LocalStart(self.devices_local, 1)
            self.threadpool.start(worker)
            WIDGETS.buttonROS2LocalLaunchShutdown.setText("Shutdown Local ROS2 Nodes")
            self.ros2_local_status = 1
        elif self.ros2_local_status == 1:
            Ui_Functions.diagnosticsConsoleLog(self, "shutting down local ROS2 nodes")
            worker = WorkerDevicesROS2LocalStop(self.devices_local, 1)
            self.threadpool.start(worker)
            WIDGETS.buttonROS2LocalLaunchShutdown.setText("Launch Local ROS2 Nodes")
            self.ros2_local_status = 0


    def clickNetworkRemoteConnectDisconnect(self):
        """
        """
        if not self.devices_remote:
            Ui_Functions.diagnosticsConsoleLog(self, "unable to connect to remote devices because no remote devices are loaded")
            return
        if not self.checkDevicesNetworkStatus(self.devices_remote):
            Ui_Functions.diagnosticsConsoleLog(self, "unable to connect to remote devices because not all remote devices are connected to the network")
            return
        if self.remote_network_status == 0:
            Ui_Functions.diagnosticsConsoleLog(self, "connecting to remote devices")
            worker = WorkerDevicesSSHConnect(self.devices_remote)
            self.threadpool.start(worker)
            WIDGETS.buttonNetworkRemoteConnectDisconnect.setText("Disconnect from Remote Devices")
            self.remote_network_status = 1
        elif self.remote_network_status == 1:
            Ui_Functions.diagnosticsConsoleLog(self, "disconnecting from remote devices")
            worker = WorkerDevicesSSHDisconnect(self.devices_remote)
            self.threadpool.start(worker)
            WIDGETS.buttonNetworkRemoteConnectDisconnect.setText("Connect to Remote Devices")
            self.remote_network_status = 0


    def clickROS2RemoteLaunchShutdown(self):
        """
        """
        if not self.devices_remote:
            Ui_Functions.diagnosticsConsoleLog(self, "unable to start remote ros2 nodes because no remote devices are loaded")
            return
        if not self.checkDevicesNetworkStatus(self.devices_remote):
            Ui_Functions.diagnosticsConsoleLog(self, "unable to start remote ros2 nodes because not all remote devices are connected to the network")
            return
        if not self.checkDevicesSSHStatus(self.devices_remote):
            Ui_Functions.diagnosticsConsoleLog(self, "unable to start remote ros2 nodes because not all remote devices are connected to the application via ssh")
            return
        if self.ros2_remote_status == 0:
            Ui_Functions.diagnosticsConsoleLog(self, "launching remote ROS2 nodes")
            worker = WorkerDevicesROS2RemoteStart(self.devices_remote, 1)
            self.threadpool.start(worker)
            WIDGETS.buttonROS2RemoteLaunchShutdown.setText("Shutdown Remote ROS2 Nodes")
            self.ros2_remote_status = 1
        elif self.ros2_remote_status == 1:
            Ui_Functions.diagnosticsConsoleLog(self, "shutting down remote ROS2 nodes")
            worker = WorkerDevicesROS2RemoteStop(self.devices_remote, 1)
            self.threadpool.start(worker)
            WIDGETS.buttonROS2RemoteLaunchShutdown.setText("Launch Remote ROS2 Nodes")
            self.ros2_remote_status = 0


    def updateExperimentDiagnosticsTiles(self):
        """
        """
        worker = WorkerDeviceUi(self.devices_local, self.devices_remote)
        self.Ui_Threadpool.start(worker)


    def updateExperimentDiagnosticsROS2(self):
        """
        """
        worker = WorkerROS2Ui(self.devices_offline + self.devices_local + self.devices_remote)
        self.Ui_Threadpool.start(worker)


class Ui_Content():
    """
    """
    def __init__(self, instance: MainWindow, category: str):
        """
        """
        super().__init__()
        self.instance = instance
        self.category = category

        self.grid = Ui_ContentGrid()

        self.button = QPushButton()
        self.button.setObjectName(f"btn_diagnostics2_{self.category}")
        self.button.setText(self.category)
        self.button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.page = QWidget()
        self.ui = Ui_tileDiagnosticsPage()
        self.ui.setupUi(self.page)
        self.ui.diagnostics2ScrollAreaLayout.setAlignment(Qt.AlignTop)
        self.page.setObjectName(f"page_diagnostics2_{category}")

        self.button.clicked.connect(self.click)
        self.layout = self.ui.diagnostics2ScrollAreaLayout

        WIDGETS.__setattr__(self.button.objectName(), self.button)
        WIDGETS.__setattr__(self.page.objectName(), self.page)

        WIDGETS.diagnosticsTilesMenu1Buttons.addWidget(self.button)
        WIDGETS.diagnosticsTilesDefaultPage.addWidget(self.page)

        self.is_selected = False


    def select(self):
        """
        """
        style = self.button.styleSheet()
        style = style.replace("", Settings.DIAGNOSTICS_SUBMENU2_STYLE)
        self.button.setStyleSheet(style)

        page = self.instance.ui.diagnosticsTilesDefaultPage.findChild(QWidget, f"{self.page.objectName().replace('btn', 'page')}")
        self.instance.ui.diagnosticsTilesDefaultPage.setCurrentWidget(page)

        self.is_selected = True


    def deselect(self):
        """
        """
        style = self.button.styleSheet()
        style = style.replace(Settings.DIAGNOSTICS_SUBMENU2_STYLE, "")
        self.button.setStyleSheet(style)

        self.is_selected = False
    

    def click(self):
        """
        """
        if self.is_selected == False:
            for content in self.instance.experiment_section:
                if content.category == self.category:
                    self.select()
                else:
                    content.deselect()




class Ui_ContentGrid():
    """
    This class trackes the indices of grid layouts assuming that the grid either has a maximum number of columns or rows. The current logic will not account for grids who dimensions are either both bounded or unbounded.
    """
    def __init__(self, n_cols: int = 2):
        """

        """
        super().__init__()
        assert(n_cols > 0)

        self.n_cols = n_cols

        self.curr_row = 1
        self.curr_col = 0
    

    def get_index_row(self):
        """
        This method gets the index of the next row in the grid assuming that if there is a maximum number of columns and that value equals the current column index, then increment the current row index and reset the current column index.
        """
        if self.n_cols:
            if self.curr_col >= self.n_cols:
                self.curr_col = 0
                self.curr_row += 1
        return self.curr_row - 1


    def get_index_col(self):
        """
        This method gets the index of the next column in the grid assuming that if there is a maximum number of columns and that value equals the current column index, then increment the current row index and reset the current column index.
        """
        self.curr_col += 1
        return self.curr_col


    def __reset__(self):
        """
        Resets the current instance's row and column indices.
        """
        self.curr_row = 1
        self.curr_col = 0


class Ui_Functions(MainWindow):
    # MAXIMIZE/RESTORE
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
    def returStatus(self):
        return GLOBAL_STATE

    # SET STATUS
    # ///////////////////////////////////////////////////////////////
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # # TOGGLE MENU
    # # ///////////////////////////////////////////////////////////////
    # def toggleMenu(self, enable):
    #     if enable:
    #         # GET WIDTH
    #         width = self.ui.leftMenuBg.width()
    #         maxExtend = Settings.MENU_WIDTH
    #         standard = 60

    #         # SET MAX WIDTH
    #         if width == 60:
    #             widthExtended = maxExtend
    #         else:
    #             widthExtended = standard

    #         # ANIMATION
    #         self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
    #         self.animation.setDuration(Settings.TIME_ANIMATION)
    #         self.animation.setStartValue(width)
    #         self.animation.setEndValue(widthExtended)
    #         self.animation.setEasingCurve(QEasingCurve.InOutQuart)
    #         self.animation.start()

    # # TOGGLE LEFT BOX
    # # ///////////////////////////////////////////////////////////////
    # def toggleLeftBox(self, enable):
    #     if enable:
    #         # GET WIDTH
    #         width = self.ui.extraLeftBox.width()
    #         widthRightBox = self.ui.extraRightBox.width()
    #         maxExtend = Settings.LEFT_BOX_WIDTH
    #         color = Settings.BTN_LEFT_BOX_COLOR
    #         standard = 0

    #         # GET BTN STYLE
    #         style = self.ui.toggleLeftBox.styleSheet()

    #         # SET MAX WIDTH
    #         if width == 0:
    #             widthExtended = maxExtend
    #             # SELECT BTN
    #             self.ui.toggleLeftBox.setStyleSheet(style + color)
    #             if widthRightBox != 0:
    #                 style = self.ui.settingsTopBtn.styleSheet()
    #                 self.ui.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
    #         else:
    #             widthExtended = standard
    #             # RESET BTN
    #             self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))
                
    #     Ui_Functions.start_box_animation(self, width, widthRightBox, "left")

    # # TOGGLE RIGHT BOX
    # # ///////////////////////////////////////////////////////////////
    # def toggleRightBox(self, enable):
    #     if enable:
    #         # GET WIDTH
    #         width = self.ui.extraRightBox.width()
    #         widthLeftBox = self.ui.extraLeftBox.width()
    #         maxExtend = Settings.RIGHT_BOX_WIDTH
    #         color = Settings.BTN_RIGHT_BOX_COLOR
    #         standard = 0

    #         # GET BTN STYLE
    #         style = self.ui.settingsTopBtn.styleSheet()

    #         # SET MAX WIDTH
    #         if width == 0:
    #             widthExtended = maxExtend
    #             # SELECT BTN
    #             self.ui.settingsTopBtn.setStyleSheet(style + color)
    #             if widthLeftBox != 0:
    #                 style = self.ui.toggleLeftBox.styleSheet()
    #                 self.ui.toggleLeftBox.setStyleSheet(style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
    #         else:
    #             widthExtended = standard
    #             # RESET BTN
    #             self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

    #         Ui_Functions.start_box_animation(self, widthLeftBox, width, "right")

    # def start_box_animation(self, left_box_width, right_box_width, direction):
    #     right_width = 0
    #     left_width = 0 

    #     # Check values
    #     if left_box_width == 0 and direction == "left":
    #         left_width = 240
    #     else:
    #         left_width = 0
    #     # Check values
    #     if right_box_width == 0 and direction == "right":
    #         right_width = 240
    #     else:
    #         right_width = 0       

    #     # ANIMATION LEFT BOX        
    #     self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
    #     self.left_box.setDuration(Settings.TIME_ANIMATION)
    #     self.left_box.setStartValue(left_box_width)
    #     self.left_box.setEndValue(left_width)
    #     self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

    #     # ANIMATION RIGHT BOX        
    #     self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
    #     self.right_box.setDuration(Settings.TIME_ANIMATION)
    #     self.right_box.setStartValue(right_box_width)
    #     self.right_box.setEndValue(right_width)
    #     self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

    #     # GROUP ANIMATION
    #     self.group = QParallelAnimationGroup()
    #     self.group.addAnimation(self.left_box)
    #     self.group.addAnimation(self.right_box)
    #     self.group.start()

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(Ui_Functions.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(Ui_Functions.deselectMenu(w.styleSheet()))

    # IMPORT THEMES FILES QSS/CSS
    # ///////////////////////////////////////////////////////////////
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.ui.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: Ui_Functions.maximize_restore(self))
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            #STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if Ui_Functions.returStatus(self):
                    Ui_Functions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

            # CUSTOM GRIPS
            self.left_grip = Ui_Grips.CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = Ui_Grips.CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = Ui_Grips.CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = Ui_Grips.CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: Ui_Functions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    def resize_grips(self):
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # /////////////////////////////////////////////////////////////////////////////////

    #     def selectMenu(getStyle):
    #     select = getStyle + Settings.MENU_SELECTED_STYLESHEET
    #     return select

    # # DESELECT
    # def deselectMenu(getStyle):
    #     deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
    #     return deselect

    # # START SELECTION
    # def selectStandardMenu(self, widget):
    #     for w in self.ui.topMenu.findChildren(QPushButton):
    #         if w.objectName() == widget:
    #             w.setStyleSheet(Ui_Functions.selectMenu(w.styleSheet()))

    # # RESET SELECTION
    # def resetStyle(self, widget):
    #     for w in self.ui.topMenu.findChildren(QPushButton):
    #         if w.objectName() != widget:
    #             w.setStyleSheet(Ui_Functions.deselectMenu(w.styleSheet()))



    
    def selectStyleDiagnosticsSubMenu2(getStyle):
        """
        
        """
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET_DIAGNOSTICS2
        return select
        # # select = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, Settings.DIAGNOSTICS_SUBMENU2_STYLESHEET_SELECTED)
        # # print(select)
        # return select


    def deselectStyleDiagnosticsSubMenu2(getStyle):
        """
        
        """
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET_DIAGNOSTICS2, "")
        return deselect

    
    def resetStyleDiagnosticsSubMenu2(self, btnName: str):
        """
        
        """
        ignore = ["btn_diagnostics_refresh"]
        for w in self.ui.diagnosticsSubMenu2.findChildren(QPushButton):
            is_same: bool = (w.objectName() == btnName)
            is_ignore: bool = (w.objectName() in ignore)
            if not is_same and not is_ignore:
                w.setStyleSheet(Ui_Functions.deselectStyleDiagnosticsSubMenu2(w.styleSheet()))
    




    def toggleStyleConnected(self, frameName, frameBool: bool):
        """
        """
        frame = eval(f"self.ui.{frameName}")
        style = frame.styleSheet()
        if frameBool:
            style = style.replace("disconnected", "connected")
        else:
            style = style.replace("connected", "disconnected")
        frame.setStyleSheet(style)
    

    def toggleStyleOnline(self, frameName: str, frameBool: bool):
        """
        """
        frame = eval(f"self.ui.{frameName}")
        style = frame.styleSheet()
        if frameBool:
            style = style.replace("offline", "online")
        else:
            style = style.replace("online", "offline")
        frame.setStyleSheet(style)




    # def selectMenu(getStyle):
    #     select = getStyle + Settings.MENU_SELECTED_STYLESHEET
    #     return select

    # # DESELECT
    # def deselectMenu(getStyle):
    #     deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
    #     return deselect



    # ///////////////////////////////////////////////////////////////
    # END - GUI DEFINITIONS

    def diagnostics_submenu2_style(self, name: str):
        """
        """
        ignore = ["btn_diagnostics2_refresh"]
        for widget in self.ui.diagnosticsSubmenu2.findChildren(QPushButton):
            is_same: bool = (widget.objectName() == name)
            is_ignore: bool = (widget.objectName() in ignore)
            if is_same == False and is_ignore == False:
                style = widget.styleSheet()
                style = style.replace(Settings.DIAGNOSTICS_SUBMENU2_STYLE, "")
                widget.setStyleSheet(style)
            elif is_same == True:
                style = widget.styleSheet()
                style = style.replace("", Settings.DIAGNOSTICS_SUBMENU2_STYLE)
                widget.setStyleSheet(style)

                page = self.ui.diagnosticsPages2.findChild(QWidget, f"{widget.objectName().replace('btn', 'page')}")
                self.ui.diagnosticsPages2.setCurrentWidget(page)
    

    def diagnosticsConsoleLog(self, message: str):
        """
        Logs a message to the diagnostics console with a time stamp.
        """
        stamp = datetime.now().strftime("[%H:%M:%S]")
        ms = f"{stamp} : {message}"
        self.ui.diagnosticsConsoleDisplay.appendPlainText(ms)
        self.ui.diagnosticsConsoleDisplay.verticalScrollBar().setValue(self.ui.diagnosticsConsoleDisplay.verticalScrollBar().maximum())


def main():
    """
    """
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())


if __name__=="__main__":
    main()
