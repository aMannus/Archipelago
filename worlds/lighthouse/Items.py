from typing import NamedTuple
from enum import IntEnum, IntFlag
from BaseClasses import Item, ItemClassification as IC
from .Enums import *


class LighthouseItem(Item):
    game = "Banjo-Kazooie Lighthouse"


class GroupTag(IntFlag):
    Notes = auto()


class LighthouseItemData(NamedTuple):
    item_id: int | None
    classification: IC = IC.progression
    quantity_in_item_pool: int = 0
    tags: GroupTag | None = None


item_data_table: dict[Items, LighthouseItemData] = {
    # Items commented out that can never appear in the item pool and are only used on Ship internally

    Items.MUSIC_NOTE: LighthouseItemData(1, IC.progression | IC.useful, 1, tags=GroupTag.Notes),
    Items.FILLER_ITEM: LighthouseItemData(1, IC.filler, 1),
    # Intentionally place the glitched item without a value. Everything else should be above this.
    Items.GLITCHED: LighthouseItemData(None),
}


item_table = {name.value: data.item_id for name,
              data in item_data_table.items() if data.item_id}


filler_items = [
    Items.FILLER_ITEM
]
