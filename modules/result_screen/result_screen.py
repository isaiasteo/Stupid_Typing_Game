import wx

from ..display_text.cronometer import cronometer


class ResultScreen(wx.Panel):
    def __init__(self, parent, data=None, next_screen=None):
        super().__init__(parent)

        self.data = data
        self.next_screen = next_screen

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.SetSizer(sizer)
