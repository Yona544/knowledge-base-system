Converting Existing BDE Reports in Crystal 6 through 8




Advantage Database Server 12  

Converting Existing BDE Reports in Crystal 6 through 8

Crystal Reports

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Converting Existing BDE Reports in Crystal 6 through 8  Crystal Reports |  |  | Feedback on: Advantage Database Server 12 - Converting Existing BDE Reports in Crystal 6 through 8 Crystal Reports crystal\_Converting\_existing\_bde\_reports\_in\_crystal\_6\_through\_8 Advantage Crystal Reports > Using the Advantage Crystal Reports Driver > Converting Existing Reports > Converting Existing BDE Reports in Crystal 6 through 8 / Dear Support Staff, |  |
| Converting Existing BDE Reports in Crystal 6 through 8  Crystal Reports |  |  |  |  |

Note: Crystal Reports versions 6 through 8 are no longer supported. The following help topic has been left in place as a courtesy for those that are still working with these unsupported versions.

To convert an existing BDE report that is currently using pdbbde.dll follow these steps:

|  |  |
| --- | --- |
| 1. | Disable "smart" linking. |

|  |  |
| --- | --- |
| a. | Choose 'File' from the main menu |

|  |  |
| --- | --- |
| b. | Choose 'Options' |

|  |  |
| --- | --- |
| c. | Select the 'Database' tab |

|  |  |
| --- | --- |
| d. | Uncheck the 'Auto-SmartLinking' option |

|  |  |
| --- | --- |
| 1. | Open the report |

|  |  |
| --- | --- |
| 2. | Choose 'Database' from the main menu |

|  |  |
| --- | --- |
| 3. | Choose 'Convert Database Driver...' from the Database menu |

|  |  |
| --- | --- |
| 4. | Check the 'Convert Database Driver on next Refresh' checkbox |

|  |  |
| --- | --- |
| 5. | Find and select pdsads.dll in the drop-down list |

|  |  |
| --- | --- |
| 6. | Click OK |

|  |  |
| --- | --- |
| 7. | If the Advantage Alias dialog does not appear immediately press the F5 key to force a refresh. |

|  |  |
| --- | --- |
| 8. | You will be prompted for an Advantage alias to use in this report. Either select an existing alias from the list provided, or click New to create a new alias. |

|  |  |
| --- | --- |
| 9. | Check the 'Converting Report From BDE Driver' checkbox |

|  |  |
| --- | --- |
| 10. | Click OK |

|  |  |
| --- | --- |
| 11. | An informational dialog will be shown reminding you to change each link in your report to the 'outer join' type. See the note below for an explanation. |

|  |  |
| --- | --- |
| 12. | Crystal will report that the base tables have changed and ask you if you want to fix up the report. Click Yes for each table. |

Note All links in the report must be converted to the 'outer join' link type in order to emulate the BDE flat file driver linking behavior. The BDE flat file driver (pdbbde.dll) includes all rows in a parent table in the result set, even if a matching key value does not exist in the child table(s). This is equivalent to an SQL left outer join. By default the Advantage Crystal Driver uses standard SQL joins (inner joins) and will not return rows unless they have matching keys in the child table(s). For this reason, all links in a report previously built using the pdbbde driver must be converted to left outer join links in order to return the same results the original report returned.

To change each link type:

|  |  |
| --- | --- |
| 1. | Choose 'Database' from the main menu. |

|  |  |
| --- | --- |
| 2. | Choose 'Visual Linking Expert...' from the Database menu. |

|  |  |
| --- | --- |
| 3. | For each link in the report do the following: |

|  |  |
| --- | --- |
| a. | Select the link by clicking on the link line. |

|  |  |
| --- | --- |
| b. | Click the 'Options...' button. |

|  |  |
| --- | --- |
| c. | Change the 'SQL Join Type' from 'Equal' to 'Left Outer'. |

|  |  |
| --- | --- |
| 13. | Close the Visual Linking Expert |

Note Crystal Reports will leave the .db file extension on tables referenced in the report, even after a database conversion has been completed. The Advantage driver uses the table basename in all instances, so this extension will not affect the report generation or functionality.