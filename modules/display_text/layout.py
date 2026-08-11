import wx


def setup_layout(panel):

    sizer = wx.BoxSizer(wx.VERTICAL)
    panel.SetSizer(sizer)

    panel.label = wx.StaticText(panel, label=panel.display_text)

    panel.label.SetForegroundColour(wx.WHITE)
    panel.label.SetBackgroundColour(wx.BLACK)

    font = panel.label.GetFont()
    font.SetPointSize(14)
    panel.label.SetFont(font)

    panel.label.Wrap(650)

    sizer.Add(panel.label, 0, wx.ALL | wx.CENTER, 20)

    panel.Layout()
