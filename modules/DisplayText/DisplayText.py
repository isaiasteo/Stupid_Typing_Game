import wx
import time

from modules.SFX.sound_effects import sfx


class DisplayText(wx.Panel):

    def __init__(self, parent, data, next_screen):
        super().__init__(parent)

        # =====================================================
        # State
        # =====================================================

        self.next_screen = next_screen

        self.target_text = str(data).replace("\r\n", "\n").replace("\r", "\n")

        self.position = 0

        # =====================================================
        # Layout
        # =====================================================

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        self.label = wx.StaticText(self, label=self.target_text)

        self.label.SetForegroundColour(wx.WHITE)
        self.label.SetBackgroundColour(wx.BLACK)

        font = self.label.GetFont()
        font.SetPointSize(14)
        self.label.SetFont(font)

        self.label.Wrap(650)

        sizer.Add(self.label, 0, wx.ALL | wx.CENTER, 20)

        # =====================================================
        # Hidden keyboard input
        # =====================================================

        self.input = wx.TextCtrl(self, style=wx.TE_PROCESS_TAB)

        self.input.SetSize((1, 1))
        self.input.SetPosition((-10, -10))

        # -----------------------------------------------------
        # Character events
        # -----------------------------------------------------

        self.input.Bind(wx.EVT_CHAR, self.on_char)

        # -----------------------------------------------------
        # Key hook
        # -----------------------------------------------------

        self.input.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)

        # Give focus to the TextCtrl
        self.input.SetFocus()

        self.Layout()

    # =========================================================
    # KEY HOOK
    # =========================================================

    def on_char_hook(self, event):

        key = event.GetKeyCode()

        # Enter / Return
        if key in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):

            self.check_character("\n")

            return

        event.Skip()

    # =========================================================
    # NORMAL CHARACTERS
    # =========================================================

    def on_char(self, event):

        unicode_key = event.GetUnicodeKey()

        if unicode_key == wx.WXK_NONE:
            event.Skip()
            return

        typed = chr(unicode_key)

        if typed == "\r":
            return

        self.check_character(typed)

    # =========================================================
    # CHECK CHARACTER
    # =========================================================

    def check_character(self, typed):

        print(f"typed = {typed!r}")

        if self.position >= len(self.target_text):
            return

        expected = self.target_text[self.position]

        # -----------------------------------------------------
        # Correct
        # -----------------------------------------------------

        if typed == expected:

            self.position += 1

            print(f"Correct: {typed!r}")

            if self.position == len(self.target_text):

                sfx("modules/DisplayText/correct.mp3")

                print("Finished!")

                self.next_screen()

        # -----------------------------------------------------
        # Wrong
        # -----------------------------------------------------

        else:

            sfx("modules/DisplayText/libby_retry.mp3")

            time.sleep(0.05)

            print(f"Wrong: {typed!r}, " f"expected {expected!r}")

            self.position = 0
