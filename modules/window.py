import wx


def create_window():
    window = wx.Frame(None, title="Stupid Typing Game", style=wx.NO_BORDER)

    window.SetBackgroundColour(wx.BLACK)

    window.ShowFullScreen(True)

    return window
