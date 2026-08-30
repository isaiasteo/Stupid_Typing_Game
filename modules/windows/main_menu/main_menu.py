import wx
import sys

from modules.components.create_button import create_button
from modules.sfx.sound_effects import sfx


class MainMenu(wx.Panel):
    def __init__(self, parent, data, next_screen):
        super().__init__(parent)

        sfx("modules/sfx/songs/Main_Menu.mp3")

        self.data = data
        self.next_screen = next_screen

        self.result_text = wx.StaticText(
            self,
            label="STUPID TYPING GAME",
        )

        self.result_text.SetForegroundColour(wx.WHITE)

        font = self.result_text.GetFont()
        font.SetPointSize(30)
        self.result_text.SetFont(font)

        btn_start = create_button(
            self,
            "Start game",
            lambda event: self.next_screen(index=0),
            size=(150, 40),
        )

        btn_exit = create_button(
            self,
            "Exit",
            lambda event: sys.exit(),
            size=(150, 40),
        )

        btn_start.SetFocus()

        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.AddStretchSpacer()
        sizer.Add(self.result_text, 0, wx.ALIGN_CENTER | wx.BOTTOM, 20)
        sizer.Add(btn_start, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10)
        sizer.Add(btn_exit, 0, wx.ALIGN_CENTER)
        sizer.AddStretchSpacer()

        self.SetSizer(sizer)
