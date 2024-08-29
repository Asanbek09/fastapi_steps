from model import Creature

_creatures: list[Creature] = [
    Creature(
        name = "yeti",
        country = "CN",
        area = "Himalayas",
        description = "Hirsute Himalayan",
        aka = "abominable Snowman"
    ),
    Creature(
        name = "sasquatch",
        country = "USA",
        area = "***",
        description = "Yeti auf",
        aka = "BigFoot"
    )
]

def get_creatures() -> list[Creature]:
    return _creatures