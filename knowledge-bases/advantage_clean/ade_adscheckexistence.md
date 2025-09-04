---
title: Ade Adscheckexistence
slug: ade_adscheckexistence
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adscheckexistence.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d09092fff5057382e1ddcb74ce08acb72093d28e
---

# Ade Adscheckexistence

AdsCheckExistence

TAdsTable/TAdsQuery.AdsCheckExistence

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsCheckExistence  Advantage TDataSet Descendant |  |  |  |  |

Checks for existence of a file.

Syntax

function AdsCheckExistence( strFileName : String ) : Boolean;

Parameter

| strFileName | File name to check the existence of. |

Description

Checks for existence of a file (any file, not just a table) named strFilename. How the existence check is done by Advantage depends on many factors. These factors include whether or not you are using a database connection) or free connection), whether you are checking for a table that is already open, or checking for a table or some other file. It also depends on the Advantage server type to which you are connected. Those server type variations are discussed below:

Advantage Internet Server connections:

If a table name is specified, and that table exists in the data dictionary (when using a database connection)), or if that table is already open on the current connection, this function will return True. Otherwise, it is assumed the specified file does not exist, and False is returned.

Advantage Database Server and Advantage Local Server connections:

If a table name is specified, and that table exists in the data dictionary (when using a database connection)), or if that table is already open on the current connection, this function will return True. Otherwise, a non-Advantage, low-level file access function is called from the client to check for existence of the specified file. If checking for file existence of a file on a server, this function cannot override normal access rights imposed by that server. If the client has access rights to the specified file, and it exists, True will be returned. If the specified file does not exist, or if the client does not have access rights to the specified file that does exist, this function will return False.

Example

{ determine if an image file exists on a remote Advantage server }

AdsSettings1.AdsServerTypes := [stADS\_REMOTE];

AdsTable1.AdsConnection := AdsConnection1;

AdsConnection1.ConnectPath := 'x:\data';

AdsTable1.Active := TRUE;

bDoesExist := AdsTable1.AdsCheckExistence( 'x:\data\picture.jpg' );

 

{ determine if an image file exists on a remote Advantage Database Sever when using an alias }

AdsSettings1.AdsServerTypes := [stADS\_AIS];

AdsConnection1.AliasName := 'MyAlias';

AdsTable1.AdsConnection := AdsConnection1;

AdsTable1.AdsCheckExistence( AdsConnection1.GetConnectionPath + AdsTable1.TableName );

See Also

None.
