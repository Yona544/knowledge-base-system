7151 Invalid Table Type




Advantage Database Server 12  

7151 Invalid Table Type

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7151 Invalid Table Type  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7151 Invalid Table Type Advantage Error Guide error\_7151\_invalid\_table\_type Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7151 Invalid Table Type  Advantage Error Guide |  |  |  |  |

Problem: A Visual FoxPro DBF table was opened with either the ADS\_CDX or ADS\_NTX table type. This error occurs if the table contains field types (e.g., currency, datetime, etc.) that are not supported by the ADS\_NTX and ADS\_CDX table types.

Solution: Use the ADS\_VFP table type when opening Visual FoxPro tables.