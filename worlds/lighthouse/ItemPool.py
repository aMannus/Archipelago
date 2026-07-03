from typing import TYPE_CHECKING

from .Enums import *
from .Items import item_data_table, LighthouseItem, GroupTag
from BaseClasses import ItemClassification
from .Locations import empty_honeycombs_location_table, \
    jiggies_location_table, jinjos_location_table, \
    molehills_location_table, mumbo_tokens_location_table, \
    notes_location_table, stop_n_swop_eggs_location_table

if TYPE_CHECKING:
    from . import LighthouseWorld


def create_item_pool(world: "LighthouseWorld") -> None:
    items_to_create: dict[str, int] = {
        item: data.quantity_in_item_pool for item, data in item_data_table.items()}
    
    if world.options.shuffle_honey_combs:
        for location_name, loc_data in empty_honeycombs_location_table.items():
            items_to_create[loc_data.vanilla_item] += 1

    if world.options.shuffle_jiggies:
        for location_name, loc_data in jiggies_location_table.items():
            items_to_create[loc_data.vanilla_item] += 1

    if world.options.shuffle_jinjos:
        for location_name, loc_data in jinjos_location_table.items():
            items_to_create[loc_data.vanilla_item] += 1

    if world.options.shuffle_molehills:
        for location_name, loc_data in molehills_location_table.items():
            items_to_create[loc_data.vanilla_item] += 1

    if world.options.shuffle_mumbo_tokens:
        for location_name, loc_data in mumbo_tokens_location_table.items():
            items_to_create[loc_data.vanilla_item] += 1

    if world.options.shuffle_notes:
        for location_name, loc_data in notes_location_table.items():
            items_to_create[loc_data.vanilla_item] += 1


    items: list[LighthouseItem] = list()
    # Add regular item pool
    for item, quantity in items_to_create.items():
        items.extend([world.create_item(item) for _ in range(quantity)])

    world.add_items_to_item_pool_list(items)
