How to Use the Advantage Client Engine




Advantage Database Server 12  

How to Use the Advantage Client Engine

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| How to Use the Advantage Client Engine  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - How to Use the Advantage Client Engine Advantage TDataSet Descendant ade\_How\_to\_use\_the\_advantage\_client\_engine Advantage TDataSet Descendant > Directly Accessing the Advantage Client Engine > How to Use the Advantage Client Engine / Dear Support Staff, |  |
| How to Use the Advantage Client Engine  Advantage TDataSet Descendant |  |  |  |  |

The Advantage Client Engine uses handles to identify every connection, table, and index. The Advantage TDataSet Descendant components wrap the handle values. Therefore, you do not need to access the handles unless you plan to call the Advantage Client Engine directly. To retrieve the handle for a specific object, use the Advantage extended methods [GetAceTableHandle](ade_getacetablehandle.htm), [GetAceIndexHandle](ade_getaceindexhandle.htm), [GetAceOrderHandle](ade_getaceorderhandle.htm), and [GetAceConnectionHandle](ade_getaceorderhandle.htm).These methods return connection, table, and/or index handles associated with an AdsDataSet instance. Once these handles are obtained, they can be used to call Advantage Client Engine APIs directly.

All available Advantage Client Engine APIs are documented in the Advantage Client Engine Help (ACE.HLP). (Note that each of the Advantage products and their corresponding Help files are installed separately.)

The prototype syntax in this Help file is in 'C'. To see the prototype syntax in Delphi/Pascal, find the function prototype in ACE.PAS, which is installed with the Advantage TDataSet Descendant.

To use Advantage Client Engine APIs directly in your code, add ACE.PAS to the "uses" clause. Then prefix the Advantage Client Engine API call with "ACE.". For example:

ulRetVal := ACE.AdsMgGetUserNames( hMgmtHandle, pchar( AdsTable1.TableName ), 0, @astUserInfo, @usArrayLen, @usSize );

The source code for the Advantage TDataSet Descendant extended methods is provided in the ADSFUNC.PAS file. This source code is an excellent example of how to use the Advantage Client Engine API.

Note It is possible to change the state of the Advantage Client Engine by calling the Advantage Client Engine APIs directly. The TAdsTable instances may make certain assumptions about the state of the Advantage Client Engine that can cause problems. The TDataSet method CheckBrowseMode is useful for synchronizing the state of the components and the underlying engine.