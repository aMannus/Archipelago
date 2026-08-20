from typing import TYPE_CHECKING

from .Enums import *
from .Items import item_data_table, LighthouseItem, GroupTag
from BaseClasses import ItemClassification
from .Locations import category_location_tables

if TYPE_CHECKING:
    from . import LighthouseWorld


def create_item_pool(world: "LighthouseWorld") -> None:
    items_to_create: dict[str, int] = {
        item: data.quantity_in_item_pool for item, data in item_data_table.items()}
    
    # A shuffled category's vanilla items all go into the pool; the rest stay preplaced.
    for option_name, table in category_location_tables.items():
        if getattr(world.options, option_name):
            for location_name, loc_data in table.items():
                if location_name not in world.included_locations:  # skip the uncreated ones
                    items_to_create[loc_data.vanilla_item] += 1
    # TODO: make the notes that aren't needed for a note door useful rather than progression

    items: list[LighthouseItem] = list()
    # Add regular item pool
    for item, quantity in items_to_create.items():
        items.extend([world.create_item(item) for _ in range(quantity)])

    world.add_items_to_item_pool_list(items)
