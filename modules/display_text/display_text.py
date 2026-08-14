import wx

from modules.sfx.sound_effects import sfx
from .layout import setup_layout
from .keyboard import setup_keyboard
from .typing import check_character
from .text_glitch import text_glitch
from .cronometer import cronometer
from .coloring import paint_progress, reset_color


class display_text(wx.Panel):

    def __init__(self, parent, data, next_screen):
        super().__init__(parent)

        self.next_screen = next_screen

        self.target_text = str(data).replace("\r\n", "\n").replace("\r", "\n")

        self.display_text = self.target_text.replace("\n", "⏎\n")

        self.position = 0

        self.cronometer = cronometer(self)

        setup_layout(self)
        setup_keyboard(self)

        self.label.Bind(wx.EVT_LEFT_DOWN, lambda event: self.input.SetFocus())

        self.glitch = text_glitch(self)

        self.input.SetFocus()

    def on_char_hook(self, event):
        key = event.GetKeyCode()

        if key in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
            self.check_character("\n")
            sfx("modules/SFX/enter.wav")
            return

        event.Skip()

    def on_char(self, event):
        unicode_key = event.GetUnicodeKey()

        if unicode_key == wx.WXK_NONE:
            event.Skip()
            return

        typed = chr(unicode_key)

        if typed == "\r":
            return

        self.check_character(typed)

    def check_character(self, typed):

        self.cronometer.start()

        result = check_character(self.target_text, self.position, typed)

        if result.correct:

            sfx("modules/SFX/click.wav")
            paint_progress(self.label, result.position)

        else:

            sfx("modules/SFX/error.wav")

            self.glitch.start()

            reset_color(self.label, len(self.target_text))

        self.position = result.position

        if result.finished:

            self.cronometer.stop()

            sfx("modules/SFX/correct.mp3")

            self.next_screen()
