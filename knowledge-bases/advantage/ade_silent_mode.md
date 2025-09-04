Silent Mode




Advantage Database Server 12  

Silent Mode

Advantage TDataSet Descendant

Managing Multiple Versions

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Silent Mode  Advantage TDataSet Descendant  Managing Multiple Versions |  |  | Feedback on: Advantage Database Server 12 - Silent Mode Advantage TDataSet Descendant Managing Multiple Versions ade\_Silent\_mode Advantage TDataSet Descendant > Managing Multiple Versions > Silent Mode / Dear Support Staff, |  |
| Silent Mode  Advantage TDataSet Descendant  Managing Multiple Versions |  |  |  |  |

To facilitate the use of batch files to automate switching between TDataSet Versions, the Switch utility can operate in a silent mode. To use the utility in silent mode, specify all required parameters via the command-line.

The command-line syntax is as follows:

TDataSet\_Switch.exe <Delphi\_IDE\_Ver> <New\_TDS\_Ver> [<Current\_TDS\_Ver>]

Where <Delphi\_IDE\_Ver> is the version of Delphi/C++Builder whose installed TDataSet is to be changed, <New\_TDS\_Ver> is the version of the TDataSet to switch to, and <Current\_TDS\_Ver> is the currently-installed TDataSet version for the Delphi IDE specified.

Note If <Current\_TDS\_Ver> is specified, the current TDataSet version will be backed-up.

To change the installed TDataSet version for Delphi 7 to version 7.1 without backing up the current TDataSet version, the following command would be used:

TDataSet\_Switch.exe "Delphi 7" "Version 7.1"