Memo Block Size




Advantage Database Server 12  

Memo Block Size

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Memo Block Size |  |  | Feedback on: Advantage Database Server 12 - Memo Block Size odbc\_Memo\_block\_size Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Memo Block Size |  |  |  |  |

Memo block size is used when creating FoxPro-compatible FPT and Advantage-proprietary ADM memo files. The size of the memo block is configurable to allow you to conserve disk space. The default value is 64 bytes. For example, if a memo has 100 bytes with a block size of 64 bytes, two blocks would be allocated to store the memo. To eliminate the 36 bytes of unused space, you may set the block size to 100. A memo block size of 50 would also result in no wasted space.

Note For FoxPro FPT files, the values that may be entered for the block size is 1 - 1024. The minimum block size allowed is 33 bytes. If 1-32 is specified, the actual block size is n x 512 bytes, where n is 1 - 32. For Advantage ADM files, valid memo block sizes are from 8-32768 bytes.