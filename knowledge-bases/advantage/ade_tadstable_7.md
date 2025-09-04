TAdsTable




Advantage Database Server 12  

TAdsTable

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable Advantage TDataSet Descendant ade\_Tadstable\_7 Advantage TDataSet Descendant > Advantage Components > TAdsTable / Dear Support Staff, |  |
| TAdsTable  Advantage TDataSet Descendant |  |  |  |  |

|  |  |  |
| --- | --- | --- |
| [Properties](ade_tadstable_properties.htm) | [Methods](ade_tadstable_methods.htm) | [Events](ade_tadstable_events.htm) |

 

[Type Definitions](ade_type_definitions.htm)

[Advantage Extended Methods](ade_advantage_extended_methods_tadstable.htm)

TAdsTable is a TDataSet descendant component that provides an encapsulation of TTable functionality and Advantage extended methods using the Advantage Database Server through the Advantage Client Engine.

Unit

AdsTable

Description

Use TAdsTable to access data in a single table using the Advantage Database Server through the Advantage Client Engine. TAdsTable provides direct access to every record and field in an underlying table, whether from FoxPro-compatible indexes for DBF tables, CA-Clipper-compatible indexes for DBF tables, or Advantage proprietary ADI indexes for ADT tables.

The Advantage TAdsTable component is equivalent to the Delphi TTable component. The Advantage TDataSet Descendant TAdsTable component provides most of the same methods, properties, and events that TTable provides. TAdsTable provides direct access to every record and field in an underlying table and provides access to extended Advantage functionality that is not available with TTable.

The TAdsTable component looks and behaves like the TTable component. One specific difference, however, is the TAdsTable.TableType property must be set to ttAdsADT, ttAdsCDX, ttAdsVFP, or ttAdsNTX for [free connections](javascript:hhpopuplink.TextPopup(popid_233455464X,FontFace,-1,-1,-1,-1)) (that is, Advantage connections not associated with an [Advantage Data Dictionary](master_accessing_an_advantage_data_dictionary_with_the_advantage_tdataset_descendant.htm)). The TAdsTable.TableType property is ignored when using a TAdsConnection component that references an Advantage Data Dictionary. In this situation, the table type stored in the data dictionary is automatically used.

TAdsTable is a descendant of TAdsDataSet, TAdsExtendedDataSet, and TAdsExtendedTable classes. TAdsDataSet, TAdsExtendedDataSet, and TAdsExtendedTable are base classes and are not to be used directly in your applications. See [Advantage TDataSet Descendant Architecture](ade_advantage_tdataset_descendant_architecture.htm) for an illustration of this hierarchy.

The numeric field type in the Advantage TDataSet Descendant table, introduced in Advantage 8.1, is mapped to the ftFMTBcd in Delphi 6 or greater version. It provides the support for exact numeric values up to 30 digits. In Delphi 5 and earlier versions, the numeric field type is mapped to either the ftInteger or ftFloat because the ftFMTBcd is not available in those Delphi releases. The ftFloat type is stored internally as IEEE Double and it has only about 15 digits of precision.

Extended Methods

The TAdsTable contains many methods that are classified as "extended methods". Each method name is prefaced with "Ads". These are wrappers of most Advantage Client Engine API's. Often, these methods closely match a method from the TTable equivalent methods. For example, the TAdsTable.AdsSkip method and the TAdsTable.Next method provide the same functionality. The TAdsTable.AdsSkip method is merely a wrapper for the Advantage Client Engine API named AdsSkip, which sets the current table position to the next subsequent row. The TAdsTable.Next component is identical to standard Delphi TTable.Next method. They both set the current table position to the next row.

In many cases, the TTable equivalent function (TAdsTable.Next in this case) is more efficient. For every extended method that is not as efficient as the TTable equivalent function, there exists a special warning in the methods documentation. For those methods, the code necessary to call the more efficient TTable equivalent function is mentioned, so that you can you use it instead. As a general rule, do not use Advantage TAdsTable extended methods unless absolutely necessary (such as when no Delphi equivalent method exists).