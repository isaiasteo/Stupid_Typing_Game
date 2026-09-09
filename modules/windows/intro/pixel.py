import wx

from modules.windows.intro.pixel_arts import pixel_arts


class PixelPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.logical_width = 640
        self.logical_height = 360

        self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_paint(self, event):
        dc = wx.PaintDC(self)

        width, height = self.GetClientSize()

        scale = int(
            min(
                width / self.logical_width,
                height / self.logical_height,
            )
        )

        offset_x = (width - self.logical_width * scale) // 2
        offset_y = (height - self.logical_height * scale) // 2

        dc.SetPen(wx.Pen(wx.WHITE))
        dc.SetBrush(wx.Brush(wx.WHITE))

        colors = {
            "1": wx.WHITE,
            "2": wx.RED,
        }

        for pixel_art in pixel_arts.values():
            x_position = pixel_art["x"]
            y_position = pixel_art["y"]
            art = pixel_art["art"]

            for y, row in enumerate(art):
                for x, value in enumerate(row):
                    if value == "0":
                        continue

                    dc.SetPen(wx.Pen(colors[value]))
                    dc.SetBrush(wx.Brush(colors[value]))

                    dc.DrawRectangle(
                        offset_x + (x_position + x) * scale,
                        offset_y + (y_position + y) * scale,
                        scale,
                        scale,
                    )
