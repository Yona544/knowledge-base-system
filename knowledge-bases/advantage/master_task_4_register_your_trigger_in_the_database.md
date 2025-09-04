Task 4: Register Your Trigger in the Database




Advantage Database Server 12  

Task 4: Register Your Trigger in the Database

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Task 4: Register Your Trigger in the Database  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Task 4: Register Your Trigger in the Database Advantage Concepts master\_Task\_4\_register\_your\_trigger\_in\_the\_database Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Task 4: Register Your Trigger in the Database  Advantage Concepts |  |  |  |  |

The final step in trigger creation is to register your trigger with the database.

|  |  |
| --- | --- |
| 1. | Open ARC. |

|  |  |
| --- | --- |
| 2. | Select Database -> Open Database from the main menu. |

|  |  |
| --- | --- |
| 3. | Enter "c:\data\trig\_tutorial.add" as the database name. |

|  |  |
| --- | --- |
| 4. | Set the Advantage Connection Type to local or remote (depending on which server type you are using). |

|  |  |
| --- | --- |
| 5. | Click the Open button. |

|  |  |
| --- | --- |
| 6. | Click the OK button at the login prompt. |

|  |  |
| --- | --- |
| 7. | Expand the tables tree item. |

|  |  |
| --- | --- |
| 8. | Expand the orders table tree item. |

|  |  |
| --- | --- |
| 9. | Highlight the triggers tree item. |

|  |  |
| --- | --- |
| 10. | Set the Trigger Type to AFTER. |

Take the appropriate steps below depending on your development environment:

Borland Delphi/Kylix

|  |  |
| --- | --- |
| 1. | Select the Windows DLL or Linux Shared Object tab. |

|  |  |
| --- | --- |
| 2. | Enter "c:\data\AdsTrigs.dll" as the Container Path and Filename. |

|  |  |
| --- | --- |
| 3. | Enter "MyFunction" as the Function Name. |

|  |  |
| --- | --- |
| 4. | Click the Save button. |

|  |  |
| --- | --- |
| 5. | Enter "t1" as the trigger name. |

|  |  |
| --- | --- |
| 6. | Click the OK button. |

Microsoft Visual Studio .NET

|  |  |
| --- | --- |
| 1. | Select the COM Object or .NET Assembly tab. |

|  |  |
| --- | --- |
| 2. | Enter "AdsTrigs.trig\_functions" as the Program ID. |

|  |  |
| --- | --- |
| 3. | Enter "MyFunction" as the Function Name. |

|  |  |
| --- | --- |
| 4. | Click the Save button. |

|  |  |
| --- | --- |
| 5. | Enter "t1" as the trigger name. |

|  |  |
| --- | --- |
| 6. | Click the OK button. |