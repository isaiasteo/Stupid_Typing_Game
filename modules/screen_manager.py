import wx


class ScreenManager:
    def __init__(self, window, screens):
        self.window = window
        self.screens = screens

        self.index = 0
        self.current_panel = None

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.window.SetSizer(self.sizer)

    def next_screen(self, data=None):
        if self.index >= len(self.screens):
            return

        if self.current_panel:
            self.current_panel.Destroy()

        self.sizer.Clear(False)

        self.current_panel = self.screens[self.index](
            self.window, data, self.next_screen
        )

        self.sizer.Add(self.current_panel, 1, wx.EXPAND)

        self.window.Layout()

        self.index += 1
