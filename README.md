# SwatchTime for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Default-blue.svg?logo=HomeAssistantCommunityStore&logoColor=white)](https://github.com/custom-components/hacs)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/andrewjswan/SwatchTime/validate.yml?logo=github)](https://github.com/andrewjswan/SwatchTime/actions)
[![GitHub](https://img.shields.io/github/license/andrewjswan/SwatchTime?color=blue)](https://github.com/andrewjswan/SwatchTime/blob/master/LICENSE)
[![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/andrewjswan/SwatchTime?include_prereleases)](https://github.com/andrewjswan/SwatchTime/releases)
[![HA Installs][installs]](https://analytics.home-assistant.io/custom_integrations.json)
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

You could either install with [HACS](https://hacs.xyz/) (recommended) or manual.

### Method 1 (recommended):

[![hacs_default](https://img.shields.io/badge/HACS-Default-blue.svg?logo=HomeAssistantCommunityStore&logoColor=white)](https://hacs.xyz/)

This integration is part of the default [HACS](https://hacs.xyz/) repository. Just click Explore and add repository and search for `SwatchTime` to install, or use this link to go directly there:

[![Add to HACS via My Home Assistant][hacs-install-image]][hasc-install-url]

### Method 2:

[![hacs_custom](https://img.shields.io/badge/HACS-Custom-blue.svg?logo=HomeAssistantCommunityStore&logoColor=white)](https://hacs.xyz/)

1. Visit **HACS** → **Integrations** → **...** (3 dots - upper top corner) → **Custom repositories**
1. Click **Add**
1. Paste `andrewjswan/SwatchTime` into the **URL** field
1. Chose `Integration` as a **Category**
1. **SwatchTime** will appear in the list of available integrations. Install it normally.

### Method 3: 

[![manual](https://img.shields.io/badge/Manual-blue.svg?logo=HomeAssistantCommunityStore&logoColor=white)](https://github.com/andrewjswan/SwatchTime/releases/latest)

1. Manually copy `swatch_time` folder from [latest release](https://github.com/andrewjswan/SwatchTime/releases/latest) to `/config/custom_components` folder.
1. Restart **Home Assistant**

## Configuration

### Method 1 - GUI:

On **Devices and Services** page, click **Add Integration** and search for **SwatchTime**.

If the integration is not in the list, you need to clear the browser cache.

### Method 2 - YAML:

```yaml
swatch_time:
```

[installs]: https://img.shields.io/badge/dynamic/json?color=41BDF5&logo=home-assistant&label=integration%20usage&suffix=%20installs&cacheSeconds=15600&url=https://analytics.home-assistant.io/custom_integrations.json&query=$.swatch_time.total
[hasc-install-url]: https://my.home-assistant.io/redirect/hacs_repository/?owner=andrewjswan&repository=SwatchTime&category=integration
[hacs-install-image]: https://my.home-assistant.io/badges/hacs_repository.svg
