from dataclasses import dataclass

@dataclass
class CreatureDataClass():
    name: str
    country: str
    area: str
    description: str
    aka: str

dataclass_thing = CreatureDataClass(
    "yeti",
    "CN",
    "Himalayas",
    "Hirsute Himalyan",
    "Abominable Snowman"
)
print("Name is", dataclass_thing.name)