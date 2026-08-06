import wx

import wx


class DisplayText(wx.Panel):
    def __init__(self, parent, data, next_screen):
        super().__init__(parent)

        self.next_screen = next_screen

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        self.label = wx.StaticText(self, label=str(data))

        self.label.SetForegroundColour(wx.WHITE)
        self.label.SetBackgroundColour(wx.BLACK)

        font = self.label.GetFont()
        font.SetPointSize(14)
        self.label.SetFont(font)

        sizer.Add(self.label, 1, wx.ALL | wx.CENTER, 20)
