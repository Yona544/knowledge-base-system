Enhance Your Advantage ADO Application




Advantage Database Server 12  

Enhance Your Advantage ADO Application

Advantage Tech Tips

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Enhance Your Advantage ADO Application  Advantage Tech Tips |  |  | Feedback on: Advantage Database Server 12 - Enhance Your Advantage ADO Application Advantage Tech Tips master\_Enhance\_Your\_Advantage\_ADO\_Application Tech Tips > ADO and OLE DB > Enhance Your Advantage ADO Application / Dear Support Staff, |  |
| Enhance Your Advantage ADO Application  Advantage Tech Tips |  |  |  |  |

With the release of Advantage 6.2, new properties were added to the Advantage OLE DB Provider allowing developers to obtain the internal Advantage Connection and Table handles. These handles can be used in various Advantage API calls to add functionality to your application. ADO provides excellent data access and manipulation capabilities but does not provide more advanced server functionality.

This tech tip discusses locking records. By explicitly locking a record, you can ensure that only one user can change a record at a time. When using server-side cursors, ADO typically uses an optimistic locking scheme where the record is only locked when changes are written to the record. Therefore you could have two users editing the same record at the same time without knowing it.

Getting Connection and Table Handles

The internal Advantage connection handle is stored in a custom ADO property when a connection to Advantage is established. This is a read-only property that can be read using the Properties.Item method of the ADO Connection Object.

Dim lhConnection as LongDim cnADS as ADODB.Connection' initialize the connection objectSet cnADS as New ADODB.Connection' open the connection to the server. Note this connection' can be used to open free ADT files on a remote server' located in the specified pathcnADS.Open Provider=Advantage OLE DB Provider;Data Source=\\server\data' get the connection handlelhConnection = cnADS.Properties.Item(ACE Connection Handle)

The internal Advantage table handle is stored in a custom ADO property when a table is opened. This is a read-only property of the ADO Recordset object and is obtained using the Properties.Item method.

Dim lhTable as LongDim rsADS as ADODB.Recordset' initialize the connection objectSet rsADS as New ADODB.Recordset' open the tablernADS.Open MyTable, cnADS, adOpenDynamic, adLockPessimistic, adCmdTable' get the connection handlelhTable = rnADS.Properties.Item(ACE Recordset Handle)

Record Locking

ADO uses an optimistic locking scheme when using server-side cursors. This means the record is locked only when it is being updated by the provider. A pessimistic locking scheme would mean the record is locked when editing begins and unlocked when updated or canceled. Optimistic locking works fine in most cases when most users will be working with different records. Pessimistic locking is beneficial when several users may try to edit the same records at the same time or exclusive use of information is required. For example, in a ticketing operation it is important that tickets be locked during the purchasing process otherwise the same ticket could be sold to two or more people.

ADO does not provide a native mechanism for placing records in an edit or locked mode. To provide this type of functionality, we will need to make an Advantage Client Engine (ACE) API call. First, you will need to obtain the table handle, and then use this handle when making the ACE API call. The ACE AdsLockRecord API requires two parameters. The first is the table handle. The second is the record number you wish to lock. Specifying 0 as the record number will lock the currently selected record. You may also use the AbsolutePosition property of the ADO Recordset to get the current record number. However, this may be unreliable when using an SQL statement with a WHERE clause. A third option is to use the ACE AdsGetRecordNum API to get the record number.

All Advantage API calls return an unsigned long value. If this value is not 0, an error occurred. You can obtain the Advantage error information by using the ACE AdsGetLastError API.

To use Advantage API calls from your application, you will need to include the appropriate header file or module containing the function definitions. These files are included with the Advantage Client Engine SDK, which is installed separately. Support for C/C++, Delphi, and Visual Basic is included in the ACE SDK.

Dim lReturn as long

Dim lErrRet as long

Dim iErrLen as integer

Dim sErrBuffer as string

 

'lock the current record. See the code above for opening

' the table

lReturn = AdsLockRecord( lhTable, 0 )

 

' check for error

Select Case lReturn

      Case 0 ' Success

      Case 5035 ' Already locked

          MsgBox Record locked by another user

      Case Else ' some other error so get more information

          ' init the error buffer

           iErrLen = AE\_MAX\_ERROR

           sErrBuffer = String( iErrLen, )

           lErrRet = AdsGetLastError( lReturn, sErrBuffer, iErrLen)

          if lErrRet = 0 then

              MsgBox sErrBuffer

          Else

              MsgBox Advantage Error & lReturn

          End If

      End If

End Select

To update the record, call the ADO Update method. Then you will need to unlock the record to allow others to edit the record. It is important to unlock the record AFTER calling Update to avoid the possibility of another user locking the record before the record is written. Use the AdsUnlockRecord API call to unlock the current record.

' Update the record

rs.Update

 

' Now explicitly unlock the record since it was explicitly

' locked earlier.

lReturn = AdsUnlockRecord( lhTable, 0 )

 

' check for error

if lReturn <> 0 then

  ' init the error buffer

   iErrLen = AE\_MAX\_ERROR

   sErrBuffer = String( iErrLen, )

   lErrRet = AdsGetLastError( lReturn, sErrBuffer, iErrLen)

  if lErrRet = 0 then

      MsgBox sErrBuffer

  Else

      MsgBox Advantage Error & lReturn

  End If

End If