Nested and Recursive Triggers




Advantage Database Server 12  

Nested and Recursive Triggers

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nested and Recursive Triggers  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Nested and Recursive Triggers Advantage Concepts master\_Nested\_and\_recursive\_triggers Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Nested and Recursive Triggers  Advantage Concepts |  |  |  |  |

Nested triggers (performing an operation in one trigger, which causes another trigger to fire) and recursive triggers are supported.

Nested and recursive triggers are limited to 64 levels of server re-entrance before an error is returned. This prevents a run-away trigger from hogging CPU time and an Advantage worker thread.

INSTEAD OF and AFTER triggers do not support recursion when called on the base table that they are assigned to. These triggers are allowed to operate on the base table without firing themselves again. However, if these triggers modify some other table that has a trigger, that trigger will be fired.