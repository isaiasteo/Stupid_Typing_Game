import wx

from modules.StoreText import StoreText


def create_submit_button(panel, text_field):
    button = wx.Button(panel, label="Submit")

    button.Bind(wx.EVT_BUTTON, lambda event: on_submit(event, text_field))

    return button


def on_submit(event, text_field):
    user_text = text_field.GetValue()
    StoreText(user_text)
