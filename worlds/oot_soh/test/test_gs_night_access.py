from .. import SohWorld
from ..Items import progressive_items, Items, Locations
from ..Enums import Regions
from .bases import SohTestBase


class TestNightGS(SohTestBase):
    options = {"closed_forest": 0}
    world: SohWorld

    def test_night_gs_no_time_reachable_location(self):
        """
        Checking if player can access KF_GS_KNOW_IT_ALL_HOUSE without a region to change time
        """
        self.collect_by_name(Items.KOKIRI_SWORD)

        self.assertFalse(self.can_reach_location(Locations.KF_GS_KNOW_IT_ALL_HOUSE),
                         f"Was able to access the night GS when shouldn't have.")

    def test_night_gs_with_time_reachable_location(self):
        """
        Checking if player can access KF_GS_KNOW_IT_ALL_HOUSE with a region to change time
        """
        self.collect_by_name([Items.KOKIRI_SWORD, Items.PROGRESSIVE_SCALE])

        self.assertTrue(self.can_reach_location(Locations.KF_GS_KNOW_IT_ALL_HOUSE),
                        f"Wasn't able to access the night GS.")
