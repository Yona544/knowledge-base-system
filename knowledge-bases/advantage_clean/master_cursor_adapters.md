---
title: Master Cursor Adapters
slug: master_cursor_adapters
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_cursor_adapters.htm
source: Advantage CHM
tags:
  - master
checksum: c8bc69d67a502629ee72d0690673b434a7fd5205
---

# Master Cursor Adapters

Cursor Adapters

Cursor Adapters

Advantage and Visual FoxPro

| Cursor Adapters  Advantage and Visual FoxPro |  |  |  |  |

The CursorAdapter in Visual FoxPro is an extensible class that uses ADO (e.g., through OLE DB) to provide access to external data. The following steps show one way to access data through a CursorAdapter. While it is possible to use an ODBC driver through ADO, the best way to use a CursorAdapter with Advantage is to go through the Advantage OLE DB provider.

| 1. | Verify that the Advantage OLE DB Provider is installed. |

| 2. | Open the Data Explorer in Visual FoxPro. You can do this by using the command "DO dataexplorer.app". The dataexplorer.app file should exist in your Visual FoxPro installation directory. |

| 3. | Add a connection in the Data Explorer. Choose the "Add Connection" button and then select "ADO Connection". |

| 4. | Click on the "Use connection string" option to use the Advantage OLE DB provider. You can use the Build button to create the connection string, or you can type it into the edit field. An example connection string to a directory containing free tables might be "Provider=Advantage.OLEDB.1;Data Source=x:\data\freetables;ServerType=ADS\_REMOTE\_SERVER; TableType=ADS\_VFP\_TABLE". This connection string specifies that Advantage Database Server (remote server) is to be used and that the table type is VFP (Visual FoxPro). An example connection string to a data dictionary using Advantage Local Server is: "Provider=Advantage.OLEDB.1;User ID=adssys;Data Source=x:\data\dd\test.add;ServerType=ADS\_LOCAL\_SERVER". |

| 5. | If you want Visual FoxPro to be able to access data natively and share it concurrently with Advantage Database Server, you need to choose compatibility locking. For example, add "LockMode=ADS\_COMPATIBLE\_LOCKING" to the connection string. The default is to use proprietary locking. |

| 6. | After creating the connection, expand the connection in Data Explorer and then expand the Tables tree. Drag (with the mouse) one of the tables onto a code window. Visual FoxPro will generate the code to create a CursorAdapter instance for that table. |

| 7. | You can use the generated code as needed. For example, add a Browse command at the bottom of the generated code and run the code to view the table. Note that you can browse tables directly from the Data Explorer too. |

See Also

[Getting Started with Visual FoxPro](master_getting_started_with_visual_foxpro.md)

[Remote Views](master_remote_views.md)

[SQL Pass Through](master_sql_pass_through.md)
