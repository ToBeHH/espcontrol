# Guition ESP32-P4 JC1060P470 (7")

7-inch touch LCD panel with ESP32-P4, running ESPHome and LVGL for home automation control. Configure buttons, temperature display, and screensaver settings through the built-in web UI -- no YAML editing required after the initial flash.

![Guition ESP32-P4 JC1060P470](../images/guition-esp32-p4-jc1060p470.jpg)

## Configuration

- **Template**: [esphome.yaml](esphome.yaml) — use the **contents of this file as your ESPHome config** in the dashboard or CLI (create or edit your device config so it matches this file).

## Where to Buy

- **Panel**: [AliExpress](https://s.click.aliexpress.com/e/_c335W0r5) (~£40)

## Stand

- **Desk mount** (3D printable): [MakerWorld](https://makerworld.com/en/models/2387421-guition-esp32p4-jc1060p470-7inch-screen-desk-mount#profileId-2614995)

## Folder Structure

```
guition-esp32-p4-jc1060p470/
├── addon/          # Connectivity, time, backlight, network, firmware update
├── assets/         # Fonts and icons
├── config/         # User-configurable button, display, and screensaver settings
├── device/         # Hardware, LVGL UI, sensors, setup screens
├── theme/          # Button and UI styling
└── esphome.yaml    # ESPHome config template
```

## Setup Flow

1. Flash firmware (set device name and WiFi credentials in `esphome.yaml`)
2. Device boots with a loading screen, then connects to WiFi
3. If WiFi fails, a setup screen guides you to connect to the device's hotspot
4. Once connected, visit the device IP in your browser to configure buttons and display
5. Press "Apply Configuration" to restart with your settings

## Web UI Configuration

The webserver v3 interface exposes these setting groups:

- **Button Configuration**: Entity ID, custom label, icon selection
- **Display Configuration**: Indoor/outdoor temperature entity IDs
- **Screensaver**: Idle timeout (30s–30min), optional presence sensor entity
- **Firmware**: Auto-update toggle, update frequency, manual check
