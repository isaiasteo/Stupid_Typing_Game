import os
import wx

from modules.window import create_window
from modules.screens import SCREENS
from modules.screen_manager import screen_manager

os.system("cls")

app = wx.App()

window = create_window()

manager = screen_manager(window, SCREENS)

manager.next_screen()

window.Show()

app.MainLoop()
