import wx


def draw_pixel_art(dc, size, pixel_art, fill=False):
    width, height = size

    if fill:
        art = pixel_art["art"]
        colors = pixel_art["colors"]

        scale = max(
            width // len(art[0]),
            height // len(art),
        )

        for y, row in enumerate(art):
            for x, value in enumerate(row):
                if value == "0":
                    continue

                color = wx.Colour(colors[value])

                dc.SetPen(wx.Pen(color))
                dc.SetBrush(wx.Brush(color))

                dc.DrawRectangle(
                    x * scale,
                    y * scale,
                    scale,
                    scale,
                )

        return

    logical_width = 640
    logical_height = 360

    scale = int(
        min(
            width / logical_width,
            height / logical_height,
        )
    )

    offset_x = (width - logical_width * scale) // 2
    offset_y = (height - logical_height * scale) // 2

    x_position = pixel_art["x"]
    y_position = pixel_art["y"]
    art = pixel_art["art"]
    colors = pixel_art["colors"]

    for y, row in enumerate(art):
        for x, value in enumerate(row):
            if value == "0":
                continue

            color = wx.Colour(colors[value])

            dc.SetPen(wx.Pen(color))
            dc.SetBrush(wx.Brush(color))

            dc.DrawRectangle(
                offset_x + (x_position + x) * scale,
                offset_y + (y_position + y) * scale,
                scale,
                scale,
            )


class PixelPanel(wx.Panel):
    def __init__(self, parent, pixel_art):
        super().__init__(parent)

        self.pixel_art = pixel_art

        self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_paint(self, event):
        dc = wx.PaintDC(self)

        draw_pixel_art(
            dc,
            self.GetClientSize(),
            self.pixel_art,
        )
