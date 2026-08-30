import wx

from .text_field_style import apply_style
from .text_field_placeholder import placeholder
from .text_field_submit_button import create_submit_button
from .text_field_filter import TextFilter
from modules.sfx.sound_effects import sfx


class text_field(wx.Panel):
    def __init__(self, parent, data, next_screen):
        super().__init__(parent)

        sfx("modules/sfx/voiceover/text_field.mp3")

        self.data = data if data is not None else {}
        self.next_screen = next_screen

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.text_field = wx.TextCtrl(
            self,
            style=wx.TE_MULTILINE,
        )

        TextFilter(self.text_field)

        placeholder(
            self.text_field,
            "Welcome.\nThis game tests your typing accuracy.\nType or paste a text, then press [Submit].\nReproduce it exactly.\nErrors are not accepted.\nProceed.",
        )

        apply_style(self.text_field)

        self.submit_button = create_submit_button(
            self,
            self.text_field,
            self.data,
            self.next_screen,
        )

        sizer.Add(self.text_field, 1, wx.ALL | wx.EXPAND, 10)
        sizer.Add(self.submit_button, 0, wx.ALIGN_CENTER | wx.BOTTOM, 20)

        self.SetSizer(sizer)
