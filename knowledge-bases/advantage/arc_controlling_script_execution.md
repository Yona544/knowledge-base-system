Controlling Script Execution




Advantage Database Server 12  

Controlling Script Execution

Advantage Data Architect

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Controlling Script Execution  Advantage Data Architect |  |  | Feedback on: Advantage Database Server 12 - Controlling Script Execution Advantage Data Architect arc\_Controlling\_script\_execution Advantage Data Architect > SQL Debugger > Controlling Script Execution / Dear Support Staff, |  |
| Controlling Script Execution  Advantage Data Architect |  |  |  |  |

This topic covers the various commands which can be used to control the execution of a script once you have stopped at a breakpoint. The commands in this topic will list the default keyboard shortcut in parentheses next to the name of the command. See the [Changing Keyboard Shortcuts](arc_changing_keyboard_shortcuts.htm) topic for details on customizing these shortcuts.

Starting a Debug Session (F5)

If you have at least one breakpoint defined, you can simply use the F5 keyboard shortcut, the same shortcut you use to run scripts that you are not debugging. The existence of a breakpoint will provide a clue to the SQL Utility that you would like to start a debug session.

If you want to start a debug session, but do not have any breakpoints defined (for example, if you plan on explicitly breaking the execution later), use the CTRL+F5 keyboard shortcut, which explicitly starts a debug session.

Stopping a Debug Session (SHIFT+F5)

Use the square stop button on the SQL Utility toolbar or the SHIFT+F5 command to stop a debug session. Breakpoints from your current debug session are maintained.

Restarting a Debug Session (F5)

To restart a debug session, press F5.

"Breaking" a Debug Session

If a script is running in debug mode and has not reached a breakpoint, you can force the script to break by clicking the pause button on the SQL Utility toolbar, or selecting Debug Break from the SQL menu.

This functionality can be helpful when trying to find infinite loops in a script, or portions of a script that are taking a considerable amount of time to finish. In these situations you can start a debug session explicitly (use the CTRL+F5 keyboard shortcut, as opposed to F5, which will only start a debug session if you have a breakpoint set). Once the script has run long enough to reach a point where you suspect it has "hung", use the debug break command to stop the script and inspect its current execution point.

Step Commands

Step Over (F10)

The Step Over command will advance the script execution one statement. If the current statement is a call to a stored procedure or function, or if it is a DML statement that fires a trigger, the debugger will NOT enter the database object.

Step Into (F11)

The Step Into command will advance the script execution one statement. If the current statement is a call to a stored procedure or function, or if it is a DML statement that fires a trigger, the debugger will step into the object and stop at the first executable statement in that object. You can also step into scripts that you run via a call to EXECUTE IMMEDIATE.

Step Out (SHIFT-F11)

The Step Out command will leave the current stack frame and stop at the next statement to be executed outside of the current stack frame. If, for example, you had stepped into a stored procedure script, a Step Out command can be performed at any point to return to the script that called the stored procedure.

Run to Cursor (F4)

The Run to Cursor command can be used to execute the script until it reaches the current cursor location. Note if breakpoints exist between the current execution point and the cursor, the debugger will stop at those breakpoints rather than continuing to the cursor position.

The step commands and the Run To Cursor command are generally used once a debug session is started, but they can also be used to start a debug session. For example, you can open a script in the SQL Utility and then hit the F10 key to start debugging from the first line in the script. The Run To Cursor command can be used in a similar fashion to start a debug session and stop when execution reaches the cursor.

Continuing After Stopping at a Breakpoint (F5)

To continue script execution until the next breakpoint (or to the end of the script), press the F5 keyboard shortcut or the Continue Execution toolbar button.

See Also

[Overview](arc_overview_debugger.htm)