"""
Pomice
~~~~~~
The modern Lavalink wrapper designed for discord.py.

:copyright: 2021, cloudwithax
:license: GPL-3.0
"""
import discord

if not discord.version_info.major >= 2:
    class DiscordPyOutdated(Exception):
        pass

    raise DiscordPyOutdated(
        "You must have discord.py (v2.0 or greater) to use this library. "
        "Uninstall your current version and install discord.py 2.0 "
        "using 'pip install discord.py'"
    )

__version__ = "1.1.8a"
__title__ = "pomice"
__author__ = "cloudwithax"

from .enums import SearchType
from .events import *
from .exceptions import *
from .filters import *
from .objects import *
from .player import Player
from .pool import *
from .queue import *
