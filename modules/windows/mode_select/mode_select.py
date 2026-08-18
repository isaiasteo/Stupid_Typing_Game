import wx

from modules.windows.mode_select.create_mode_card import create_mode_card
from modules.windows.mode_select.select_mode import select_mode


class ModeSelect(wx.Panel):
    def __init__(self, parent, data, next_screen):
        super().__init__(parent)

        self.data = data if data is not None else {}
        self.next_screen = next_screen
        self.selected_mode = None

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(self, label="Choose a Game Mode")
        title.SetForegroundColour(wx.WHITE)

        font = title.GetFont()
        font.SetPointSize(18)
        font.MakeBold()
        title.SetFont(font)

        main_sizer.Add(title, 0, wx.ALL | wx.CENTER, 15)

        self.result_text = wx.StaticText(self, label="Choose a game flavor")
        self.result_text.SetForegroundColour(wx.LIGHT_GREY)

        main_sizer.Add(self.result_text, 0, wx.BOTTOM | wx.CENTER, 10)

        self.scroll = wx.ScrolledWindow(self, style=wx.HSCROLL)
        self.scroll.SetScrollRate(20, 0)

        self.cards_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.scroll.SetSizer(self.cards_sizer)

        modes = [
            {
                "id": "easy",
                "title": "Easy",
                "description": (
                    "Marathons starts with a single step. \n \n"
                    "*Color marks the position"
                ),
                "image": "modules/images/easy_mode.png",
            },
            {
                "id": "normal",
                "title": "Normal",
                "description": (
                    "The intended way to be played. \n \n" "*No visual clue to aid"
                ),
                "image": "modules/images/normal_mode.jpg",
            },
            {
                "id": "hard",
                "title": "Hard",
                "description": (
                    "Where did the text go? \n \n" "* You need to use your memory."
                ),
                "image": "modules/images/hard_mode.png",
            },
        ]

        for mode in modes:
            card = create_mode_card(
                self.scroll,
                mode,
                self.handle_mode_selection,
            )

            self.cards_sizer.Add(card, 0, wx.ALL, 10)

        main_sizer.Add(self.scroll, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        self.continue_button = wx.Button(self, label="Continue")
        self.continue_button.Disable()
        self.continue_button.Bind(wx.EVT_BUTTON, self.on_continue)

        main_sizer.Add(self.continue_button, 0, wx.ALL | wx.CENTER, 15)

        self.SetSizer(main_sizer)

    def handle_mode_selection(self, mode):
        self.selected_mode = select_mode(
            mode,
            self.data,
            self.cards_sizer,
            self.continue_button,
            self.result_text,
        )

    def on_continue(self, event):
        if self.selected_mode is not None:
            self.next_screen(index=1, data=self.data)
