Error Object Interfaces Supported




Advantage Database Server 12  

Error Object Interfaces Supported

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Error Object Interfaces Supported  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Error Object Interfaces Supported Advantage OLE DB Provider (for ADO) oledb\_Error\_object\_interfaces\_supported Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Errors > Error Object Interfaces Supported / Dear Support Staff, |  |
| Error Object Interfaces Supported  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The ErrorObject, ErrorRecord, and CustomErrorObject objects are supported with the Advantage OLE DB Provider. Below is the list of supported interfaces in each of the ErrorObject, ErrorRecord, and CustomErrorObject objects. Generally, for each interface listed, all the methods will be supported.

ErrorObject Object

|  |
| --- |
| IErrorRecords |

ErrorRecord Object

|  |
| --- |
| IErrorInfo |

CustomErrorObject Object

|  |
| --- |
| IErrorLookup |

Implementation Details by Method

The Advantage OLE DB Provider supports consumer-available IErrorRecords interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| AddErrorRecord | Adds a record to an OLE DB error object. |
| GetBasicErrorInfo | Fills an ERRORINFO structure with basic information about an error. An ERRORINFO structure contains members that identify the HRESULT return value for the error, and the provider and interface on which the error applies. |
| GetCustomErrorObject | Not supported. |
| GetErrorInfo | Returns a reference on an IErrorInfo interface. |
| GetErrorParameters | The Advantage OLE DB Provider does not return parameters to the consumer through GetErrorParameters. |
| GetRecordCount | Count of error records available. |

The Advantage OLE DB Provider supports IErrorInfo interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetDescription | Descriptive error message string. |
| GetGUID | GUID of the interface that defined the error. |
| GetHelpContext | Returns the help context identifier if the error was Advantage specific and 0 otherwise. |
| GetHelpFile | Returns the Advantage Error Guide help file name if the error was Advantage specific and NULL otherwise. |
| GetSource | String ADSOLEDB.DLL. |

The Advantage OLE DB Provider supports IErrorLookup interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetErrorDescription | Returns the error message and source, based on the return code and the provider-specific error number. |
| GetHelpInfo | Returns the path of the Help file and the context ID of the topic that explains the error. For Advantage errors, the help file will be ADSERROR.HLP. |
| ReleaseErrors | Releases any dynamic error information associated with a dynamic error ID. |