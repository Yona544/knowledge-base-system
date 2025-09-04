7087 Permission not granted for the requested operation




Advantage Database Server 12  

7087 Permission not granted for the requested operation

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7087 Permission not granted for the requested operation  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7087 Permission not granted for the requested operation Advantage Error Guide error\_7087\_permission\_not\_granted\_for\_the\_requested\_operation Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7087 Permission not granted for the requested operation  Advantage Error Guide |  |  |  |  |

Problem: An operation on a database table failed because it requires permission not granted to the user performing the operation. Some of the possible causes are:

|  |  |
| --- | --- |
| · | Attempting to update an existing row in the table but the UPDATE permission was not granted on the table or not granted on some columns to be modified, |

|  |  |
| --- | --- |
| · | Attempting to insert a new row in the table but the INSERT permission was not granted on the table |

|  |  |
| --- | --- |
| · | Attempting to delete a row in a table but the DELETE permission was not granted on the table |

|  |  |
| --- | --- |
| · | Attempting to set a filter or scope on a table but the filter expression or the scope index contains columns that the user has no READ permission |

Solution: If the requested operation is necessary, the database administrator must grant the user the appropriate permission.

Problem: An attempt to open a [free table](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)) failed because access to [free table](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)) is restricted on this [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)).

Solution: If the requested operation is necessary, the application must not set the CheckFreeTableAccess option to true when connecting to the data dictionary.