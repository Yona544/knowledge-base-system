Performing Index Operations with OLE DB




Advantage Database Server 12  

Performing Index Operations with OLE DB

Advantage Tech Tips

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Performing Index Operations with OLE DB  Advantage Tech Tips |  |  | Feedback on: Advantage Database Server 12 - Performing Index Operations with OLE DB Advantage Tech Tips master\_Performing\_Index\_Operations\_wit Tech Tips > ADO and OLE DB > Performing Index Operations with OLE DB / Dear Support Staff, |  |
| Performing Index Operations with OLE DB  Advantage Tech Tips |  |  |  |  |

ADO and OLE DB are part of Microsoft's universal data access strategy. These technologies make it very easy to retrieve, view and modify information in a table or database. However, most ADO implementations do not include native support for index operations. In-fact ADOX was developed for the Microsoft Jet Provider specifically to provide index management functionality.

Advantage provides a rich API for creating and maintaining indexes. Most of these API calls require Connection or Table handles that are available from the Advantage OLE DB provider. Index operations will be demonstrated using Visual Basic code.

First Steps

Many index operations (e.g., creation and reindex) require exclusive use of a table. To open a table exclusively with ADO, you must set the Mode property of your connection component to adModeShareExclusive (see the code example below).

When using the Advantage OLE DB provider you must also open the table using the adCmdTableDirect option in order to open a table for exclusive use

We will also be using the Advantage Client Engine (ACE) API calls, so we will need the ACE Connection and ACE Recordset handles. You will also need to add ACE.BAS to your project.

Dim lhConnection as Long  
Dim cnExclusive as ADODB.Connection  
   
' initialize the connection object  
Set cnExclusive as New ADODB.Connection  
   
' open the connection to the server  
cnExclusive.Mode = adModeShareExclusive  
cnExclusive.Provider = Advantage.OLEDB.1  
cnExclusive.Open Data Source=\\server1\share1\data  
   
' get the connection handlel  
hConnection = cnExclusive.Properties.Item( ACE Connection Handle )   
   
Dim lhTable as Long  
Dim rsADS as ADODB.Recordset  
   
' initialize the recordset object  
Set rsADS as New ADODB.Recordset  
   
' open the table  
rsADS.Open MyTable, cnExclusive, adOpenDynamic, adLockPessimistic, adCmdTableDirect  
   
' get the recordset handlel  
hTable = rsADS.Properties.Item( ACE Recordset Handle )

Reindexing

Now that the table is opened exclusively, you can reindex the table. AdsReindex rebuilds all the indexes associated with the open table. You can also use AdsReindex61 to rebuild the indexes and change the index page size (.ADI indexes only). The default page size is 512 bytes with a maximum value of 8192 bytes. If you want to create an ADI index with the maximum page size, we recommend that you use the ADS\_MAX\_ADI\_PAGESIZE constant defined in ACE.BAS.

' Return value of ACE API

Dim lReturn As Long   
   
' Reindex the table  
lReturn = AdsReindex( lhTable )  
   
' or you can use AdsReindex61   
lReturn = AdsReindex61( lhTable, 2048 )   
   
If lReturn = 0 Then   
   MsgBox Reindex complete  
Else   
   ' error you can display a custom message here   
End If

Advantage has the ability to perform a progress callback during index operations. There are examples of this functionality available on the Advantage Developer Zone (DevZone.AdvantageDatabase.com). Choose the Examples link from the Downloads menu.

Common Index Operations

In day-to-day operations, you may have a need to list the available indexes on a table so the user can sort the data. ADO allows for setting of the active index using the Recordset's Index property. However, you cannot get the list of available indexes through ADO.

To get a list of available indexes, you will need to use two ACE API functions. First, use AdsGetAllIndexes to get handles for all the available indexes. Next, use the AdsGetIndexName API to get the names for all the returned handles. You do not need to have the table opened exclusively to make these API calls.

Dim lReturn As Long   
' Return value of ACE API  
   
Dim ahIndex( ADS\_MAX\_TAGS ) As Long   
' Array for index handles  
   
Dim asTagNames( ADS\_MAX\_TAGS ) as String   
' Array for index names  
   
Dim iNumTags As Integer   
' Tag count  
   
Dim iTagLen As Integer   
' Length of tag name  
   
Dim x As Integer   
' Loop variable  
   
Dim sTagName As String   
' Buffer for tag name   
   
' initialize the tag number  
iNumTags = ADS\_MAX\_TAGS  
   
' get the index handles  
lReturn = AdsGetAllIndexes( lhTable, ahIndex(0), iNumTags )   
If lReturn <> 0 Then   
   ' error you can display a custom message here   
   Exit Sub  
End If   
   
' Get the tag names  
For x = 0 To iNumTags - 1   
   ' Initialize the variables   
    iTagLen = ADS\_MAX\_TAG\_NAME   
    sTagName = String( iTagLen, )   
   
   ' Fill the string with spaces   
    lReturn = AdsGetIndexName( ahIndex(x), sTagName, iTagLen )   
   
   If lReturn = 0 Then   
        asTagNames(x) = sTagName   
   Else   
       ' error you can display a custom message here   
   End If  
End For