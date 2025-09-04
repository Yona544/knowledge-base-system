---
title: Dotnet Adsdataadapter Missingschemaaction
slug: dotnet_adsdataadapter_missingschemaaction
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdataadapter_missingschemaaction.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 8063b5f4842f4d415cf2c134f3bff44b86367b8c
---

# Dotnet Adsdataadapter Missingschemaaction

AdsDataAdapter.MissingSchemaAction

AdsDataAdapter.MissingSchemaAction

Advantage .NET Data Provider

| AdsDataAdapter.MissingSchemaAction  Advantage .NET Data Provider |  |  |  |  |

Indicates or specifies whether missing source tables, columns, and their relationships are added to the data set schema, ignored, or cause an error to be raised.

public MissingSchemaAction MissingSchemaAction {get; set;}

Remarks

The following table shows the valid values. The default is Add.

| Member Name | Description |
| Add | Adds the necessary columns to complete the schema. |
| AddWithKey | Adds the necessary columns and primary key information to complete the schema. |
| Error | A SystemException is generated. |
| Ignore | Ignores the extra columns. |
