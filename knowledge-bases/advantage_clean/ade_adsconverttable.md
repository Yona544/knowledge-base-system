---
title: Ade Adsconverttable
slug: ade_adsconverttable
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsconverttable.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 6c778cdd0fa9e4e30fa4efad8e5d1fe17511861e
---

# Ade Adsconverttable

AdsConvertTable

TAdsTable/TAdsQuery.AdsConvertTable

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsConvertTable  Advantage TDataSet Descendant |  |  |  |  |

Converts a dataset structure and associated records to a new table of a different type.

Syntax

procedure AdsConvertTable( const strFileName : string;

eTableType : TadsTableTypes );

Parameters

| strFileName | Name of the file to copy to. |
| eTableType | Type of table. |

Description

The new table will contain data types capable of storing the information, but the field size may change. For example, when converting from a DBF dataset, AdsfldNUMERIC fields are converted to the same type but the field size will be increased by one. This is because the AdsfldNUMERIC type in the ADT table reserves one byte for the sign of the values stored in the field.

Whenever conversions to DBF tables are performed, the new DBF table will contain only standard DBF field types if possible. These data types include AdsfldLOGICAL, AdsfldNUMERIC, AdsfldDATE, AdsfldSTRING, and AdsfldMEMO

The records copied to the new table depend on the filter option selected under AdsTableOptions.AdsFilterOptions and AdsTableOptions.AdsScopeOptions. The following table determines how the different combinations of these options will behave:

| Options Set | Respects Filters | Respects Scopes |
| RESPECT\_WHEN\_COUNTING  RESPECT\_SCOPES\_WHEN\_COUNTING | X | X |
| RESPECT\_WHEN\_COUNTING  IGNORE\_SCOPES\_WHEN\_COUNTING | X | X |
| IGNORE\_WHEN\_COUNTING  RESPECT\_SCOPES\_WHEN\_COUNTING |  | X |
| IGNORE\_WHEN\_COUNTING  IGNORE\_SCOPES\_WHEN\_COUNTING |  |  |

Index files will not be copied as they can be created after the copy. The resulting table must be opened by the application after making the copy in order to use it.

You cannot convert Paradox tables with this method. Use the Advantage Data Architect to convert Paradox tables to Advantage tables. The Advantage Data Architect can be downloaded from the Advantage Developer Zone Web site at http://DevZone.AdvantageDatabase.com.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

 

Note This function is illegal in a transaction.

Example

AdsTable1.DatabaseName := 'x:\Data';

AdsTable1.TableType := ttAdsCDX;

AdsTable1.TableName := 'zipcode.DBF';

AdsTable1.Active := TRUE;;

 

AdsTable1.AdsConvertTable( 'x:\data\zipcode.adt', ttAdsADT );

See Also

[AdsCopyTableContents](ade_adscopytablecontents.md)

[AdsCopyTableStructure](ade_adscopytablestructure.md)
