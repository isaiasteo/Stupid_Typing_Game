import wx

from modules.DisplayText import display_text


def create_submit_button(panel, text_field):
    button = wx.Button(panel, label="Submit")

    button.Bind(wx.EVT_BUTTON, lambda event: on_submit(event, text_field, panel))

    return button


def on_submit(event, text_field, panel):
    button = event.GetEventObject()

    user_text = text_field.GetValue()

    if not user_text.strip():
        return

    button.Destroy()
    text_field.Destroy()

    display_text(panel, user_text)

    panel.Layout()
