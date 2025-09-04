StoreActive




Advantage Database Server 12  

TAdsDataSet.StoreActive

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDataSet.StoreActive  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDataSet.StoreActive Advantage TDataSet Descendant ade\_Storeactive Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDataSet.StoreActive  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm) [TAdsQuery](ade_tadsquery.htm) [TAdsStoredProc](ade_tadsstoredproc.htm)

Syntax

property StoreActive: Boolean read FbStoreActive write FbStoreActive;

Description

The StoreActive property specifies whether or not the Active property is written to the DFM file when the form is saved.

The default value of the StoreActive property is True.

If you prefer the Active property never be saved with a form, create a TAdsTable/TAdsQuery/TAdsStoredProc descendant and set the FbStoreActive member variable to False in the constructor.

See Also

[StoreConnected](ade_storeconnected.htm)