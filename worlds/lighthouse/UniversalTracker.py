from typing import TYPE_CHECKING
from .Options import *

if TYPE_CHECKING:
    from . import LighthouseWorld


def setup_options_from_slot_data(world: "LighthouseWorld") -> None:
    if hasattr(world.multiworld, "re_gen_passthrough"):
        if "Banjo-Kazooie Lighthouse" in world.multiworld.re_gen_passthrough:
            world.using_ut = True
            world.passthrough = world.multiworld.re_gen_passthrough["Lighthouse"]
            world.options.shuffle_honey_combs.value = world.passthrough["shuffle_honey_combs"]
            world.options.shuffle_jiggies.value = world.passthrough["shuffle_jiggies"]
            world.options.shuffle_jinjos.value = world.passthrough["shuffle_jinjos"]
            world.options.shuffle_molehills.value = world.passthrough["shuffle_molehills"]
            world.options.shuffle_mumbo_tokens.value = world.passthrough["shuffle_mumbo_tokens"]
            world.options.shuffle_notes.value = world.passthrough["shuffle_notes"]
            # when adding new options to this, use .get, and set the default to whatever was before the option was made
            # this will make it back-compatible with seeds generated on earlier versions
            # the below do not need to be handled in UT at all, since they do not affect logic
            # apworld_version
        else:
            world.using_ut = False
    else:
        world.using_ut = False
