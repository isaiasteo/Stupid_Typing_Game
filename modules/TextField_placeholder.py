import wx
from modules.TextField_placeholderStyle import apply_style


class Placeholder:

    def __init__(self, textctrl, text):
        self.textctrl = textctrl

        self.label = wx.StaticText(textctrl.GetParent(), label=text)

        apply_style(self.label)

        x, y = textctrl.GetPosition()
        self.label.SetPosition((x + 18, y + 12))  # 8

        textctrl.Bind(wx.EVT_TEXT, self.update)
        self.label.Bind(wx.EVT_LEFT_DOWN, self.focus)

        self.update(None)

    def update(self, event):
        self.label.Show(self.textctrl.IsEmpty())

    def focus(self, event):
        self.textctrl.SetFocus()
