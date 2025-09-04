TableType




Advantage Database Server 12  

TAdsTable.TableType

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.TableType  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.TableType Advantage TDataSet Descendant ade\_Tabletype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.TableType  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm)

Indicates the table/index structure for the table that this component encapsulates.

Syntax

type TAdsTableTypes = (ttAdsCDX, ttAdsVFP, ttAdsNTX, ttAdsADT);

 

property TableType: TAdsTableTypes;

Description

Use TableType to specify the table structure. TableType can be set to one of the following values:

|  |  |
| --- | --- |
| Value | Meaning |
| ttAdsCDX | Table is a FoxPro compatible table type with CDX/IDX indexes |
| ttAdsVFP | Table is a Visual FoxPro compatible table type with CDX/IDX indexes |
| ttAdsNTX | Table is a CA-Clipper compatible table type with NTX indexes |
| ttAdsADT | (Default) Table is an Advantage proprietary table type with ADI indexes. |

Note This property is ignored when using a [TAdsConnection](ade_tadsconnection_7.htm) component that references an Advantage Data Dictionary. In this situation the table type stored in the dictionary is automatically used.