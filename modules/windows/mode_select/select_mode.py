import wx


def select_mode(mode, data, cards_sizer, continue_button, result_text, scroll):
    selected_mode = mode["id"]

    data["mode"] = selected_mode

    continue_button.Enable()
    result_text.SetLabel(f"Selected: {mode['title']}")

    selected_card = None

    for item in cards_sizer.GetChildren():
        card = item.GetWindow()

        if card is None:
            continue

        selected = getattr(card, "mode", {}).get("id") == selected_mode

        if selected:
            selected_card = card

        card.SetBackgroundColour(
            wx.Colour(70, 110, 160) if selected else wx.Colour(40, 40, 40)
        )

        card.Refresh()

    if selected_card is not None:
        scroll_width = scroll.GetClientSize().width
        card_position = selected_card.GetPosition().x
        card_width = selected_card.GetSize().width

        target = card_position - (scroll_width - card_width) // 2
        scroll.Scroll(max(0, target // 20), 0)

    scroll_width = scroll.GetClientSize().width
    card_position = selected_card.GetPosition().x
    card_width = selected_card.GetSize().width

    target = card_position - (scroll_width - card_width) // 2
    scroll.Scroll(max(0, target // 20), 0)

    return selected_mode
