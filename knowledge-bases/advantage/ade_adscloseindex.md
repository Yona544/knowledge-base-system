AdsCloseIndex




Advantage Database Server 12  

TAdsTable.AdsCloseIndex

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsCloseIndex  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsCloseIndex Advantage TDataSet Descendant ade\_Adscloseindex Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsCloseIndex  Advantage TDataSet Descendant |  |  |  |  |

Closes an index order.

Syntax

procedure AdsCloseIndex( strTag : String );

Parameter

|  |  |
| --- | --- |
| strTag | Tag name of the index order to close. If this is a tag of an index order within a compound index file, then the file is closed. The file is not deleted. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: CloseIndexFile. See your Delphi documentation for more information about this native Delphi method.

Description

It is not possible to close an AutoOpen index. Any attempts to use an index tag that is closed with an Advantage Client Engine function will raise an exception. The index file can be reopened as long as the table it is associated with is open.

Note Updating data in a table without all associated indexes being opened can result in index corruption. If such corruption occurs, it can be repaired by calling AdsReindex on the table handle.

Example

AdsTable1.OpenIndexFile( x:\path\file.ext );

 

AdsTable1.CloseIndexFile( file );

See Also

[AdsCloseAllIndexes](ade_adscloseallindexes.htm)

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsOpenIndex](ade_adsopenindex.htm)