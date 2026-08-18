from modules.windows.text_field.text_field import text_field
from modules.windows.display_text.display_text import display_text
from modules.windows.result_screen.result_screen import ResultScreen
from modules.windows.main_menu.main_menu import MainMenu
from modules.windows.mode_select.mode_select import ModeSelect

SCREENS = [
    text_field,  # index 0
    display_text,  # index 1
    ResultScreen,  # index 2
    MainMenu,  # index 3
    ModeSelect,  # index 4
]
