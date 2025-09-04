Movement Operations




Advantage Database Server 12  

Movement Operations

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Movement Operations  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Movement Operations Advantage Concepts master\_Movement\_operations Advantage Concepts > Advantage ISAM Concepts > Movement Operations / Dear Support Staff, |  |
| Movement Operations  Advantage Concepts |  |  |  |  |

There are several basic movement operations available for use on Advantage ISAM files. For the Advantage TDataSet Descendant, the following table shows the TDataSet specific method names for movement operations and the equivalent generic Advantage operations.

|  |  |
| --- | --- |
| TDataSet Specific Methods | Advantage Generic Operation |
| First | [Go Top](master_go_top_movement.htm) |
| Last | [Go Bottom](master_go_bottom_movement.htm) |
| FindKey, FindNearest, GotoKey, GotoNearest | [Seek](master_seek_movement.htm) |
| Next, Prior, MoveBy | [Skip](master_skip_movement.htm) |
| GotoBookmark | [Go To](master_go_to_movement.htm) |
| Locate | \* |

\* Advantage does not have a direct equivalent to the Delphi/C++Builder specific Locate method. Advantage implements a Locate in the Advantage TDataSet Descendant by doing either a Seek or an [Advantage Optimized Filter](master_advantage_optimized_filters.htm).

ADO Specific Methods/Properties

For the ActiveX Data Objects (ADO), the following table shows the ADO specific method names for movement operations and the equivalent generic Advantage operations.

|  |  |
| --- | --- |
| ADO Specific Methods/Properties | Advantage Generic Operation |
| MoveFirst | [Go Top](master_go_top_movement.htm) |
| MoveLast | [Go Bottom](master_go_bottom_movement.htm) |
| Seek | [Seek](master_seek_movement.htm) |
| MoveNext, MovePrevious | [Skip](master_skip_movement.htm) |
| \*\*Bookmark | [Go To](master_go_to_movement.htm) |
| Find | [Locate](master_locate_movement.htm) |

\*\* Setting the ADO Bookmark property to a valid record number is the same as doing an ISAM Go To when using ADO with the Advantage OLE DB Provider.