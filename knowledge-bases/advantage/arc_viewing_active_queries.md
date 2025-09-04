Viewing Active Queries




Advantage Database Server 12  

Viewing Active Queries

Advantage Data Architect

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Viewing Active Queries  Advantage Data Architect |  |  | Feedback on: Advantage Database Server 12 - Viewing Active Queries Advantage Data Architect arc\_Viewing\_active\_queries Advantage Data Architect > Advantage Utilities > Advantage Management Utility > Viewing Active Queries / Dear Support Staff, |  |
| Viewing Active Queries  Advantage Data Architect |  |  |  |  |

The Active Queries screen displays all queries currently being processed by the Advantage Database Server. A query can only be cancelled if it is on a data dictionary connection and the Advantage Management Utility has an administrative connection to that data dictionary.

Field Descriptions

Query Number

Unique identifier of the query. This is used to cancel the query by right clicking on the grid.

Active

True if the query is being actively processed by the server. A query must be active to be cancelled.

Percent Complete

Estimated percentage of query execution completed. This value is null when the query is not active.

Connection Name

The Advantage clients computer name.

Seconds Until Finished

The estimated number of seconds until query execution is completed.

Database

The connection path of the query being executed by the Advantage Database Server.

Query

The SQL statement being processed by the Advantage Database Server.

Start Time

The time on the Advantage Database Server when the query execution was started.