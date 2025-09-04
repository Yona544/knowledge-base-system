SetProcedureProperty




Advantage Database Server 12  

TAdsDictionary.SetProcedureProperty

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.SetProcedureProperty  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.SetProcedureProperty Advantage TDataSet Descendant ade\_Setprocedureproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.SetProcedureProperty  Advantage TDataSet Descendant |  |  |  |  |

Sets one property associated with a stored procedure definition in the data dictionary.

Syntax

procedure TAdsDictionary.SetProcedureProperty( strProcedureName : string;

usProperty : UNSIGNED16;

pvProperty : pointer;

usPropertyLen : UNSIGNED16);

Parameters

|  |  |
| --- | --- |
| strProcedureName (I) | Name of the stored procedure object to set the associated property. |
| usPropertyID (I) | Index of a procedure property to set. See Remarks for allowed values. |
| pvProperty (I) | Pointer to the buffer where the property is stored. |
| usPropertyLen (I) | The size of the property specified by the pvProperty. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the strProcedureName does not specify a valid stored procedure in the database. |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid procedure property ID, or the specified property cannot be set. |

Remarks

SetProcedureProperty sets one property associated with the specified stored procedure. The new property overwrites the existing property in the data dictionary. The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_COMMENT | Stores a new description for the stored procedure definition. The pvProperty parameter is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If pvProperty is NULL or an empty string, the description is removed. |
| ADS\_DD\_PROC\_INPUT | Changes the input parameter definition for the stored procedure. The format of this string is the same as the string passed into AdsCreateTable to define fields in a table. This definition will be used to create a table that will be populated with the input values. The pvProperty parameter is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If the stored procedure has no input, pass NULL for pvProperty. |
| ADS\_DD\_PROC\_OUTPUT | Changes the output parameter definition for the stored procedure. The format of this string is the same as the string passed into AdsCreateTable to define fields in a table. This definition will be used to create a table that will be populated with the output values. The pvProperty parameter is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If the stored procedure has no output, pass NULL for pvProperty. |
| ADS\_DD\_PROC\_DLL\_NAME | Changes the stored procedure container file name. This value must be a relative path from the Advantage Data Dictionary (.ADD) file. The pvProperty parameter is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. |
| ADS\_DD\_PROC\_DLL\_FUNCTION\_NAME | Changes the procedure name within the stored procedure container file name. This is the name of the function that is executed when the stored procedure is called. The pvProperty parameter is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. |

See Also

[AddProcedure](ade_addprocedure.htm)

[RemoveProcedure](ade_removeprocedure.htm)

[GetProcedureProperty](ade_getprocedureproperty.htm)