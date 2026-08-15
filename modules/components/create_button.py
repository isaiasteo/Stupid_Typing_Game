import wx


def create_button(parent, label, callback, position=(0, 0), size=None):
    button = wx.Button(parent, label=label)

    button.SetPosition(position)

    if size is not None:
        button.SetSize(size)

    font = button.GetFont()
    font.SetPointSize(12)
    button.SetFont(font)

    button.Bind(wx.EVT_BUTTON, callback)

    return button
