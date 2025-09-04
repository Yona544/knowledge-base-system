Using Third-Party Components with Advantage




Advantage Database Server 12  

Using Third-Party Components with Advantage

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using Third-Party Components with Advantage  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Using Third-Party Components with Advantage Advantage TDataSet Descendant ade\_Using\_third\_party\_components\_with\_advantage Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Using Third-Party Components with Advantage  Advantage TDataSet Descendant |  |  |  |  |

Advantage TDataSet Descendant

The Advantage TDataSet Descendant is compatible with all data-aware components that ship with Delphi/C++Builder, with the exception of TBatchMove (For TBatchMove functionality see the [TAdsBatchMove](ade_tadsbatchmove.htm) component).

For third-party components to work with the Advantage TDataSet Descendant, the component must be engineered to work with a generic TDataSet descendant or standard TDataSource class. This means that the component must not type-cast the dataset to a TTable or any other descendant other than TAdsDataset, TAdsTable, TAdsQuery, or TAdsStoredProc. It also means that the component must not make any direct BDE API function calls (for example DbiGetRecordCount).