import wx


class DisplayText(wx.Panel):

    def __init__(self, parent, data, next_screen):
        super().__init__(parent)

        self.next_screen = next_screen
        self.target_text = str(data)
        self.position = 0

        # -------------------------
        # Layout
        # -------------------------

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        # Text the user needs to type
        self.label = wx.StaticText(self, label=self.target_text)

        self.label.SetForegroundColour(wx.WHITE)
        self.label.SetBackgroundColour(wx.BLACK)

        font = self.label.GetFont()
        font.SetPointSize(14)
        self.label.SetFont(font)

        self.label.Wrap(650)

        sizer.Add(self.label, 0, wx.ALL | wx.CENTER, 20)

        # -------------------------
        # Keyboard input
        # -------------------------

        self.input = wx.TextCtrl(self, style=wx.TE_PROCESS_TAB)

        # Make it effectively invisible
        self.input.SetSize((1, 1))
        self.input.SetPosition((-10, -10))

        # Listen for keyboard characters
        self.input.Bind(wx.EVT_CHAR, self.on_char)

        # Give the TextCtrl keyboard focus
        self.input.SetFocus()

        self.Layout()

    def on_char(self, event):

        key = event.GetUnicodeKey()

        # Ignore special keys
        if key == wx.WXK_NONE:
            event.Skip()
            return

        typed = chr(key)

        # Prevent going past the end
        if self.position >= len(self.target_text):
            return

        expected = self.target_text[self.position]

        if typed == expected:

            self.position += 1

            print(f"Correct: {typed!r}")

            # Finished typing the entire text
            if self.position == len(self.target_text):

                print("Finished!")

                self.next_screen()

        else:

            print(f"Wrong: {typed!r}, " f"expected {expected!r}")
