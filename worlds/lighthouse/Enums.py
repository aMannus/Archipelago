from enum import StrEnum, IntEnum, auto, Enum
# allows defining orders with fewer functions; with this decorator only __eq__ and __lt__ is needed, and since enums implement __eq__ we can just implement __lt__
from functools import total_ordering


class Regions(StrEnum):
    """List of all region enums"""

    ROOT = "Menu"
    ROOT_EXITS = "Root Exits"


class Items(StrEnum):
    JINJO = "Jinjo"
    MUSIC_NOTE = "Music Note"
    FILLER_ITEM = "Filler Item"
    MAX = "Max"
    # Universal Tracker Required
    GLITCHED = "Glitched Item"


class Locations(StrEnum):
    BANJOS_POCKET = "Banjo's Pocket"
    FINAL_BOSS = "Final Boss"
    ANOTHER_LOCATION = "Another Location"


class Events(StrEnum):
    CAN_ENTER_X_AREA = "Can Enter X Area"
    GAME_COMPLETED = "Game Completed"
