from dataclasses import dataclass
from Options import Choice, Toggle, DefaultOnToggle, Range, PerGameCommonOptions, StartInventoryPool, Visibility, OptionGroup, OptionSet, Accessibility
from .Enums import Items


class ShuffleHoneyCombs(DefaultOnToggle):
    """
    Shuffles empty honey comb locations and shuffles them into the item pool.
    """
    display_name = "Shuffle Honey Combs"


class ShuffleJiggies(DefaultOnToggle):
    """
    Shuffles jiggy locations and shuffles them into the item pool.
    """
    display_name = "Shuffle Jiggies"


class ShuffleJinjos(DefaultOnToggle):
    """
    Shuffles all coloured jinjo locations and shuffles them into the item pool.
    """
    display_name = "Shuffle Jinjos"


class ShuffleMolehills(Toggle):
    """
    Shuffles molehills amongst each other, so all molehills will teach a random ability.
    """
    display_name = "Shuffle Molehills"


class ShuffleMumboTokens(Toggle):
    """
    Shuffles mumbo locations and shuffles them into the item pool.
    """
    display_name = "Shuffle Mumbo Tokens"


class ShuffleNotes(Toggle):
    """
    Shuffles all note locations and shuffles them into the item pool.
    """
    display_name = "Shuffle Notes"


@dataclass
class LighthouseOptions(PerGameCommonOptions):
    shuffle_honey_combs: ShuffleHoneyCombs
    shuffle_jiggies: ShuffleJiggies
    shuffle_jinjos: ShuffleJinjos
    shuffle_molehills: ShuffleMolehills
    shuffle_mumbo_tokens: ShuffleMumboTokens
    shuffle_notes: ShuffleNotes
    start_inventory_from_pool: StartInventoryPool


lighthouse_option_groups = [
    OptionGroup("Shuffle Options", [
        ShuffleHoneyCombs,
        ShuffleJiggies,
        ShuffleJinjos,
        ShuffleMolehills,
        ShuffleMumboTokens,
        ShuffleNotes,
    ])
]
