import wx

from modules.sfx.sound_effects import sfx
from modules.images.pixel import PixelPanel
from modules.images.pixel_arts import pixel_arts


class intro(wx.Panel):
    def __init__(self, parent, data, next_screen):
        super().__init__(parent)

        sfx("modules/sfx/intro.mp3")

        self.data = data
        self.next_screen = next_screen

        logo_path = "modules/images/pngs/intro_logo.png"

        image = wx.Image(logo_path, wx.BITMAP_TYPE_PNG)
        image = image.Scale(300, 300, wx.IMAGE_QUALITY_HIGH)

        self.logo = wx.StaticBitmap(self, bitmap=wx.Bitmap(image))

        self.pixel_panel = PixelPanel(self, pixel_arts["github"])

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.logo.SetPosition((795, 200))

        sizer.Add(self.pixel_panel, 1, wx.EXPAND)

        self.SetSizer(sizer)

        wx.CallLater(4000, self.finish_intro)

    def finish_intro(self):
        self.next_screen(index=3)
