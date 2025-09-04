Troubleshooting




Advantage Database Server 12  

Troubleshooting

Advantage TDataSet Descendant

Managing Multiple Versions

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Troubleshooting  Advantage TDataSet Descendant  Managing Multiple Versions |  |  | Feedback on: Advantage Database Server 12 - Troubleshooting Advantage TDataSet Descendant Managing Multiple Versions ade\_Troubleshooting Advantage TDataSet Descendant > Managing Multiple Versions > Troubleshooting / Dear Support Staff, |  |
| Troubleshooting  Advantage TDataSet Descendant  Managing Multiple Versions |  |  |  |  |

In the event a switch operation fails, you can add the following two lines to the "CustomSettings.ini" file in the application directory (or create the file if it does not exist).

[Settings]

TraceLog = 1

If these lines are present, the application will create a log file named TDSSwitch.log in the application directory. This file will contain some additional information that can be used to help determine what happened. In addition, following is a list of errors that the application can return:

1000 More data is available. (This should never be returned by the application.)

1001 No Delphi/C++Builder IDEs were detected.

1002 The Delphi/C++Builder IDE is not supported by this version of the utility.

1003 The top-level backup directory could not be located.

1004 The backup operation failed. See the specific error code for more information.

1005 The design-time BPL in-use by the selected IDE could not be determined.

1006 The TDataSet Install directory could not be located.

1007 Unable to write to the registry.

1008 Unable to read from the registry.

1009 The buffer passed to a function was insufficient to hold the value returned.

1010 The TDataSet Switch failed. See the specific error code for more information.

1011 The ace32.dll file could not be located in the search path.

1012 A seek operation inside a file failed.

1013 A file read failure occurred.