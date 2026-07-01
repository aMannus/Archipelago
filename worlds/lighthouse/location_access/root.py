from ..LogicHelpers import *

if TYPE_CHECKING:
    from .. import LighthouseWorld


class EventLocations(StrEnum):
    FINAL_BOSS_DEFEATED = "Final Boss Defeated"


def set_region_rules(world: "LighthouseWorld") -> None:
    # Root
    # Events
    add_events(Regions.ROOT, world, [
        (EventLocations.FINAL_BOSS_DEFEATED, Events.GAME_COMPLETED, lambda bundle: True_())
    ])
    # Locations
    add_locations(Regions.ROOT, world, [
        (Locations.BANJOS_POCKET, lambda bundle: True_()),
        (Locations.FINAL_BOSS, lambda bundle: True_())
    ])
    # Connections
    connect_regions(Regions.ROOT, world, [
        (Regions.ROOT_EXITS, lambda bundle: True_())
    ])
