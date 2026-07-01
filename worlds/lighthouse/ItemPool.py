from typing import TYPE_CHECKING

from .Enums import *
from .Items import item_data_table, filler_items, LighthouseItem
from BaseClasses import ItemClassification

if TYPE_CHECKING:
    from . import LighthouseWorld


def create_item_pool(world: "LighthouseWorld") -> None:
    items_to_create: dict[str, int] = {
        item: data.quantity_in_item_pool for item, data in item_data_table.items()}

    items: list[LighthouseItem] = list()
    # Add regular item pool
    for item, quantity in items_to_create.items():
        items.extend([world.create_item(item) for _ in range(quantity)])

    world.add_items_to_item_pool_list(items)


def get_filler_item(world: "LighthouseWorld") -> str:
    return world.random.choice(filler_items)
