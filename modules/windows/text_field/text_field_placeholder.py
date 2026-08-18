import wx
from modules.windows.text_field.text_field_placeholder_style import apply_style


class placeholder:

    def __init__(self, textctrl, text):
        self.textctrl = textctrl

        self.label = wx.StaticText(textctrl.GetParent(), label=text)

        apply_style(self.label)

        x, y = textctrl.GetPosition()
        self.label.SetPosition((x + 18, y + 12))

        textctrl.Bind(wx.EVT_TEXT, self.update)
        self.label.Bind(wx.EVT_LEFT_DOWN, self.focus)
        textctrl.SetFocus()

        self.update(None)

    def update(self, event):
        self.label.Show(self.textctrl.IsEmpty())

    def focus(self, event):
        self.textctrl.SetFocus()
