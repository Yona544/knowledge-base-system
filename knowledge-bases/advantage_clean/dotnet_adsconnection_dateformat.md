---
title: Dotnet Adsconnection Dateformat
slug: dotnet_adsconnection_dateformat
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_dateformat.htm
source: Advantage CHM
tags:
  - dotnet
checksum: a486053fc6569fec7089d0907680652132375957
---

# Dotnet Adsconnection Dateformat

AdsConnection.DateFormat

AdsConnection.DateFormat

Advantage .NET Data Provider

| AdsConnection.DateFormat  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the current date format on an open connection.

public string DateFormat{ get; set; )

Remarks

DateFormat affects how Advantage interprets date literals that appear directly in SQL statements. Normally, it is best to use the ANSI style date format ('yyyy-MM-dd') when specifying dates in SQL statements. The ANSI style is given preference in the case where a date value could be interpreted as a valid date with either format. If you specify DateFormat as 'DD/MM/YYYY', then the following SQL statements would be equivalent:

insert into demo10 (doh) values ('2000-01-13')

insert into demo10 (doh) values ('1/13/2000')

When setting DateFormat, the value is analyzed to determine the placement as well as the correct number of digits for the day, month, and year. DateFormat can also be used to specify separators in the date format. For example, "DD/MM/YYYY" and "DD-MM-YYYY" are both valid date formats. Only one character separators are supported.

The format retrieved may not be identical to the one set. For example, "dd-mm-yyyy" will return a format of "DD-MM-CCYY" (where CC is the century portion of the year).

Note The AdsConnection must be open when getting or setting DateFormat.

See Also

[AdsDataReader.GetDateTime](dotnet_adsdatareader_getdatetime.md)

[AdsExtendedReader.SetDateTime](dotnet_adsextendedreader_setdatetime.md)
