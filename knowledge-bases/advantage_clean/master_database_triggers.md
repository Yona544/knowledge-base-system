---
title: Master Database Triggers
slug: master_database_triggers
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_database_triggers.htm
source: Advantage CHM
tags:
  - master
checksum: 3b15b43da874e5fde59c9aab829a9e021f59659f
---

# Master Database Triggers

Database Triggers

Database Triggers

Advantage Concepts

| Database Triggers  Advantage Concepts |  |  |  |  |

Trigger Event Types

Database triggers are a type of [trigger](master_what_is_a_trigger_.md) that is defined at the database object level (as opposed to being associated with a table). Database triggers are fired in response to certain events.  Currently, the following combinations of trigger type and event types are supported:

| Event Type | Supported Trigger Types | Description |
| OPEN\_TABLE | BEFORE, AFTER | Fires when low level open table requests are made. A BEFORE trigger fires before the open attempt is made, so it can fire for open requests on non-existent tables. An AFTER trigger fires after successfully opening the table. A trigger that throws an exception (or inserts a row into the \_\_error table) will cause the open table request to be cancelled and an error returned. Note that when table caching is in effect (the default with SQL statements) not all opens for the user will necessarily be logged. For example, if a the SQL "SELECT \* FROM mytable" is run 5 times by a user, it is possible that only the first open request will result in firing the trigger. |
| CLOSE\_TABLE | BEFORE, AFTER | Fires when a low level close request is made. Note that the close request does not necessarily mean the file is physically being closed. Advantage opens each table physically only one time and references counts the actual opens. CLOSE\_TABLE triggers cannot be used to cancel the close request. Errors returned from the trigger are logged to the Advantage error log (e.g., ads\_err.adt), but the error is then ignored by the server. |
| CONNECT | AFTER | Fires after a successful connection to a data dictionary. If the trigger throws an exception (or inserts a row into the \_\_error table), the connection will be disallowed except for ADSSYS. When ADSSYS connects, the trigger will fire, but errors are ignored and the connection is allowed. If the trigger does throw an exception or return an error, the native error that is returned to the client will be [7109](error_7109_database_logins_are_disabled.md). |
| DISCONNECT | BEFORE | Fires at the beginning of the disconnect process. DISCONNECT triggers cannot be used to cancel the disconnect request. If a trigger returns an error, the error is logged, but it is ignored by the disconnect logic. |

Note: Database triggers are stored in the data dictionary as trigger objects (the same as table triggers). If you create a database trigger in a dictionary and then use that dictionary with older versions of Advantage (pre v12.0), it is possible that some system tables won't be retrieved if requested. And, of course, the database triggers will not be fired.

Example

As an example, to define a trigger that logs when a certain table is opened and closed, you might create triggers such as the following. For syntax information and additional examples, see the [Create Trigger Syntax](master_create_trigger.md).

CREATE TRIGGER LogOpenTable ON DATABASE AFTER OPEN\_TABLE

BEGIN

  IF \_\_info.tablename = 'Salaries' THEN

     INSERT INTO logopenclose VALUES (now(), \_\_info.UserName, \_\_info.ClientName,

          \_\_info.FullPath, \_\_info.TrigEvent );

  END IF;

END;

 

 

CREATE TRIGGER LogOpenTable ON DATABASE BEFORE CLOSE\_TABLE

BEGIN

  IF \_\_info.tablename = 'Salaries' THEN

     INSERT INTO logopenclose VALUES (now(), \_\_info.UserName, \_\_info.ClientName,

          \_\_info.FullPath, \_\_info.TrigEvent );

  END IF;

END;

\_\_INFO Table

The \_\_info table contains read-only information about the event. For OPEN\_TABLE and CLOSE\_TABLE event types, the available information in the \_\_info table includes the following:

| Field Name | Field Type | Description |
| UserID | Integer | The internally maintained user ID that is associated with each individual connection. A possible use for this value might be to associate different individual events with each other. |
| TrigType | CiChar(10) | The trigger type (e.g., BEFORE, AFTER). |
| TrigEvent | CiChar(15) | The event type (e.g., OPEN\_TABLE, CLOSE\_TABLE) |
| TableName | CiChar(256) | The base name of the table. For temporary tables this is the temporary name used to create the table (without the # hash symbol prefix). |
| FullPath | CiChar(256) | The physical file path of the table. |
| UserName | CiChar(50) | The database login name. |
| ClientName | CiChar(50) | The client workstation name if available. |
| OpenCount | Integer | The number of open instances of this table. This is only available for AFTER OPEN\_TABLE and BEFORE CLOSE\_TABLE tiggers. It is empty/null for other triggers since the information is not available at that time. |
| IsShared | Logical | Indicates if the table is opened shared (false indicates exclusive open). |
| IsFree | Logical | Indicates if the table open is as a free table (not listed in the dictionary). |
| LockType | Integer | This value indicates the locking type requested (0 = ADS\_COMPATIBLE\_LOCKING, 1 = ADS\_PROPRIETARY\_LOCKING). |
| TableType | Integer | This indicates the table type requsted (1 = ADS\_NTX, 2 = ADS\_CDX, 3 = ADS\_ADT, 4 = ADS\_VFP). |
| IsDirect | Logical | A value of TRUE Indicates the table is opened directly from the client (e.g., a navigational type of open) and FALSE indicates it was opened in response to a request on the server (e.g., part of an SQL statement). This is only available for OPEN\_TABLE events. |
| IsTemp | Logical | Indicates if the it is a temporary table. |

The \_\_info table for CONNECT and DISCONNECT events contains the following fields:

| Field Name | Field Type | Description |
| UserID | Integer | The internally maintained user ID that is associated with each individual connection. A possible use for this value might be to associate different individual events with each other. |
| TrigType | CiChar(10) | The trigger type (e.g., BEFORE, AFTER). |
| TrigEvent | CiChar(15) | The event type (e.g., OPEN\_TABLE, CLOSE\_TABLE) |
| UserName | CiChar(50) | The database login name |
| ClientName | CiChar(50) | The client workstation name if available. |
| LoginName | CiChar(50) | The client workstation login name if available. |
| ConnPath | CiChar(256) | The database connection path. |
| Address | CiChar(30) | The client network address if available. |
| AppID | CiChar(70) | The application identifier ([ApplicationID](master_applicationid.md)). |
| OpCount | Integer | The number of operations recorded by the user. This is the number of low level operations that the server tracks (not necessarily individual client requests). For example, a single SQL statement can result in many low level operations. |
| StmtCount | Integer | The number of SQL statements executed by this connection. |
| CommType | CiChar(10) | Indicates the communications type. These include TCP\_IP, UDP\_IP, TLS, or SMC (shared memory comm). For local server usage, this will have the value LOCAL. See [sp\_GetSecurityInfo](master_sp_getsecurityinfo.md). |
| EncrType | CiChar(10) | Indicates the type of encryption in use by the connection if applicable. Values included AES128, AES256, RC4. See [sp\_GetSecurityInfo](master_sp_getsecurityinfo.md). |
| TLSCipher | CiChar(20) | For TLS connections, this shows the cipher in use. See [sp\_GetSecurityInfo](master_sp_getsecurityinfo.md). |
| TLSVersion | CiChar(20) | For TLS connections, this shows the version information. See [sp\_GetSecurityInfo](master_sp_getsecurityinfo.md). |

Table Type in Database Triggers

The table type that is in effect when triggers run depend on the current settings in effect (e.g., the settings in use by the currently running SQL statement). For CONNECT triggers, no SQL statement will be active yet, so the table type will default to ADT. This should not typically be a problem unless you are accessing a free table (or creating a free table in the trigger). The table type in that case will be dependent on the most recent SQL setting. Therefore, it is advisable to use database tables (as opposed to free tables) inside triggers to avoid the possibility of unexpected table type dependencies.
