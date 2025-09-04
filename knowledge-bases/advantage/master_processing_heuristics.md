Processing Heuristics




Advantage Database Server 12  

Processing Heuristics

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Processing Heuristics  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Processing Heuristics Advantage SQL Engine master\_Processing\_heuristics Advantage SQL > SQL Functionality > Processing Heuristics / Dear Support Staff, |  |
| Processing Heuristics  Advantage SQL Engine |  |  |  |  |

Processing for SQL statements is performed almost entirely on the server. In general, the client sends the SQL statements to the Advantage Database Server, which then executes them. For SELECT statements, the server initializes the cursor and returns a handle to the client. The client then uses that handle in much the same way it uses normal table handles. For other statements (CREATE, DROP, INSERT, UPDATE, and DELETE), the processing is completed entirely on the server, and a status code is passed back to the client. Note that when you use Advantage Local Server, all processing is performed on the client workstation, so there is no division of processing between a client and a server. Otherwise, the general processing steps apply whether Advantage Database Server or Advantage Local Server is being used.

Transferring the Entire Table to the Client

During execution of SQL statements, only information requested by the client application will be transferred to the client. For example, it is not possible for an entire table to be transferred to the client unless the client specifically requests each record.

How Live Cursors are Processed

The following steps are performed for live cursors:

|  |  |
| --- | --- |
| · | •   Client application requests execution of SQL statement (e.g., SELECT \* from employee where empid < 100 order by lastname) |

|  |  |
| --- | --- |
| · | •   The Advantage Client Engine passes SQL statement (with parameters if supplied) to the server. |

|  |  |
| --- | --- |
| · | •   Server parses the statement and determines it can be a live cursor. |

|  |  |
| --- | --- |
| · | •   Server sets the AOF (Advantage Optimized Filter) "empid < 100". |

|  |  |
| --- | --- |
| · | •   Server determines if there is an available index for the ORDER BY clause. If so, it is used; otherwise it builds a temporary index to satisfy the ORDER BY. |

|  |  |
| --- | --- |
| · | •   Server returns the cursor handle to the Advantage Client Engine. |

|  |  |
| --- | --- |
| · | •   The client application uses the cursor handle in the same fashion as a normal table handle. Only the records requested by the client application are passed from the server to the Advantage Client Engine. |

How Static Cursors are Processed

The following steps are performed for static cursors:

|  |  |
| --- | --- |
| · | •   Client application requests execution of SQL statement (e.g., SELECT \* from customer, orders where customer.id = orders.custid and customer.name = 'Company') |

|  |  |
| --- | --- |
| · | •   The Advantage Client Engine passes SQL statement (with parameters if supplied) to the server. |

|  |  |
| --- | --- |
| · | •   Server parses the statement and determines it cannot be a live cursor. |

|  |  |
| --- | --- |
| · | •   Server executes the SQL statement and creates a temporary static cursor with the first row of the rowset. |

|  |  |
| --- | --- |
| · | •   Server returns the handle of the static cursor to the Advantage Client Engine. |

|  |  |
| --- | --- |
| · | •   The client application uses the cursor handle in the same fashion as it does a read-only table. Again, only the records of the static cursor requested by the client application are stored in a temporary file that is then passed from the server to the Advantage Client Engine. The temporary table is populated sequentially up to the requested record. |

|  |  |
| --- | --- |
| · | •   When the client application closes the cursor, the server removes the temporary static cursor. |

How Non-Select Statements are Processed

The following steps are performed for non-select statements:

|  |  |
| --- | --- |
| · | •   Client application requests execution of SQL statement (e.g., DELETE from customer where id = 10) |

|  |  |
| --- | --- |
| · | •   The Advantage Client Engine passes SQL statement (with parameters if supplied) to the server. |

|  |  |
| --- | --- |
| · | •   Server parses the statement and determines that it does not produce a rowset. |

|  |  |
| --- | --- |
| · | •   Server executes the SQL statement and returns the status to the client. |

Note When statements are prepared via AdsPrepareSQL, they can be executed via AdsExecuteSQL multiple times. The actual statement is passed to the server on the first call to AdsExecuteSQL. Each subsequent call to AdsExecuteSQL uses the existing parsed statement on the server and only the changed parameters are passed to the server.