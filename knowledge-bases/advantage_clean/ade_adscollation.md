---
title: Ade Adscollation
slug: ade_adscollation
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adscollation.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 0def6099ada4efa03170396638a1460d7be78fd7
---

# Ade Adscollation

ade\_Adscollation

AdsTableOptions.AdsCollation

Advantage TDataSet Descendant

| AdsTableOptions.AdsCollation  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.md)

Specifies the ANSI/OEM and Unicode collation to be used when comparing and sorting character data.

Syntax

 

property AdsTableOptions.AdsCollation;

 

Example

AdsQuery1.AdsTableOptions.AdsCollation := 'ANSI:en\_us';

Description

This setting specifies the collation that the ANSI and Unicode character data should be compared and sorted. This property, if set, overrides the AdsTableOptions.AdsCharType property. The property string consists two parts separated by the colon (:) character. The first part is the collation setting for ANSI, i.e. code page encoded, character data. The second part is the collation setting for Unicode character data. The collation for the code page encode string may be 'ANSI', 'OEM' or one of the dynamic collations such as 'POLISH\_VFP\_CI\_AS\_1250'. The 'ANSI' and 'OEM' setting specifies that server's default ANSI or OEM collation should be used. The collation for the Unicode character data is in the format of 'language\_locale\_option'. For example, 'en\_us' for English(US) or 'pl\_PL\_ads\_ci' for Polish(Poland) case insensitive. The available ANSI/OEM and Unicode collations can be retrieved by executing the sp\_getCollations() stored procedure:

execute procedure sp\_getCollations(null)

It is not required to specify both parts. If no Unicode fields are used in the application, the second part of the collation (including the colon character) may be omitted. For example: AdsQuery1.AdsTableOptions.AdsCollation := 'ANSI'; If there are Unicode character in the database, and the Unicode collation is not specified, the server will use a default Unicode collation that best matches the ANSI/OEM collation. The sp\_getCollations() stored procedure lists the default Unicode collation for the given ANSI/OEM collations. To specify only Unicode collation, include the colon character in the specification. For example, AdsQuery1.AdsTableOptions.AdsCollation := ':en\_us'; In this case, the Unicode character data will be sorted and compared using the en\_us collation. The non-Unicode character data will be sorted and compared using the setting specified by the AdsTableOptions.AdsCharType.

See Also

[AdsTableOptions.AdsCharType](ade_adschartype.htm "AdsCharType")

[sp\_getCollations](master_sp_getcollations.htm "sp_getCollations")

[Collation Support](master_collation_support.htm "Collations")
