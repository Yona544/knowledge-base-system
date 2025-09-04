SourceTableType




Advantage Database Server 12  

TAdsQuery.SourceTableType

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsQuery.SourceTableType  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsQuery.SourceTableType Advantage TDataSet Descendant ade\_Sourcetabletype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsQuery.SourceTableType  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.htm)

Indicates the table/index structure for the table that this component extracts data from.

Syntax

type TAdsTableTypes = (ttAdsCDX, ttAdsVFP, ttAdsADT);

 

property SourceTableType: TAdsTableTypes;

Description

Use SourceTableType to specify the table structure. SourceTableType can be set to either of the following values:

|  |  |
| --- | --- |
| Value | Meaning |
| ttAdsCDX | Table is a FoxPro compatible table type with CDX/IDX indexes. |
| ttAdsVFP | Table is a Visual FoxPro compatible table type with CDX/IDX indexes. |
| ttAdsADT | (Default) Table is an Advantage proprietary table type with ADI indexes. |

Note The ttAdsNTX file format is not supported on [free connections](javascript:hhpopuplink.TextPopup(popid_233455464X,FontFace,-1,-1,-1,-1)). NTX indexes are supported with TAdsQuery instances on [database connections](javascript:hhpopuplink.TextPopup(popid_330761683X,FontFace,-1,-1,-1,-1)) that use an [Advantage Data Dictionary](master_advantage_data_dictionary.htm). Create a new dictionary using the [Advantage Data Architect](ade_advantage_data_architect.htm), then reference [Accessing an Advantage Data Dictionary](master_accessing_an_advantage_data_dictionary_with_the_advantage_tdataset_descendant.htm) for information on configuring your application to access the dictionary.

 

Note This property is ignored when using a TAdsConnection component that references an [Advantage Data Dictionary](master_advantage_data_dictionary.htm). In this situation the table type stored in the dictionary is automatically used.