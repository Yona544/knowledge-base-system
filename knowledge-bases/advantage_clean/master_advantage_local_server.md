---
title: Master Advantage Local Server
slug: master_advantage_local_server
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_local_server.htm
source: Advantage CHM
tags:
  - master
checksum: 8ccad23debb9e609fd40e73ed2fa2b4c8b4c75ec
---

# Master Advantage Local Server

Server Type: Advantage Local Server

Server Type: Advantage Local Server

Advantage Concepts

| Server Type: Advantage Local Server  Advantage Concepts |  |  |  |  |

The Advantage Local Server allows Advantage applications access to data files located locally, in shared environments, or in peer-to-peer environments. The Advantage Local Server is a non-client/server solution and can be used to access data on computers that are not running the Advantage Database Server. The Advantage Local Server is called directly by the Advantage Client Engine, both of which exist as either Windows DLLs or Linux shared objects. If the data files exist on a local workstation, no network connection is necessary nor is network communication used between the Advantage client and the Advantage Local Server.

There is no cost for the Advantage Local Server. The Advantage Local Server is installed with all Advantage Windows and Linux client products (which are also free). This allows you to develop applications for single and multi-user environments and distribute them royalty-free when using the Advantage Local Server.

The Windows version of the Advantage Local Server is a DLL named ADSLOC32.DLL. The Linux version of the Advantage Local Server is a shared object named libadsloc.so.

The Advantage Local Server allows both single-user and multiple-user access to data files. The Advantage Local Server file that is installed with Advantage client products contains a physical limitation such that only five or fewer users can concurrently access any table. This limitation was implemented to allow developers the ability to encourage their customers to upgrade to the Advantage Database Server client/server solution when more than five concurrent users were being used so as to reduce data corruption, increase application performance, and reduce support costs. If you wish to have more than five concurrent users accessing data via the Advantage Local Server, inquire about such support with your Advantage Sales representative or Advantage distributor.

Licensing Note If an Advantage application is distributed to work without the Advantage Database Server (i.e., it uses the Advantage Local Server to access data), the application must act as a "client" that directly accesses and uses the data. The application cannot act as "middleware" or as a "server" by having the data forwarded by any means to a separate computer. In other words, it is illegal to use the Advantage Local Server with a Web server, an application server, a terminal server, or any other type of middleware or server product to access data on behalf of remote computers. An Advantage Database Server (a.k.a., remote server) product must be purchased and used to allow an Advantage application to access data on behalf of applications running on remote computers.

See also

[Advantage Local Server Configuration](master_advantage_local_server_configuration.md)

[Benefits of Selecting the Advantage Local Server](master_benefits_of_selecting_the_advantage_local_server.md)

[Limitations of Selecting the Advantage Local Server](master_limitations_of_selecting_the_advantage_local_server.md)

[Advantage Server Types](master_advantage_server_types.md)
