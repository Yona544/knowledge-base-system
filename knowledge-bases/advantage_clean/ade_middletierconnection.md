---
title: Ade Middletierconnection
slug: ade_middletierconnection
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_middletierconnection.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 5fa95b50149db65e16eb04b9109355f99cd0d443
---

# Ade Middletierconnection

MiddleTierConnection

TAdsConnection.MiddleTierConnection

Advantage TDataSet Descendant

| TAdsConnection.MiddleTierConnection  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Specifies if this connection lives in a middle-tier server and will be used on the behalf of remote clients.

Syntax

property MiddleTierConnection: Boolean;

Description

Set MiddleTierConnection to True when writing a middle-tier server application such as a MIDAS server application.

If the MiddleTierConnection property is set to True the application will correctly maintain user and connection counts for the remote clients that connect to the Advantage Database Server through the application server.

The MiddleTierConnection property only affects connections to the Advantage Database Server. Connections to Advantage Local Server are not affected by this property.

If multiple TAdsConnection objects are used per remote request only set MiddleTierConnection to True for one of the TAdsConnection objects.

If a connection pooling algorithm is being implemented set MiddleTierConnection to True for each TAdsConnection instance in the pool.

If more than one TAdsConnection component is used in the application you may see what you consider to be an incorrect user count with the first instance of the application. For example, if you have two TAdsConnection components in your middle tier application you should have one TAdsConnection component with the MiddleTierConnection property set to True, and all additional TAdsConnection components used in the application should have the MiddleTierConnection property set to False. In this situation, the first instance of the middle tier application will show up as 2 users and 2 connections. This is the expected behavior. When the next instance of the application is started you will see the expected behavior: 3 users and 3 connections, then 4 users and 4 connections, etc.

Because you are using an extra TAdsConnection component (the instance with MiddleTierConnection set to False) it counts as an extra user. The extra user consumed by that connection is not, however, incremented with every new instance of the application. See the diagram below for an explanation.

You can have any number of "utility" connections, as long as they don't have the MiddleTierConnection property set to True they will only consume one user.

License Notes

In general, this property was added to allow an Advantage middleware type of application to increment the Advantage Database Server user count for each remote client workstation indirectly accessing the Advantage Database Server. This provides an easy way for Advantage middleware applications to abide by the Advantage Database Server license agreement as related to remote client workstations taking up a "user" towards the maximum number of licensed users. The two sections of the Advantage client license agreements that discuss licensing issues are as follows. Note that it is illegal to use a middleware type of application with the Advantage Local Server.

| 1. | Advantage Database Server Connections. If this SOFTWARE PRODUCT is used in conjunction with an Advantage Database Server (a.k.a. a remote server), any computer connecting to the Advantage Database Server through this SOFTWARE PRODUCT will be considered a "User" and must consume a User towards the maximum number of licensed users. |

| 2. | Advantage Local Server Connections. If an application using this SOFTWARE PRODUCT is distributed to work without the Advantage Database Server (i.e., it uses the Advantage Local Server to access data), the application must act as a "client" that directly accesses and uses the data. The application cannot act as "middleware" or as a "server" by having the data forwarded by any means to a separate computer. In other words, it is illegal to use the Advantage Local Server with a Web server, an application server, a terminal server, or any other type of middleware or server product to access data on behalf of remote computers. An Advantage Database Server (a.k.a. remote server) product must be purchased and used to allow this SOFTWARE PRODUCT to access data on behalf of applications running on remote computers. |

Example

procedure TMyRemoteData.RemoteDataModuleCreate(Sender: TObject);

begin

 

{\* Set MiddleTierConnection flag because this is the middle-tier server object \*}

AdsConnection.MiddleTierConnection := TRUE;

{\* Open the table for the entire client session \*}

DemoTable.Open;

 

end;
