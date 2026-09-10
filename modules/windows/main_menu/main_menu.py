import wx
import sys

from modules.components.create_button import create_button
from modules.sfx.sound_effects import sfx
from modules.images.pixel import draw_pixel_art
from modules.images.pixel_arts import pixel_arts


class MainMenu(wx.Panel):
    def __init__(self, parent, data, next_screen):
        super().__init__(parent)

        sfx("modules/sfx/songs/Main_Menu.mp3")

        self.data = data
        self.next_screen = next_screen
        self.pixel_art = pixel_arts["Main_Menu"]

        self.Bind(wx.EVT_PAINT, self.on_paint)

        self.title_font = wx.Font(
            30,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL,
        )

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
        sizer.Add((0, 20))
        sizer.Add(btn_start, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10)
        sizer.Add(btn_exit, 0, wx.ALIGN_CENTER)
        sizer.AddStretchSpacer()

        self.SetSizer(sizer)

    def on_paint(self, event):
        dc = wx.PaintDC(self)

        draw_pixel_art(
            dc,
            self.GetClientSize(),
            self.pixel_art,
            fill=True,
        )

        dc.SetTextForeground(wx.WHITE)
        dc.SetFont(self.title_font)

        text = "STUPID TYPING GAME"
        text_width, text_height = dc.GetTextExtent(text)

        width, height = self.GetClientSize()

        x = (width - text_width) // 2
        y = (height - text_height) // 2 - 80

        dc.DrawText(text, x, y)
