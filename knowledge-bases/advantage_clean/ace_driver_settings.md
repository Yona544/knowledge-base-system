---
title: Ace Driver Settings
slug: ace_driver_settings
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_driver_settings.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 421587a10041e37c02dd4ef47733e4b88773a929
---

# Ace Driver Settings

Driver Settings

Driver Settings

Advantage Client Engine

| Driver Settings  Advantage Client Engine |  |  |  |  |

There are several driver setting options that are set globally for the Advantage Client Engine process. These include settings such as the epoch, whether to show deleted records, and the date format. These settings apply to all connections, tables, and indexes in the process.

Note that these functions AdsSetLastError, AdsGetLastError, AdsRegisterCallbackFunction, and AdsClearCallbackFunction work on a thread level rather than globally. For example, if thread A calls an Advantage Client Engine API and an error occurs, only thread A may call AdsGetLastError to retrieve the information for that error.
