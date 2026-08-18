import wx


def create_mode_card(parent, mode, on_select):
    card = wx.Panel(parent, size=(300, 400))
    card.SetBackgroundColour(wx.Colour(40, 40, 40))

    sizer = wx.BoxSizer(wx.VERTICAL)

    image = wx.StaticBitmap(card, size=(280, 220))

    original_image = wx.Image(mode["image"], wx.BITMAP_TYPE_ANY)

    resized = original_image.Scale(280, 220, wx.IMAGE_QUALITY_HIGH)

    image.SetBitmap(wx.Bitmap(resized))

    sizer.Add(image, 0, wx.EXPAND | wx.ALL, 10)

    title = wx.StaticText(card, label=mode["title"])
    title.SetForegroundColour(wx.WHITE)

    font = title.GetFont()
    font.SetPointSize(14)
    font.MakeBold()
    title.SetFont(font)

    sizer.Add(title, 0, wx.CENTER | wx.ALL, 5)

    description = wx.StaticText(card, label=mode["description"])
    description.SetForegroundColour(wx.LIGHT_GREY)

    sizer.Add(description, 0, wx.EXPAND | wx.ALL, 10)

    card.SetSizer(sizer)

    card.Bind(wx.EVT_LEFT_UP, lambda event: on_select(mode))

    image.Bind(wx.EVT_LEFT_UP, lambda event: on_select(mode))

    title.Bind(wx.EVT_LEFT_UP, lambda event: on_select(mode))

    description.Bind(wx.EVT_LEFT_UP, lambda event: on_select(mode))

    card.mode = mode

    return card
