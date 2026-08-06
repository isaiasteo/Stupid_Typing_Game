import wx

import wx


def create_submit_button(panel, text_field, next_screen):
    button = wx.Button(panel, label="Submit")

    button.Bind(wx.EVT_BUTTON, lambda event: on_submit(event, text_field, next_screen))

    return button


def on_submit(event, text_field, next_screen):

    user_text = text_field.GetValue()

    if not user_text.strip():
        return

    next_screen(user_text)
