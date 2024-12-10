
from PySide6.QtCore import Qt, QRunnable, QThreadPool
from PySide6.QtWidgets import QWidget, QPlainTextEdit

from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from modules.logger import Ui_Logger
from modules.network import NetworkFunctions
from modules.other.ui_tileDiagnosticsSensor import Ui_tileDiagnosticsSensor
from modules.other.ui_tileDiagnosticsUGV import Ui_tileDiagnosticsUGV
from modules.other.ui_tileDiagnosticsUAV import Ui_tileDiagnosticsUAV
from modules.other.ui_tileDiagnosticsLine import Ui_tileDiagnosticsROS2Line
import subprocess
from typing import List, Union


class DeviceUi():
    """
    Manages the ui attributes and methods for a mess2 app diagnostics instance.
    """
    def __init__(self):
        """
        Initializes ui attributes.
        """
        # battery icons
        self.style_battery_percentage_0 = "background-image: url(:/icons/images/icons2/battery_0.png);"
        self.style_battery_percentage_25 = "background-image: url(:/icons/images/icons2/battery_25.png);"
        self.style_battery_percentage_50 = "background-image: url(:/icons/images/icons2/battery_50.png);"
        self.style_battery_percentage_75 = "background-image: url(:/icons/images/icons2/battery_75.png);"
        self.style_battery_percentage_100 = "background-image: url(:/icons/images/icons2/battery_100.png);"
        self.style_battery_percentage_na = "background-image: url(:/icons/images/icons2/battery_na.png);"

        # network connection icons
        self.style_network_connected = "background-image: url(:/icons/images/icons2/network_connected.png);"
        self.style_network_disconnected = "background-image: url(:/icons/images/icons2/network_disconnected.png);"
        self.style_network_na = "background-image: url(:/icons/images/icons2/network_na.png);"

        # mess2 app connection icons
        self.style_ssh_connected = "background-image: url(:/icons/images/icons2/ssh_connected.png);"
        self.style_ssh_disconnected = "background-image: url(:/icons/images/icons2/ssh_disconnected.png);"
        self.style_ssh_na = "background-image: url(:/icons/images/icons2/ssh_na.png);"

        # mess2 device types
        self.types_sensor = [
            "sensor",
            "vicon",
            "flir"
        ]
        self.types_ugvs = [
            "ugv",
            "burger",
            "waffle",
            "waffle_pi",
            "wafflepi"
        ]
        self.types_uavs = [
            "uav",
            "hawk"
        ]

        # mess2 widget options
        self.types_ui = {
            "sensor": "Ui_tileDiagnosticsSensor",
            "ugv": "Ui_tileDiagnosticsUGV",
            "uav": "Ui_tileDiagnosticsUAV"
        }

        self.widget = QWidget()
        self.ui: Union[Ui_tileDiagnosticsSensor, Ui_tileDiagnosticsUGV, Ui_tileDiagnosticsUAV] = None

        self.battery_percentage_text = None
        self.battery_percentage_style = None


    def ui_lookup(self, type: str):
        """
        """
        if type in self.types_sensor:
            result = self.types_ui.get("sensor", None)
        elif type in self.types_ugvs:
            result = self.types_ui.get("ugv", None)
        elif type in self.types_uavs:
            result = self.types_ui.get("uav", None)
        else:
            result = None
        return result


    def set_name_text(self, value: str):
        """
        Updates the device's name text in the app gui.
        """
        self.ui.name_text.setText(value)


    def set_battery_percentage_text(self, value: str):
        """
        Updates the device's battery percentage text in the app gui.
        """
        if value != self.battery_percentage_text:
            self.ui.battery_text.setText(value)
            self.battery_percentage_text = value


    def set_battery_percentage_icon(self, value: float):
        """
        Updates the device's battery percentage icon in the app gui.
        """
        if value < -1.0:
            replacement = self.style_battery_percentage_na
        elif value < 0.20:
            replacement = self.style_battery_percentage_0     # should be 0
        elif value < 0.30:
            replacement = self.style_battery_percentage_25     # should be 1
        elif value < 0.55:
            replacement = self.style_battery_percentage_50     # should be 2
        elif value < 0.80:
            replacement = self.style_battery_percentage_75     # should be 3
        else:
            replacement = self.style_battery_percentage_100     # should be 5

        if replacement != self.battery_percentage_style:
            style_old = self.widget.styleSheet()
            style_new = style_old.replace(self.style_battery_percentage_0, replacement)
            style_new = style_new.replace(self.style_battery_percentage_25, replacement)
            style_new = style_new.replace(self.style_battery_percentage_50, replacement)
            style_new = style_new.replace(self.style_battery_percentage_75, replacement)
            style_new = style_new.replace(self.style_battery_percentage_100, replacement)
            style_new = style_new.replace(self.style_battery_percentage_na, replacement)
            self.widget.setStyleSheet(style_new)
            self.battery_percentage_style = replacement


    def set_ssh_icon(self, value: bool):
        """
        Updates the device's SSH icon in the app gui. If the value is None, the SSH icon in the app gui will be disabled.
        """
        style = self.widget.styleSheet()
        if value == None:
            style = style.replace(self.style_ssh_connected, self.style_ssh_na)
            style = style.replace(self.style_ssh_disconnected, self.style_ssh_na)
        elif value == True:
            style = style.replace(self.style_ssh_na, self.style_ssh_connected)
            style = style.replace(self.style_ssh_disconnected, self.style_ssh_connected)
        elif value == False:
            style = style.replace(self.style_ssh_na, self.style_ssh_disconnected)
            style = style.replace(self.style_ssh_connected, self.style_ssh_disconnected)
        self.widget.setStyleSheet(style)


    def set_network_icon(self, value: bool):
        """
        Updates the device's network icon in the app gui. If the value is None, the network icon in the app gui will be disabled.
        """
        style = self.widget.styleSheet()
        if value == None:
            style = style.replace(self.style_network_connected, self.style_network_na)
            style = style.replace(self.style_network_disconnected, self.style_network_disconnected)
        elif value == True:
            style = style.replace(self.style_network_na, self.style_network_connected)
            style = style.replace(self.style_network_disconnected, self.style_network_connected)
        elif value == False:
            style = style.replace(self.style_network_na, self.style_network_disconnected)
            style = style.replace(self.style_network_connected, self.style_network_disconnected)
        self.widget.setStyleSheet(style)


    def set_ip_text(self, value: str):
        """
        Updates the device's ip text in the app gui.
        """
        self.ui.ip_text.setText(value)


class DeviceFunctions():
    """
    Manages the non-ui attributes and methods for a mess2 app diagnostics instance.
    """
    def __init__(self):
        """
        Initializes non-ui attributes.
        """
        self.network = NetworkFunctions()


class Device(DeviceFunctions, DeviceUi):
    """
    Manages a mess2 app diagnostics device. 
    """
    def __init__(self, type: str, name: str, ip: str, username: str = "ubuntu", password="1234", port: int = -1, logger: QPlainTextEdit = None, threadpool: QThreadPool = None, enable_network: bool = True, enable_ssh: bool = False, enable_battery: bool = False, commands: List[str] = [], nodes: List[str] = []):
        """
        Initializes device attributes and shows the device in the mess2 app.
        """
        DeviceFunctions.__init__(self)
        DeviceUi.__init__(self)

        # device discriminators
        self.type = type
        self.name = name

        # device network information
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port

        #
        self.enable_network = enable_network
        self.enable_ssh = enable_ssh
        self.enable_battery = enable_battery

        # device visual information
        self.nodes = []
        self.ui_draw(nodes)

        #
        self.logger = Ui_Logger(logger)
        self.threadpool = threadpool

        # ROS2 integrations
        self.commands = commands        # commands to be executed by device
        self.processes: List[subprocess.Popen] = []             # stores processes
        self.pids: List[int] = []


    def __del__(self):
        """
        Safely destroys the device by closing any active SSH connections.
        """
        self.network.disconnect()


    def ui_draw(self, nodes: List[str]):
        """
        """
        self.widget.setObjectName(f"{self.type}_{self.name.replace(' ', '_').replace('.', '_')}")
        if self.type == None:
            pass
        else:
            self.ui = Ui_tileDiagnosticsUGV()
            self.ui.setupUi(self.widget, self.enable_network, self.enable_ssh, self.enable_battery)
            self.set_name_text(self.name)

            if hasattr(self.ui, "battery_text"):
                self.set_battery_percentage_text("n/a")
                self.ui.battery_text.setAlignment(Qt.AlignRight)

            if hasattr(self.ui, "battery_icon"):
                self.set_battery_percentage_icon(-2.0)

            if hasattr(self.ui, "ssh_icon"):
                self.set_ssh_icon(False)
                self.ui.ssh_icon.clicked.connect(self.click_ssh)

            if hasattr(self.ui, "network_icon"):
                self.set_network_icon(False)
            
            self.set_ip_text(self.ip)
            self.ui.nodesLayout.setAlignment(Qt.AlignTop)
        
        counter = 1
        for node in nodes:
            if counter > 3:
                break
            widget = QWidget()
            widget.setObjectName(f"line{counter}")
            ui = Ui_tileDiagnosticsROS2Line()
            ui.setupUi(widget)
            ui.node.setText(node)
            ui.status_running.setText("")
            self.ui.nodesLayout.addWidget(widget, counter, 1)
            self.ui.nodesLayout.setAlignment(Qt.AlignTop)
            self.nodes.append(ui)
            counter += 1


    def ui_redraw(self, battery_percentage_text: str = None, battery_percentage_value: float = None, status_ssh: bool = None, status_network: bool = None):
        """
        Updates the device's dynamic app gui elements with new values if updates are necessary. Any parameters that are no
        """        
        # only update battery percentage text if value has changed (check performed in method). 
        if hasattr(self.ui, "battery_text") and battery_percentage_text != None:
            self.set_battery_percentage_text(battery_percentage_text)

        # only update battery percentage icon if value causes style change (check performed in method).
        if hasattr(self.ui, "battery_icon") and battery_percentage_value != None:
            self.set_battery_percentage_icon(battery_percentage_value)

        # only update ssh icon if ssh status changed
        if hasattr(self.ui, "ssh_icon") and status_ssh != None:
            if self.network.status_ssh != status_ssh:
                self.set_ssh_icon(status_ssh)
                self.network.status_ssh = status_ssh

        # only update network icon if network status changed
        if hasattr(self.ui, "network_icon") and status_network != None:
            if self.network.status_network != status_network:
                self.set_network_icon(status_network)
                self.network.status_network = status_network


    def ui_node_running(self, ui: Ui_tileDiagnosticsROS2Line):
        """
        """
        ui.status_running.setText("running")
        ui.status_not_running.setText("")


    def ui_node_not_running(self, ui: Ui_tileDiagnosticsROS2Line):
        """
        """
        ui.status_running.setText("")
        ui.status_not_running.setText("not running")


    def click_ssh(self):
        """
        """
        if self.network.status_ssh == True:
            worker = WorkerDeviceSSHDisconnect(self)
        else:
            worker = WorkerDeviceSSHConnect(self)
        self.threadpool.start(worker)


class WorkerDeviceUi(QRunnable):
    """
    Manages threaded worker to check and update network connection icons.
    """
    def __init__(self, local: List[Device], remote: list[Device]):
        """
        """
        super().__init__()
        self.local = local
        self.remote = remote


    def run(self):
        """
        Executes the network and/or SSH checks for the given devices and calls redraw_ui with both results.
        """
        results_network = defaultdict(lambda: None)
        results_ssh = defaultdict(lambda: None)

        with ThreadPoolExecutor() as executor:
            futures_network = {executor.submit(device.network.ping, device.ip): device for device in self.local + self.remote if device.name != "" and device.name != None}
            futures_ssh = {executor.submit(device.network.status): device for device in self.remote if device.name != "" and device.name != None}
            
            for future in futures_network:
                try:
                    device = futures_network[future]
                    result = future.result()
                    results_network[device.name] = result
                except Exception as e:
                    pass
            
            for future in futures_ssh:
                try:
                    device = futures_ssh[future]
                    result = future.result()
                    results_ssh[device.name] = result
                except Exception as e:
                    pass

            for device in self.local + self.remote:
                try:
                    if device.name != "" and device.name != None:
                        status_network = results_network[device.name]
                        status_ssh = results_ssh[device.name]
                        device.ui_redraw(
                            battery_percentage_text=None,
                            battery_percentage_value=None,
                            status_network=status_network,
                            status_ssh=status_ssh
                        )
                except Exception as e:
                    pass


def ssh_connect(device: Device):
    """
    Establishes an SSH connection with a remote device with more-involved networking logic and diagnostics logging.
    """
    if device.network.status_network == True:
        if device.network.status_ssh == True:
            device.logger.log(f"{device.name} already connected via ssh")
        elif device.network.connect(hostname=device.ip, username=device.username, password=device.password, port=device.port):
            device.ui_redraw(status_ssh=True)
            device.network.status_ssh = True
            device.logger.log(f"opened SSH connection with {device.name}")
        else:
            device.logger.log(f"unable to establish SSH connection with {device.name}")


class WorkerDeviceSSHConnect(QRunnable):
    """
    Manages threaded worker to establish an SSH connection with a single device.
    """
    def __init__(self, device: Device):
        """
        """
        super().__init__()
        self.device = device


    def run(self):
        """
        """
        ssh_connect(self.device)
        

class WorkerDevicesSSHConnect(QRunnable):
    """
    Manages threaded worker to establish SSH connections with multiple devices.
    """
    def __init__(self, devices: List[Device]):
        """
        """
        super().__init__()
        self.devices = devices


    def run(self):
        """
        """
        for device in self.devices:
            if device.name != "" and device.name != None:
                ssh_connect(device)


def ssh_disconnect(device: Device):
    """
    Closes an SSH connection with a remote device using more-involved networking logic and diagnostics logging.
    """
    if device.network.status_ssh == False:
        device.logger.log(f"{device.name} already disconnected from SSH")
    elif device.network.status_ssh == True:
        if device.network.disconnect():
            device.ui_redraw(status_ssh=False)
            device.network.status_ssh = False
            device.logger.log(f"closed SSH connection with {device.name}")
        else:
            device.logger.log(f"unable to close SSH connection with {device.name}")


class WorkerDeviceSSHDisconnect(QRunnable):
    """
    Manages threaded worker to close an SSH connection with a single device.
    """
    def __init__(self, device: Device):
        """
        """
        super().__init__()
        self.device = device


    def run(self):
        """
        """
        ssh_disconnect(self.device)
        

class WorkerDevicesSSHDisconnect(QRunnable):
    """
    Manages threaded worker to close SSH connections with multiple devices.
    """
    def __init__(self, devices: List[Device]):
        """
        """
        super().__init__()
        self.devices = devices


    def run(self):
        """
        """
        for device in self.devices:
            if device.name != "" and device.name != None:
                ssh_disconnect(device)


class WorkerDeviceROS2LocalStart(QRunnable):
    """
    """
    def __init__(self, device: Device):
        """
        """
        super().__init__()
        self.device = device


    def run(self):
        """
        """
        self.device.network.local.start(self.device)


class WorkerDeviceROS2LocalStop(QRunnable):
    """
    """
    def __init__(self, device: Device):
        """
        """
        super().__init__()
        self.device = device


    def run(self):
        """
        """
        self.device.network.local.stop(self.device)


class WorkerDevicesROS2LocalStart(QRunnable):
    """
    """
    def __init__(self, devices: List[Device]):
        """
        """
        super().__init__()
        self.devices = devices


    def run(self):
        """
        """
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(device.network.local.start, device): device for device in self.devices if device.name != "" and device.name != None}


class WorkerDevicesROS2LocalStop(QRunnable):
    """
    """
    def __init__(self, devices: List[Device]):
        """
        """
        super().__init__()
        self.devices = devices


    def run(self):
        """
        """
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(device.network.local.stop, device): device for device in self.devices if device.name != "" and device.name != None}


class WorkerDeviceROS2RemoteStart(QRunnable):
    """
    """
    def __init__(self, device: Device):
        """
        """
        super().__init__()
        self.device = device


    def run(self):
        """
        """
        self.device.network.remote.start(self.device)


class WorkerDeviceROS2RemoteStop(QRunnable):
    """
    """
    def __init__(self, device: Device):
        """
        """
        super().__init__()
        self.device = device


    def run(self):
        """
        """
        self.device.network.remote.stop(self.device)


class WorkerDevicesROS2RemoteStart(QRunnable):
    """
    """
    def __init__(self, devices: List[Device]):
        """
        """
        super().__init__()
        self.devices = devices


    def run(self):
        """
        """
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(device.network.remote.start, device): device for device in self.devices if device.name != "" and device.name != None}


class WorkerDevicesROS2RemoteStop(QRunnable):
    """
    """
    def __init__(self, devices: List[Device]):
        """
        """
        super().__init__()
        self.devices = devices


    def run(self):
        """
        """
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(device.network.remote.stop, device): device for device in self.devices if device.name != "" and device.name != None}
