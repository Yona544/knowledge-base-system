Caution About Extended Methods




Advantage Database Server 12  

Caution About Extended Methods

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Caution About Extended Methods  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Caution About Extended Methods Advantage TDataSet Descendant ade\_Caution\_about\_extended\_methods Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Caution About Extended Methods  Advantage TDataSet Descendant |  |  |  |  |

The TAdsTable extended methods are wrappers around the Advantage Client Engine functionality. Many of these extended methods have functionality that very closely matches that available in native TTable methods (and the TAdsTable methods inherited from native Delphi). Extended methods were added to TAdsTable for completeness only. The native TTable methods (and TAdsTable methods inherited from native Delphi) are usually the faster and more efficient way to perform certain tasks.

The Delphi TDataSet class is very complex and manages many records within its own buffers. To prevent the Advantage extended methods circumventing the buffer management, the Advantage TAdsTable extended methods call various native TDataSet methods to ensure proper buffer management occurs. These extra calls to native TDataSet methods makes Advantage extended methods often much less efficient than if the native TDataSet methods were called directly. The Delphi native methods were implemented in the most efficient way possible. It is recommended that the native TTable methods or the methods in TAdsTable inherited from native Delphi be used rather than the extended methods in TAdsTable.

For example, consider the AdsSetString extended method. This extended method is similar to the native Delphi TField.AsString method. Both store a string value into the field. The Advantage extended method is much less efficient, however, because it must first flush any pending updates to the existing record buffer in TDataSet, re-read the record to be updated (in case any other user had updated it), write the field change directly to the Advantage Client Engine record buffer, flush the record to the Advantage Database Server, and then call the Delphi Refresh method to make the field update apparent to the TDataSet. If a grid is active, this Refresh method will not only re-read the updated record, but all records in the grid. The native Delphi TField.AsString method, on the other hand, simply stores the value into the current TDataSet record buffer. No record flushes or record re-reads are required because Delphi is managing its internal record buffer(s). Updating a field via the native Delphi AsString method will require a fraction of the operations an the AdsSetString extended method requires.

If the AdsSetString extended method were not implemented in this manner, that is, if it did not flush any pending updates, re-read the record, update the new field, flush the record to the server, and then refresh the current record buffer, field updates would be lost. To see how field updates would be lost if AdsSetString were not implemented as described, consider an application that calls AdsSetString for Field\_1 and AsString on Field\_2, in either order. Since AdsSetString writes the Advantage Client Engine record buffer and not the TDataSet record buffer, when the data is eventually posted via the Post method, the entire TDataSet record buffer, which contains all fields, would be written to the Advantage Client Engine overwriting any fields previously updated via AdsSetString.