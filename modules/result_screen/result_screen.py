import wx

from modules.components.create_button import create_button


class ResultScreen(wx.Panel):
    def __init__(self, parent, data, next_screen):
        super().__init__(parent)

        self.data = data
        self.next_screen = next_screen

        self.result_text = wx.StaticText(self, label=str(self.data["time"]))
        self.result_text.SetForegroundColour(wx.WHITE)
        font = self.result_text.GetFont()
        font.SetPointSize(14)
        self.result_text.SetFont(font)

        btn_retype = create_button(
            self,
            "Retype",
            lambda event: self.next_screen(index=1, data=self.data["text"]),
            position=(330, 200),
            size=(120, 40),
        )
        btn_restart = create_button(
            self,
            "Restart",
            lambda event: self.next_screen(index=0),
            position=(330, 300),
            size=(120, 40),
        )

        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(self.result_text, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(sizer)
