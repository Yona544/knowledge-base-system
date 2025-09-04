7123 Unreconginzed Field Type




Advantage Database Server 12  

7123 Unreconginzed Field Type

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7123 Unreconginzed Field Type  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7123 Unreconginzed Field Type Advantage Error Guide error\_7123\_unreconginzed\_field\_type Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7123 Unreconginzed Field Type  Advantage Error Guide |  |  |  |  |

Problem: An unrecognized field type was found in the table. The table was either created by a newer version of Advantage, or it has been corrupted.

Solution: Verify the version of Advantage Database Server supports the field type. If not, upgrade the server to a newer version that does. If it already does support the field type, then the table is most likely physically corrupt. If the table is an ADT (Advantage Proprietary Table), run the ADT table repair utility (ADTFIX.EXE) against the offending ADT table. This utility is available for download from the Advantage Developer Zone Web site in the "Tools & Utilities" section, <http://DevZone.AdvantageDatabase.com>.