Errors Overview




Advantage Database Server 12  

Errors Overview

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Errors Overview  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Errors Overview Advantage OLE DB Provider (for ADO) oledb\_Errors\_overview Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Errors > Errors Overview / Dear Support Staff, |  |
| Errors Overview  Advantage OLE DB Provider (for ADO) |  |  |  |  |

COM objects report errors through the HRESULT return code of object member functions. A COM HRESULT is a bit-packed structure. COM provides macros that dereference structure members.

COM specifies the IErrorInfo interface. The interface exposes methods such as GetDescription, allowing clients to extract error detail from COM servers. OLE DB extends IErrorInfo to support the return of multiple error information packets on a single-member function execution.

The Advantage OLE DB Provider exposes the OLE DB recordenhanced IErrorInfo error object interface.