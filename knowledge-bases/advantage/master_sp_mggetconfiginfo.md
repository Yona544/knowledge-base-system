sp\_mgGetConfigInfo




Advantage Database Server 12  

sp\_mgGetConfigInfo

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_mgGetConfigInfo  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_mgGetConfigInfo Advantage SQL Engine master\_Sp\_mggetconfiginfo Advantage SQL > System Procedures > Procedures > sp\_mgGetConfigInfo / Dear Support Staff, |  |
| sp\_mgGetConfigInfo  Advantage SQL Engine |  |  |  |  |

Returns Advantage Database Server configuration information. This procedure only returns the configuration items that do not affect memory.

Syntax

EXECUTE PROCEDURE sp\_mgGetConfigInfo()

Parameters

|  |  |
| --- | --- |
| Item (O) | Name of the item. |
| Value (O) | Value from the server. |

Remarks

This procedure returns the following items:

|  |  |
| --- | --- |
| Stat Dump Interval | Statistics dump interval |
| Error Log Max | Maximum size of the error log |
| Error Log Path | Location to write the error log file |
| Burst Packets | Number of packets per burst |
| Sort Buffer | Index sort buffer size |
| Sent IP Port | IP send port number |
| Receive IP Port | IP receive port number |
| Ghost Timeout | Disconnection time for partial connections |
| Flush Frequency | How often Local Server writes changes to disk |
| Keep Alive Timeout | When not using semaphore files. In milliseconds |
| Internet Port | Port for internet (AIS) connections |
| Max Conn Failures | Maximum internet connection failures allowed |
| Internet Keep Alive | In milliseconds |
| Compression Level | Compression option at server |
| Use IP | Use IP communications only \*Win9x\* |
| Flush Every Update | Write changes to disk immediately \*Win9x\* |
| NetWare Login Names | Display connections using user names (Deprecated) |
| Use Semaphore Files | Whether or not to use semaphore connection files |
| Semaphore File Path | Location of semaphore files on the server |
| Use Dynamic AOFs | Indicates if [filter membership](master_differences_between_aofs_and_traditional_record_filters.htm) is affected by modifications other users make to data. |
| Use Internet | 0 if internet port is not specified |
| Transaction Log Path | Location of transaction log files |
| Receive SSL Port | SSL (TLS) receive port number |
| SQL Statement Limit | The default number of SQL statements that a connection can have open at one time. See [SQL\_STATEMENT\_LIMIT](master_sql_statement_limit.htm). |
| User SQL Statement Limit | The number of SQL statements that the current connection can have open at one time.  See [sp\_SetStatementLimit](master_sp_setstatementlimit.htm). |

Example

EXECUTE PROCEDURE sp\_mgGetConfigInfo();

See Also

[sp\_mgGetConfigMemory](master_sp_mggetconfigmemory.htm)