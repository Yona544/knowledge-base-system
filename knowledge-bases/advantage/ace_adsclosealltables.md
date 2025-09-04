AdsCloseAllTables




Advantage Database Server 12  

AdsCloseAllTables

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCloseAllTables  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCloseAllTables Advantage Client Engine ace\_Adsclosealltables Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCloseAllTables  Advantage Client Engine |  |  |  |  |

Closes all open tables in the application

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCloseAllTables (void); |

Parameters

None.

Remarks

AdsCloseAllTables will close ALL tables opened for the application. Any associated index or memo files will also be closed. The Advantage Client Engine will NOT disconnect from the server when all tables are closed, and settings specified by [AdsCacheOpenTables](ace_adscacheopentables.htm) will be obeyed. Changes in the tables are flushed, and implicit locks are released.

Note Closing tables is illegal in a transaction. AdsCloseAllTables will return the error code AE\_ILLEGAL\_COMMAND\_DURING\_TRANS if any tables are in transactions, and those tables will not be closed. All tables that are not in transactions will be closed.

Example

[Click Here](ace_examples.htm#adsclosealltablesexample)

See Also

[AdsCloseTable](ace_adsclosetable.htm)

[AdsOpenTable](ace_adsopentable.htm)

[AdsCloseCachedTables](ace_adsclosecachedtables.htm)