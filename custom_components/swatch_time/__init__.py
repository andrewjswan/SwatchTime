"""The swatch_time component."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import PLATFORMS


async def async_setup(hass: HomeAssistantType, hass_config: dict):
    """Set up Swatch Time from a config entry."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Swatch Time from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload Swatch Time config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)