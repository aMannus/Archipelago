import logging
from typing import NamedTuple, TYPE_CHECKING
from BaseClasses import MultiWorld, Region, LocationProgressType
from .Enums import *
from .Locations import category_location_tables, stop_n_swop_eggs_location_table
from .location_access import root

if TYPE_CHECKING:
    from . import LighthouseWorld

logger = logging.getLogger("LIGHTHOUSE.Regions")


class LighthouseRegionData(NamedTuple):
    connecting_regions: list[str] = []


class LighthouseRegion(Region):
    game = "Banjo-Kazooie Lighthouse"

    def __init__(self, name: str, player: int, multiworld: MultiWorld, hint: str | None = None):
        super().__init__(name, player, multiworld, hint)


def create_regions_and_locations(world: "LighthouseWorld") -> None:

    # Fill region data table based on the regions enum list
    region_data_table: dict[str, LighthouseRegionData] = {}
    for entry in Regions:
        region_data_table[entry] = LighthouseRegionData([])

    # Create regions.
    for region_name in region_data_table.keys():
        region = LighthouseRegion(region_name, world.player, world.multiworld)
        world.multiworld.regions.append(region)
        region.add_exits(region_data_table[region_name].connecting_regions)

    # Create locations
    for table in category_location_tables.values():
        world.included_locations.update(table)
    world.included_locations.update(stop_n_swop_eggs_location_table)

    # Set region rules and location rules after all locations are created
    all_regions = [root]
    for region in all_regions:
        region.set_region_rules(world)

    # add_locations pops what it creates, so whatever is left in included_locations is a
    # check the rando lists but that no region places. It stays there as this world's skip
    # list -- place_locked_items and the item pool both leave those alone.
    for location_name in world.included_locations:
        logger.warning("%s is in Locations.py but no region places it; skipping", location_name)


def place_locked_item(location: Locations, item: Items, world: "LighthouseWorld") -> None:
    lighthouse_item = world.create_item(item)
    world.get_location(location).place_locked_item(lighthouse_item)
    world.preplaced_items.append(lighthouse_item)

def place_locked_items(world: "LighthouseWorld") -> None:
    # Preplace items when they're not shuffled.
    for option_name, table in category_location_tables.items():
        if not getattr(world.options, option_name):
            for location_name, loc_data in table.items():
                if location_name not in world.included_locations:  # skip the uncreated ones
                    set_vanilla_location(location_name, loc_data.vanilla_item, world)


def set_vanilla_location(location: str, item: Items, world: "LighthouseWorld") -> None:
    vanilla_item = world.create_item(item, True)
    world.get_location(location).place_locked_item(vanilla_item)
    world.get_location(location).address = None
    world.get_location(location).item.code = None


def connect_to_root(location: Locations, world: "LighthouseWorld"):
    loc = world.get_location(location)

    # Connect to Root if not already
    region = loc.parent_region
    root = world.get_region(Regions.ROOT)
    if region != root:
        region.locations.remove(loc)
        loc.parent_region = root
        root.locations.append(loc)
