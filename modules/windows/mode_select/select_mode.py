import wx


def select_mode(mode, data, cards_sizer, continue_button, result_text):
    selected_mode = mode["id"]

    data["mode"] = selected_mode

    continue_button.Enable()
    result_text.SetLabel(f"Selected: {mode['title']}")

    for item in cards_sizer.GetChildren():
        card = item.GetWindow()

        if card is None:
            continue

        selected = getattr(card, "mode", {}).get("id") == selected_mode

        card.SetBackgroundColour(
            wx.Colour(70, 110, 160) if selected else wx.Colour(40, 40, 40)
        )

        card.Refresh()

    return selected_mode
