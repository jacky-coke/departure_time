from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN

class FahrzeitenConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Departure Time Manager."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(
                title="Departure Time Manager",
                data=user_input
            )

        schema = vol.Schema({
            vol.Required("auto_entitaet"): str,  # Auto-Entität
        })
        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            description_placeholders={"integration_name": "Departure Time Manager"},
        )
