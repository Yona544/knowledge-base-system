---
title: Dotnet Adsconnection Servertime
slug: dotnet_adsconnection_servertime
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_servertime.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 21be8d67f8c3de5987e3c00d13b55f59b3eec159
---

# Dotnet Adsconnection Servertime

AdsConnection.ServerTime

AdsConnection.ServerTime

Advantage .NET Data Provider

| AdsConnection.ServerTime  Advantage .NET Data Provider |  |  |  |  |

Gets the current server time on an open connection.

public DateTime ServerTime {get;}

Remarks

Retrieves the current time and date from the server via the Advantage Database Server. ServerTime is useful if the Advantage client application is running at a site that is in a different time zone than where the data is located and is being accessed by the Advantage Database Server. When Advantage is used in a WAN environment or is being used with the Advantage Internet Server, the Advantage client and Advantage server will often be located in different time zones. This API allows time, date, and timestamp fields to be populated with a consistent date and time, that is, the date and time of the server location.

Note The AdsConnection must be open when getting ServerTime.
