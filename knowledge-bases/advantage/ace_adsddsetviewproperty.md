AdsDDSetViewProperty




Advantage Database Server 12  

AdsDDSetViewProperty

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDSetViewProperty  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDSetViewProperty Advantage Client Engine ace\_Adsddsetviewproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDSetViewProperty  Advantage Client Engine |  |  |  |  |

Sets one property associated with a view in the data dictionary.

Syntax

UNSIGNED32 AdsDDSetViewProperty( ADSHANDLE hDBConn,

UNSIGNED8 \*pucViewName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 usPropertyLen );

Parameters

|  |  |
| --- | --- |
| hDBConn (I) | Handle of a database connection. |
| pucViewName (I) | Name of the view object to set the associated property. |
| usPropertyID (I) | Index of a view property to set. See Remarks for allowed values. |
| pvProperty (I) | Pointer to the buffer where the property is stored. |
| usPropertyLen (I) | The size of the property specified by the pvProperty. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the pucViewName does not specify a valid view in the database. |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid view property ID, or the specified property cannot be set. |

Remarks

AdsDDSetViewProperty sets one property associated with the specified view. The new property overwrites the existing property in the data dictionary. The primary benefit to using this API over deleting and re-creating the view is that it maintains existing permissions on the view object. The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

ALTER permissions on the view are required to modify data dictionary view properties. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_COMMENT | Stores a new description for the view. The pvProperty parameter is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If pvProperty is NULL or empty string, the view description is removed. |
| ADS\_DD\_VIEW\_STMT | Changes the SQL SELECT statement associated with the view. |
| ADS\_DD\_VIEW\_STMT\_W | Changes the SQL SELECT statement associated with the view.  Encoded as UTF-16 string. |

Example

After making a connection to the database, set a new statement for "view1".

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

ulReturnCode = AdsDDSetViewProperty( hDD, "View1", ADS\_DD\_VIEW\_STMT, "select \* from test", 19 );

See Also

[AdsDDAddView](ace_adsddaddview.htm)

[AdsDDRemoveView](ace_adsddremoveview.htm)

[AdsDDGetViewProperty](ace_adsddgetviewproperty.htm)

[sp\_ModifyViewProperty](master_sp_modifyviewproperty.htm)