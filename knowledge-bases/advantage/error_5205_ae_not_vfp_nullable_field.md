5205 AE\_NOT\_VFP\_NULLABLE\_FIELD




Advantage Database Server 12  

5205 AE\_NOT\_VFP\_NULLABLE\_FIELD

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5205 AE\_NOT\_VFP\_NULLABLE\_FIELD  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5205 AE\_NOT\_VFP\_NULLABLE\_FIELD Advantage Error Guide error\_5205\_ae\_not\_vfp\_nullable\_field Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5205 AE\_NOT\_VFP\_NULLABLE\_FIELD  Advantage Error Guide |  |  |  |  |

Problem: An operation was performed that requires a nullable field. For example, this error can occur if AdsSetNull is called for a field that cannot be set to NULL. This error may also occur when executing an UPDATE or INSERT statement with a NUL parameter that results in an attempt to set a Visual FoxPro field to NULL. For example, using the Advantage Client Engine API AdsSetEmpty on an SQL parameter will cause a NULL value to be used.

Solution: Verify that the application is specifying the correct field. If necessary, restructure the Visual FoxPro table so that the field can be set to NULL.