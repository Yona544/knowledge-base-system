---
title: Dotnet Adsdatareader Recordsaffected
slug: dotnet_adsdatareader_recordsaffected
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_recordsaffected.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 3f7785ddc796dba58a13550151bb65485bcd4cc0
---

# Dotnet Adsdatareader Recordsaffected

AdsDataReader.RecordsAffected

AdsDataReader.RecordsAffected

Advantage .NET Data Provider

| AdsDataReader.RecordsAffected  Advantage .NET Data Provider |  |  |  |  |

Gets the number of rows changed, inserted, or deleted by execution of the SQL statement.

public int RecordsAffected { get; }

Remarks

RecordsAffected retrieves the number of rows changed, inserted, or deleted; 0 if no rows were affected or the statement failed; and -1 for SELECT statements.

See Also

[AdsCommand.ExecuteNonQuery](dotnet_adscommand_executenonquery.md)
