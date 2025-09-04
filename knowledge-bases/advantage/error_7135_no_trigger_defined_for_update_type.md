7135 No trigger defined for update type




Advantage Database Server 12  

7135 No trigger defined for update type

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7135 No trigger defined for update type  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7135 No trigger defined for update type Advantage Error Guide error\_7135\_no\_trigger\_defined\_for\_update\_type Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7135 No trigger defined for update type  Advantage Error Guide |  |  |  |  |

Problem: Triggers exist for the view, but not for the update type (INSERT, UPDATE, DELETE).

Solution: In order to update a static view, at least one trigger must exist for that update type. Create a trigger for that update type or do not perform that update to the static view.