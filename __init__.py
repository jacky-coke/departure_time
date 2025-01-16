from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry):
    """Set up Departure Time Manager from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    # Example service registration
    async def add_time_service(call):
        time = call.data.get("time")
        times = hass.states.get(f"{DOMAIN}.times").state.split(",")
        times.append(time)
        hass.states.async_set(f"{DOMAIN}.times", ",".join(times))

    async def remove_time_service(call):
        time = call.data.get("time")
        times = hass.states.get(f"{DOMAIN}.times").state.split(",")
        times = [t for t in times if t != time]
        hass.states.async_set(f"{DOMAIN}.times", ",".join(times))

    hass.services.async_register(DOMAIN, "add_time", add_time_service)
    hass.services.async_register(DOMAIN, "remove_time", remove_time_service)

    # Initialize an entity to store times
    hass.states.async_set(f"{DOMAIN}.times", "")

    return True
