from dataclasses import dataclass
from Options import Choice, Toggle, DefaultOnToggle, Range, PerGameCommonOptions, StartInventoryPool, Visibility, OptionGroup, OptionSet, Accessibility
from .Enums import Items


class ClosedForest(Choice):
    """
    On - Kokiri Sword & Deku Shield are required to access the Deku Tree, and completing the Deku Tree is required to access the Lost Woods Bridge Exit.
    Deku Only - Kokiri boy no longer blocks the path to the Bridge but Mido still requires the Kokiri Sword and Deku Shield to access the tree.
    Off - Mido no longer blocks the path to the Deku Tree. Kokiri boy no longer blocks the path out of the forest.
    """
    display_name = "Closed Forest"
    option_on = 0
    option_deku_only = 1
    option_off = 2
    default = 2


@dataclass
class LighthouseOptions(PerGameCommonOptions):
    closed_forest: ClosedForest
    start_inventory_from_pool: StartInventoryPool


lighthouse_option_groups = [
    OptionGroup("Options", [
        ClosedForest,
    ])
]
