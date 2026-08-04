import wx


def display_text(panel, text):
    label = wx.StaticText(panel, label=text)

    font = label.GetFont()
    font.SetPointSize(14)
    label.SetBackgroundColour(wx.Colour(20, 20, 20))
    label.SetForegroundColour(wx.Colour(255, 255, 255))
    faceName = "Segoe UI"
    label.SetFont(font)

    panel.GetSizer().Add(label, 1, wx.ALL | wx.CENTER, 20)

    panel.Layout()

    return label
