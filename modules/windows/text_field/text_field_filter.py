import wx

ALLOWED_CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 \t\r\n!@#$%^&*()-_=+[]{}\\|;:'\",.<>/?`~áàâãäéèêëíìîïóòôõöúùûüçÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÜÇ"


class TextFilter:
    def __init__(self, text_ctrl):
        self.text_ctrl = text_ctrl
        self.timer = wx.Timer(self.text_ctrl)
        self.text_ctrl.Bind(wx.EVT_TIMER, self._purge, self.timer)
        self.timer.Start(1000)

    def _purge(self, event):
        current_text = self.text_ctrl.GetValue()
        filtered_text = "".join(
            char for char in current_text if char in ALLOWED_CHARACTERS
        )

        if current_text != filtered_text:
            position = self.text_ctrl.GetInsertionPoint()

            removed_before = sum(
                char not in ALLOWED_CHARACTERS for char in current_text[:position]
            )

            self.text_ctrl.ChangeValue(filtered_text)
            self.text_ctrl.SetInsertionPoint(max(0, position - removed_before))
