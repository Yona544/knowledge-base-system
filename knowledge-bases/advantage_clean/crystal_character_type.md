---
title: Crystal Character Type
slug: crystal_character_type
product: Advantage Database Server
component: Crystal Reports
version: "12"
category: API
original_path_html: crystal_character_type.htm
source: Advantage CHM
tags:
  - crystal
  - crystal-reports
checksum: 108cf41d734f869988f58c1a51e1c16101ad48bb
---

# Crystal Character Type

Character Type

Character Type

Crystal Reports

| Character Type  Crystal Reports |  |  |  |  |

By default, the Advantage Crystal Reports Driver uses the ADS\_ANSI character type when opening .DBF tables. To force the Advantage Crystal Reports Driver to use the ADS\_OEM character type, add the following two lines to your ads.ini file:

 [Crystal]

 CharType=2 ; ADS\_ANSI=1 ADS\_OEM=2

If specified in the [Crystal] section of the ads.ini file, the setting will be global for use by all reports. If instead you would like to add a per-alias Character Type, the following syntax can be used (and often will already exist in your ads.ini file, as this is the format the Advantage Data Architect uses to store additional alias information):

 

 [<YourAliasName>\_info]

 CharType=ansi

Note when using a per-alias CharType, a string format is used, as opposed to 1 and 2 which are used in the global [Crystal] section.
