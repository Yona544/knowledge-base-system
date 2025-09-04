AXSQL Refresh Functionality




Advantage Database Server 12  

AXSQL Refresh Functionality

Advantage AXSQL RDDs

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AXSQL Refresh Functionality  Advantage AXSQL RDDs |  |  | Feedback on: Advantage Database Server 12 - AXSQL Refresh Functionality Advantage AXSQL RDDs vo\_Axsql\_refresh\_functionality Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Using the Advantage AXSQL RDDs > AXSQL Refresh Functionality / Dear Support Staff, |  |
| AXSQL Refresh Functionality  Advantage AXSQL RDDs |  |  |  |  |

The normal DBServer:Refresh() method is used to refresh a single record of an open table. With the AXSQL RDDs, this method has some additional functionality. For live cursors, the AXSQL RDDs will simply refresh the current record, just as a normal DBServer would. With static cursors, the AXSQL RDDs will re-execute the SQL query thereby refreshing the entire result set. In addition, the Found flag will be set to TRUE if the RDD was able to reposition to the same record it was on before the refresh. If after the refresh the record which the RDD was on had changed, the RDD will remain on that record, but the Found flag will be set to FALSE. If after the refresh the original record no longer exists, the RDD will be positioned at the top of the cursor and the Found flag will be set to FALSE.

The AdsSQLServer:Refresh() method accepts new SQL parameters as an array of key-value pairs.  If provided, the given parameters will be set on the statement before the query is refreshed.  For example:

oServer:Refresh({{ "Lastname", "Coles" }, {"Firstname", "Jenny" }} )

See the [Parameter Support](vo_axsql_parameters.htm) page for more information.