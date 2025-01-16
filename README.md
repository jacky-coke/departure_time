# Departure Time Manager

The **Departure Time Manager** integration for Home Assistant allows you to dynamically manage and automate departure times for your vehicle or other entities.

## Features
- Add or remove departure times dynamically via the Home Assistant UI.
- Automatically clear expired departure times 5 minutes after they pass.
- Provides a sensor displaying the next upcoming departure time.
- Fully customizable logic to fit your needs.

## Installation

1. Clone or download this repository.
2. Copy the `departure_time_manager` folder into your `custom_components` directory in your Home Assistant configuration folder.
3. Restart Home Assistant.

## Configuration

1. In the Home Assistant UI, navigate to **Settings > Devices & Services**.
2. Click **Add Integration** and search for "Departure Time Manager".
3. During setup, specify the entity representing your car or another device.

## Usage

- Add a new departure time by calling the service `departure_time_manager.add_time` with the desired time in `HH:MM` format.
- Remove a departure time by calling the service `departure_time_manager.remove_time` with the specific time to delete.
- The sensor `sensor.next_departure_time` will always show the next upcoming departure time.

## Localization

This integration supports English (`en`) and German (`de`) translations.

## Example Services

### Add a Departure Time

```yaml
service: departure_time_manager.add_time
data:
  time: "08:30"
```

### Remove a Departure Time

```yaml
service: departure_time_manager.remove_time
data:
  time: "08:30"
```

## Development

Feel free to fork this repository and contribute to its development. Pull requests are welcome!

## License

This project is licensed under the MIT License.
