7133 Triggers are not allowed on live views




Advantage Database Server 12  

7133 Triggers are not allowed on live views

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7133 Triggers are not allowed on live views  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7133 Triggers are not allowed on live views Advantage Error Guide error\_7133\_triggers\_are\_not\_allowed\_on\_live\_views Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7133 Triggers are not allowed on live views  Advantage Error Guide |  |  |  |  |

Problem: A trigger was created on a live view. Triggers are only allowed on static views.

Solution: Create the trigger on the view's table or re-write the view such that it produces a static cursor.