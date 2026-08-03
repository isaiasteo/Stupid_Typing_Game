def StoreText(user_text):
    with open("user_text.txt", "w", encoding="utf-8") as file:
        file.write(user_text)
