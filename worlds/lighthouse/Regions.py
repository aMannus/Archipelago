from typing import NamedTuple, TYPE_CHECKING
from BaseClasses import MultiWorld, Region, LocationProgressType
from .Enums import *
from .Locations import empty_honeycombs_location_table, \
    jiggies_location_table, jinjos_location_table, \
    molehills_location_table, mumbo_tokens_location_table, \
    notes_location_table, stop_n_swop_eggs_location_table
from .location_access import root

if TYPE_CHECKING:
    from . import LighthouseWorld


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
    world.included_locations.update(empty_honeycombs_location_table)
    world.included_locations.update(jiggies_location_table)
    world.included_locations.update(jinjos_location_table)
    world.included_locations.update(molehills_location_table)
    world.included_locations.update(mumbo_tokens_location_table)
    world.included_locations.update(notes_location_table)
    world.included_locations.update(stop_n_swop_eggs_location_table)

    # Set region rules and location rules after all locations are created
    all_regions = [root]
    for region in all_regions:
        region.set_region_rules(world)


def place_locked_item(location: Locations, item: Items, world: "LighthouseWorld") -> None:
    lighthouse_item = world.create_item(item)
    world.get_location(location).place_locked_item(lighthouse_item)
    world.preplaced_items.append(lighthouse_item)

def place_locked_items(world: "LighthouseWorld") -> None:
    # Preplace items when they're not shuffled.
    if not world.options.shuffle_honey_combs:
        for location_name, loc_data in empty_honeycombs_location_table.items():
            set_vanilla_location(location_name, loc_data.vanilla_item, world)

    if not world.options.shuffle_jiggies:
        for location_name, loc_data in jiggies_location_table.items():
            set_vanilla_location(location_name, loc_data.vanilla_item, world)

    if not world.options.shuffle_jinjos:
        for location_name, loc_data in jinjos_location_table.items():
            set_vanilla_location(location_name, loc_data.vanilla_item, world)

    if not world.options.shuffle_molehills:
        for location_name, loc_data in molehills_location_table.items():
            set_vanilla_location(location_name, loc_data.vanilla_item, world)

    if not world.options.shuffle_mumbo_tokens:
        for location_name, loc_data in mumbo_tokens_location_table.items():
            set_vanilla_location(location_name, loc_data.vanilla_item, world)

    if not world.options.shuffle_notes:
        for location_name, loc_data in notes_location_table.items():
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
