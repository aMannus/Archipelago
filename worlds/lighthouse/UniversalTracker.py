from typing import TYPE_CHECKING
from .Options import *

if TYPE_CHECKING:
    from . import LighthouseWorld


def setup_options_from_slot_data(world: "LighthouseWorld") -> None:
    if hasattr(world.multiworld, "re_gen_passthrough"):
        if "Banjo-Kazooie Lighthouse" in world.multiworld.re_gen_passthrough:
            world.using_ut = True
            world.passthrough = world.multiworld.re_gen_passthrough["Lighthouse"]
            # A seed generated before an option existed didn't shuffle that category, so
            # missing keys default to off and stay back-compatible.
            for option_name in SHUFFLE_OPTIONS:
                getattr(world.options, option_name).value = world.passthrough.get(option_name, 0)
            # the below do not need to be handled in UT at all, since they do not affect logic
            # apworld_version
        else:
            world.using_ut = False
    else:
        world.using_ut = False
