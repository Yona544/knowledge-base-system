---
title: Vo Class Axdbserver
slug: vo_class_axdbserver
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_class_axdbserver.htm
source: Advantage CHM
tags:
  - vo
checksum: 8f248cf3661ec33f309ef86c62a7c3ef4e300bef
---

# Vo Class Axdbserver

CLASS AxDBServer

CLASS AxDBServer

Advantage Visual Objects RDD

| CLASS AxDBServer  Advantage Visual Objects RDD |  |  |  |  |

This example class, named AxDBServer, inherits from the DBServer class. The AxDBServer class overrides methods to slightly change the behavior of the DBServer class.

\_DLL FUNC DBFAXSAdsIsServerLoaded ( pucServer AS PSZ, pbLoaded REF WORD ) AS LONGINT PASCAL:ACE32.AdsIsServerLoaded

\_DLL FUNC DBFAXSAdsFileToBinary ( hTbl AS LONGINT, pucFldName AS PSZ, usBinaryType AS WORD, pucFileName AS PSZ ) AS LONGINT PASCAL:ACE32.AdsFileToBinary

\_DLL FUNC DBFAXSAdsBinaryToFile ( hTbl AS LONGINT, pucFldName AS PSZ, pucFileName AS PSZ ) AS LONGINT PASCAL:ACE32.AdsBinaryToFile

\_DLL FUNC DBFAXSAdsBeginTransaction ( hConnect AS LONGINT ) AS LONGINT PASCAL:ACE32.AdsBeginTransaction

\_DLL FUNC DBFAXSAdsCommitTransaction ( hConnect AS LONGINT ) AS LONGINT PASCAL:ACE32.AdsCommitTransaction

\_DLL FUNC DBFAXSAdsRollbackTransaction ( hConnect AS LONGINT ) AS LONGINT PASCAL:ACE32.AdsRollbackTransaction

\_DLL FUNC DBFAXSAdsInTransaction ( hConnect AS LONGINT, pbInTrans REF WORD ) AS LONGINT PASCAL:ACE32.AdsInTransaction

\_DLL FUNC DBFAXSAdsSetServerType ( usServerOptions AS WORD ) AS LONGINT PASCAL:ACE32.AdsSetServerType

\_DLL FUNC DBFAXSAdsGetConnectionType ( hConnect AS LONGINT, pusConnectType REF WORD ) AS LONGINT PASCAL:ACE32.AdsGetConnectionType

\_DLL FUNC DBFAXSAdsFindConnection ( pucServerName AS PSZ, phConnect REF LONGINT ) AS LONGINT PASCAL:ACE32.AdsFindConnection

\_DLL FUNC DBFAXSAdsEnableEncryption( hTbl AS DWORD, pucPassword AS PSZ ) AS DWORD PASCAL:ACE32.AdsEnableEncryption

\_DLL FUNC DBFAXSAdsDisableEncryption( hTbl AS DWORD ) AS DWORD PASCAL:ACE32.AdsDisableEncryption

 

DEFINE AX\_BEGIN\_TRANSACTION := 1

DEFINE AX\_COMMIT\_TRANSACTION := 2

DEFINE AX\_ROLLBACK\_TRANSACTION := 3

DEFINE AX\_ISACTIVE\_TRANSACTION := 4

DEFINE DBI\_GET\_ACE\_TABLE\_HANDLE := DBI\_USER + 110

DEFINE DBOI\_AXS\_PERCENT\_INDEXED := 1805

DEFINE \_SET\_AXSLOCKING     := \_SET\_USER + 1

DEFINE \_SET\_RIGHTSCHECKING    := \_SET\_USER + 2

DEFINE DBFAXS\_ADS\_LOCAL\_SERVER := 1

DEFINE DBFAXS\_ADS\_REMOTE\_SERVER := 2

DEFINE DBFAXS\_ADS\_AIS\_SERVER := 4

DEFINE DBOI\_GET\_ACE\_INDEX\_HANDLE := 1806

 

CLASS AxDBServer INHERIT DBServer

 

DECLARE METHOD AX\_BLOB2File

DECLARE METHOD AX\_File2BLOB

DECLARE METHOD AX\_SetPassword

DECLARE METHOD AX\_isServerLoaded

 

////////////////////////////////////////////////////////////////////////////////

METHOD Init(oFileSpec, lShareMode, lReadOnlyMode, cDriver) CLASS AxDBServer

IF IsNil(cDriver)

  cDriver := "AXDBFNTX"

  // cDriver := "DBFCDXAX"

ENDIF

SUPER:Init(oFileSpec, lShareMode, lReadOnlyMode, cDriver)

 

////////////////////////////////////////////////////////////////////////////////

METHOD AX\_GetAceTableHandle() CLASS AxDBServer

// Returns the table handle for the current workarea. This handle can be used

// to call the Advantage Client Engine directly.

// Returns a 0 if there is a problem.

RETURN SELF:INFO( DBI\_GET\_ACE\_TABLE\_HANDLE )

 

////////////////////////////////////////////////////////////////////////////////

METHOD AX\_GetAceIndexHandle( uIndexFile, uOrder ) CLASS AxDBServer

// Returns an index handle for the current workarea. This handle can be used

// to call the Advantage Client Engine directly.

// Returns a 0 if there is a problem or if no index was found.

 

// uIndexFile -- filename or NIL

// uOrder -- order name, number, or NIL

RETURN SELF:ORDERINFO( DBOI\_GET\_ACE\_INDEX\_HANDLE, uIndexFile, uOrder )

////////////////////////////////////////////////////////////////////////////////

METHOD AX\_File2BLOB( cFileName AS STRING, cFieldName AS STRING ) CLASS AxDBServer

LOCAL ulRetCode AS LONGINT

LOCAL hTable AS LONGINT

 

hTable := SELF:AX\_GetAceTableHandle()

ulRetCode := DBFAXSAdsFileToBinary( hTable, String2Psz( cFieldName ), ;

6 /\*ADS\_BINARY\*/, String2Psz( cFileName ))

RETURN ( ulRetCode = 0 )

 

////////////////////////////////////////////////////////////////////////////////

METHOD AX\_PercentIndexed() CLASS AxDBServer

// Return the percentage of keys added to a currently building index

RETURN DBORDERINFO( DBOI\_AXS\_PERCENT\_INDEXED )

 

////////////////////////////////////////////////////////////////////////////////

METHOD AX\_AXSLocking( bMode ) CLASS AxDBServer

// Return and optionally set the AXS locking status

LOCAL bRetVal

 

// If the paramter passed in is not a Logical value, then set it to NIL

IF ( ValType( bMode ) != 'L' )

bMode := NIL

ENDIF

 

bRetVal := SELF:RDDINFO( \_SET\_AXSLOCKING, bMode )

 

// If the Returned bool is NIL, then Return the default setting

IF ( IsNil( bRetVal ) )

bRetVal := True

ENDIF

 

RETURN ( bRetVal )

 

////////////////////////////////////////////////////////////////////////////////

METHOD AX\_RightsCheck( bMode ) CLASS AxDBServer

// Return and optionally set the AXS Rights Checking status

LOCAL bRetVal

 

// If the paramter passed in is not a Logical value, then set it to NIL

IF ( ValType( bMode ) != 'L' )

bMode := NIL

ENDIF

 

bRetVal := SELF:RDDINFO( \_SET\_RIGHTSCHECKING, bMode )

 

// If the Returned bool is NIL, then Return the default setting

IF ( IsNil( bRetVal ) )

bRetVal := True

ENDIF

 

RETURN( bRetVal )

 

////////////////////////////////////////////////////////////////////////////////

METHOD AX\_Transaction( iAction ) CLASS AxDBServer // Transaction call

LOCAL usInTrans AS WORD

LOCAL ulRetVal AS LONGINT

/\*

\* Transaction Processing METHOD. The parameter can be

\* AX\_BEGIN\_TRANSACTION

\* AX\_COMMIT\_TRANSACTION

\* AX\_ROLLBACK\_TRANSACTION

\* AX\_ISACTIVE\_TRANSACTION

\*/

usInTrans := 0

IF ( IsNil( iAction )) // if no arguments, then return ISACTIVE

  iAction := AX\_ISACTIVE\_TRANSACTION

ENDIF

 

DO CASE

CASE iAction = AX\_BEGIN\_TRANSACTION

  ulRetVal := DBFAXSAdsBeginTransaction( 0 )

  RETURN (ulRetVal == 0)

 

CASE iAction = AX\_COMMIT\_TRANSACTION

  ulRetVal := DBFAXSAdsCommitTransaction( 0 )

  RETURN (ulRetVal == 0)

 

CASE iAction = AX\_ROLLBACK\_TRANSACTION

  ulRetVal := DBFAXSAdsRollbackTransaction( 0 )

  RETURN (ulRetVal == 0)

 

CASE iAction = AX\_ISACTIVE\_TRANSACTION

  ulRetVal := DBFAXSAdsInTransaction( 0, @usInTrans )

  RETURN ( usInTrans != 0 )

ENDCASE

 

// Shouldn't get here

RETURN FALSE

 

////////////////////////////////////////////////////////////////////////////////

METHOD AX\_BLOB2File( cFileName AS STRING, cFieldName AS STRING ) CLASS AxDBServer

// copy a BLOB to a file

LOCAL hTable AS LONGINT

LOCAL ulRetCode AS LONGINT

 

hTable := SELF:AX\_GetAceTableHandle()

ulRetCode := DBFAXSAdsBinaryToFile( hTable, String2Psz( cFieldName ), String2Psz( cFileName ))

RETURN ( ulRetCode == 0 )

 

////////////////////////////////////////////////////////////////////////////////

METHOD AX\_SetPassword( szEncodeKey AS STRING ) CLASS AxDBServer

// Set password for record encryption

IF ( IsNil( szEncodeKey ) .or. (szEncodeKey == '' ))

DBFAXSAdsDisableEncryption( SELF:AX\_GetAceTableHandle() )

ELSE

DBFAXSAdsEnableEncryption( SELF:AX\_GetAceTableHandle(), String2Psz( szEncodeKey ) )

ENDIF

RETURN

 

////////////////////////////////////////////////////////////////////////////////

METHOD AX\_SetServerType( lUseRemoteServer, lUseInternetServer, ;

lUseLocalServer ) CLASS AxDBServer

// determine which Advantage server to connect to

LOCAL usServerTypes AS WORD

LOCAL ulRetCode AS LONGINT

 

usServerTypes := 0

IF( lUseRemoteServer )

usServerTypes := \_or( usServerTypes, DBFAXS\_ADS\_REMOTE\_SERVER )

ENDIF

IF( lUseInternetServer )

usServerTypes := \_or( usServerTypes, DBFAXS\_ADS\_AIS\_SERVER )

ENDIF

IF( lUseLocalServer )

usServerTypes := \_or( usServerTypes, DBFAXS\_ADS\_LOCAL\_SERVER )

ENDIF

 

ulRetCode := DBFAXSAdsSetServerType( usServerTypes )

 

RETURN ( ulRetCode == 0 )

 

////////////////////////////////////////////////////////////////////////////////

METHOD AX\_IsServerLoaded( cFileName AS STRING ) CLASS AxDBServer

// Return .T. if Advantage is loaded.

// cFileName must start with a drive letter ("X:\")

// or a UNC path ("\\server\volume\path\")

 

LOCAL usLoaded AS WORD

 

usLoaded := 0

DBFAXSAdsIsServerLoaded ( String2Psz( cFileName ), @usLoaded )

 

RETURN ( usLoaded != 0 )

 

////////////////////////////////////////////////////////////////////////////////

METHOD AX\_UsingClientServer( ) CLASS AxDBServer

// return .T. if the current workarea is using Advantage Server or AIS Server and

// .F. IF USING Advantage RDD IN a LOCAL mode

LOCAL ulRetCode AS LONGINT

LOCAL ConnectionHandle AS LONGINT

LOCAL usServerType AS WORD

LOCAL strFileName AS STRING

 

strFileName := SELF:INFO( DBI\_FULLPATH )

ulRetCode := DBFAXSAdsFindConnection( String2Psz( strFileName ), @ConnectionHandle )

ulRetCode := DBFAXSAdsGetConnectionType( ConnectionHandle, @usServerType )

RETURN ( usServerType == DBFAXS\_ADS\_REMOTE\_SERVER ) .OR. ( usServerType == DBFAXS\_ADS\_AIS\_SERVER )
