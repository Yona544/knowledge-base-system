SET <system variable>




Advantage Database Server 12  

SET <system variable>

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SET <system variable>  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - SET <system variable> Advantage SQL Engine master\_Set\_system\_variable\_ Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| SET <system variable>  Advantage SQL Engine |  |  |  |  |

Set the specified system variable or configuration to the specified value.

Syntax

SET <system variable> = expr

<system variable> ::= identifier

Remark

The SET <system variable> statement is used to change system configurations affecting the behavior of subsequent SQL statements. The <system variable> identifies the system configuration to modify and the expr designates how the configuration should change. The configurable system variables and their allowed values are the following:

::conn.collation This variable specifies the default collation for statements allocated on the connection. The connection collation is used only for statements (query handle) that specify default as the collation. The expr should be a character expression that evaluates to a string in the format [ANSI\_OEM\_COLLATION][:UNICODE\_COLLATION]. Either or both parts may be specified. The ANSI\_OEM\_COLLATION may be one of the ANSI/OEM collation names retrieved from using [sp\_GetCollations](master_sp_getcollations.htm) or it may be 'default\_ansi' or 'default\_oem' to use the default ANSI or OEM collation stamped into the Advantage Database Server. The UNICODE collation may be one of the Unicode collation names retrieved from [sp\_GetCollations](master_sp_getcollations.htm). See [Collation Support](master_collation_support.htm) for additional information.

::stmt.collation This variable specifies the collation language to use when executing subsequent statements on this statement handle. The expr should be a character expression that evaluates to a string in the format [ANSI\_OEM\_COLLATION][:UNICODE\_COLLATION]. Either or both parts may be specified. The ANSI\_OEM\_COLLATION may be one of the ANSI/OEM collation names retrieved from using [sp\_GetCollations](master_sp_getcollations.htm) or it may be 'default' to use the connections collation, or 'default\_ansi' or 'default\_oem' to use the default ANSI or OEM collation stamped into the Advantage Database Server respectively. The UNICODE collation may be one of the Unicode collation names retrieved from [sp\_GetCollations](master_sp_getcollations.htm). See [Collation Support](master_collation_support.htm) for additional information.

See Also

[System Variables](master_system_variables.htm)