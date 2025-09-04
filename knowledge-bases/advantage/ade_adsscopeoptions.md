AdsScopeOptions




Advantage Database Server 12  

AdsTableOptions.AdsScopeOptions

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTableOptions.AdsScopeOptions  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsTableOptions.AdsScopeOptions Advantage TDataSet Descendant ade\_Adsscopeoptions Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsTableOptions.AdsScopeOptions  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.htm)

When determining the record count, key count, or key position, indicates whether to respect the scope/range applied to the data set.

Syntax

type TAdsRespectScopes = ( IGNORE\_SCOPES\_WHEN\_COUNTING,

RESPECT\_SCOPES\_WHEN\_COUNTING );

 

property AdsTableOptions.AdsScopeOptions;

Description

This setting specifies whether scopes/ranges are respected or ignored when using the following methods: [AdsGetKeyCount](ade_adsgetkeycount.htm), [AdsGetKeyNum](ade_adsgetkeynum.htm), and [AdsGetRecordCount](ade_adsgetrecordcount.htm). Unlike the AdsFilterOptions property, the performance of methods affected by this setting is similar no matter which scope setting is specified.