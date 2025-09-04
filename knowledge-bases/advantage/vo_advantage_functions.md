Advantage Functions




Advantage Database Server 12  

Advantage Functions

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Functions  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - Advantage Functions Advantage Visual Objects and Vulcan.NET RDD vo\_Advantage\_functions Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Advanced  Functions > Overview / Dear Support Staff, |  |
| Advantage Functions  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Advantage provides advanced features to Visual Objects and Vulcan.NET through additional functions. These functions are more specific to Advantage and client/server features and thus, require the Advantage RDD be available within the application.

To use Advantage advanced functions, an additional Advantage library is needed. For Visual Objects an Application Export File (.AEF) is provided that contains a library file, DBFAXS. The AEF must be imported into the Visual Objects repository in order for the library to be accessible. The application then must reference the library. In order for the changes to take effect, the application must be recompiled.  For Vulcan.NET additional source files DBFAXS.prg and DBFAXS.vh are provided that contain the DBFAXS library of functions.  These files must be added to you Vulcan.NET project.

The SetSelectiveRelation method in the CAVO DBServer does not provide accurate relations. This problem has been fixed in Visual Objects version 2.0b-1. For earlier versions, the file, ADSDBSER.AEF, containing the AdsDBServer is provided to fix this problem. All data servers that will use the SetSelectiveRelation method must inherit from AdsDBServer instead of DBServer.

The object-oriented examples used in the following function descriptions are based on a class named AxDBServer. See [CLASS AxDBServer](vo_class_axdbserver.htm) for a code sample.

[AX\_AXSLocking()](vo_ax_axslocking.htm)

[AX\_BLOB2File()](vo_ax_blob2file.htm)

[AX\_File2BLOB()](vo_ax_file2blob.htm)

[AX\_GetAceIndexHandle()](vo_ax_getaceindexhandle.htm)

[AX\_GetAceTableHandle()](vo_ax_getacetablehandle.htm)

[AX\_IsServerLoaded()](vo_ax_isserverloaded.htm)

[AX\_PercentIndexed()](vo_ax_percentindexed.htm)

[AX\_RightsCheck()](vo_ax_rightscheck.htm)

[AX\_SetConnectionHandle()](vo_ax_setconnectionhandle.htm)

[AX\_SetPassword()](vo_ax_setpassword.htm)

[AX\_SetServerType()](vo_ax_setservertype.htm)

[AX\_Transaction()](vo_ax_transaction.htm)

[AX\_UsingClientServer()](vo_ax_usingclientserver.htm)