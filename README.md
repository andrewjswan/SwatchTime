# SwatchTime for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-blue.svg)](https://github.com/custom-components/hacs)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/andrewjswan/SwatchTime/validate.yml?logo=github)](https://github.com/andrewjswan/SwatchTime/actions)
[![GitHub](https://img.shields.io/github/license/andrewjswan/SwatchTime?color=blue)](https://github.com/andrewjswan/SwatchTime/blob/master/LICENSE)
[![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/andrewjswan/SwatchTime?include_prereleases)](https://github.com/andrewjswan/SwatchTime/releases)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/downloads-pre/andrewjswan/SwatchTime/latest/total?label=release@downloads)](https://github.com/andrewjswan/SwatchTime/releases)
[![StandWithUkraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md)

Create [Swatch / Internet Time](https://en.wikipedia.org/wiki/Swatch_Internet_Time) sensor for [Home Assistant](https://www.home-assistant.io/).

![Swatch Time](logo.png)

## Description

In version Home Assistant 2024.2.0, it was decided to [remove](https://github.com/home-assistant/core/pull/106871) the Swatch / Internet time (beat) sensor from the Time & Date integration, a message appeared in the logs:
```
The `beat` Time & Date sensor is being removed
This stops working in version 2024.7.0. Please address before upgrading.
Please remove the `beat` key from the `display_options` for the time_date entry in your configuration.yaml file and restart Home Assistant to fix this issue.
```
This custom integration returns this sensor to Home Assistant, the functionality remains the same.

## Installation

**Method 1.** [HACS](https://hacs.xyz/) custom repo:

> HACS > Integrations > 3 dots (upper top corner) > Custom repositories > URL: `andrewjswan/SwatchTime`, Category: Integration > Add > wait > SwatchTime > Install

**Method 2.** Manually copy `swatch_time` folder from [latest release](https://github.com/andrewjswan/SwatchTime/releases/latest) to `/config/custom_components` folder.

## Configuration

**Method 1.** GUI:

> Configuration > Integrations > Add Integration > **SwatchTime**

If the integration is not in the list, you need to clear the browser cache.

**Method 2.** YAML:

```yaml
swatch_time:
```
