Troubleshooting




Advantage Database Server 12  

Troubleshooting

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Troubleshooting |  |  | Feedback on: Advantage Database Server 12 - Troubleshooting odbc\_Troubleshooting Advantage ODBC Driver > Introduction > Troubleshooting / Dear Support Staff, |  |
| Troubleshooting |  |  |  |  |

If you receive the message "[Microsoft][ODBC DLL] Specified driver could not be loaded", when attempting to connect to a data source with the Advantage ODBC Driver, it may mean that one of the required DLLs could not be loaded. The Advantage ODBC Driver requires the following DLLs:

ADSODBC.DLL

ADSSET.DLL

ACE32.DLL or ACE64.DLL

AXCWS32.DLL or AXCWS64.DLL (only required for Advantage Database Server access)

ADSLOC32.DLL or ADSLOC64.DLL (only required for Advantage Local Server access)

Verify that the above DLLs are in your client's search path. The Advantage ODBC Driver setup utility, which is accessed from the ODBC administrator, has a button ("Check DLLs") that will display a list of the necessary DLLs and whether or not they were found.

If you are not able to edit tables attached to Microsoft Access via the Advantage ODBC Driver, it may be because the table does not have a unique index. This actually applies to any attached table - not just tables attached with Advantage. Microsoft Access requires a unique index so that it can update the correct record when the table is edited. You can create a unique index on a table with the SQL command "CREATE INDEX ndxname ON tblname (colname) CANDIDATE". You can also create a unique index within Access that will be stored in the Access database file (.mdb). Be aware, though, that the index will be updated by Access when editing the table, but will not be updated by other applications that use the data.