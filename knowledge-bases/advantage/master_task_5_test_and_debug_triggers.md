Task 5: Test and Debug




Advantage Database Server 12  

Task 5: Test and Debug

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Task 5: Test and Debug  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Task 5: Test and Debug Advantage Concepts master\_Task\_5\_test\_and\_debug\_triggers Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Task 5: Test and Debug  Advantage Concepts |  |  |  |  |

The final step of this tutorial will be to configure your development environment to debug your trigger. Basic trigger debugging techniques are described in the general [trigger](master_triggers.htm) documentation. Please read [Debugging Triggers](master_debugging_triggers.htm) before continuing.

The steps below will configure your development environment to use the Advantage Local Server to debug your trigger. Once you have tried your trigger with local server, you can come back and re-configure your development environment to use the Advantage Database Server (as described in the [Debugging Triggers](master_debugging_triggers.htm) topic.)

Take the appropriate steps below depending on your development environment:

Borland Delphi/Kylix

|  |  |
| --- | --- |
| 1. | Select Run -> Parameters from the main menu. |

|  |  |
| --- | --- |
| 2. | Enter the path to ARC as the host application (default path is c:\Program Files\Advantage X.x\ARC\arc32.exe). |

|  |  |
| --- | --- |
| 3. | Click the OK button. |

|  |  |
| --- | --- |
| 4. | Select Project -> Options from the main menu. |

|  |  |
| --- | --- |
| 5. | Select the Linker tab. |

|  |  |
| --- | --- |
| 6. | Check Include TD32 debug info and Include remote debug symbols. These are necessary to debug, but keep in mind they make the binary bigger, and should be removed when doing a release build. |

|  |  |
| --- | --- |
| 7. | Click the OK button. |

|  |  |
| --- | --- |
| 8. | Set a breakpoint at the beginning of MyFunction. |

|  |  |
| --- | --- |
| 9. | Select Run -> Run from the main menu to start the debugger. |

|  |  |
| --- | --- |
| 10. | Skip to the bottom of this page and continue with the environment-independent steps. |

Microsoft Visual Studio .NET (C# users)

|  |  |
| --- | --- |
| 1. | Highlight AdsTrigs in the Solution Explorer. |

|  |  |
| --- | --- |
| 2. | Select Project -> Properties from the main menu. |

|  |  |
| --- | --- |
| 3. | Select Configuration Properties. |

|  |  |
| --- | --- |
| 4. | Select Debugging. |

|  |  |
| --- | --- |
| 5. | Change the Debug Mode to Program. |

|  |  |
| --- | --- |
| 6. | Enter the path to ARC as the Start Application (default path is c:\Program Files\Advantage X.x\ARC\arc32.exe). |

Note In some versions of Visual Studio you will have to click the Apply button before it will let you enter the application path and filename.

|  |  |
| --- | --- |
| 7. | Click the OK button. |

|  |  |
| --- | --- |
| 8. | Set a breakpoint at the beginning of MyFunction |

|  |  |
| --- | --- |
| 9. | Select Debug -> Start to start the debugger. |

|  |  |
| --- | --- |
| 10. | Skip to the bottom of this page and continue with the environment-independent steps. |

Microsoft Visual Studio .NET (VB users)

|  |  |
| --- | --- |
| 1. | Highlight AdsTrigs in the Solution Explorer. |

|  |  |
| --- | --- |
| 2. | Select Project -> Properties from the main menu. |

|  |  |
| --- | --- |
| 3. | Select Configuration Properties. |

|  |  |
| --- | --- |
| 4. | Select Debugging. |

|  |  |
| --- | --- |
| 5. | Select the Start External Program radio button. |

|  |  |
| --- | --- |
| 6. | Enter the path to ARC as the External Program (default path is c:\Program Files\Advantage X.x\ARC\arc32.exe). |

Note In some versions of Visual Studio you will have to click the Apply button before it will let you enter the application path and filename.

|  |  |
| --- | --- |
| 7. | Click the OK button. |

|  |  |
| --- | --- |
| 8. | Set a breakpoint at the beginning of MyFunction |

|  |  |
| --- | --- |
| 9. | Select Debug -> Start to start the debugger. |

|  |  |
| --- | --- |
| 10. | Skip to the bottom of this page and continue with the environment-independent steps. |

The following steps should be completed for all development environments:

|  |  |
| --- | --- |
| 1. | Use ARC to open the orders table (using local server). |

|  |  |
| --- | --- |
| 2. | Add a new record and post it. |

|  |  |
| --- | --- |
| 3. | The debugger will stop on your breakpoint. |

|  |  |
| --- | --- |
| 4. | Step through the trigger code to get a better understanding of how your trigger works. |

Congratulations! Youve just written and tested your first trigger.