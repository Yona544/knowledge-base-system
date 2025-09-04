---
title: Dotnet Adsdatareader Read
slug: dotnet_adsdatareader_read
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_read.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 99736569dc77c88addec3170cf9df6ee808d454e
---

# Dotnet Adsdatareader Read

AdsDataReader.Read

AdsDataReader.Read

Advantage .NET Data Provider

| AdsDataReader.Read  Advantage .NET Data Provider |  |  |  |  |

Advances the AdsDataReader to the next record.

public bool Read();

Remarks

Read returns True if it successfully positioned to the next row and False if there are no more rows. The default position of the AdsDataReader is prior to the first record. Therefore, you must call Read to begin accessing any data.

See Also

[AdsCommand.ExecuteReader](dotnet_adscommand_executereader.md)

[RecordCache](dotnet_adsdatareader_recordcache.md)
