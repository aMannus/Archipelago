from typing import NamedTuple
from BaseClasses import Item, ItemClassification as IC
from .Enums import *


class LighthouseItem(Item):
    game = "Banjo-Kazooie Lighthouse"


class GroupTag(IntFlag):
    BlueEgg = auto()
    EmptyHoneyComb = auto()
    ExtraLife = auto()
    Honeycomb = auto()
    Jiggy = auto()
    Jinjo = auto()
    Molehill = auto()
    MumboToken = auto()
    Note = auto()
    StopNSwap = auto()


class LighthouseItemData(NamedTuple):
    item_id: int | None
    classification: IC = IC.progression
    quantity_in_item_pool: int = 0
    tags: GroupTag | None = None


item_data_table: dict[Items, LighthouseItemData] = {
    # Items commented out that can never appear in the item pool and are only used on Ship internally
    Items.BLUE_EGG: LighthouseItemData(140, IC.filler, 0, tags=GroupTag.BlueEgg),
    Items.EMPTY_HONEYCOMB_BUBBLEGLOOP_SWAMP: LighthouseItemData(1, IC.useful, 0, tags=GroupTag.EmptyHoneyComb),
    Items.EMPTY_HONEYCOMB_CLANKERS_CAVERN: LighthouseItemData(2, IC.useful, 0, tags=GroupTag.EmptyHoneyComb),
    Items.EMPTY_HONEYCOMB_CLICK_CLOCK_WOOD: LighthouseItemData(3, IC.useful, 0, tags=GroupTag.EmptyHoneyComb),
    Items.EMPTY_HONEYCOMB_FREEZEEZY_PEAK: LighthouseItemData(4, IC.useful, 0, tags=GroupTag.EmptyHoneyComb),
    Items.EMPTY_HONEYCOMB_GOBIS_VALLEY: LighthouseItemData(5, IC.useful, 0, tags=GroupTag.EmptyHoneyComb),
    Items.EMPTY_HONEYCOMB_MAD_MONSTER_MANSION: LighthouseItemData(7, IC.useful, 0, tags=GroupTag.EmptyHoneyComb),
    Items.EMPTY_HONEYCOMB_MUMBOS_MOUNTAIN: LighthouseItemData(8, IC.useful, 0, tags=GroupTag.EmptyHoneyComb),
    Items.EMPTY_HONEYCOMB_RUSTY_BUCKET_BAY: LighthouseItemData(9, IC.useful, 0, tags=GroupTag.EmptyHoneyComb),
    Items.EMPTY_HONEYCOMB_SPIRAL_MOUNTAIN: LighthouseItemData(10, IC.useful, 0, tags=GroupTag.EmptyHoneyComb),
    Items.EMPTY_HONEYCOMB_TREASURE_TROVE_COVE: LighthouseItemData(11, IC.useful, 0, tags=GroupTag.EmptyHoneyComb),
    Items.EXTRA_LIFE: LighthouseItemData(141, IC.filler, 0, tags=GroupTag.ExtraLife),
    Items.HONEYCOMB: LighthouseItemData(142, IC.filler, 0, tags=GroupTag.Honeycomb),
    Items.JIGGY_BUBBLEGLOOP_SWAMP: LighthouseItemData(12, IC.progression, 0, tags=GroupTag.Jiggy),
    Items.JIGGY_CLANKERS_CAVERN: LighthouseItemData(13, IC.progression, 0, tags=GroupTag.Jiggy),
    Items.JIGGY_CLICK_CLOCK_WOOD: LighthouseItemData(14, IC.progression, 0, tags=GroupTag.Jiggy),
    Items.JIGGY_FREEZEEZY_PEAK: LighthouseItemData(15, IC.progression, 0, tags=GroupTag.Jiggy),
    Items.JIGGY_GOBIS_VALLEY: LighthouseItemData(16, IC.progression, 0, tags=GroupTag.Jiggy),
    Items.JIGGY_GRUNTILDAS_LAIR: LighthouseItemData(17, IC.progression, 0, tags=GroupTag.Jiggy),
    Items.JIGGY_MAD_MONSTER_MANSION: LighthouseItemData(18, IC.progression, 0, tags=GroupTag.Jiggy),
    Items.JIGGY_MUMBOS_MOUNTAIN: LighthouseItemData(19, IC.progression, 0, tags=GroupTag.Jiggy),
    Items.JIGGY_RUSTY_BUCKET_BAY: LighthouseItemData(20, IC.progression, 0, tags=GroupTag.Jiggy),
    Items.JIGGY_TREASURE_TROVE_COVE: LighthouseItemData(21, IC.progression, 0, tags=GroupTag.Jiggy),
    Items.JINJO_BLUE_BUBBLEGLOOP_SWAMP: LighthouseItemData(22, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_BLUE_CLANKERS_CAVERN: LighthouseItemData(23, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_BLUE_CLICK_CLOCK_WOOD: LighthouseItemData(24, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_BLUE_FREEZEEZY_PEAK: LighthouseItemData(25, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_BLUE_GOBIS_VALLEY: LighthouseItemData(26, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_BLUE_MAD_MONSTER_MANSION: LighthouseItemData(27, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_BLUE_MUMBOS_MOUNTAIN: LighthouseItemData(28, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_BLUE_RUSTY_BUCKET_BAY: LighthouseItemData(29, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_BLUE_TREASURE_TROVE_COVE: LighthouseItemData(30, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_GREEN_BUBBLEGLOOP_SWAMP: LighthouseItemData(31, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_GREEN_CLANKERS_CAVERN: LighthouseItemData(32, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_GREEN_CLICK_CLOCK_WOOD: LighthouseItemData(33, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_GREEN_FREEZEEZY_PEAK: LighthouseItemData(34, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_GREEN_GOBIS_VALLEY: LighthouseItemData(35, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_GREEN_MAD_MONSTER_MANSION: LighthouseItemData(36, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_GREEN_MUMBOS_MOUNTAIN: LighthouseItemData(37, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_GREEN_RUSTY_BUCKET_BAY: LighthouseItemData(38, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_GREEN_TREASURE_TROVE_COVE: LighthouseItemData(39, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_ORANGE_BUBBLEGLOOP_SWAMP: LighthouseItemData(40, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_ORANGE_CLANKERS_CAVERN: LighthouseItemData(41, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_ORANGE_CLICK_CLOCK_WOOD: LighthouseItemData(42, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_ORANGE_FREEZEEZY_PEAK: LighthouseItemData(43, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_ORANGE_GOBIS_VALLEY: LighthouseItemData(44, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_ORANGE_MAD_MONSTER_MANSION: LighthouseItemData(45, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_ORANGE_MUMBOS_MOUNTAIN: LighthouseItemData(46, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_ORANGE_RUSTY_BUCKET_BAY: LighthouseItemData(47, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_ORANGE_TREASURE_TROVE_COVE: LighthouseItemData(48, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_PINK_BUBBLEGLOOP_SWAMP: LighthouseItemData(49, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_PINK_CLANKERS_CAVERN: LighthouseItemData(50, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_PINK_CLICK_CLOCK_WOOD: LighthouseItemData(51, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_PINK_FREEZEEZY_PEAK: LighthouseItemData(52, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_PINK_GOBIS_VALLEY: LighthouseItemData(53, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_PINK_MAD_MONSTER_MANSION: LighthouseItemData(54, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_PINK_MUMBOS_MOUNTAIN: LighthouseItemData(55, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_PINK_RUSTY_BUCKET_BAY: LighthouseItemData(56, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_PINK_TREASURE_TROVE_COVE: LighthouseItemData(57, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_YELLOW_BUBBLEGLOOP_SWAMP: LighthouseItemData(58, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_YELLOW_CLANKERS_CAVERN: LighthouseItemData(59, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_YELLOW_CLICK_CLOCK_WOOD: LighthouseItemData(60, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_YELLOW_FREEZEEZY_PEAK: LighthouseItemData(61, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_YELLOW_GOBIS_VALLEY: LighthouseItemData(62, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_YELLOW_MAD_MONSTER_MANSION: LighthouseItemData(63, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_YELLOW_MUMBOS_MOUNTAIN: LighthouseItemData(64, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_YELLOW_RUSTY_BUCKET_BAY: LighthouseItemData(65, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.JINJO_YELLOW_TREASURE_TROVE_COVE: LighthouseItemData(66, IC.progression, 0, tags=GroupTag.Jinjo),
    Items.MOLEHILL_BARGE: LighthouseItemData(67, IC.progression, 0, tags=GroupTag.Molehill),
    Items.MOLEHILL_BEAK_BOMB: LighthouseItemData(68, IC.progression, 0, tags=GroupTag.Molehill),
    Items.MOLEHILL_BEAK_BUSTER: LighthouseItemData(69, IC.progression, 0, tags=GroupTag.Molehill),
    Items.MOLEHILL_CAMERA_CONTROL: LighthouseItemData(70, IC.progression, 0, tags=GroupTag.Molehill),
    Items.MOLEHILL_CLAW_SWIPE: LighthouseItemData(71, IC.progression, 0, tags=GroupTag.Molehill),
    Items.MOLEHILL_CLIMB: LighthouseItemData(72, IC.progression, 0, tags=GroupTag.Molehill),
    Items.MOLEHILL_DIVE: LighthouseItemData(73, IC.progression, 0, tags=GroupTag.Molehill),
    Items.MOLEHILL_EGGS: LighthouseItemData(74, IC.progression, 0, tags=GroupTag.Molehill),
    Items.MOLEHILL_FLAP_FLIP: LighthouseItemData(75, IC.progression, 0, tags=GroupTag.Molehill),
    Items.MOLEHILL_FLIGHT: LighthouseItemData(76, IC.progression, 0, tags=GroupTag.Molehill),
    Items.MOLEHILL_SHOCK_JUMP: LighthouseItemData(77, IC.progression, 0, tags=GroupTag.Molehill),
    Items.MOLEHILL_TALON_TROT: LighthouseItemData(78, IC.progression, 0, tags=GroupTag.Molehill),
    Items.MOLEHILL_TURBO_TALON: LighthouseItemData(79, IC.progression, 0, tags=GroupTag.Molehill),
    Items.MOLEHILL_WADING_BOOTS: LighthouseItemData(80, IC.progression, 0, tags=GroupTag.Molehill),
    Items.MOLEHILL_WONDERWING: LighthouseItemData(81, IC.progression, 0, tags=GroupTag.Molehill),
    Items.MUMBO_TOKEN: LighthouseItemData(143, IC.progression, 0, tags=GroupTag.MumboToken),
    Items.MUSIC_NOTE_BUBBLEGLOOP_SWAMP: LighthouseItemData(92, IC.progression_deprioritized_skip_balancing, 0, tags=GroupTag.Note),
    Items.MUSIC_NOTE_CLANKERS_CAVERN: LighthouseItemData(93, IC.progression_deprioritized_skip_balancing, 0, tags=GroupTag.Note),
    Items.MUSIC_NOTE_CLICK_CLOCK_WOOD: LighthouseItemData(94, IC.progression_deprioritized_skip_balancing, 0, tags=GroupTag.Note),
    Items.MUSIC_NOTE_FREEZEEZY_PEAK: LighthouseItemData(95, IC.progression_deprioritized_skip_balancing, 0, tags=GroupTag.Note),
    Items.MUSIC_NOTE_GOBIS_VALLEY: LighthouseItemData(96, IC.progression_deprioritized_skip_balancing, 0, tags=GroupTag.Note),
    Items.MUSIC_NOTE_MAD_MONSTER_MANSION: LighthouseItemData(97, IC.progression_deprioritized_skip_balancing, 0, tags=GroupTag.Note),
    Items.MUSIC_NOTE_MUMBOS_MOUNTAIN: LighthouseItemData(98, IC.progression_deprioritized_skip_balancing, 0, tags=GroupTag.Note),
    Items.MUSIC_NOTE_RUSTY_BUCKET_BAY: LighthouseItemData(99, IC.progression_deprioritized_skip_balancing, 0, tags=GroupTag.Note),
    Items.MUSIC_NOTE_TREASURE_TROVE_COVE: LighthouseItemData(100, IC.progression_deprioritized_skip_balancing, 0, tags=GroupTag.Note),
    Items.STOP_N_SWOP_EGG_BLUE: LighthouseItemData(101, IC.progression, 0, tags=GroupTag.StopNSwap),
    Items.STOP_N_SWOP_EGG_CYAN: LighthouseItemData(102, IC.progression, 0, tags=GroupTag.StopNSwap),
    Items.STOP_N_SWOP_EGG_GREEN: LighthouseItemData(103, IC.progression, 0, tags=GroupTag.StopNSwap),
    Items.STOP_N_SWOP_EGG_PINK: LighthouseItemData(104, IC.progression, 0, tags=GroupTag.StopNSwap),
    Items.STOP_N_SWOP_EGG_RED: LighthouseItemData(105, IC.progression, 0, tags=GroupTag.StopNSwap),
    Items.STOP_N_SWOP_EGG_YELLOW: LighthouseItemData(106, IC.progression, 0, tags=GroupTag.StopNSwap),
    Items.STOP_N_SWOP_ICE_KEY: LighthouseItemData(107, IC.progression, 0, tags=GroupTag.StopNSwap),
    # Intentionally place the glitched item without a value. Everything else should be above this.
    Items.GLITCHED: LighthouseItemData(None),
}


item_table = {name.value: data.item_id for name,
              data in item_data_table.items() if data.item_id}
