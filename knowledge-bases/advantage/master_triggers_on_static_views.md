Triggers on Static Views




Advantage Database Server 12  

Triggers on Static Views

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Triggers on Static Views  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Triggers on Static Views Advantage Concepts master\_Triggers\_on\_static\_views Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Triggers on Static Views  Advantage Concepts |  |  |  |  |

Triggers can be defined on views for the purpose of manually updating tables used by static views. Normally, static views are not updatable, but by defining a trigger on a static view, the trigger can then perform updates to the underlying tables of the view. As a convenience, the static cursor (temporary table) of a view will be updated in addition to firing the trigger. The theory here is that the trigger would update the underlying tables of the view, therefore, modifying the contents of the view.

Notes

Result sets populated by SELECT statements on static views are not updatable. Use UPDATE/INSERT/DELETE SQL statements or open the view directly (using AdsOpenTable for example) instead.