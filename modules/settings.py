
import datetime
import os
import re

class Settings():
    # APP SETTINGS
    # ///////////////////////////////////////////////////////////////
    ENABLE_CUSTOM_TITLE_BAR = True
    MENU_WIDTH = 240
    LEFT_BOX_WIDTH = 240
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 500

    # BTNS LEFT AND RIGHT BOX COLORS
    BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
    BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"

    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(0, 204, 255, 255), stop:0.5 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    """

    # DIAGNOSTICS SUBMENU 2 STYLESHEETS
    MENU_SELECTED_STYLESHEET_DIAGNOSTICS2 = """
    background-color: rgb(40, 44, 52); 
    border-bottom: 3px solid rgb(0, 204, 255); 
    border-top: 3px solid transparent; 
    """

    # CONNECTED ICON TOGGLE
    ICON_IS_DISCONNECTED = """background-image: url(:/icons/images/icons2/status_disconnected.png);"""
    ICON_IS_CONNECTED = """background-image: url(:/icons/images/icons2/status_connected.png);"""










    DIAGNOSTICS_SUBMENU2_STYLE = """
    background-color: rgb(40, 44, 52); 
    border-bottom: 3px solid rgb(0, 204, 255); 
    border-top: 3px solid transparent; 
    """


    DIAGNOSTICS_MENU2_IS_NOT_READY = """
#buttonExperimentRunAbort  {
color: rgb(201, 201, 201);
background-color: rgb(35, 28, 30);
font-size: 14px;
min-height: 36px;
max-height: 36px;
border: 2px solid rgb(217, 83, 79);
border-radius: 12px;
}
"""
    DIAGNOSTICS_MENU2_IS_READY = """
#buttonExperimentRunAbort  {
color: rgb(201, 201, 201);
background-color: rgb(35, 79, 61);
font-size: 14px;
min-height: 36px;
max-height: 36px;
border: 2px solid rgb(60, 179, 113);
border-radius: 12px;
}
"""
    DIAGNOSTICS_MENU2_IS_RUNNING = """
#buttonExperimentRunAbort  {
color: rgb(201, 201, 201);
background-color: rgb(35, 28, 30);
font-size: 14px;
min-height: 36px;
max-height: 36px;
border: 2px solid rgb(217, 83, 79);
border-radius: 12px;
}
"""


    def get_experiment_trial_path(path):
        """
        """
        expanded_path = os.path.expanduser(f"~/{path}")
        if not os.path.exists(expanded_path):
            os.makedirs(expanded_path)
            return "0001"
        past_trials = [name for name in os.listdir(expanded_path) if os.path.isdir(os.path.join(expanded_path, name))]
        last_index = 0
        for trial in past_trials:
            match = re.match(r'^(\d+)_', trial)
            if match:
                index = int(match.group(1))
                if index > last_index:
                    last_index = index
        curr_index = last_index + 1
        trial = f"{curr_index:04d}"
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"{path}/{trial}_{date}_{time}"
        