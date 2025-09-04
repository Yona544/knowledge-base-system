AdsDDDeployDatabase




Advantage Database Server 12  

AdsDDDeployDatabase

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDDeployDatabase  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDDeployDatabase Advantage Client Engine ace\_Adsdddeploydatabase Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDDeployDatabase  Advantage Client Engine |  |  |  |  |

Eases deployment of applications using Advantage Data Dictionaries. Specifically, a data dictionary can be defined and then deployed to an existing database consisting of a directory containing free tables and/or indexes. Those free tables and indexes will then be incorporated into the deployed data dictionary as defined within the data dictionary.

Note This API does not support deploying an Advantage Data Dictionary to another Advantage Data Dictionary. It is strictly a means to bring free tables into an Advantage Data Dictionary.

Syntax

UNSIGNED32 AdsDDDeployDatabase ( UNSIGNED8\* pucDestination,

UNSIGNED8\* pucDestinationPassword,

UNSIGNED8\* pucSource,

UNSIGNED8\* pucSourcePassword,

UNSIGNED16 usServerTypes,

UNSIGNED16 usValidateOption,

UNSIGNED16 usBackupFiles,

UNSIGNED32 ulOptions );

Parameters

|  |  |
| --- | --- |
| pucDestination(I) | The full path to the existing database consisting of the free tables to be added to the newly deployed database. |
| pucDestinationPassword(I) | This parameter is currently ignored. It is reserved for future use. |
| pucSource(I) | The full path to the source Advantage Data Dictionary file containing the updated data definitions to deploy. |
| pucSourcePassword(I) | The password to the source Advantage Data Dictionary. If the source data dictionary is not password protected use NULL. |
| ulServerType(I) | The server type to use for the deployment. Values can be ADS\_AIS\_SERVER, ADS\_REMOTE\_SERVER and/or ADS\_LOCAL\_SERVER. |
| ulValidateOptions(I) | If the Advantage Data Dictionary being deployed contains any field or record level constraints, the usValidateOption parameter specifies the type of validation to perform on existing records in the table. This parameter is ignored otherwise. Values can be:  ADS\_NO\_VALIDATE Does not perform any validation on existing records in the table. CAUTION: Using this option can logically corrupt tables and is strongly discouraged. If an index is available on the field in question, validating constraints is a quick operation and should always be performed.  ADS\_VALIDATE\_WRITE\_FAIL This option performs validation based on any constraints defined in the Advantage Data Dictionary. It will delete all records that do not pass constraints from the destination tables and write them to a fail table. The table will be placed in a child directory of the destination path with the name "fail". The table will be of the form: <tablename>\_fail.adt. |
| usBackupFiles(I) | True Will back up existing files before the deployment begins. All files will be placed in the backup directory off of the destination path.  False Will not backup the existing tables before deployment begins. |
| ulOptions(I) | This parameter is currently ignored. It is reserved for future use. |

Remarks

AdsDDDeployDatabase allows you to deploy a database by shipping only the Advantage Data Dictionary files. These files have the extensions, .add, .ai, and .am.

Note Due to current limitations, Linux clients calling this function will be forced to use a local server connection. If the remote server flag is passed in as the server type, it will be ignored. In addition, with Linux the backup of some tables may not succeed due to case sensitivity of file extensions. To avoid this ambiguity, include LOWERCASE\_ALL\_PATHS in the Advantage Local Server Configuration file.

 

Note The client must have sufficient rights to the source and destination directories in order to call this API. In addition, the current user must have administrative rights to all database objects in order to replicate them. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Scenario

A customer has been running an Advantage-enabled application that does not use Advantage Data Dictionary features. The developer upgrades the application to use the new data dictionary features. The developer wants to deploy the new application without the hassle of writing extensive code to add or manually add the customers existing tables, constraints, referential integrity rules, etc. to the new data dictionary. Using AdsDDDeployDatabase will do all of that work for them, so they only have to ship the three dictionary files and the short utility that calls the AdsDDDeployDatabase API.

Steps to a good deployment:

|  |  |
| --- | --- |
| 1. | Backup your existing data files! You have the option of doing this through the API, but it is also a good idea to do the backups yourself, in case there is a large amount of data and not enough drive space. |

|  |  |
| --- | --- |
| 2. | Verify your destination path is correct. The API uses the relative table path stored in the dictionary to find the existing tables. If it cannot find a table, it will assume it should create a new one. |

|  |  |
| --- | --- |
| 3. | Verify that your deployment has file access permissions. Make sure the application that calls this API has read/write access to all files and folders related to the deployment. |

|  |  |
| --- | --- |
| 4. | Verify all users are logged out. Make sure nobody has any one of the data files open. If the deployment utility cannot open the tables for exclusive use, the deployment will fail. |

Restrictions

You are not allowed to do the following during a deployment:

|  |  |
| --- | --- |
| · | Change field names on an existing table |

|  |  |
| --- | --- |
| · | Rename an existing table |

|  |  |
| --- | --- |
| · | Have any encrypted tables in the destination |

|  |  |
| --- | --- |
| · | Change index names. |

If a table in the source data dictionary is not found on the destination drive, it will be assumed that a new table needs to be created. An empty table will therefore be created where defined within the Advantage Data Dictionary.

What you can do

You can make the following changes during deployment:

|  |  |
| --- | --- |
| · | Add new tables to the database |

|  |  |
| --- | --- |
| · | Add new fields to a table |

|  |  |
| --- | --- |
| · | Remove existing fields |

|  |  |
| --- | --- |
| · | Add new indexes |

|  |  |
| --- | --- |
| · | Remove existing indexes |

|  |  |
| --- | --- |
| · | Register a callback function using AdsRegisterProgressCallback |

After the Deployment

|  |  |
| --- | --- |
| · | Your source Advantage Data Dictionary will have its files renamed to adsbackup.add, adsbackup.am, and adsbackup.ai |

|  |  |
| --- | --- |
| · | Your destination Advantage Data Dictionary will take on the original name of the source data dictionary |

|  |  |
| --- | --- |
| · | Backups will be located in a child directory of the destination path named "backup" |

|  |  |
| --- | --- |
| · | Fail tables will be located in a child directory of the destination path named "fail" |

|  |  |
| --- | --- |
| · | A deployment log file, adsdeploy.log, will be in the destination directory |

Example

For this example, the source data dictionary exists in our destination path. A callback function is registered to give updates on the deployment progress. Any invalidated records will be put into fail tables.

/\*

\* Deployment supports callback functionality for progress information.

\* This is our callback function

\*/

WINAPI ShowPercentage( UNSIGNED16 usPercentDone , UNSIGNED32 ulCallbackID)

{

printf( "\nPercent Done: %d\n", usPercentDone );

return 0;

}

 

 

int main( int argc, char \*argv[] )

{

UNSIGNED32 ulRetVal;

 

/\* Register the callback function for progress information \*/

ulRetVal = AdsRegisterCallbackFunction( ShowPercentage, 0 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

 

/\*

\* This deploys the Advantage Data Dictionary, newdb.add, to

\* the destination directory ..\DD\_source.

\* has finished, there will be the following files in the

\* destination directory:

\* newdb.add (this is the newly deployed data dictionary)

\* newdb.am

\* newdb.ai

\* adsbackup.add (this was the source data dictionary)

\* adsbackup.am

\* adsbackup.ai

\* backup (directory with copies of original tables)

\* fail (directory containing tables with records that

\* failed any constraints)

\* adsdeploy.log (log file of the deployment)

\*/

ulRetVal = AdsDDDeployDatabase( "..\\DD\_Dest",

NULL,

"..\\DD\_source\\newdb.add",

NULL,

ADS\_REMOTE\_SERVER,

ADS\_VALIDATE\_WRITE\_FAIL,

TRUE,

ADS\_DEFAULT );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsClearCallbackFunction();

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

return AE\_SUCCESS;

}

See Also

[AdsRegisterProgressCallback](ace_adsregisterprogresscallback.htm)

[AdsClearCallbackFunction](ace_adsclearcallbackfunction.htm)