Advantage Client Engine Architecture




Advantage Database Server 12  

Advantage Client Engine Architecture

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Client Engine Architecture  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - Advantage Client Engine Architecture Advantage Client Engine ace\_Advantage\_client\_engine\_architecture Advantage Client Engine > Introduction > Advantage Client Engine Architecture / Dear Support Staff, |  |
| Advantage Client Engine Architecture  Advantage Client Engine |  |  |  |  |

The Advantage Client Engine (ACE) is a custom-designed Application Programming Interface (API) created specifically to provide client/server access to standard Xbase DBF tables or Advantage proprietary ADT tables using the [Advantage Database Server](master_advantage_database_server.htm). The Advantage Client Engine supports native programming languages such as Borland Delphi, Borland Kylix, Borland C++Builder, Microsoft Visual Basic, Microsoft Visual C/C++, Microsoft Visual FoxPro, and CA-Visual Objects. The Advantage Client Engine also operates as the foundation for the following Advantage products: Advantage TDataSet Descendant for Delphi/Kylix/C++Builder, Advantage ODBC Driver, Advantage OLE DB Provider for ADO, Advantage .NET Data Provider, Advantage Perl DBD, and Advantage CA-Visual Objects RDDs.

The Advantage Client Engine was designed to provide database functionality through an API. In order to make using the Advantage Client Engine API simple and consistent, the concept of a handle-based hierarchy of objects has been introduced. As shown in the diagram below, [index handles](ace_index_handles.htm) are associated with [table handles](ace_table_handles.htm). Table handles and [cursor handles](ace_cursor_handles.htm) are associated with [connection handles](ace_connection_handles.htm), in a hierarchical manner. A connection is established with the Advantage server, tables and cursors are opened under a connection, and indexes are opened under a table. This provides more flexibility and control to the application developer because some functions exhibit different behavior depending on the type of handle passed to them. For example, an AdsSkip moves in indexed order when passed an index handle, and in natural order when passed a table or cursor handle.

There are several [Driver Settings](ace_driver_settings.htm) that are set globally for the Advantage Client Engine process that affect how applications are run.

For programmers migrating from an Xbase language, a current work area was specified with a Select() function, and each subsequent database operation applied to that work area. Now, with the Advantage Client Engine, the work area concept has been replaced with the handle-based hierarchy of objects, with the "work area" being determined by which handle is specified. Connection handles have been added to allow flexibility in connecting or disconnecting with the Advantage Server, as well as control over operations that are associated with specific connections.