sp\_DropLink




Advantage Database Server 12  

sp\_DropLink

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_DropLink  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_DropLink Advantage SQL Engine master\_Sp\_droplink Advantage SQL > System Procedures > Procedures > sp\_DropLink / Dear Support Staff, |  |
| sp\_DropLink  Advantage SQL Engine |  |  |  |  |

Removes either a local link or a global link from the current connection.

Syntax

sp\_DropLink (

Name, CHARACTER, 200,

Global, LOGICAL )

Parameters

|  |  |
| --- | --- |
| Name (I) | The name or path of the link to drop. If the path is given, the first link matching the given path will be dropped. |
| Global (I) | True to remove the global link alias from the data dictionary. This parameter can only be set to True for a database connection with administrative permissions. If this parameter is True, the Name parameter must specify the link alias in the data dictionary. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | This error may be returned if the Global parameter is True and the specified link cannot be found in the data dictionary. |

Remarks

This function can be used to either drop an active link from the current connection or remove a global link from the data dictionary. Since the database server maintains information on the active links, dropping active links from the current connection will free some resources consumed by the server.

Example

The execution of the following SQL statement creates an implicit link to the ARCHIVE database. The implicit link is then dropped.

SELECT Max(LastDate) FROM "n:\MyData\ARCHIVE\ARCHIVE.ADD".Table1;

 

EXECUTE PROCEDURE sp\_DropLink ( 'n:\MyData\ARCHIVE\ARCHIVE.ADD', FALSE );

 

See Also

[sp\_CreateLink](master_sp_createlink.htm)

[sp\_ModifyLink](master_sp_modifylink.htm)