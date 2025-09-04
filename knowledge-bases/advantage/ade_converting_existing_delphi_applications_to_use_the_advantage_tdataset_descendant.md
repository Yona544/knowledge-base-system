Converting Existing Delphi Applications to use the Advantage TDataSet Descendant




Advantage Database Server 12  

Converting Existing Delphi/C++Builder Applications to Use the Advantage TDataSet Descendant

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Converting Existing Delphi/C++Builder Applications to Use the Advantage TDataSet Descendant  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Converting Existing Delphi/C++Builder Applications to Use the Advantage TDataSet Descendant Advantage TDataSet Descendant ade\_Converting\_existing\_delphi\_applications\_to\_use\_the\_advantage\_tdataset\_descendant Advantage TDataSet Descendant > Converting Existing Delphi Applications > Converting Existing Delphi Applications to use the Advantage TDataSet Descendant / Dear Support Staff, |  |
| Converting Existing Delphi/C++Builder Applications to Use the Advantage TDataSet Descendant  Advantage TDataSet Descendant |  |  |  |  |

This section describes the steps necessary to convert an existing Delphi application to use the Advantage TDataSet Descendant. The information shows how to convert TTable instances to TAdsTable instances without having to reconfigure persistent fields, datasource links, or table properties.

 

Converting TTable instances to TAdsTable instances

This section includes generic instruction for converting an application to use the Advantage TDataSet Descendant. Specific instructions using the Delphi demo applications will be provided in a later section. The easiest way to convert TTable instances to TAdsTable instances and preserve your current table configuration is to view your data form as text and then make only the necessary changes.

Note TQuery and TStoredProc instances can be converted to TAdsQuery and TAdsStoredProc instances using this same kind of process.

|  |  |
| --- | --- |
| 1. | Right-Click on your form and choose View as Text from the quick menu. You will now see the text representation of your form and all of the objects on the form. |

|  |  |
| --- | --- |
| 2. | Search for TTable |

|  |  |
| --- | --- |
| 3. | For each TTable object you find do the following: |

|  |  |
| --- | --- |
| 4. | Change TTable to TAdsTable. For example the line "object tblMaster: TTable" would be changed to "object tblMaster: TAdsTable" |

|  |  |
| --- | --- |
| 5. | Below the object declaration you will find the DatabaseName property. If this property does not already include the path to your data then replace it with the path. (e.g., X:\ADS\DATA) or the alias name defined in the ads.ini file |

|  |  |
| --- | --- |
| 6. | Below the DatabaseName property you will find the TableName property. Under most circumstances your table name will change after converting to the Advantage table format (e.g., MYTABLE.DB will change to MYTABLE.ADT). If this is the case then change the TableName property to reflect this new extension. |

|  |  |
| --- | --- |
| 7. | Once you are finished changing all of your table declarations right-click in the edit window and select View as Form from the quick menu. You should now see TAdsTable objects in place of your original TTable objects. |

|  |  |
| --- | --- |
| 8. | Select Save from the File menu. |

|  |  |
| --- | --- |
| 9. | After making these changes, the next time you build the project Delphi will warn you that some declarations have changed and offer to correct them for you. Select yes and let Delphi correct the rest of the declarations. |

Converting the Delphi demo projects to use the Advantage TDataSet Descendant

Now lets try the generic method from the previous section with a few existing applications from the Delphi demo directory.

Note If you cannot find the demo directory, reference your Delphi installation documentation for details on how to re-install with this option.

 

CtrlGrid Demo

|  |  |
| --- | --- |
| 1. | Select Open Project from the File menu |

|  |  |
| --- | --- |
| 2. | Browse to your Delphi database demo directory, the default directory is C:\PROGRAM FILES\<Company Name>\<Delphi Product>\DEMOS\DB |

|  |  |
| --- | --- |
| 3. | Browse into the CtrlGrid directory and open CtrlGrid.dpr |

|  |  |
| --- | --- |
| 4. | Press [F9] to build and run the application. Use this time to get familiar with the application and verify that it is working correctly with the BDE. |

|  |  |
| --- | --- |
| 5. | Select Forms from the View menu and select DM1, the data module for this application. |

|  |  |
| --- | --- |
| 6. | Right-click on the data module (DM1) and select View as Text. In this text file you will find the declarations for three tables; tblMaster, tblIndustry, and tblHoldings. |

|  |  |
| --- | --- |
| 7. | In the tblMaster declaration change the object type from TTable to TAdsTable. On the next line you will find the databasename property, change it to contain the path to your data (e.g., X:\ADS\DATA). Finally you will see the tablename property, which will need to be changed from MASTER.DBF to MASTER.ADT. |

|  |  |
| --- | --- |
| 8. | Scroll down until you find the tblIndustry declaration. Change the object type from TTable to TAdsTable. Change the databasename property to your data path (e.g., X:\ADS\DATA), and the tablename from industry.dbf to industry.adt. |

|  |  |
| --- | --- |
| 9. | Scroll down until you find the tblHoldings declaration. As before change the object type from TTable to TAdsTable, the databasename to your data path (e.g., X:\ADS\DATA), and the tablename from holdings.dbf to holdings.adt. |

|  |  |
| --- | --- |
| 10. | Right-click in the editor window and select View as Form from the menu. Note the TTable objects will now appear as TAdsTable objects. |

|  |  |
| --- | --- |
| 11. | Highlight each of the three tables and change their active properties in the Delphi Object Inspector to True. |

|  |  |
| --- | --- |
| 12. | Select Options from the Project menu. |

|  |  |
| --- | --- |
| 13. | Select the Directories/Conditionals tab. |

|  |  |
| --- | --- |
| 14. | In the Search Path field enter the path to your Advantage TDataSet Descendant files so that Delphi can find the necessary source files when building your project. The default is C:\Program Files\Advantage X.x\TDataSet\Delphi? |

|  |  |
| --- | --- |
| 15. | Select Save All from the File menu to save these new changes. |

|  |  |
| --- | --- |
| 16. | After making these changes the next time you build the project Delphi will warn you that some declarations have changed and offer to correct them for you. Select yes and let Delphi correct the rest of the declarations. |

|  |  |
| --- | --- |
| 17. | Press [F9] to build and run the application. Ctrlgrid is now using the Advantage TDataSet Descendant for all database access. |

 

FishFact

|  |  |
| --- | --- |
| 1. | Select Open Project from the File menu |

|  |  |
| --- | --- |
| 2. | Browse to your Delphi database demo directory, the default directory is C:\PROGRAM FILES\BORLAND\DELPHI?\DEMOS\DB |

|  |  |
| --- | --- |
| 3. | Browse into the FishFact directory and open FISHFACT.DPR |

|  |  |
| --- | --- |
| 4. | Press [F9] to build and run the application. Use this time to familiarize yourself with the application and verify that it is working correctly with the BDE. |

|  |  |
| --- | --- |
| 5. | Select Forms from the View and select Form1 |

|  |  |
| --- | --- |
| 6. | Right-click on the form and select View as Text from the quick menu. |

|  |  |
| --- | --- |
| 7. | Select Find from the Search menu and search for TTable. |

|  |  |
| --- | --- |
| 8. | Change Table1s object type from TTable to TAdsTable. |

|  |  |
| --- | --- |
| 9. | Change the databasename property from DBDEMOS to your data path (e.g., X:\ADS\DATA). |

|  |  |
| --- | --- |
| 10. | Right-click in the editor window and select View as Form from the menu. Note the TTable objects will now appear as TAdsTable objects. |

|  |  |
| --- | --- |
| 11. | Select Options from the Project menu. |

|  |  |
| --- | --- |
| 12. | Select the Directories/Conditionals tab. |

|  |  |
| --- | --- |
| 13. | In the Search Path field enter the path to your Advantage TDataSet Descendant files so that Delphi can find the necessary source files when building your project. The default is C:\Program Files\Advantage X.x\TDataSet\Delphi? |

|  |  |
| --- | --- |
| 14. | Select Save All from the File menu to save these new changes. |

|  |  |
| --- | --- |
| 15. | After making these changes the next time you build the project Delphi will warn you that some declarations have changed and offer to correct them for you. Select yes and let Delphi correct the rest of the declarations. |

|  |  |
| --- | --- |
| 16. | Press [F9] to build and run the application. FishFact is now using the Advantage TDataSet Descendant for all database access. |

 

GDSDemo

|  |  |
| --- | --- |
| 1. | Select Open Project from the File menu |

|  |  |
| --- | --- |
| 2. | Browse to your Delphi database demo directory, the default directory is C:\PROGRAM FILES\BORLAND\DELPHI?\DEMOS\DB |

|  |  |
| --- | --- |
| 3. | Browse into the GDSDemo directory and open GDSDEMO.DPR |

|  |  |
| --- | --- |
| 4. | Press [F9] to build and run the application. Use this time to familiarize yourself with the application and verify that it is working correctly with the BDE. |

|  |  |
| --- | --- |
| 5. | Select Forms from the View and select StdDataForm |

|  |  |
| --- | --- |
| 6. | Right-click on the form and select View as Text from the quick menu. |

|  |  |
| --- | --- |
| 7. | Select Find from the Search menu and search for TTable. |

|  |  |
| --- | --- |
| 8. | Change the Orders table object type from TTable to TAdsTable. |

|  |  |
| --- | --- |
| 9. | Change the databasename property from DBDEMOS to your data path (e.g., X:\ADS\DATA). |

|  |  |
| --- | --- |
| 10. | Right-click in the editor window and select View as Form from the menu. Note the TTable objects will now appear as TAdsTable objects. |

|  |  |
| --- | --- |
| 11. | Select Options from the Project menu. |

|  |  |
| --- | --- |
| 12. | Select the Directories/Conditionals tab. |

|  |  |
| --- | --- |
| 13. | In the Search Path field enter the path to your Advantage TDataSet Descendant files so that Delphi can find the necessary source files when building your project. The default is C:\Program Files\Advantage X.x\TDataSet\Delphi? |

|  |  |
| --- | --- |
| 14. | Select Save All from the File menu to save these new changes. |

|  |  |
| --- | --- |
| 15. | After making these changes the next time you build the project Delphi will warn you that some declarations have changed and offer to correct them for you. Select yes and let Delphi correct the rest of the declarations. |

|  |  |
| --- | --- |
| 16. | Press [F9] to build and run the application. GDSDemo is now using the Advantage TDataSet Descendant for all database access. |