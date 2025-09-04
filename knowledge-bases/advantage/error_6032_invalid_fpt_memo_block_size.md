6032 Invalid FPT memo block size




Advantage Database Server 12  

6032 Invalid FPT memo block size

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6032 Invalid FPT memo block size  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6032 Invalid FPT memo block size Advantage Error Guide error\_6032\_invalid\_fpt\_memo\_block\_size Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6032 Invalid FPT memo block size  Advantage Error Guide |  |  |  |  |

Problem: An invalid FPT memo block size was specified.

Solution: Correct the program so that a valid FPT memo block size is set. Set the block size to <n>. If <n> is 1-32 inclusive, the block size is 512 \* bytes where <n> is 1 to unlimited bytes. If <n> is greater than 32, the block size is <n> bytes.