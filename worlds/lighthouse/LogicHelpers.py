from typing import TYPE_CHECKING

from BaseClasses import Location, Region
from .Locations import LighthouseLocation
from .Enums import *
from .Items import LighthouseItem
from rule_builder.rules import *
from rule_builder.field_resolvers import *
from .Options import *

if TYPE_CHECKING:
    from . import LighthouseWorld

import logging
logger = logging.getLogger("LIGHTHOUSE.Logic")

def add_locations(parent_region: Regions, world: "LighthouseWorld", locations: list[tuple[Locations, Rule]]) -> None:
    mLocations : list[tuple[str, int, Rule]] = list()
    for loc in locations:
        locationName = str(loc[0])
        if locationName in world.included_locations:
            locationAddress = world.included_locations.pop(loc[0]).loc_id
            if len(loc) > 1:
                locationRule = loc[1]((parent_region, world)) if callable(loc[1]) else loc[1]
            mLocations.append((locationName, locationAddress, locationRule))

    if len(mLocations) > 0:
        # Create the whole batch of locations at once
        world.get_region(str(parent_region)).add_locations({mLoc[0]: mLoc[1] for mLoc in mLocations}, LighthouseLocation)

        # Set rules
        for mLocation in mLocations:
            locationRule = mLocation[2]
            location: Location = world.get_location(mLocation[0])
            world.set_rule(location, locationRule)


def connect_regions(parent_region: Regions, world: "LighthouseWorld", child_regions: list[tuple[Regions, Rule]]) -> None:
    parentRegion: Region = world.get_region(str(parent_region))

    for region in child_regions:
        childRegion = world.get_region(region[0])
        
        if len(region) > 1:
            regionRule = region[1]((parent_region, world)) if callable(region[1]) else region[1]  # type: ignore # noqa
        world.create_entrance(parentRegion, childRegion, regionRule)


def add_events(parent_region: Regions, world: "LighthouseWorld", events: list[tuple[StrEnum, Events | StrEnum, Rule]]) -> None:
    parentRegion: Region = world.get_region(str(parent_region))

    for event in events:
        eventName = str(event[0])
        eventItemName = str(event[1])
        eventRule = event[2]((parent_region, world)) if callable(event[2]) else event[2]
        # test_for_age_check(eventRule, parent_region, world)
        parentRegion.add_event(eventName, eventItemName, eventRule, LighthouseLocation, LighthouseItem)
