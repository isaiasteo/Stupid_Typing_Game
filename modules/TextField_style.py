import wx


def apply_style(textctrl):
    textctrl.SetBackgroundColour(wx.Colour(20, 20, 20))

    font = wx.Font(
        14,
        wx.FONTFAMILY_DEFAULT,
        wx.FONTSTYLE_NORMAL,
        wx.FONTWEIGHT_NORMAL,
        faceName="Segoe UI",
    )

    textctrl.SetForegroundColour(wx.Colour(255, 255, 255))
    textctrl.SetFont(font)
