from dataclasses import dataclass, fields
from Options import Choice, Toggle, DefaultOnToggle, Range, PerGameCommonOptions, StartInventoryPool, Visibility, OptionGroup, OptionSet, Accessibility
from .Enums import Items


class ShuffleBeehiveHoneycombs(Toggle):
    """
    Shuffles the honeycomb pieces hidden in beehives and shuffles them into the item pool.
    """
    display_name = "Shuffle Beehive Honeycombs"


class ShuffleBlueEggs(Toggle):
    """
    Shuffles blue egg pickups and shuffles them into the item pool.
    """
    display_name = "Shuffle Blue Eggs"


class ShuffleEmptyHoneycombs(DefaultOnToggle):
    """
    Shuffles empty honey comb locations and shuffles them into the item pool.
    """
    display_name = "Shuffle Empty Honeycombs"


class ShuffleExtraLives(Toggle):
    """
    Shuffles extra life pickups and shuffles them into the item pool.
    """
    display_name = "Shuffle Extra Lives"


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


class ShuffleMusicNotes(Toggle):
    """
    Shuffles all note locations and shuffles them into the item pool.
    """
    display_name = "Shuffle Music Notes"


class ShuffleStopNSwop(Toggle):
    """
    Shuffles the Stop 'N' Swop eggs and the Ice Key and shuffles them into the item pool.
    """
    display_name = "Shuffle Stop 'N' Swop"


@dataclass
class LighthouseOptions(PerGameCommonOptions):
    shuffle_beehive_honeycombs: ShuffleBeehiveHoneycombs
    shuffle_blue_eggs: ShuffleBlueEggs
    shuffle_empty_honeycombs: ShuffleEmptyHoneycombs
    shuffle_extra_lives: ShuffleExtraLives
    shuffle_jiggies: ShuffleJiggies
    shuffle_jinjos: ShuffleJinjos
    shuffle_molehills: ShuffleMolehills
    shuffle_mumbo_tokens: ShuffleMumboTokens
    shuffle_music_notes: ShuffleMusicNotes
    shuffle_stop_n_swop: ShuffleStopNSwop
    start_inventory_from_pool: StartInventoryPool


# One per upstream RO_SHUFFLE_* option. Everything that gates a check category off these
# (which locations exist, which items enter the pool, slot data, UT) iterates this.
SHUFFLE_OPTIONS = tuple(f.name for f in fields(LighthouseOptions) if f.name.startswith("shuffle_"))


lighthouse_option_groups = [
    OptionGroup("Shuffle Options", [
        ShuffleBeehiveHoneycombs,
        ShuffleBlueEggs,
        ShuffleEmptyHoneycombs,
        ShuffleExtraLives,
        ShuffleJiggies,
        ShuffleJinjos,
        ShuffleMolehills,
        ShuffleMumboTokens,
        ShuffleMusicNotes,
        ShuffleStopNSwop,
    ])
]
