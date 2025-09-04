AdsDDGetRefIntegrityProperty




Advantage Database Server 12  

AdsDDGetRefIntegrityProperty

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDGetRefIntegrityProperty  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDGetRefIntegrityProperty Advantage Client Engine ace\_Adsddgetrefintegrityproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDGetRefIntegrityProperty  Advantage Client Engine |  |  |  |  |

Gets a specified property from the data dictionary for a referential integrity (RI) constraint.

Syntax

|  |  |
| --- | --- |
| UNSIGNED 32 | AdsDDGetRefIntegrityProperty(ADSHANDLE hDBConn,  UNSIGNED8 \*pucRIName,  UNSIGNED16 usPropertyID,  UNSIGNED8 \*pucProperty,  UNSIGNED16 \*pusPropertyLen ); |

 

Parameters

|  |  |
| --- | --- |
| hDBConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pucRefName (I) | The name of the RI constraint in the data dictionary. |
| usPropertyID (I) | The property to retrieve. (See below for possible values.) |
| pucProperty (O) | A buffer to hold the property value. |
| pusPropertyLen (I/O) | Length of given buffer on input, length of returned data on output. |

Description

AdsDDGetRefIntegrityProperty will retrieve the specified RI property for a table from the data dictionary.

The following are the valid values for usPropertyID:

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_RI\_PRIMARY\_TABLE | The name of the parent table of the RI constraint that contains the primary key index. This property is returned as a NULL terminated string. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_RI\_PRIMARY\_INDEX | The name of the primary key index of the RI constraint. This property is returned as a NULL terminated string. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_RI\_FOREIGN\_TABLE | The name of the child table of the RI constraint that contains the foreign key index. ADS\_DD\_RI\_FOREIGN\_TABLE is returned as a NULL terminated string. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_RI\_FOREIGN\_INDEX | The name of the foreign key index of the RI constraint. ADS\_DD\_RI\_FOREIGN\_INDEX is returned as a NULL terminated string. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_RI\_NO\_PKEY\_ERROR | The custom error message used for primary key violation errors. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_RI\_CASCADE\_ERROR | The custom error message used for cascade errors. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_RI\_UPDATERULE | The update rule for the RI constraint. ADS\_DD\_RI\_UPDATERULE is returned as a 1-byte (UNSIGNED8) number with the following possible values: ADS\_DD\_RI\_CASCADE, ADS\_DD\_RI\_RESTRICT, ADS\_DD\_RI\_SETNULL, ADS\_DD\_RI\_SETDEFAULT. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_RI\_DELETERULE | The delete rule for the RI constraint. ADS\_DD\_RI\_DELETERULE is returned as a 1-byte (UNSIGNED8) number with the following possible values: ADS\_DD\_RI\_CASCADE, ADS\_DD\_RI\_RESTRICT, ADS\_DD\_RI\_SETNULL, ADS\_DD\_RI\_SETDEFAULT. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid table property or the specified property cannot be retrieved. |
| AE\_INSUFFICIENT\_BUFFER | The size of the property to be copied into pvProperty is larger than the buffer size specified by usPropertyLen. The required buffer length is returned in usPropertyLen when this error occurs. |
| AE\_PROPERTY\_NOT\_SET | The requested property is not set in the data dictionary. No data is returned in pvProperty and usPropertylen. |

Example

void DumpRIObjectInfo( ADSHANDLE hDD, UNSIGNED8 \*pucRIName )

{

UNSIGNED8 aucBig[65000];

UNSIGNED16 usBufferSize;

SIGNED32 lGraphID;

FILE \*hFile;

 

hFile = fopen( "c:\\temp\\output.txt", "a+" );

 

fprintf( hFile, "\n" );

fprintf( hFile, "RI OBJECT NAME: %s\n", pucRIName );

 

usBufferSize = sizeof( aucBig );;

if ( AE\_SUCCESS == AdsDDGetRefIntegrityProperty( hDD, pucRIName, ADS\_DD\_RI\_PRIMARY\_TABLE, aucBig, &usBufferSize ))

{

fprintf( hFile, "Primary Table: %s\n", aucBig );

}

else

fprintf( hFile, "No primary table?!?\n" );

 

usBufferSize = sizeof( aucBig );;

if ( AE\_SUCCESS == AdsDDGetRefIntegrityProperty( hDD, pucRIName, ADS\_DD\_RI\_PRIMARY\_INDEX, aucBig, &usBufferSize ))

{

fprintf( hFile, " Primary Index: %s\n", aucBig );

}

else

fprintf( hFile, " No primary index?!?\n" );

 

usBufferSize = sizeof( aucBig );;

if ( AE\_SUCCESS == AdsDDGetRefIntegrityProperty( hDD, pucRIName, ADS\_DD\_RI\_FOREIGN\_TABLE, aucBig, &usBufferSize ))

{

fprintf( hFile, "Foreign Table: %s\n", aucBig );

}

else

fprintf( hFile, "No foreign table?!?\n" );

 

usBufferSize = sizeof( aucBig );;

if ( AE\_SUCCESS == AdsDDGetRefIntegrityProperty( hDD, pucRIName, ADS\_DD\_RI\_FOREIGN\_INDEX, aucBig, &usBufferSize ))

{

fprintf( hFile, " Foreign Index: %s\n", aucBig );

}

else

fprintf( hFile, " No foreign index?!?\n" );

 

usBufferSize = sizeof( UNSIGNED8 );;

if ( AE\_SUCCESS == AdsDDGetRefIntegrityProperty( hDD, pucRIName, ADS\_DD\_RI\_UPDATERULE, aucBig, &usBufferSize ))

{

fprintf( hFile, "Update Rule: " );

switch( aucBig[0] )

{

case ADS\_DD\_RI\_CASCADE : fprintf( hFile, "cascade\n" ); break;

case ADS\_DD\_RI\_RESTRICT : fprintf( hFile, "restrict\n" ); break;

case ADS\_DD\_RI\_SETNULL : fprintf( hFile, "set null\n" ); break;

case ADS\_DD\_RI\_SETDEFAULT : fprintf( hFile, "set default\n" ); break;

default: fprintf( hFile, "ERROR, UNKNOWN UPDATE RULE!\n" );

}

}

else

fprintf( hFile, "ERROR GETTING UPDATE RULE!\n" );

 

usBufferSize = sizeof( UNSIGNED8 );;

if ( AE\_SUCCESS == AdsDDGetRefIntegrityProperty( hDD, pucRIName, ADS\_DD\_RI\_DELETERULE, aucBig, &usBufferSize ))

{

fprintf( hFile, "Delete Rule: " );

switch( aucBig[0] )

{

case ADS\_DD\_RI\_CASCADE : fprintf( hFile, "cascade\n" ); break;

case ADS\_DD\_RI\_RESTRICT : fprintf( hFile, "restrict\n" ); break;

case ADS\_DD\_RI\_SETNULL : fprintf( hFile, "set null\n" ); break;

case ADS\_DD\_RI\_SETDEFAULT : fprintf( hFile, "set default\n" ); break;

default: fprintf( hFile, "ERROR, UNKNOWN DELETE RULE!\n" );

}

}

else

fprintf( hFile, "ERROR GETTING DELETE RULE!\n" );

fclose( hFile );

 

}

See Also

[AdsDDCreateRefIntegrity62](ace_adsddcreaterefintegrity62.htm)

[AdsDDRemoveRefIntegrity](ace_adsddremoverefintegrity.htm)

[system.relations](master_system_relations.htm)