sp\_GetLinks




Advantage Database Server 12  

sp\_GetLinks

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_GetLinks  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_GetLinks Advantage SQL Engine master\_sp\_GetLinks Advantage SQL > System Procedures > Procedures > sp\_GetLinks / Dear Support Staff, |  |
| sp\_GetLinks  Advantage SQL Engine |  |  |  |  |

Retrieve the links in the current dictionary.

Syntax

sp\_GetLinks()

Parameters

None

Output

|  |  |
| --- | --- |
| LinkAlias (O) | The link alias name |
| Path (O) | The path to the linked data dictionary. This path will be converted to a UNC path if the original connection path is not to the local machine. |

Remarks

Calls to this procedure are only allowed if the current connection is to the active [root dictionary](master_root_dictionary.htm) and the user is a member of the SERVER:Monitor group.

The UNC conversion will be based on the connection path used by the current connection. For example, assume dictionary c:\d1\dictionary.add has a link alias D2 which uses a relative path to c:\d2\dictionary2.add and that there are two distinct shares or server side aliases pointing to the same directory.

If User A Connects to \\server\XYZ\d1\dictionary.add, the UNC conversion for relative link D2 will be \\server\XYZ\d2\dictionary2.add.

If User B connects using \\server\serveralias\d1\dictionary.add, the UNC conversion for relative link D2 will be \\server\serveralias\d2\dictionary.add.

See Also

[sp\_CreateLink](master_sp_createlink.htm)