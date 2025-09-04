sp\_mgGetErrorLog




Advantage Database Server 12  

sp\_mgGetErrorLog

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_mgGetErrorLog  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_mgGetErrorLog Advantage SQL Engine master\_sp\_mgGetErrorLog Advantage SQL > System Procedures > Procedures > sp\_mgGetErrorLog / Dear Support Staff, |  |
| sp\_mgGetErrorLog  Advantage SQL Engine |  |  |  |  |

Retrieve error log entries from the ads\_err.adt and/or ads\_err.dbf error log files.

Syntax

sp\_mgGetErrorLog();

sp\_mgGetErrorLog( MaxEntries, Integer );

sp\_mgGetErrorLog( MaxAdtEntries, Integer; MaxDbfEntries, Integer );

Parameters

The output parameters for this procedure are the same as the ads\_err.adt error log.

Remarks

sp\_mgGetErrorLog is an administrative procedure that will return the newest error entries from the error logs. This procedure may only be run on the active [root dictionary](master_root_dictionary.htm) and the user must be a member of the [SERVER:Monitor](master_database_base_roles.htm) group.

When this procedure is called without parameters, a default value of 25 is used for the number of entries to retrieve from both the ads\_err.adt and ads\_err.dbf error logs (if they both exist). The single parameter version specifies the number of entries for both error logs. And the two parameter version allows you to specify a specific number from each error log. In all cases, the newest error entries are retrieved.

When the request returns entries from both the ADT and DBF error logs, the ADT entries will be listed first followed by the DBF entries. Note that the entries from the DBF error log will have NULL values for the Error\_Number field. Also, the individual Date and Time fields from ads\_err.dbf are combined into the single DateTime field in the output.

Example

// Retrieve 10 entries from the ADT error log and 5 from the DBF error log

EXECUTE PROCEDURE sp\_mgGetErrorLog(10, 5);

 

// Retrieve 5 entries from each error log and order them by DateTime

SELECT Error\_Number, DateTime, Error\_Code, Ads\_Source, src\_Line, FileName

    FROM ( EXECUTE\_PROCEDURE sp\_mgGetErrorLog(5, 5)) x

    ORDER BY DateTime