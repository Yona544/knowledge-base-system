Maximum Size of Error Log Info




Advantage Database Server 12  

Maximum Size of Error Log Info

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Maximum Size of Error Log Info |  |  | Feedback on: Advantage Database Server 12 - Maximum Size of Error Log Info arc\_Maximum\_size\_of\_error\_log\_info Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Maximum Size of Error Log Info |  |  |  |  |

Default = 1000 Kbytes. Range = 1 - no upper limit.

The error log file size is the maximum file size the error log file (ADS\_ERR.DBF or ADS\_ERR.ADT), can reach. Once the maximum file size is attained, the first one-third of the records in the error log table are marked for deletion and packed automatically. With ADS\_ERR.DBF, new entries are appended to the end of the file. With ADS\_ERR.ADT, record recycling is used, so the new entries may not be at the physical end of the table. Viewing ADS\_ERR.ADT in ERROR\_NUMBER index order will ensure that the errors are displayed in the order they are logged.

The error log is a table used to record any errors encountered by the Advantage Database Server during execution of client applications. The ADS\_ERR.DBF error log file may be viewed using any standard DBF utility. ADS\_ERR.ADT is an Advantage proprietary format table and can be viewed with Advantage Data Architect.