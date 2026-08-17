It comes from a user pasted chunk of text. User copies something, pastes it to the clipboard of the stupid game. The goal is to perfect type the text pasted. No time limit, but with a second counter. Upon successful entry of the whole text, a simple screen is displayed: "X seconds". For each typed character, the game checks if it was the right one pressed. For example, the text says: "An apple a day keeps the doctor away." For each letter typed, the game checks whether the right key was pressed, or the right character was inserted in the field, whichever is less CPU expensive. IF a character was entered wrong, a simple sound effect plays, and then... this is interesting part: the whole progress is erased, and the user should start typing the text again from the beginning.

That's it. This is the whole thing. Pretty simple.

# Python version 3.13
# pip install wx
# pip install pygame

![Screenshot](modules/images/screenshots/screenshot_1.png)
