import wx


class ResultScreen(wx.Panel):
    def __init__(self, parent, data=None, next_screen=None):
        super().__init__(parent)

        self.data = data
        self.next_screen = next_screen

        self.result_text = wx.StaticText(self, label=str(self.data))

        self.result_text.SetForegroundColour(wx.WHITE)

        font = self.result_text.GetFont()
        font.SetPointSize(14)
        self.result_text.SetFont(font)

        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(self.result_text, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(sizer)
