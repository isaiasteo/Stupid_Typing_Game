import wx


class Placeholder:

    def __init__(self, textctrl, text):
        self.textctrl = textctrl

        self.label = wx.StaticText(textctrl.GetParent(), label=text)

        self.label.SetForegroundColour(wx.Colour(120, 120, 120))

        x, y = textctrl.GetPosition()
        self.label.SetPosition((x + 8, y + 8))

        textctrl.Bind(wx.EVT_TEXT, self.update)
        self.label.Bind(wx.EVT_LEFT_DOWN, self.focus)

        self.update(None)

    def update(self, event):
        self.label.Show(self.textctrl.IsEmpty())

    def focus(self, event):
        self.textctrl.SetFocus()
