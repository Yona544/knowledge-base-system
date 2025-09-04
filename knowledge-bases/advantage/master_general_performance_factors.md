General Performance Factors




Advantage Database Server 12  

General Performance Factors

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| General Performance Factors  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - General Performance Factors Advantage Database Server master\_General\_performance\_factors Advantage Database Server > Performance Factors > General Performance Factors / Dear Support Staff, |  |
| General Performance Factors  Advantage Database Server |  |  |  |  |

The following are general keys to performance when using Advantage.

Increase Memory and CPU Speed on the Server

With the Advantage Database Server, the file server is no longer an unintelligent shared hard drive. The server CPU and memory are now more fully utilized. So, increasing the amount of memory and the speed of the CPU should always help performance of the Advantage Database Server. Servers with only 64 MB of RAM will probably not provide optimum performance. If the workstations are Pentium IVs, and the server is a Pentium II, the Advantage Database Server may not provide the kind of performance you are looking for. At a minimum, the file server should have at least as much RAM and as fast a CPU as the client workstations.

Compression

Using compression for communications between the client and server may improve performance in low bandwidth situations. See [Communications Compression](master_communications_compression.htm) for more information.

Leave Tables Open Once They've been Opened

This tip for improved performance only applies to developers using direct navigational database access to Advantage. In other words, it only applies if opening tables directly. It is not applicable when using SQL to access your database. Database developers who create non-client/server applications are often trained to open tables, do whatever work and operations are necessary, and then quickly close the table before corruption problems occur or an overuse of file handles on the client workstations causes problems. Since the Advantage Database Server opens all files on the server, table corruption is eliminated, and no file handles are ever used on the client workstations. This fact combined with the fact that opening tables is one of the slowest individual database operations that can be performed leads us to recommend limiting the number of times tables and index files are closed and re-opened. In general, for best performance, frequently used tables and their associated index files should not be closed once they are opened. Simply leave them open after they've been opened for the first time. For some applications, it may make sense to open all tables and index files at application startup, and keep them open during the entire application. This eliminates the slow open, close, then re-open series of table operations and leads to overall improvement in application performance. If tables must be opened throughout the application, using UNC paths and using "ignore rights" security may slightly increase the speed of opens.

Use Advantage Optimized Filters

Convert your applications to use Advantage Optimized Filters (AOFs) rather than traditional record filters. AOFs can be up to 1000 times faster than traditional record filters. See [Advantage Optimized Filters](master_advantage_optimized_filters.htm).

Optimize Use of Advantage Read-Ahead Record Caching

Proper use of Read-Ahead Record Caching in your applications can improve Skip operation performance by 100 times. See [Read-Ahead Record Caching](master_read_ahead_record_caching.htm) for more information.

Turn Foreground Performance Boost Off

If using the Advantage Database Server for Windows, turn off the "foreground boost for the foreground process" on the Windows Server. Since the Advantage Database Server is a service, it runs as a background process. If foreground processes are given a performance boost, Advantage Database Server performance will suffer. Foreground boost can be turned off via the Performance tab under the System Properties icon in the Control Panel folder.

Do Not Use NTX Indexes and DBT Memos

There are several non-performance reasons to use index and memo formats other than NTX indexes. NTX index files allow only one index order per index file. Both CDX and ADI indexes are compound indexes. That means you can have multiple individual index orders per CDX or ADI index file. Having compound index files makes application development easier because there are fewer files to open and maintain. CDX and ADI indexes also have the concept of auto-open index files. If a CDX or ADI index file has the same base name as the table name, that index file will be automatically opened when the table is opened and cannot be closed until it is automatically closed when the table is closed. This makes application development even easier with CDX and ADI indexes than with NTX indexes, because your application never needs to open or close index files. NTX indexes have no auto-open functionality unless the DBF table and NTX indexes have been added to a database defined in a data dictionary.

More important than the "ease of development" features with NTXs vs. CDXs or ADIs, is the poor performance associated with NTX indexes and DBT memo files relative to the other index and memo file formats. CDX and ADI indexes store index data in a compressed format. NTX indexes do not. For example, if you have an index created on "last name", and there are 69 "Smith" last names in the index, an NTX will literally have "Smith" 69 times in the index, including trailing spaces. CDX and ADI indexes, on the other hand, would store "Smith" a maximum of one time, and never literally store trailing spaces. This means CDX and ADI indexes can store much more data in a smaller file. Any time the index is accessed to be read, searched, or updated, there is much less data that needs to be read from disk with CDX and ADI indexes than with an NTX index. Since file I/O is so slow relative to any operation you can do in memory, NTX index access will always be much slower than CDX or ADI index access because 2 to 10 times the amount of disk reads and writes will occur.

DBT memo files also perform much more poorly than FPT or ADM memo files. This is mainly due to the extra disk space needed for DBT memos due to their large and inefficient block size. But more importantly, is that DBT memos do not store the memo data length anywhere, whereas FPT memos and ADM memos do have the length of memo data readily accessible. This means that any time memo data is read from a DBT memo, the length of the DBT memo data must be sequentially counted, byte-by-byte, until a special terminator indicator is reached. FPT and ADM memos have the memo length available so that no sequential search is ever required. The sequential counting of memo data length causes DBT memo access to be slower than FPT and ADM memo access.

Limit the Number of Index Orders (Tags) Per CDX

In a multi-user system where data is being updated, developers have a decision to make regarding the trade-off between ease of development and performance when using CDX index files. As discussed in the "Do Not Use NTX Indexes and DBT Memos" section above, CDX indexes can make application index usage very simple because all index orders (tags) can be contained within a single auto-open compound CDX index file that relieves the application from having to explicitly open or close index files. CDX index files, however, do not have per-index order write lock functionality. There is only per-file write locking available. This means that any time any application in the multi-user system is updating an individual index order in the CDX, no other application on the entire system can gain access to any index order in the CDX index file for reading or writing. When there are many index orders per CDX and updates are occurring in a multi-user system, that CDX will become a bottleneck and lead to poor application throughput.

If, on the other hand, index orders are divided among multiple CDX index files, updating a single index order in one of the CDX index files will have no effect on access to the other CDX index files. For example, if you have 50 index orders in a single CDX index file, and some application needs to write to the "last name" index order in that CDX, no other users on the system will be able to access any index orders in that CDX while the update is occurring. If, however, you created 5 separate CDX index files, each with 10 index orders, some application updating the "last name" index order would only keep other users on the system from accessing one of the CDX index files while that update was in progress. The other 4 index files would be available to be read from, or written to, by all other applications on the network.

In this example scenario, the ease of development vs. performance trade-off can be seen. For maximum ease of development, putting all 50 index orders in a single auto-open CDX index file would require no specific index open/close code to be written. For best performance, however, dividing up the index orders into 5 CDX index files and writing the extra code to make sure all index files are opened and closed, would provide optimum multi-user performance. Note that this issue only applies to CDX index files and not ADI index files because ADI index files do have per-index order write locking functionality.