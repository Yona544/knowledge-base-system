AdsFilterOptions




Advantage Database Server 12  

AdsTableOptions.AdsFilterOptions

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTableOptions.AdsFilterOptions  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsTableOptions.AdsFilterOptions Advantage TDataSet Descendant ade\_Adsfilteroptions Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsTableOptions.AdsFilterOptions  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.htm)

When determining the record count, indicates whether to respect the filtering applied to the dataset. Filtering consists of all applicable filters, ranges, and scopes.

Syntax

type TAdsRespectFilters = ( IGNORE\_WHEN\_COUNTING, RESPECT\_WHEN\_COUNTING );

 

property AdsTableOptions.AdsFilterOptions;

Description

This setting affects whether filters, ranges, and scopes are respected or ignored using the following methods: [AdsGetKeyCount](ade_adsgetkeycount.htm), [AdsGetKeyNum](ade_adsgetkeynum.htm), [AdsGetRecordCount](ade_adsgetrecordcount.htm), and [AdsGetRecordNum](ade_adsgetrecordnum.htm). In addition, this setting affects whether filters are respected or ignored using the following methods: [AdsCopyTable](ade_adscopytable.htm), [AdsCopyTableContents](ade_adscopytablecontents.htm).

When using RESPECT\_WHEN\_COUNTING, this function will skip through every or many records in a table and could be extremely slow depending on how many records pass the filter, range, and scope. It is not recommended to use this function except on very small tables.

When using IGNORE\_WHEN\_COUNTING with [AdsCopyTable](ade_adscopytable.htm), [AdsCopyTableContents](ade_adscopytablecontents.htm), [AdsGetRecordCount](ade_adsgetrecordcount.htm), and [AdsGetRecordNum](ade_adsgetrecordnum.htm), the operations will occur much faster than if using RESPECT\_WHEN\_COUNTING. When using IGNORE\_WHEN\_COUNTING with [AdsGetKeyCount](ade_adsgetkeycount.htm) and [AdsGetKeyNum](ade_adsgetkeynum.htm), these operations may still be quite slow with large indexes because every or many keys in the index are literally counted.