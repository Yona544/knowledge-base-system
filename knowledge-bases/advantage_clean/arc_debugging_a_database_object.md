---
title: Arc Debugging A Database Object
slug: arc_debugging_a_database_object
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_debugging_a_database_object.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: a1f8797d28c25734d18cca984d0ebb57d01b9764
---

# Arc Debugging A Database Object

Debugging a Database Object

Debugging a Database Object

Advantage Data Architect

| Debugging a Database Object  Advantage Data Architect |  |  |  |  |

This topic covers the basic steps involved in starting a debug session to debug a database object. This example provides the steps necessary to debug a stored procedure. Other database objects such as triggers and user defined functions can be debugged using similar steps. For more detailed information on controlling execution once a session is started, see the [Controlling Script Execution](arc_controlling_script_execution.md) topic.

Note These instructions use keyboard shortcuts, but the menu items or toolbar buttons can be used as well.

To start a debug session and debug a stored procedure:

| 1. | Start the Advantage Data Architect (ARC). |

| 2. | Press the CTRL+Q key combination to start the SQL Utility. |

| 3. | Press the CTRL+B key combination to show the object breakpoint dialog. |

| 4. | Either type in the name of a stored procedure, or use the drop-down list to select a stored procedure. Click OK to close the dialog. |

| 5. | At this point you can either open an existing script that calls the stored procedure, or enter a new script that executes the procedure in question. Later in this topic a tip is provided that explains how to have ARC automatically write a test script and set up a debug session, but for learning purposes the rest of these instructions will describe the "long way". |

| 6. | Select File -> Open SQL Script from the main menu to open an existing script, or select File -> New SQL Script from the main menu to start a new script. |

| 7. | If starting a new script, the following script can be used for testing. Paste this script into the editor and press CTRL+S to save the script. Note the procedure name and parameters will need to be changed to match your stored procedure. |

EXECUTE PROCEDURE MyProcedure( :input1, :input2 );

| 1. | Press the F5 key to run the script. |

| 2. | If you have not supplied values in the past for the parameters, ARC will prompt you for parameter data. Enter that data and click OK. If in the future you want to change the parameter data you have supplied, select Parameters from the SQL menu. |

| 3. | The SQL Utility will run the script and execution will stop at the first line in your stored procedure. The debugger will highlight the current line of execution. Variables will be visible in the Variables window. You can also hover the mouse over variables in the editor and their value will appear as a popup hint. Use the "step over" command (F10) to step line by line through your script. |

| 4. | When you are finished, either press F5 to let the script execution continue, or press SHIFT+F5 to stop the debug session. |

Once you are familiar with object breakpoints and the functionality they provide, you may want to use a shortcut when debugging database objects. If you right-click on an object in the database, most objects have a Debug/Test quick menu option. Selecting this option will automatically open an SQL Utility window, set an object breakpoint on the object, and write a small test script that can be used to debug the object.

Note Trigger objects have a Test/Debug button on the trigger properties dialog (right-click on the table and select Triggers to open this dialog).

An alternate approach to using an object breakpoint is to simply step into the object from your base script. In the example above, a line breakpoint can be set on the EXECUTE PROCEDURE call. Once execution stops there, you can press F11 to step into the procedure. The same method works for user defined functions, as well as DML statements that fire triggers. For example, if you had an INSERT statement in your base script, and the table has an insert trigger defined, you can press F11 when execution reaches the INSERT statement and step into the trigger source code.

Once object source code is loaded into the debugger, you can make changes and persist these changes back to the database by saving the editor buffer. You can then press F5 to start a new debug session and test the changes you have just made to the object. The SQL Utility will automatically save modified buffers each time a debug session is initiated, so you can simply make changes in the editor and press F5 to immediately test your changes.

See Also

[Overview](arc_overview_debugger.md)
