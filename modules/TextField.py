import wx
from .TextField_style import apply_style
from .TextField_placeholder import Placeholder


class TextField(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.text = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        apply_style(self.text)

        sizer.Add(self.text, 1, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(sizer)

        Placeholder(self.text, "Write something...")
