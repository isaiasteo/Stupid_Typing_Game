import wx
import wx.richtext


def paint_progress(text_control, position):
    style = wx.TextAttr()
    style.SetTextColour(wx.Colour(255, 105, 180))

    text_control.SetStyle(
        wx.richtext.RichTextRange(0, position),
        style,
    )


def reset_color(text_control, text_length):
    style = wx.TextAttr()
    style.SetTextColour(wx.WHITE)

    text_control.SetStyle(
        wx.richtext.RichTextRange(0, text_length),
        style,
    )
