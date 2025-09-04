AdsCharType




Advantage Database Server 12  

AdsTableOptions.AdsCharType

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTableOptions.AdsCharType  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsTableOptions.AdsCharType Advantage TDataSet Descendant ade\_Adschartype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsTableOptions.AdsCharType  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.htm)

Indicates the character set used to store the data within the table.

Syntax

type TAdsCharTypes = ( ANSI, OEM );

 

property AdsTableOptions.AdsCharType;

Description

Type of character set used to store data in the table. Options are ANSI and OEM. For compatibility with DOS-based CA-Clipper applications, OEM should be specified. The OEM setting has no effect on Advantage proprietary ADT tables, which always use the ANSI setting.

In addition to the ANSI and OEM values, this can also be set to one of the [dynamic collation](master_collation_support.htm) languages such as GENERAL\_VFP\_CI\_AS\_1252.