import wx


class screen_manager:
    def __init__(self, window, screens):
        self.window = window
        self.screens = screens

        self.index = 3
        self.current_panel = None

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.window.SetSizer(self.sizer)

    def next_screen(self, data=None, index=None):
        if index is not None:
            self.index = index

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

    def restart(self):
        self.index = 0
        self.next_screen()
