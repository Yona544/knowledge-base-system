---
title: Arc Setting Breakpoints
slug: arc_setting_breakpoints
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_setting_breakpoints.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: ec2c9147ed85d02977186c88991716dc7d613a2b
---

# Arc Setting Breakpoints

Setting Breakpoints

Setting Breakpoints

Advantage Data Architect

| Setting Breakpoints  Advantage Data Architect |  |  |  |  |

A breakpoint is a location in the script execution where you would like the debugger to stop and present debug information (such as current variable values).

Two types of breakpoints are supported; line and object. A line breakpoint is simply a location in a script. An object breakpoint instructs the debugger to stop at the very first line in the specified object. The object can be a stored procedure, trigger, user defined function, etc.

Line Breakpoint

A line breakpoint can be set using any of the following techniques:

- Place the cursor at a specific line in the editor and press the F9 key. Pressing the F9 key again will clear the breakpoint.

- Place the cursor at a specific line in the editor and select Debug -> Select/Clear Breakpoint from the SQL menu.

- Use the mouse and click once in the editor gutter on the line you would like to create a breakpoint at. The editor gutter is the slim gray strip on the left side of the editor buffer that contains the script source code.

- Select the Breakpoints tab at the bottom of the SQL Utility window. Select New -> Break at Current Line from the breakpoint menu.

Note Line breakpoints can also be set inside database objects (such as stored procedures) once the objects source code has been loaded into an editor tab, which usually happens after hitting an initial object breakpoint, or by stepping into a database object using the "step in" debug command.

Object Breakpoint

An object breakpoint can be set using any of the following techniques:

- Press the CTRL+B key combination to bring up the object breakpoint dialog. Either start typing the name of the object, or use the drop-down menu to select an object. Click OK.

- Select the Breakpoints tab at the bottom of the SQL Utility window. Select New -> Break in Object from the breakpoint menu. Either start typing the name of the object, or use the drop-down menu to select an object. Click OK.

If you have multiple breakpoints defined, you can double-click on a breakpoint row in the Breakpoints tab and the editor will jump to the specified breakpoint. Note this only works for line breakpoints.

See Also

[Overview](arc_overview_debugger.md)
