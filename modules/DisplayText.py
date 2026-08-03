import wx


def display_text(panel, text):
    label = wx.StaticText(panel, label=text)

    # Optional
    font = label.GetFont()
    font.SetPointSize(14)
    label.SetFont(font)

    panel.GetSizer().Add(label, 0, wx.ALL | wx.CENTER, 20)
    panel.Layout()

    return label
