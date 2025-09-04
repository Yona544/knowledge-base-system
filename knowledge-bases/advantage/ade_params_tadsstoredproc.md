Params




Advantage Database Server 12  

TAdsStoredProc.Params

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsStoredProc.Params  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsStoredProc.Params Advantage TDataSet Descendant ade\_Params\_tadsstoredproc Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsStoredProc.Params  Advantage TDataSet Descendant |  |  |  |  |

[TAdsStoredProc](ade_tadsstoredproc.htm)

Stores the input and output parameters for a stored procedure.

Syntax

property Params: TParams;

Description

Access Params at runtime to set input parameter names, values, and data types dynamically (at design time use the Parameters editor to set parameter information). Params is an array of parameter values.

An application can also access Params after executing a stored procedure to retrieve the output parameters returned to the procedure by the server.

Output parameters are supported and will be populated and returned via a call to TAdsStoredProc.ExecProc. To open a result cursor from a stored procedure, or to access the output parameters as a single-row result set use the TAdsStoredProc.Open method.

If the Params object contains a parameter of type ptResult this parameter will be populated with the return value from the procedure execution, and no exceptions will be raised if the procedure execution returns an error. If a ptResult parameter is defined it is the callers responsibility to check the return code.

See Also

[RefreshParams](ade_refreshparams.htm)