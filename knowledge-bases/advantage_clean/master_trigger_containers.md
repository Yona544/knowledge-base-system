---
title: Master Trigger Containers
slug: master_trigger_containers
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_trigger_containers.htm
source: Advantage CHM
tags:
  - master
checksum: 6130b3e0367934041ba6c70e5b09abda1f3db92f
---

# Master Trigger Containers

Trigger Containers

Trigger Containers

Advantage Concepts

| Trigger Containers  Advantage Concepts |  |  |  |  |

Advantage triggers can be implemented in a variety of containers: [SQL scripts](master_sql_script_overview.md), .NET Assemblies, Win32 DLLs, COM objects, or Linux shared objects.

Note See the [SQL scripts](master_sql_script_overview.md) documentation for details on script syntax and functionality. SQL scripts are the recommended container type. However, if the scripting language does not meet your needs, one of the alternate container types can be used.

A simple AFTER DELETE trigger that saves a copy of the deleted row to a backup table is shown below:

INSERT INTO backup\_orders SELECT \* FROM \_\_old

All other trigger containers export a function with a pre-defined prototype, which the Advantage server will call when firing a trigger.

A trigger project template is included with the Advantage TDataSet Descendant installation and with the Advantage OLE DB Provider installation. The projects can be found under the appropriate File -> New menu in each development environment.

Delphi/C++Builder/Kylix: File -> New -> Advantage tab

Microsoft Visual Studio .NET: File -> New -> Project (templates exist for VB and C#)

The trigger function interface is shown below. Note that any development environment that can create a supported container can be used to implement a trigger.

Delphi//Kylix

function MyTrigger

(

ulConnectionID : UNSIGNED32;

hConnection : ADSHANDLE;

pcTriggerName : PChar;

pcTableName : PChar;

ulEventType : UNSIGNED32;

ulTriggerType : UNSIGNED32;

ulRecNo : UNSIGNED32

) : UNSIGNED32;

 

VB.NET

Public Function MyTrigger

(

ByVal ulConnectionID As Int32, \_

ByVal hConnection As Int32, \_

ByVal strTriggerName As String, \_

ByVal strTableName As String, \_

ByVal ulEventType As Int32, \_

ByVal ulTriggerType As Int32, \_

ByVal ulRecNo As Int32) As Int32

)

C#.NET

Public Int32 MyTrigger

(

Int32 ulConnectionID,

Int32 hConnection,

String strTriggerName,

String strTableName,

Int32 ulEventType,

Int32 ulTriggerType,

Int32 ulRecNo

)

 

ulConnectionID is a unique id which can be used to identify the user who caused this trigger to fire.

 

hConnection is an active ACE connection handle which should be used by the trigger. This connection handle is already active, and has the same permissions as the client. All operations performed on a connection handle other than hConnection will not be part of the existing transaction, and will not be rolled back in case of an error.

 

strTriggerName is the name of the dictionary object name of the trigger that is begin fired.

 

strTableName is the name of the table the trigger is being fired on.

 

ulEventType is the ACE event type (INSERT, UPDATE or DELETE) of the trigger that is being fired.

 

ulTriggerType is the ACE trigger type (BEFORE, INSTEAD OF, or AFTER) of the trigger that is being fired.

 

ulRecNo is the record number of the record that caused this trigger to fire.

 

The trigger function return code is currently not used (all errors are returned via the \_\_error table). The return value has been reserved for future use. All triggers should currently return zero. Failure to do so could result in trigger failures when upgrading to future versions of Advantage.

Advantage TDataSet Descendant templates for extended procedures and triggers support version 4 or greater of Borland C++Builder, and version 4 or greater of Borland Delphi. While native support for earlier versions is not provided, the templates can be modified slightly to build using older versions. Replace calls to TAdsConnection.Execute with TAdsQuery instances that perform the same updates.
