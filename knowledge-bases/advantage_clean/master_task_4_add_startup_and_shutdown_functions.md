---
title: Master Task 4 Add Startup And Shutdown Functions
slug: master_task_4_add_startup_and_shutdown_functions
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_task_4_add_startup_and_shutdown_functions.htm
source: Advantage CHM
tags:
  - master
checksum: 810987282d03e1b09a11eac2e836c5759edce52d
---

# Master Task 4 Add Startup And Shutdown Functions

Task 4: Add Startup and Shutdown Functions

Task 4: Add Startup and Shutdown Functions

Advantage Concepts

| Task 4: Add Startup and Shutdown Functions  Advantage Concepts |  |  |  |  |

We need to take some time to discuss session management. It would be nice if your AEP did not have to create connections, tables, and queries every time it was called.

To help facilitate this sort of functionality, AEP containers can implement two special procedures; Startup and Shutdown. The Startup function will be called by Advantage, on a per-connection basis, the first time a procedure inside of the AEP container is called. The Shutdown function will be called, on a per-connection basis, as each connection that has used the AEP container is closed. This means the Startup function is called once for each Advantage connection that begins using procedures inside of the AEP container, and the Shutdown function is also called once for each Advantage connection that has used procedures inside of the AEP container.

It is important when developing AEPs to keep in mind that they will be run by a multi-threaded server (Advantage). The Advantage Database Server does not necessarily use the same thread every time it executes requests for the client, so thread variables are not a suitable solution for providing client-specific storage in an AEP. All AEP functions are passed a unique identifier, the ulConnectionID parameter. This parameter can be used by the developer to uniquely identify a client connection. Resources allocated on behalf of the client (connections, open tables, etc) can be tied to this unique connection id, and retrieved at a later time.

TDataSet Descendant users will find documentation in the Advantage TDataSet Descendant Help (ADE.HLP) for the TAdsAEPSessionMgr object. (Note that each of the Advantage products and their corresponding Help files are installed separately.)

This object can be used to manage data modules created on a per-connection basis. It provides the functionality to save a newly allocated data module, and retrieve the same data module each time an Advantage Extended Procedure is called. The data module can then be uniquely identified, and released, from the Shutdown function.

Keeping this in mind take some time to familiarize yourself with the Startup and Shutdown functions that were generated for you in the AEP template.

Add Table Components to Access Our Data Files:

| 1. | Select an AdsTable component and place it on dm1. |

Object Inspector:

Name tblSalesReps

Databasename DataConn

TableName salesreps

| 2. | Select an AdsTable component and place it on dm1. |

Object Inspector:

Name tblCustomers

Databasename DataConn

TableName customers

| 3. | Select an AdsTable component and place it on dm1. |

Object Inspector:

Name tblProducts

Databasename DataConn

TableName products

| 4. | Select an AdsTable component and place it on dm1. |

Object Inspector:

Name tblOrders

Databasename DataConn

TableName orders

Initialize Your Data Module Tables:

It would be nice to have the tables we are going to be using open at all times. Lets put some code in our Startup function to open our tables after the data module has been created.

Add four open calls, one for each table, as shown in the code below.

function Startup( ulConnectionID: UNSIGNED32;

hConnection: ADSHANDLE

): UNSIGNED32;

{$IFDEF WIN32}stdcall;{$ENDIF}{$IFDEF LINUX}cdecl;{$ENDIF} // Do not change the prototype.

var

DM1 : TDM1;

begin

 

DM1 := nil;

Result := AE\_SUCCESS;

 

try

DM1 := TDM1.Create( nil );

 

{\* Configure DataConn to use the active handle hConnection. \*}

DM1.DataConn.SetHandle( hConnection );

{\* No need to activate the connection, SetHandle does that automatically. \*}

 

{\* Place tables on the data module, assign DataConn as their Databasname

\* property, and then open them here. \*}

DM1.tblCustomers.Open;

DM1.tblOrders.Open;

DM1.tblProducts.Open;

DM1.tblSalesReps.Open;

 

 

{\* Add this data module to the session manager, so we can retrieve it for

\* the user identified by ulConnectionID the next time they need it. \*}

AEPSessionMgr.AddDM( ulConnectionID, DM1 );

 

except

on E : EAdsDatabaseError do

{\* ADS-specific error, use ACE error code \*}

if assigned( DM1 ) then

DM1.DataConn.Execute( 'INSERT INTO \_\_error VALUES ( ' + IntToStr( E.ACEErrorCode ) + ', ' + QuotedStr( E.Message ) + ' )' )

else

Result := E.ACEErrorCode;

on E : exception do

{\* other error \*}

if assigned( DM1 ) then

DM1.DataConn.Execute( 'INSERT INTO \_\_error VALUES ( 1, ' + QuotedStr( E.Message ) + ' )' )

else

Result := 1;

end;

 

end;
