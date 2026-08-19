import wx


def create_window():
    window = wx.Frame(None, title="Stupid Typing Game", size=(800, 600))

    window.SetBackgroundColour(wx.BLACK)

    window.Centre()

    return window
