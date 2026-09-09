import wx

from modules.sfx.sound_effects import sfx


class intro(wx.Panel):
    def __init__(self, parent, data, next_screen):
        super().__init__(parent)

        sfx("modules/sfx/intro.mp3")

        self.data = data
        self.next_screen = next_screen

        self.result_text = wx.StaticText(
            self,
            label="github.com/isaiasteo",
        )

        self.result_text.SetForegroundColour(wx.WHITE)

        font = self.result_text.GetFont()
        font.SetPointSize(30)
        self.result_text.SetFont(font)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(
            self.result_text,
            0,
            wx.ALIGN_CENTER | wx.TOP,
            500,
        )

        self.SetSizer(sizer)

        wx.CallLater(4000, self.finish_intro)

    def finish_intro(self):
        self.next_screen(index=3)
