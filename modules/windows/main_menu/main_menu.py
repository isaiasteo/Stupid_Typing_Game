import wx
import sys

from modules.components.create_button import create_button


class MainMenu(wx.Panel):
    def __init__(self, parent, data, next_screen):
        super().__init__(parent)

        self.data = data
        self.next_screen = next_screen

        self.result_text = wx.StaticText(
            self,
            label=str("STUPID TYPING GAME"),
        )
        self.result_text.SetForegroundColour(wx.WHITE)
        font = self.result_text.GetFont()
        font.SetPointSize(30)
        self.result_text.SetFont(font)

        btn_start = create_button(
            self,
            "Start game",
            lambda event: self.next_screen(index=0),
            position=(320, 200),
            size=(150, 40),
        )
        btn_start.SetFocus()
        btn_exit = create_button(
            self,
            "Exit",
            lambda event: sys.exit(),
            position=(320, 250),
            size=(150, 40),
        )

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.result_text, 0, wx.ALL | wx.CENTER, 10)
        self.SetSizer(sizer)
