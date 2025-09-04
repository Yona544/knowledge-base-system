Data Conversion Using Advantage Data Architect




Advantage Database Server 12  

Data Conversion Using Advantage Data Architect

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data Conversion Using Advantage Data Architect  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Data Conversion Using Advantage Data Architect Advantage TDataSet Descendant ade\_Data\_conversion\_using\_advantage\_data\_architect Advantage TDataSet Descendant > Converting Existing Delphi Applications > Data Conversion Using Advantage Data Architect / Dear Support Staff, |  |
| Data Conversion Using Advantage Data Architect  Advantage TDataSet Descendant |  |  |  |  |

The first step in any conversion is to move existing data to the Advantage data format. It is possible to write your own Delphi/C++Builder application for this purpose, but you will most likely find it easier to use the [Advantage Data Architect](ade_advantage_data_architect.htm).

|  |  |
| --- | --- |
| 1. | Create a new data directory to store your Advantage files. |

|  |  |
| --- | --- |
| 2. | Select Connection, Create New Connection from the main menu. |

|  |  |
| --- | --- |
| 3. | In the ConnectionPath property, enter the path you created in step 1. |

|  |  |
| --- | --- |
| 4. | In the DatabaseName property enter a name for this new connection. |

|  |  |
| --- | --- |
| 5. | Click the OK button. |

|  |  |
| --- | --- |
| 6. | From the Tools menu, choose Import Data. |

|  |  |
| --- | --- |
| 7. | Select the type of data you will be importing. |

|  |  |
| --- | --- |
| 8. | In the source file name edit box, enter the path to your data in the Import Filename text box, or click the browse button to search. |

|  |  |
| --- | --- |
| 9. | Select the desired Import Table Type |

|  |  |
| --- | --- |
| 10. | Enter the destination alias for the new connection you created above. This is where all of your new Advantage tables will be created. |

|  |  |
| --- | --- |
| 11. | Click the Finish button to begin the data conversion. |

Note You will encounter a Paradox Import Note when converting Paradox tables that have primary indexes defined. By default, the PRIMARY index is not the default index with an Advantage application. The PRIMARY index can be set as the default index in the Advantage Data Dictionary or otherwise, the PRIMARY indexes will need to be explicitly activated in your application. Click OK to continue.

|  |  |
| --- | --- |
| 13. | When the conversion is finished, click Close. |

 

Note See [Data Types](ade_data_types.htm) for more information if converting from Paradox tables.