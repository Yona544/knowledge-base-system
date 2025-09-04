AdsOpenIndex




Advantage Database Server 12  

TAdsTable.AdsOpenIndex

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsOpenIndex  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsOpenIndex Advantage TDataSet Descendant ade\_Adsopenindex Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsOpenIndex  Advantage TDataSet Descendant |  |  |  |  |

Opens an index file and associates all index orders in it with the given table.

Syntax

procedure AdsOpenIndex( strIndexName : String );

Parameter

|  |  |
| --- | --- |
| strIndexName | Filename of index to open. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: OpenIndexFile. See your Delphi documentation for more information about this native Delphi method.

Description

AdsOpenIndex opens all handles of index orders in the index file. If the index file is NOT a compound index (CDX or ADI), it will have only one index order. If the index file is a compound CDX or ADI index, multiple index orders may be opened.

Example

AdsTable1.OpenIndexFile( x:\path\file.ext );

AdsTable1.CloseIndexFile( file );

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsGetAllIndexes](ade_adsgetallindexes.htm)

[AdsGetIndexHandle](ade_adsgetindexhandle.htm)