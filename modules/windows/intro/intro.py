import wx

from modules.sfx.sound_effects import sfx
from modules.windows.intro.pixel import PixelPanel


class intro(wx.Panel):
    def __init__(self, parent, data, next_screen):
        super().__init__(parent)

        sfx("modules/sfx/intro.mp3")

        self.data = data
        self.next_screen = next_screen

        self.pixel_panel = PixelPanel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.pixel_panel, 1, wx.EXPAND)

        self.SetSizer(sizer)

        wx.CallLater(4000, self.finish_intro)

    def finish_intro(self):
        self.next_screen(index=3)
