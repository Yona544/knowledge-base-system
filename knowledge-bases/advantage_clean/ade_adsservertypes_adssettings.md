---
title: Ade Adsservertypes Adssettings
slug: ade_adsservertypes_adssettings
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsservertypes_adssettings.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d86e81e88d908042a396d79d1c95bc0686aa7b19
---

# Ade Adsservertypes Adssettings

AdsServerTypes

TAdsSettings.AdsServerTypes

Advantage TDataSet Descendant

| TAdsSettings.AdsServerTypes  Advantage TDataSet Descendant |  |  |  |  |

[TAdsSettings](ade_tadssettings_7.md)

Defines the Advantage server types to which connections should be attempted.

Syntax

property AdsServerTypes : TAdsServerTypes;

Parameters

TAdsServerTypes = set of TAdsServerType

TAdsServerType = ( stADS\_REMOTE, stADS\_LOCAL, stADS\_AIS )

Description

AdsServerTypes should be set prior to any Advantage connections. Any new Advantage connection will observe this setting. Any existing Advantage connections will not be changed, therefore, new table opens may use existing connections.

The set items are defined as follows:

stADS\_REMOTE (Set to True by default): Specifies that all tables that will be opened reside in databases that are located on remote machines running the Advantage Database Server.

stADS\_AIS (Set to True by default): Specifies that specified tables will be opened through an Internet connection that are located on remote machines running an Internet-enabled Advantage Database Server.

Note An Advantage Data Dictionary connection must be used to get an Internet connection. (See [Accessing an Advantage Data Dictionary with the Advantage TDataSet Descendant](master_accessing_an_advantage_data_dictionary_with_the_advantage_tdataset_descendant.md)).

stADS\_LOCAL (Set to False by default): Specifies that all tables will be opened using the Advantage Local Server rather than the Advantage Database Server.

One or more of the properties listed above can be set to True, meaning that they will be active.

See [Advantage Server Types](master_advantage_server_types.md) for more information.

Note If stADS\_REMOTE, stADS\_AIS, and stADS\_LOCAL are all set to True, this will specify that tables will be opened with either the [Advantage Database Server](master_advantage_database_server.md), the Advantage Database Server via an Internet connection, or the [Advantage Local Server](master_advantage_local_server.md). If the table is on a networked drive to which you have a physical connection, the remote Advantage Database Server connection will be attempted first. If the Advantage Database Server could not be found within two seconds, a connection to the Advantage Internet Server is attempted. If an Internet address is not specified for the server in the ads.ini file, or the connection to Advantage Internet Server fails, the Advantage Local Server will be used. All subsequent opens for that UNC path or drive letter will not have the two-second delay.

 

Note The [TAdsConnection.AdsServerTypes](ade_adsservertypes_adsconnection.md) property overrides the TAdsSettings.AdsServerTypes value if the application is using a TAdsConnection component(s). The Advantage server connection for the TAdsConnection component will only attempt to use the server types indicated in the property set. If the set is empty, which is the default, the TAdsSettings.AdsServerTypes property set will be used. If multiple server types are needed to be used within an application, it is often easier to use multiple TAdsConnection components and set the Advantage server type via the TAdsConnection.AdsServerTypes property as opposed to using the TAdsSettings.AdsServerTypes property.
