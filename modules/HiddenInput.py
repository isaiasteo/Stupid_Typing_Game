import wx


class HiddenInput(wx.TextCtrl):
    def __init__(self, parent):
        super().__init__(parent)

        self.SetMinSize((1, 1))
        self.SetBackgroundColour(parent.GetBackgroundColour())
        self.SetForegroundColour(parent.GetBackgroundColour())
        self.SetWindowStyleFlag(wx.BORDER_NONE)

        self.SetFocus()
