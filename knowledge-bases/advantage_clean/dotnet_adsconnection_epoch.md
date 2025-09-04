---
title: Dotnet Adsconnection Epoch
slug: dotnet_adsconnection_epoch
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_epoch.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 5610fbb3fe4a4d06c5aeb76ce0f870e298174b3b
---

# Dotnet Adsconnection Epoch

AdsConnection.Epoch

AdsConnection.Epoch

Advantage .NET Data Provider

| AdsConnection.Epoch  Advantage .NET Data Provider |  |  |  |  |

Sets the default epoch to determine how dates without century digits are interpreted.

public static short Epoch{ get; set; }

Remarks

Epoch determines how date literals that appear directly in SQL statements are interpreted if they contain only two-year digits. For example, if a date is given as "5/15/98", then the Epoch value will be used to determine the full four-digit year. If a date is given as "5/15/1998", then the Epoch setting is not used. Setting Epoch affects all currently connected Advantage servers, and will be sent to any Advantage servers with which new connections are established.

Epoch will be interpreted as the 100-year range for the two-digit year. For example, if the Epoch value is 1970, a two digit year of "96" will be interpreted as 1996, while a two digit year of "12" will be interpreted as 2012.

The default epoch value is 1900. Dates are physically stored in the table with the century information. Thus, changing the epoch setting does not affect dates in existing tables.

Note Epoch is a global setting that affects the behavior of the entire application.

See Also

[DateFormat](dotnet_adsconnection_dateformat.md)
