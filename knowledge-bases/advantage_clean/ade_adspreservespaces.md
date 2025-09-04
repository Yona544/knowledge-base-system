---
title: Ade Adspreservespaces
slug: ade_adspreservespaces
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adspreservespaces.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3558eb6992183d88f547583ec60507f679495f13
---

# Ade Adspreservespaces

AdsPreserveSpaces

AdsTableOptions.AdsPreserveSpaces

Advantage TDataSet Descendant

| AdsTableOptions.AdsPreserveSpaces  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.md)

Boolean flag used to specify if you want character fields set as empty strings to be written as a buffer of spaces instead of converted to a NULL/empty value.

Syntax

property AdsTableOptions.AdsPreserveSpaces

Description

The default value of this option is False, which will result in behavior that mimics Paradox behavior, where empty strings are set as NULL when posting new field values.

If you change this option to True, any character fields that are assigned an empty string value, or are assigned a buffer of spaces, will be written as such, and will not be converted into a NULL value.

Note that fields that are not specifically set (during an append/insert operation, for example) will still contain NULL values unless you explicitly set the fields to contain empty strings.
