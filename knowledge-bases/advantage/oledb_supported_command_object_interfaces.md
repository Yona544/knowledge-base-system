Supported Command Object Interfaces




Advantage Database Server 12  

Supported Command Object Interfaces

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Supported Command Object Interfaces  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Supported Command Object Interfaces Advantage OLE DB Provider (for ADO) oledb\_Supported\_command\_object\_interfaces Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Commands > Supported Command Object Interfaces / Dear Support Staff, |  |
| Supported Command Object Interfaces  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Command object is supported with the Advantage OLE DB Provider. Below is the list of supported interfaces in the Command object. Generally, for each interface listed, all the methods will be supported.

Command Object

|  |  |  |  |
| --- | --- | --- | --- |
| IAccessor | IColumnsInfo | ICommand | ICommandProperties |
| ICommandText | IConvertType | ICommandPrepare | ICommandWithParameters |
| ISupportErrorInfo |  |  |  |

Implementation Details by Method

The Advantage OLE DB Provider supports IAccessor interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| AddRefAccessor | Adds a reference count to an existing accessor. |
| CreateAccessor | Creates an accessor from a set of bindings. Optimized and ByRef accessors are not supported by the Advantage OLE DB Provider. |
| GetBindings | Returns the bindings in an accessor. |
| ReleaseAccessor | Releases an accessor. |

The Advantage OLE DB Provider supports IColumnsInfo interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetColumnInfo | Returns the column metadata needed by most consumers. |
| MapColumnIDs | Returns an array of ordinals of the columns in a rowset that are identified by the specified column IDs. |

The Advantage OLE DB Provider supports ICommand interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| Cancel | Cancels the current command execution. With the Advantage OLE DB Provider, canceling a synchronous command is supported if it is canceled from another thread. Canceling an asynchronous command is not supported because asynchronous commands are not supported. |
| Execute | Executes the command. |
| GetDBSession | Returns an interface pointer to the session that created the command. |

The Advantage OLE DB Provider supports ICommandProperties interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetProperties | Returns the list of properties in the Rowset property group that are currently requested for the rowset. |
| SetProperties | Sets properties in the Rowset property group. |

The Advantage OLE DB Provider supports ICommandText interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetCommandText | Returns the text command set by the last call to SetCommandText. |
| SetCommandText | Sets the command text, replacing the existing command text. |

The Advantage OLE DB Provider supports IConvertType interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| CanConvert | Gives information about the availability of type conversions on a command or on a rowset. |

The Advantage OLE DB Provider supports ICommandPrepare interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| Prepare | Validates and optimizes the current command. |
| Unprepare | Discards the current command execution plan. |

The Advantage OLE DB Provider supports ICommandWithParameters interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| GetParameterInfo | Gets a list of the commands parameters, their names, and their types. |
| MapParameterNames | Returns an array of parameter ordinals when given named parameters. |
| SetParameterInfo | Specifies the native data type of each parameter. |

The Advantage OLE DB Provider supports ISupportErrorInfo interface member functions as described in the following table.

|  |  |
| --- | --- |
| Member Function | Description |
| InterfaceSupportsErrorInfo | Indicates whether a specific OLE DB interface can return OLE DB error objects. |