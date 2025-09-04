AX\_GetAceIndexHandle()




Advantage Database Server 12  

AX\_GetAceIndexHandle()

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AX\_GetAceIndexHandle()  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - AX\_GetAceIndexHandle() Advantage Visual Objects and Vulcan.NET RDD vo\_Ax\_getaceindexhandle Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Advanced  Functions > AX\_GetAceIndexHandle() / Dear Support Staff, |  |
| AX\_GetAceIndexHandle()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Returns the Advantage Client Engine index handle that corresponds with the specified index in the current work area. The handle can be used to call any Advantage Client Engine API directly.

Syntax

AX\_GetAceIndexHandle( [<cIndexFile>], [<cOrder> | <nPosition>) -> DWORD

|  |  |
| --- | --- |
| <cIndexFile> | The name of an index file, including an optional drive and directory (no extension should be specified). Use this argument with <cOrder> to remove ambiguity when there are two or more orders with the same name in different index files. |
| <cOrder> | <nPosition> | The name of the order about which you want the handle or a number representing its position in the order list. (For single-order index files, the order name is the eight-letter index file name.) Using the order name is the preferred method since the position may be difficult to determine using multiple-order index files. Invalid values are ignored. |

If no index file or order is specified, the controlling order is assumed.

Returns

An Advantage Client Engine index order handle or 0 if no index was found.

Description

This function returns the Advantage Client Engine Index handle of the specified index. This function returns 0 if the index was not active or found. The handle can be used to call any Advantage Client Engine API directly. The APIs can be imported into Visual Objects from the ACE.AEF file.

The AX\_GetAceIndexHandle function gets the index handle from the current work area. If you are unsure which work area is current, use select() to set it. For example:

select( dbServer:workarea )

or

select( dbServer:alias )

To avoid all ambiguity you could also retrieve the index handle directly from the DBServer object using the Info method. For example:

dbServer:Info( DBOI\_GET\_ACE\_INDEX\_HANDLE )

DBOI\_GET\_ACE\_INDEX\_HANDLE is defined in the dbfaxs.aef library.