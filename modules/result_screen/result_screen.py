import wx

from modules.components.create_button import create_button


def restart(event):
    print("Restart pressed, nothing happened.")


def record(event):
    print("Submit pressed, nothing happened.")


class ResultScreen(wx.Panel):
    def __init__(self, parent, data, next_screen):
        super().__init__(parent)

        self.data = data
        self.next_screen = next_screen

        self.result_text = wx.StaticText(self, label=str(self.data))
        self.result_text.SetForegroundColour(wx.WHITE)
        font = self.result_text.GetFont()
        font.SetPointSize(14)
        self.result_text.SetFont(font)

        btn_restart = create_button(
            self, "Restart", restart, position=(250, 200), size=(120, 40)
        )
        btn_save_record = create_button(
            self, "Save Record", record, position=(450, 200), size=(120, 40)
        )

        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(self.result_text, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(sizer)
