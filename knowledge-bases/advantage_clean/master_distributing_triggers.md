---
title: Master Distributing Triggers
slug: master_distributing_triggers
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_distributing_triggers.htm
source: Advantage CHM
tags:
  - master
checksum: d6b2a02028ab3fa96799d591e3186927242551ac
---

# Master Distributing Triggers

Distributing Triggers

Distributing Triggers

Advantage Concepts

| Distributing Triggers  Advantage Concepts |  |  |  |  |

Script triggers are stored inside the database and require no extra distribution efforts.

Other trigger containers need to be distributed along with the database (the .add file).

WIN32 DLLs and Linux shared objects should be distributed with the .add file. Place them on the disk using the same relative path as when they were registered.

COM containers and .NET Assemblies can be installed anywhere on the server machine. These containers must be registered using either regsvr32.exe (for COM containers) or regasm (for .NET assemblies). See the documentation that came with your development environment for registration details.
