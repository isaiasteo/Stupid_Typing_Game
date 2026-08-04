import wx
from .TextField_style import apply_style


def display_text(panel, text):
    label = wx.StaticText(panel, label=text)

    panel.GetSizer().Add(label, 0, wx.ALL | wx.CENTER, 20)

    panel.Layout()

    return label
