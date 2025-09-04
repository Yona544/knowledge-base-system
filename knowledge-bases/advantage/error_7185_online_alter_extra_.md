7185 Online Alter Extra Indexes




Advantage Database Server 12  

7185 Online Alter Extra Indexes

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7185 Online Alter Extra Indexes  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7185 Online Alter Extra Indexes Advantage Error Guide Error\_7185\_Online\_Alter\_Extra\_ Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7185 Online Alter Extra Indexes  Advantage Error Guide |  |  |  |  |

Problem: Extra indexes belonging to the alter table were found open but not specified in the ALTER call.

Solution1: Add the extra non-auto open indexes to a data dictionary to ensure they get opened during the ALTER call.

Solution2: Close all other instances of the table being altered so no extra indexes are found.  Only do this if you are certain the changes during the alter do not require rebuilding the extra indexes.