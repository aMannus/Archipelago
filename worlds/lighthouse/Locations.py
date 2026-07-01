from enum import StrEnum, IntFlag, auto
from typing import NamedTuple
from BaseClasses import CollectionState, Location
from .Enums import Locations


class LighthouseLocation(Location):
    game = "Banjo-Kazooie Lighthouse"


class LocTag(IntFlag):
    Overworld = auto()
    Boss = auto()


class LighthouseLocData(NamedTuple):
    loc_id: int | None = None
    tags: IntFlag | None = None


base_location_table: dict[str, LighthouseLocData] = {
    # Some are disabled because they're not real locations (ex Ganon and hint locations).

    Locations.BANJOS_POCKET: LighthouseLocData(2, LocTag.Overworld),
    Locations.FINAL_BOSS: LighthouseLocData(3, LocTag.Overworld)
}


another_location_table: dict[str, LighthouseLocData] = {
    Locations.ANOTHER_LOCATION: LighthouseLocData(3, LocTag.Overworld),
}


location_data_table: dict[str, LighthouseLocData] = {
    **base_location_table,
    **another_location_table,
}


location_table = {str(name): locdata.loc_id for name,
                  locdata in location_data_table.items()}
