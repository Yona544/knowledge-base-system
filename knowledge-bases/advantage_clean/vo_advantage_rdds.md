---
title: Vo Advantage Rdds
slug: vo_advantage_rdds
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_advantage_rdds.htm
source: Advantage CHM
tags:
  - vo
checksum: 3cc24fd561cd89a94f6cc5b568639e73e7872ce4
---

# Vo Advantage Rdds

Advantage RDDs

Advantage RDDs

Advantage Visual Objects and Vulcan.NET RDD

| Advantage RDDs  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Visual Objects and Vulcan.NET provide an interface through which "back-end" engines can be accessed. This interface access is supported through Replaceable Database Drivers (RDDs).

Eight Advantage RDDs are provided to work with Visual Objects and Vulcan.NET: two for accessing NTX indexes (AXDBFNTX & AXSQLNTX) two for accessing CDX indexes (AXDBFCDX & AXSQLCDX) two for the Advantage proprietary file format (ADSADT & AXSQLADT) and two for the Visual FoxPro file format (AXDBFVFP & AXSQLVFP).

RDDs are responsible for data storage and retrieval in your Visual Objects or Vulcan.NET application. In order for the RDDs to respond to requests made by your application, the requests are transferred across the network to the file server. The file server retrieves the raw data and returns it to the client workstation for processing.

Advantage, however, is built on the client/sever model and moves much of the processing from the client to the Advantage server. This reduces network traffic and increases performance while offering a higher level of data integrity.

[Advantage RDDs](vo_creating_your_application_with_the_advantage_libraries.md) are easily used in Visual Objects or Vulcan.NET applications. First, you need to reference the Advantage RDD in your application. Visual Objects or Vulcan.NET will then automatically send commands to be processed to the referenced RDD. Second, if you require advanced Advantage functionality such as [Advantage Transaction Processing](master_transaction_processing_system.md), you will need to use an additional Advantage library, DBFAXS. This library must be imported into the Visual Objects repository or added to your Vulcan.NET project to be used in your application. Third, if you wish to access the Advantage Client Engine functionality in your Visual Objects application, you will need to add the Advantage Client Engine library to your applications properties.  In Vulcan.NET, the Advantage Client Engine library is included in the AdvantageRDD assembly.

The Advantage RDDs listed below are provided to support the following file formats:

| Advantage RDD | Table Type | Index Type | Memo Type |
| AXDBFNTX / AXSQLNTX | DBF | NTX | DBT |
| AXDBFCDX / AXSQLCDX | DBF | CDX/IDX | FPT |
| ADSADT / AXSQLADT | ADT | ADI | ADM |
| AXDBFVFP / AXSQLVFP | DBF | CDX/IDX | FPT |
