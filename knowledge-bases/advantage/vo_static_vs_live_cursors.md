Static vs. Live Cursors




Advantage Database Server 12  

Static vs. Live Cursors

Advantage AXSQL RDDs

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Static vs. Live Cursors  Advantage AXSQL RDDs |  |  | Feedback on: Advantage Database Server 12 - Static vs. Live Cursors Advantage AXSQL RDDs vo\_Static\_vs\_live\_cursors Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Using the Advantage AXSQL RDDs > Static vs. Live Cursors / Dear Support Staff, |  |
| Static vs. Live Cursors  Advantage AXSQL RDDs |  |  |  |  |

SQL result sets returned from Advantage are called cursors. Cursors come in two flavors: live and static. A live cursor is a cursor that can be updated. It is essentially an open table with any specified filters (WHERE clause) or orderings (ORDER BY) applied.

A static cursor is a cursor that is read-only. Static cursors are the result of SQL queries where Advantage had to create a temporary table to contain the result set. Any updates to that temporary table wouldnt be reflected in the base tables of the query, so the result set is marked read-only.

The AXSQL RDDs treat both types of cursors the same way and it is important for you to understand that static cursors typically cannot be updated. See [Cursor Types](master_cursor_types.htm) for more information on cursors. Despite all static cursors being read-only, there exists one method by which the base tables of a static cursor can be updated by updating a static cursor. This is done by creating triggers on a view. For more information see [Triggers on Static Views](master_triggers_on_static_views.htm).