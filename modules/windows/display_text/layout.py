import wx
import wx.richtext


def setup_layout(panel):

    sizer = wx.BoxSizer(wx.VERTICAL)
    panel.SetSizer(sizer)

    panel.label = wx.richtext.RichTextCtrl(
        panel,
        style=wx.richtext.RE_READONLY,
    )

    panel.label.SetCanFocus(False)
    panel.label.Enable(False)
    panel.label.Bind(wx.EVT_LEFT_DOWN, lambda event: None)
    panel.label.Bind(wx.EVT_LEFT_UP, lambda event: None)
    panel.label.Bind(wx.EVT_RIGHT_DOWN, lambda event: None)
    panel.label.Bind(wx.EVT_RIGHT_UP, lambda event: None)
    panel.label.Bind(wx.EVT_MOTION, lambda event: None)
    panel.label.SetCanFocus(False)

    panel.label.SetBackgroundColour(wx.BLACK)

    font = panel.label.GetFont()
    font.SetPointSize(14)
    panel.label.SetFont(font)

    panel.label.WriteText(panel.display_text)

    if panel.mode == "hard":
        text_colour = wx.BLACK
    else:
        text_colour = wx.WHITE

    panel.label.SetForegroundColour(text_colour)

    panel.label.SetStyle(
        0,
        len(panel.display_text),
        wx.TextAttr(colText=text_colour),
    )

    sizer.Add(panel.label, 1, wx.ALL | wx.EXPAND, 20)

    panel.Layout()
