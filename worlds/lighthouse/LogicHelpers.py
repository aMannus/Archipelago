from typing import TYPE_CHECKING

from BaseClasses import Location, Region
from .Locations import LighthouseLocation
from .Enums import *
from .Items import LighthouseItem, GroupTag
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


# Mumbo's price list, from __transformation_getCost() in core2/mumbo.c. Tokens are a
# global stash, so like the rando this counts every token held, not just the world's own.
TRANSFORMATION_COST: dict[Transformations, int] = {
    Transformations.TERMITE: 5,
    Transformations.CROC: 10,
    Transformations.WALRUS: 15,
    Transformations.PUMPKIN: 20,
    Transformations.BEE: 25,
}

# Jiggies per puzzle, from D_803947F8 in lair/jigsawpicture.c (lair order, which is
# not the level_e order the rando's CanOpenWorld indexes by).
PUZZLE_COST: dict[Worlds, int] = {
    Worlds.MUMBOS_MOUNTAIN: 1,
    Worlds.TREASURE_TROVE_COVE: 2,
    Worlds.CLANKERS_CAVERN: 5,
    Worlds.BUBBLEGLOOP_SWAMP: 7,
    Worlds.FREEZEEZY_PEAK: 8,
    Worlds.GOBIS_VALLEY: 9,
    Worlds.MAD_MONSTER_MANSION: 10,
    Worlds.RUSTY_BUCKET_BAY: 12,
    Worlds.CLICK_CLOCK_WOOD: 15,
    Worlds.GRUNTILDAS_LAIR: 25,  # the Door of Grunty picture
}

PUZZLE_BOARD_EVENT: dict[Worlds, Events] = {
    world: Events[f"PUZZLE_BOARD_{world.name}"] for world in Worlds if world != Worlds.GRUNTILDAS_LAIR
} | {Worlds.GRUNTILDAS_LAIR: Events.PUZZLE_BOARD_GRUNTILDA}


def can_use_transformation(transformation: Transformations) -> Rule:
    return HasGroup(GroupTag.MumboToken.name, TRANSFORMATION_COST[transformation])


def can_unlock_world(world: Worlds) -> Rule:
    return HasGroup(GroupTag.Jiggy.name, PUZZLE_COST[world]) & Has(PUZZLE_BOARD_EVENT[world])


def can_unlock_note_door(notes: int) -> Rule:
    return HasGroup(GroupTag.Note.name, notes) & Has(Events[f"NOTE_DOOR_{notes}"])


def can_collect_jinjos(world: Worlds) -> Rule:
    return HasAll(*(Items[f"JINJO_{colour}_{world.name}"] for colour in ("BLUE", "GREEN", "ORANGE", "PINK", "YELLOW")))


def can_attack() -> Rule:
    # Claw Swipe also teaches Roll and Rat-a-tat Rap, so one item covers all three.
    return HasAny(Items.MOLEHILL_CLAW_SWIPE, Items.MOLEHILL_EGGS, Items.MOLEHILL_BEAK_BUSTER,
                  Items.MOLEHILL_WONDERWING, Items.MOLEHILL_BARGE)


def can_extend_jump_distance() -> Rule:
    # Flap Flip also teaches Feathery Flap.
    return HasAny(Items.MOLEHILL_FLAP_FLIP, Items.MOLEHILL_CLAW_SWIPE, Items.MOLEHILL_TALON_TROT)


BREAKS_OBJECT: dict[Events, tuple[Items, ...]] = {
    Events.BREAK_OBJECT_BOULDER: (Items.MOLEHILL_BARGE, Items.MOLEHILL_EGGS, Items.MOLEHILL_BEAK_BUSTER,
                                  Items.MOLEHILL_WONDERWING),
    Events.BREAK_OBJECT_BRICK_WALL: (Items.MOLEHILL_BARGE, Items.MOLEHILL_WONDERWING, Items.MOLEHILL_CLAW_SWIPE,
                                     Items.MOLEHILL_EGGS),
    Events.BREAK_OBJECT_CELLAR_CASK: (Items.MOLEHILL_BARGE, Items.MOLEHILL_WONDERWING, Items.MOLEHILL_CLAW_SWIPE,
                                      Items.MOLEHILL_EGGS),
    Events.BREAK_OBJECT_WOODEN_DOOR: (Items.MOLEHILL_BARGE, Items.MOLEHILL_WONDERWING, Items.MOLEHILL_CLAW_SWIPE,
                                      Items.MOLEHILL_EGGS),
    Events.BREAK_OBJECT_GNAWTYS_BOULDER: (Items.MOLEHILL_BARGE, Items.MOLEHILL_BEAK_BUSTER, Items.MOLEHILL_EGGS,
                                          Items.MOLEHILL_WONDERWING),
    Events.BREAK_OBJECT_GRATE: (Items.MOLEHILL_EGGS, Items.MOLEHILL_CLAW_SWIPE),
    Events.BREAK_OBJECT_IRON_GATE: (Items.MOLEHILL_BARGE, Items.MOLEHILL_WONDERWING, Items.MOLEHILL_CLAW_SWIPE),
    Events.BREAK_OBJECT_WEB: (Items.MOLEHILL_EGGS,),
    Events.BREAK_OBJECT_WINDOWS: (Items.MOLEHILL_EGGS, Items.MOLEHILL_WONDERWING, Items.MOLEHILL_CLAW_SWIPE),
}


def can_break_object(object_type: Events) -> Rule:
    return HasAny(*BREAKS_OBJECT[object_type])


def can_kill_enemy(enemy: Enemies) -> Rule:
    if enemy == Enemies.SIR_SLUSH:
        return HasAll(Items.MOLEHILL_BEAK_BOMB, Items.MOLEHILL_FLIGHT)
    return HasAny(Items.MOLEHILL_BARGE, Items.MOLEHILL_WONDERWING, Items.MOLEHILL_CLAW_SWIPE)
