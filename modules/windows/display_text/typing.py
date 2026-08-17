from dataclasses import dataclass


@dataclass
class CharacterResult:
    position: int
    correct: bool
    finished: bool


def check_character(target_text, position, typed):

    if position >= len(target_text):
        return CharacterResult(position=position, correct=False, finished=True)

    expected = target_text[position]

    if typed == expected:

        position += 1

        if position == len(target_text):
            return CharacterResult(position=0, correct=True, finished=True)

        return CharacterResult(position=position, correct=True, finished=False)

    return CharacterResult(position=0, correct=False, finished=False)
