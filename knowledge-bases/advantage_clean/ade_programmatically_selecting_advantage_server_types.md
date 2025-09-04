---
title: Ade Programmatically Selecting Advantage Server Types
slug: ade_programmatically_selecting_advantage_server_types
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_programmatically_selecting_advantage_server_types.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2f4a1158273b6b3c932a9047b3d7815b9ac52ef4
---

# Ade Programmatically Selecting Advantage Server Types

Programmatically Selecting Advantage Server Types

Programmatically Selecting Advantage Server Types

Advantage TDataSet Descendant

| Programmatically Selecting Advantage Server Types  Advantage TDataSet Descendant |  |  |  |  |

Advantage server types can be selected programmatically using one of three methods:

- Setting the TAdsConnection component's AdsServerTypes property:

[Selecting Advantage Server Types via the TAdsConnection Component](ade_selecting_advantage_server_types_via_the_tadsconnection_component.md)

- Setting the TAdsSettings component's [AdsServerTypes](ade_adsservertypes_adssettings.md) property:

[Selecting Advantage Server Types via the TAdsSettings Component](ade_selecting_advantage_server_types_via_the_tadssettings_component.md)

- Setting the value for the ADS\_SERVER\_TYPE key in the ads.ini file:

[Selecting Advantage Server Types via the ADS.INI File](master_selecting_advantage_server_types_via_the_ads_ini_file.md)

The ADS\_SERVER\_TYPE setting in the ads.ini will only be used if a TAdsConnection or TAdsSettings component is not used in the application.
