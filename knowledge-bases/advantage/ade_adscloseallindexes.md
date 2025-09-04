AdsCloseAllIndexes




Advantage Database Server 12  

TAdsTable.AdsCloseAllIndexes

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsCloseAllIndexes  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsCloseAllIndexes Advantage TDataSet Descendant ade\_Adscloseallindexes Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsCloseAllIndexes  Advantage TDataSet Descendant |  |  |  |  |

Closes all index orders for a given table.

Syntax

procedure AdsCloseAllIndexes;

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: CloseIndexFile. See your Delphi documentation for more information about this native Delphi method.

Description

It is not possible to close an AutoOpen index. If the table has an AutoOpen index, AdsCloseAllIndexes will not raise an exception, but index order handles from the AutoOpen index will still be valid.

Note Updating data in a table without all associated indexes being opened can result in index corruption. If such corruption occurs, it can be repaired by calling AdsReindex on the table handle.

Example

While AdsTable1.IndexFiles.Count > 0

AdsTable1.CloseIndexFile( AdsTable1.IndexFiles.Strings[0] );

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsOpenIndex](ade_adsopenindex.htm)

[AdsReindex](ade_adsreindex.htm)