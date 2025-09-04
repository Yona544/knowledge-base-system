Installing the Optional Advantage Extended Libraries




Advantage Database Server 12  

Installing the Optional Advantage Extended Libraries

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Installing the Optional Advantage Extended Libraries  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - Installing the Optional Advantage Extended Libraries Advantage Visual Objects and Vulcan.NET RDD vo\_Installing\_the\_\_optional\_advantage\_aef\_files Advantage Visual Objects and Vulcan.NET RDD > Introduction > Installing the Optional Advantage Extended Libraries / Dear Support Staff, |  |
| Installing the Optional Advantage Extended Libraries  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

The Advantage AEF files for Visual Objects, DBFAXS.AEF, ACE.AEF, and AdsDBSer.AEF, are installed with the setup program. To import the AEF and use the library, follow the steps below.

|  |  |
| --- | --- |
| 1. | From the Visual Objects Application Browser, select File on the menu bar, then Import. |

|  |  |
| --- | --- |
| 2. | Choose DBFAXS.AEF from the Advantage directory and click OK to import the library. |

|  |  |
| --- | --- |
| 3. | Choose ACE.AEF from the Advantage directory and click OK to import the library. |

|  |  |
| --- | --- |
| 4. | Click on the application that will use the Advantage advanced commands and functions. |

|  |  |
| --- | --- |
| 5. | Select Application on the menu bar, then Properties to edit the data in the Applications Properties window. |

|  |  |
| --- | --- |
| 6. | Click on the DBFAXS entry in the Available list of libraries to put the entry into the Libraries list. |

|  |  |
| --- | --- |
| 7. | Add the AdsDBServer to the Libraries list. |

|  |  |
| --- | --- |
| 8. | Change the application server class to inherit from AdsDBServer instead of DBServer. |

|  |  |
| --- | --- |
| 9. | Compile the application. |

The Advantage Extended Libraries for Vulcan.NET, DBFAXS.prg, DBFAXS.vh, and AdsSQLServer.prg are installed with the setup program.  To Add these files to your Vulcan.NET project follow the steps below.

|  |  |
| --- | --- |
| 1. | Select your project in the Solution Explorer. |

|  |  |
| --- | --- |
| 2. | Either right click on the project name and select Add -> Existing Item or click Project -> Add Existing Item on the menu bar. |

|  |  |
| --- | --- |
| 3. | Browse to the Advantage Vulcan.NET installation directory (C:\Program Files\Advantage X.x\Vulcan.NET by default) and select DBFAXS.vh, DBFAXS.prg, and AdsSQLServer.prg. |

|  |  |
| --- | --- |
| 4. | Right click on your project and select "Add Reference..." or click Project -> Add Reference... from the menu bar. |

|  |  |
| --- | --- |
| 5. | Scroll to the bottom of the component list and select "Vulcan.NET VO-Compatible RDD Classes Library" then click OK. |

|  |  |
| --- | --- |
| 6. | Compile the application. |