Return Codes




Advantage Database Server 12  

Return Codes

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Return Codes  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Return Codes Advantage OLE DB Provider (for ADO) oledb\_Return\_codes Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Errors > Return Codes / Dear Support Staff, |  |
| Return Codes  Advantage OLE DB Provider (for ADO) |  |  |  |  |

At the most basic level, a member function either succeeds or fails. At a somewhat more precise level, a function can succeed but its success might not be identical to that intended by the application developer.

When an Advantage OLE DB Provider member function returns S\_OK, the function succeeded.

When an Advantage OLE DB Provider member function does not return S\_OK, the COM HRESULT-unpacking FAILED and IS\_ERROR macros can determine the overall success or failure of a function.

If FAILED or IS\_ERROR returns TRUE, the Advantage OLE DB Provider consumer is assured that member function execution failed. When FAILED or IS\_ERROR return FALSE and the HRESULT does not equal S\_OK, the Advantage OLE DB Provider consumer is assured that the function succeeded in some sense. The consumer can retrieve detailed information on this success-with-information return from the Advantage OLE DB Provider error interfaces. Also, in the case where a function clearly fails (the FAILED macro returns TRUE), extended error information is available from the Advantage OLE DB Provider error interfaces.

The Advantage OLE DB Provider consumers commonly encounter the DB\_S\_ERRORSOCCURRED success-with-information HRESULT return. Typically, member functions that return DB\_S\_ERRORSOCCURRED define one or more parameters that deliver status values to the consumer. No error information may be available to the consumer other than that returned in status-value parameters, so consumers should implement application logic that retrieves status values when they are available.

The Advantage OLE DB Provider member functions do not return the success code S\_FALSE. Any Advantage OLE DB Provider member function always returns S\_OK to indicate success.