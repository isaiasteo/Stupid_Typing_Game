import wx


def setup_keyboard(panel):

    panel.input = wx.TextCtrl(panel, style=wx.TE_PROCESS_TAB)

    panel.input.SetSize((1, 1))
    panel.input.SetPosition((-10, -10))

    panel.input.Bind(wx.EVT_CHAR, panel.on_char)

    panel.input.Bind(wx.EVT_CHAR_HOOK, panel.on_char_hook)
