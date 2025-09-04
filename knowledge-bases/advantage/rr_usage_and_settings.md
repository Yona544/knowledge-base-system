Usage and Settings




Advantage Database Server 12  

Usage and Settings

Advantage with R&R ReportWorks

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Usage and Settings  Advantage with R&R ReportWorks |  |  | Feedback on: Advantage Database Server 12 - Usage and Settings Advantage with R&R ReportWorks rr\_Usage\_and\_Settings Advantage with R&R ReportWorks > Usage and Settings / Dear Support Staff, |  |
| Usage and Settings  Advantage with R&R ReportWorks |  |  |  |  |

An additional driver is not required to use Advantage with R&R ReportWorks. The standard Advantage Client Engine (ace32/64.dll) and the Advantage Communications Layer (axcws32/64.dll) are the only client DLLs necessary.

To enable Advantage access from either the R&R XBase designer or the runtime, you must set the rr\_use\_ads environment variable (see table below).

Environment Variables

As there is no Advantage-specific connection type inside R&R, Advantage options and functionality is controlled via environment variables.

|  |  |
| --- | --- |
| Variable Name | Description |
| rr\_use\_ads | This setting is required, otherwise R&R will not attempt to use Advantage. Example:  rr\_use\_ads=1 |
| rr\_ads\_show\_errors | This setting can be used if debugging problems and you want to see the Advantage error codes and messages as they occur (instead of getting a                     generic file error from R&R). Example:  rr\_ads\_show\_errors=1 |
| rr\_ads\_connection\_string | This setting can be used to provide a connection string that Advantage will use for opening tables on behalf of R&R ReportWorks. If you are using data dictionaries, then this setting should probably be used. Advantage will obtain a connection defined by this [connection string](ace_adsconnect101.htm).  For example,    rr\_ads\_connection\_string=Data Source = \\myserver\data\test.add;ServerType = REMOTE; User ID=theuser; Password=thepassword;    The name of the table in the dictionary must match the base name of the physical file. R&R ReportWorks requests file opens using the full table path (since it has no knowledge of the data dictionary). Advantage then extracts the table name from the path and uses that name when opening the table through the dictionary. |
| rr\_ads\_index\_map | This setting can be used if you have index files that are not structural (base file name is different from the table file name). In this case the Advantage driver needs to be told what tables the indexes belong to, for example:    rr\_ads\_index\_map=index1.cdx=sometable.dbf;index2.cdx=sometable.dbf    Note that this map must be used even when using a data dictionary if the indexes are not structural. |
| rr\_ads\_table\_passwords | This setting can be used to pass encryption passwords for encrypted free tables. A semi-colon delimited list of tablename/password pairs can be                     specified, or a single password for use with all tables can be specified. For example:    rr\_ads\_table\_passwords=table1.adt=mypassword1;table2=mypassword2                              or      rr\_ads\_table\_passwords=password\_for\_all |
| rr\_ads\_locking | This setting can be used to specify the Advantage locking mode. The default locking mode is "compatible". To specify proprietary locking use:    rr\_ads\_locking=proprietary |
| rr\_ads\_chartype | This setting can be used to specify the Advantage character type. The default char type is ANSI. To set it to OEM use:    rr\_ads\_chartype=oem |