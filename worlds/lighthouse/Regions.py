from typing import NamedTuple, TYPE_CHECKING
from BaseClasses import MultiWorld, Region, LocationProgressType
from .Enums import *
from .Locations import base_location_table, \
    another_location_table
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

    # Base locations
    world.included_locations.update(base_location_table)

    # Gold Skulltulas (Overworld)
    world.included_locations.update(
        another_location_table)

    # Set region rules and location rules after all locations are created
    all_regions = [root]
    for region in all_regions:
        region.set_region_rules(world)


def place_locked_item(location: Locations, item: Items, world: "LighthouseWorld") -> None:
    lighthouse_item = world.create_item(item)
    world.get_location(location).place_locked_item(lighthouse_item)
    world.preplaced_items.append(lighthouse_item)


def place_locked_items(world: "LighthouseWorld") -> None:
    if world.options.closed_forest == "off":
        world.get_location(Locations.BANJOS_POCKET).progress_type = LocationProgressType.PRIORITY


def connect_to_root(location: Locations, world: "LighthouseWorld"):
    loc = world.get_location(location)

    # Connect to Root if not already
    region = loc.parent_region
    root = world.get_region(Regions.ROOT)
    if region != root:
        region.locations.remove(loc)
        loc.parent_region = root
        root.locations.append(loc)
