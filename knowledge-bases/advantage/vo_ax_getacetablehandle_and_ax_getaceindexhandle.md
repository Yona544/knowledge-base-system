AX\_GetAceTableHandle and AX\_GetAceIndexHandle




Advantage Database Server 12  

AX\_GetAceTableHandle and AX\_GetAceIndexHandle

Advantage AXSQL RDDs

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AX\_GetAceTableHandle and AX\_GetAceIndexHandle  Advantage AXSQL RDDs |  |  | Feedback on: Advantage Database Server 12 - AX\_GetAceTableHandle and AX\_GetAceIndexHandle Advantage AXSQL RDDs vo\_Ax\_getacetablehandle\_and\_ax\_getaceindexhandle Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Using the Advantage AXSQL RDDs > AX\_GetAceTableHandle and AX\_GetAceIndexHandle / Dear Support Staff, |  |
| AX\_GetAceTableHandle and AX\_GetAceIndexHandle  Advantage AXSQL RDDs |  |  |  |  |

With the AXSQL RDDs the AX\_GetAceTableHandle and AX\_GetAceIndexHandle utility functions still work. The AX\_GetAceTableHandle function will return the cursor handle of the result set. In most ways a cursor handle is just like a normal ACE table handle.

The AX\_GetAceIndexHandle function will return the index handle of the cursor if one is available. Typically an index handle will only be available with the AXSQL RDDs if the query had an ORDER BY specified. An index handle would also be available if an index order was created on a result set after it was instantiated.