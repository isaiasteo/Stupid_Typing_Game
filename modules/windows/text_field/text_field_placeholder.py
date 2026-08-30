import wx
from modules.windows.text_field.text_field_placeholder_style import apply_style


class placeholder:

    def __init__(self, textctrl, text):
        self.textctrl = textctrl

        self.label = wx.StaticText(textctrl.GetParent(), label=text)

        apply_style(self.label)

        textctrl.Bind(wx.EVT_TEXT, self.update)
        self.label.Bind(wx.EVT_LEFT_DOWN, self.focus)
        textctrl.SetFocus()

        wx.CallAfter(self.center)

        self.update(None)

    def center(self):
        x, y = self.textctrl.GetPosition()
        width, height = self.textctrl.GetSize()

        label_width, label_height = self.label.GetBestSize()

        self.label.SetPosition(
            (
                x + (width - label_width) // 2,
                y + (height - label_height) // 2,
            )
        )

    def update(self, event):
        self.label.Show(self.textctrl.IsEmpty())

    def focus(self, event):
        self.textctrl.SetFocus()
