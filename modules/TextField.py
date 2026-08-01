import wx


class TextField(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.text = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        sizer.Add(self.text, 1, wx.ALL | wx.EXPAND, 10)

        self.SetSizer(sizer)
