"""Constants for the Swatch Time integration."""
from __future__ import annotations

from typing import Final

from homeassistant.const import Platform

DOMAIN: Final = "swatch_time"
PLATFORMS = [Platform.SENSOR]

CONF_DISPLAY_OPTIONS = "display_options"

OPTION_TYPES = [
    "swatch_time",
]