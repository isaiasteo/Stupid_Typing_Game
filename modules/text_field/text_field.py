import wx
from .text_field_style import apply_style
from .text_field_placeholder import Placeholder
from .text_field_submit_button import create_submit_button


class TextField(wx.Panel):
    def __init__(self, parent, data, next_screen):
        super().__init__(parent)

        self.next_screen = next_screen

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.text_field = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        Placeholder(
            self.text_field,
            "Welcome. \n This game will test your typing skills. \n To start, type or paste a text, then press [Submit] \n Your job is to perfectly type was was submited. \n \n Good luck!",
        )

        apply_style(self.text_field)

        self.submit_button = create_submit_button(
            self, self.text_field, self.next_screen
        )

        sizer.Add(self.text_field, 1, wx.ALL | wx.EXPAND, 10)
        sizer.Add(self.submit_button, 0, wx.ALL, 10)

        self.SetSizer(sizer)
