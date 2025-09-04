---
title: Ace Adsddcreatetrigger
slug: ace_adsddcreatetrigger
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddcreatetrigger.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 74138bbb82cc483f01b3d92a00121ceec77bf522
---

# Ace Adsddcreatetrigger

AdsDDCreateTrigger

AdsDDCreateTrigger

Advantage Client Engine

| AdsDDCreateTrigger  Advantage Client Engine |  |  |  |  |

Adds a new trigger to the data dictionary.

Syntax

UNSIGNED32 AdsDDCreateTrigger( ADSHANDLE hDictionary, UNSIGNED8 \*pucName,

UNSIGNED8 \*pucTableName, UNSIGNED32 ulTriggerType,

UNSIGNED32 ulEventTypes, UNSIGNED32 ulContainerType,

UNSIGNED8 \*pucContainer, UNSIGNED8 \*pucFunctionName,

UNSIGNED32 ulPriority, UNSIGNED8 \*pucComments,

UNSIGNED32 ulOptions );

 

UNSIGNED32 AdsDDCreateTrigger100( ADSHANDLE hDictionary, UNSIGNED8 \*pucName,

UNSIGNED8 \*pucTableName, UNSIGNED32 ulTriggerType,

UNSIGNED32 ulEventTypes, UNSIGNED32 ulContainerType,

WCHAR      \*pwcContainer, UNSIGNED8 \*pucFunctionName,

UNSIGNED32 ulPriority, UNSIGNED8 \*pucComments,

UNSIGNED32 ulOptions );

Parameters

| hDictionary (I) | A data dictionary connection. |
| pucName (I) | The name of the trigger to be created. |
| pucTableName (I) | The name of the table the trigger will fire on. When creating [database triggers](master_database_triggers.md), this should be NULL. |
| ulTriggerType (I) | The type of trigger to create. This value can be ADS\_TRIGTYPE\_BEFORE, ADS\_TRIGTYPE\_INSTEADOF, ADS\_TRIGTYPE\_CONFLICTON, or ADS\_TRIGTYPE\_AFTER. |
| ulEventTypes (I) | The kind of event the trigger should fire on. For table triggers, the value can be ADS\_TRIGEVENT\_INSERT, ADS\_TRIGEVENT\_UPDATE, or ADS\_TRIGEVENT\_DELETE. For [database triggers](master_database_triggers.md), this can be ADS\_TRIGEVENT\_OPEN\_TABLE, ADS\_TRIGEVENT\_CLOSE\_TABLE, ADS\_TRIGEVENT\_CONNECT, or ADS\_TRIGEVENT\_DISCONNECT. |
| ulContainerType (I) | The kind of container the trigger lives in. This value can be ADS\_TRIG\_WIN32DLL, ADS\_TRIG\_COM, or ADS\_TRIG\_SCRIPT. |
| pucContainer (I)  pwcContainer(I) | The container. If the container type is ADS\_TRIG\_WIN32DLL this value should be the path and dll name (or linux path and shared object name). If the container type is ADS\_TRIG\_COM this value should be the ProgID of a COM object or a .NET assembly. If the container type is ADS\_TRIG\_SCRIPT, this should be a pointer to the trigger script statements. |
| pucFunctionName (I) | The name of the function to call inside the container. This value is ignored if the container type is ADS\_TRIG\_SCRIPT. |
| ulPriority (I) | Firing order priority if multiple triggers of the same type exist on a table (for example, multiple AFTER triggers). |
| pucComments (I) | Optional description of the trigger. |
| ulOptions (I) | This is a bit field for defining the options for creating table triggers. These options are ignored for [database triggers](master_database_triggers.md). The options can be ORed together. The options are:  ADS\_TRIGOPTIONS\_DEFAULT: Default options. Trigger values tables will be passed to the trigger (\_\_old and \_\_new tables) and will include memo and blob data.  ADS\_TRIGOPTIONS\_WANT\_MEMOS\_AND\_BLOBS: Currently the same as ADS\_TRIGOPTIONS\_DEFAULT.  ADS\_TRIGOPTIONS\_WANT\_VALUES: Trigger values tables will be passed to the trigger, but will not include memo or blob data.  ADS\_TRIGOPTIONS\_NO\_VALUES: Trigger values tables will not be passed to the trigger.  ADS\_TRIGOPTIONS\_NO\_TRANSACTION: Implicit transaction will not be started for this trigger. |

Remarks

AdsDDCreateTrigger and AdsDDCreateTrigger100 can only be executed successful to create table triggers by users that have both ALTER permission on the table and CREATE PROCEDURE permission in the database. When creating [database triggers](master_database_triggers.md), users must have ALTER permission on the database.

Trigger creation does not verify library or .NET assembly existence. If a trigger is defined on a library or assembly that does not exist, a run-time error will occur when the trigger is executed.

Statements inside script triggers are validated for syntactical correctness only. If any semantic errors exist, a run-time error will occur when the trigger is executed.

If a trigger container is in use, and modifications are made to a trigger definition (including trigger addition or deletion), the changes will not take effect until all users who have used a trigger in that container disconnect from the database.

Currently trigger creation and deletion will not affect tables already opened by the server. For example, if table1 is opened by active clients, and the administrator adds a new trigger to table1, the trigger will not activate until all active users have closed table1 and it has been re-opened.

See [Triggers](master_triggers.md) for detailed trigger information.

Example

ulRetVal = AdsDDCreateTrigger( hConn,

"MyTrigger",

"mytable",

ADS\_TRIGTYPE\_AFTER,

ADS\_TRIGEVENT\_INSERT,

ADS\_TRIG\_WIN32DLL,

"x:\data\AdsTriggers.dll",

"myfunction",

1 /\* priority \*/,

"my first trigger ",

ADS\_TRIGOPTIONS\_DEFAULT );

See Also

[AdsDDRemoveTrigger](ace_adsddremovetrigger.md)
