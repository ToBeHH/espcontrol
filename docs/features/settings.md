---
title: Settings
description:
  How to configure appearance, brightness, temperature display, screensaver, backup, and firmware settings on your Espcontrol panel.
---

# Settings

The Settings tab in the [Setup](/features/setup) lets you adjust how your panel looks and behaves. Each section can be expanded or collapsed by tapping its heading.

## Appearance

- **On colour** — the colour buttons show when a device is switched on. Use the colour picker or type a colour code (for example, `FF8C00` for orange).
- **Off colour** — the colour buttons show when a device is switched off.

## Brightness

- **Daytime brightness** — how bright the screen is during the day (10%–100%).
- **Nighttime brightness** — how bright the screen is at night (10%–100%).
- **Sunrise / Sunset** — shows when the brightness will change each day. These update automatically based on your timezone.

## Temperature

- **Indoor temperature** — turn this on and choose which temperature sensor from Home Assistant to display (for example, a room thermometer).
- **Outdoor temperature** — same as above, but for an outdoor sensor.

Both temperatures appear in the top bar of the panel. You can enable one, both, or neither.

## Screensaver

The screensaver dims the screen and shows a gentle animation when the panel isn't being used. There are two ways to control it:

- **Timer** — the screensaver turns on after a set amount of idle time. Choose from **5, 10, 15, 20, 30, or 45 minutes**, or **1 hour**. The default is 5 minutes.
- **Sensor** — the screensaver is controlled by a motion or presence sensor. When the sensor detects someone nearby, the screen wakes up. When nobody is detected, the screen goes to sleep. Enter the name of your motion sensor from Home Assistant (for example, `binary_sensor.hallway_presence`).

Touching the screen always wakes it up, regardless of which mode you use.

## Backup

- **Export** — saves your entire setup (buttons, subpages, colours, and display settings) as a file you can keep as a backup.
- **Import** — loads a previously saved file to restore your setup. If you're loading a backup from a different-sized panel, the buttons are rearranged to fit automatically.

## Firmware

- **Version** — which version of the software your panel is running.
- **Check for Update** — press this to look for a newer version right now.
- **Auto Update** — turn this on to let the panel update itself automatically.
- **Update Frequency** — how often to check: Hourly, Daily, Weekly, or Monthly. Only shown when Auto Update is on.