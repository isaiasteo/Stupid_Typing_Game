import wx
import wx.richtext


def paint_progress(text_control, position, mode="easy"):
    reset_color(
        text_control,
        len(text_control.GetValue()),
        mode,
    )

    style = wx.TextAttr()
    style.SetTextColour(wx.Colour(255, 105, 180))

    text = text_control.GetValue()

    display_position = 0
    logical_position = 0

    for character in text:

        if logical_position >= position:
            break

        display_position += 1

        if character != "⏎":
            logical_position += 1

    text_control.SetStyle(
        wx.richtext.RichTextRange(0, display_position),
        style,
    )


def reset_color(text_control, text_length, mode="easy"):
    style = wx.TextAttr()

    if mode == "hard":
        style.SetTextColour(wx.BLACK)
    else:
        style.SetTextColour(wx.WHITE)

    text_control.SetStyle(
        wx.richtext.RichTextRange(0, text_length),
        style,
    )
