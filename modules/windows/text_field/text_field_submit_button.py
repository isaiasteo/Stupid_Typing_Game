import wx


def create_submit_button(panel, text_field, data, next_screen):
    button = wx.Button(panel, label="Submit")

    button.Bind(
        wx.EVT_BUTTON, lambda event: on_submit(event, text_field, data, next_screen)
    )

    return button


def on_submit(event, text_field, data, next_screen):
    user_text = text_field.GetValue()

    if not user_text.strip():
        return

    data["text"] = user_text

    next_screen(index=4, data=data)
