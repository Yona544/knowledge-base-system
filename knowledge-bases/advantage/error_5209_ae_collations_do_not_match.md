5209 AE\_COLLATIONS\_DO\_NOT\_MATCH




Advantage Database Server 12  

5209 AE\_COLLATIONS\_DO\_NOT\_MATCH

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5209 AE\_COLLATIONS\_DO\_NOT\_MATCH  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5209 AE\_COLLATIONS\_DO\_NOT\_MATCH Advantage Error Guide error\_5209\_ae\_collations\_do\_not\_match Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5209 AE\_COLLATIONS\_DO\_NOT\_MATCH  Advantage Error Guide |  |  |  |  |

Problem: A table was opened that has one or more indexes built with collations that do not match the currently specified collation.

Solution: The purpose of this error is to raise visibility to the potential optimization problems that can occur when [dynamic collations](master_collation_support.htm) are used. For example, if the static OEM collation is currently being used and a table has an index built using MACHINE\_VFP\_BIN\_895, then this error will be generated when the table is opened. This can be avoided by specifying the appropriate dynamic collation for the table or SQL statement.

If an application needs to use multiple collations concurrently on a single table, this error can be turned off with the [sp\_AllowMultipleCollations](master_sp_allowmultiplecollations.htm) system procedure.