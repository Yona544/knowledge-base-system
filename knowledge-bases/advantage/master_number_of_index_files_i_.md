Number of Index Files (-I)




Advantage Database Server 12  

Number of Index Files (-I)

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Number of Index Files (-I)  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Number of Index Files (-I) Advantage Database Server master\_Number\_of\_index\_files\_i\_ Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Number of Index Files (-I)  Advantage Database Server |  |  |  |  |

Default = 150 index files. Range = 1 no upper limit.

This is the initial number of index files that can be open on the Advantage Database Server at one time.

The "Number of Index Files" configuration setting on the Advantage Database Server is a per-server setting. That is, one index file must be available per index file opened, no matter how many clients have that index file open. For example, if 128 Advantage clients have opened the same 14 index files, there must be at least 14 index files configured on the Advantage Database Server. Thus, the "Number of Index Files" configuration setting is similar to the "Number of Tables" setting; in that, both settings are the number of files opened "per server" and not the number of files opened "per client".

If an Advantage application attempts to open an index file on the Advantage Database Server that has not yet been opened by any Advantage application, and the configured number of index files have already been opened, the Advantage Database Server will attempt to allocate more resources to accommodate more open indexes. If that allocation fails, the Advantage application that is attempting to open that index file will receive a 7006 error, Maximum number of index files exceeded, until an index file "element" becomes available.

Note This configurable setting is per index FILE. It does not matter if the index file is a single-order index file, such as an NTX or IDX index, or if it is a multiple-order index file, such as a CDX or ADI index. The number of orders that exist in a CDX or ADI index file that are opened has no effect on this setting.