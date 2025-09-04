7124 Incorrect Record Count




Advantage Database Server 12  

7124 Incorrect Record Count

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7124 Incorrect Record Count  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7124 Incorrect Record Count Advantage Error Guide error\_7124\_incorrect\_record\_count Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7124 Incorrect Record Count  Advantage Error Guide |  |  |  |  |

Problem: The table contains an incorrect record count in its header. The physical length of the table does not equal the table header length plus the field header length times the number of fields plus the record count times the record length.

Solution 1: If the physical table ends at the logical end of a record, the record count in the header will be automatically updated by Advantage. However, any indexes built on the table will likely be logically or physically corrupt. All indexes on the table should then be rebuilt.

Solution 2: If the physical table does not end at the logical end of a record, the table is physically corrupt. If the table is an ADT (Advantage Proprietary Table), run the ADT table repair utility (ADTFIX.EXE) against the offending ADT table. This utility is available for download from the Advantage Developer Zone Web site in the "Tools & Utilities" section, <http://DevZone.AdvantageDatabase.com>. Once the table has been fixed, all indexes on the table should then be rebuilt.