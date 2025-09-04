---
title: Arc Debugging An External Application
slug: arc_debugging_an_external_application
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_debugging_an_external_application.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: c2e389671b3eaa3590efecfde0e067ae68a0b54e
---

# Arc Debugging An External Application

Debugging an External Application

Debugging an External Application

Advantage Data Architect

| Debugging an External Application  Advantage Data Architect |  |  |  |  |

In addition to debugging scripts that are run inside of ARC, the debugger can also debug scripts being run by other applications. This functionality is not available on Advantage Local Server connections.

The basic steps required to start a debug session and debug a stored procedure that is run by an external application are described below. This example provides the steps necessary to debug a stored procedure. Other database objects such as triggers and user defined functions can be debugged using similar steps.

To start a debug session and debug a stored procedure that is run by an external application:

| 1. | Start the Advantage Data Architect (ARC). |

| 2. | Press the CTRL+Q key combination to start the SQL Utility. |

| 3. | Press the CTRL+B key combination to show the object breakpoint dialog. |

| 4. | Either type in the name of a stored procedure, or use the drop-down list to select a stored procedure. Click OK to close the dialog. |

| 5. | Press the CTRL+SHIFT+F5 key combination to start a Debug All New Connections session. |

Note If the Debug All New Connections option is not in the menu, or if the CTRL+SHIFT+F5 key does not start a debug session, you are likely currently connected using an Advantage Local Server connection. Close the SQL Utility and change your connection to use a remote server connection (via the connection properties).

| 1. | The SQL Utility will enter debug mode and wait for a new database connection to run the stored procedure. |

| 2. | Use another application (or a second instance of ARC) to execute the stored procedure. |

| 3. | When the next database connection runs the stored procedure, execution will stop at the first line in your stored procedure. The debugger will highlight the current line of execution. Variables will be visible in the Variables window. You can also hover the mouse over variables in the editor and their value will appear as a popup hint. Use the "step over" command (F10) to step line by line through your script. |

| 4. | When you are finished, either press F5 to let the script execution continue, or press SHIFT+F5 to stop the debug session. Stopping the debug session will release all server connections that were stopped on the breakpoint. |

Debugging all new connections has various implications. All new connections to the database are considered "debugee" connections, and will respect any breakpoints you have set. This means if multiple new connections execute the stored procedure in the example above, all of these connections will stop at the first line in the stored procedure. These new connections will not advance until you explicitly tell them to, or the debug session is ended.

The Connections tab in the debugger can be used to examine the state of all suspended connections, and it can be used to switch the current debugging context to a different connection. You can double-click a row in the connections table to switch debugging context. Once changed, the variable data, call stack information, and source code will be changed to reflect the state of the connection you have selected. If you would like to release this connection, simply press the F5 key to let it continue. To release all suspended connections, stop the debug session by pressing the SHIFT+F5 key combination.

If you are currently stopped at a breakpoint, and would like to debug a connection that is not currently suspended, double-click the connection in the Connections tab. The debugger will attempt to suspend the selected connection and display its debug context.

See Also

[Overview](arc_overview_debugger.md)
