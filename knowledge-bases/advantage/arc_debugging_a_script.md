Debugging a Script




Advantage Database Server 12  

Debugging a Script

Advantage Data Architect

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Debugging a Script  Advantage Data Architect |  |  | Feedback on: Advantage Database Server 12 - Debugging a Script Advantage Data Architect arc\_Debugging\_a\_script Advantage Data Architect > SQL Debugger > Debugging a Script / Dear Support Staff, |  |
| Debugging a Script  Advantage Data Architect |  |  |  |  |

This topic covers the basic steps involved in starting a debug session to debug a script. For more detailed information on controlling execution once a session is started, see the [Controlling Script Execution](arc_controlling_script_execution.htm) topic.

Note These instructions use keyboard shortcuts, but the menu items or toolbar buttons can be used as well.

To start a debug session:

|  |  |
| --- | --- |
| 1. | Start the Advantage Data Architect (ARC). |

|  |  |
| --- | --- |
| 2. | Press the CTRL-Q key combination to start the SQL Utility. |

|  |  |
| --- | --- |
| 3. | Select File -> "Open SQL Script" from the main menu to open an existing script, or select File -> "New SQL Script" from the main menu to start a new script. |

|  |  |
| --- | --- |
| 4. | If starting a new script, the following script can be used for testing. Paste this script into the editor and press CTRL-S to save the script. |

DECLARE I integer;

I = 0;

While ( I < 10 ) do

I = I + 1;

End While;

|  |  |
| --- | --- |
| 1. | Place the cursor on a location in the script where you would like to stop the script execution and press the F9 key. A breakpoint will be created and the line in the editor will be highlighted. |

|  |  |
| --- | --- |
| 2. | Press the F5 key to run the script. |

|  |  |
| --- | --- |
| 3. | The SQL Utility will run the script until your breakpoint is reached, at which point script execution will pause and the debugger will highlight the current line of execution. Variables will be visible in the Variables window. You can also hover the mouse over variables in the editor and their value will appear as a popup hint. Use the "step over" command (F10) to step line by line through your script. |

|  |  |
| --- | --- |
| 4. | When you are finished, either press F5 to let the script execution continue, or press SHIFT+F5 to stop the debug session. |

See Also

[Overview](arc_overview_debugger.htm)