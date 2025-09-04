Table Handles




Advantage Database Server 12  

Table Handles

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Table Handles  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - Table Handles Advantage Client Engine ace\_Table\_handles Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Table Handles  Advantage Client Engine |  |  |  |  |

Each table that is opened through the Advantage Client Engine via [AdsOpenTable](ace_adsopentable.htm) or [AdsCreateTable](ace_adscreatetable.htm) has an associated handle. This table handle is returned in the parameter list in each of these calls and must be passed to other API calls that operate on tables (e.g., [AdsSetString](ace_adssetstring.htm)).

Table handles are generally equivalent to the work area concept. They are always associated with a connection handle, but with a zero sent to the Advantage Client Engine as a connection handle on the open or create, you need not store or worry about that connection handle. The most significant change with this implementation is that it requires the user to maintain these table handles to be able to pass them as parameters to the Advantage Client Engine API.

A table handle requires a work area resource on the server. The table handle encapsulates the core of Advantage Client Engine functionality, therefore, all data manipulation, table information, and natural order movement is based on the table handle. Index handles are also associated with a parent table handle. Table handles are invalid after calling [AdsCloseTable](ace_adsclosetable.htm) or [AdsDisconnect](ace_adsdisconnect.htm) for the connection on which the table is opened, or [AdsApplicationExit](ace_adsapplicationexit.htm).