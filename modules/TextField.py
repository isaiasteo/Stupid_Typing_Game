import wx


class TextField(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.text = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.text.SetBackgroundColour(wx.Colour(20, 20, 20))
        font = wx.Font(
            14,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL,
            faceName="Segoe UI",
        )
        self.text.SetForegroundColour(wx.Colour(255, 255, 255))  # 0 - 255
        self.text.SetFont(font)

        sizer.Add(self.text, 1, wx.ALL | wx.EXPAND, 10)

        self.SetSizer(sizer)
