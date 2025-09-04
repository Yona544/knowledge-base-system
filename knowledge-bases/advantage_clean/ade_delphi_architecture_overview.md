---
title: Ade Delphi Architecture Overview
slug: ade_delphi_architecture_overview
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_delphi_architecture_overview.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 8b49f9cd75f6cad4132c77d935066c3ca8fe65d4
---

# Ade Delphi Architecture Overview

Delphi Architecture Overview

Architecture Overview

Advantage TDataSet Descendant

| Architecture Overview  Advantage TDataSet Descendant |  |  |  |  |

The concepts, terminology, and examples documented in this Help file were developed based on the assumption that the reader has a basic understanding of database theory. This includes understanding concepts such as databases, tables, and indexes. It is also assumed that the reader has previously developed a database application. For information on all these topics in relation to Delphi, see the Delphi Help documentation Developing Database Applications as well as the sample database applications included with your Delphi development kit.

Database Applications

When developing database applications using Delphi (also applicable to C++Builder), you have most likely used the Delphi data access components and the Delphi data-aware components. The data access components appear on the Data Access page of the Component Palette within Delphi. Some examples of the components are TTable, TQuery, TDataSource, and TDatabase. The data-aware components appear on the Data Controls component page. Examples of these components include DBGrid, DBEdit, and DBMemo. The components on the Data Access page encapsulate all data retrieval and manipulation. The components on the Data Controls page provide functionality to visually display and edit data such as edit boxes and grids.

Delphi Data Access Components

The most commonly used Data access components are TTable, TQuery, and TDataSet. The TTable and TQuery Delphi components are data providers. The TTable component is a descendant of the TDataSet component and provides all functionality associated with a database table. The database table exists on a hard drive. Program access and table manipulation is performed by the TTable component. The TQuery component is also a descendant of the TDataSet component. It encapsulates a result set based on an SQL query. All reads and writes to the database are handled by the TQuery component.

In Windows, both the TTable component and the TQuery component traditionally employ the Borland Database Engine (BDE). The BDE is the native server for many Borland products such as dBASE, Delphi, and C++Builder. It is the database engine that handles all of the low-level database request routines. The TTable and TQuery components traditionally use the BDE to gain access to the actual data or data server. When using native Delphi components, the data can reside in a file, such as a dBASE style DBF file or a Paradox DB file, or can be provided by a third-party database server product such as Oracle or InterBase.

Delphi Data Control Components

The set of Delphi components that provide a visual presentation of data are the data-aware components. These components appear on the Data Controls page of the Component Palette and retrieve data by making requests to a TDataSet component. Some of these commonly used components are TDBGrid, TDBMemo, and TDBImage, TDBEdit. For example, the TDBGrid component displays the data from the TDataSet in a two dimensional grid. It allows the user to visually navigate and edit the data within the grid.

When utilizing data-aware controls, your TDataSet component must be associated with a TDataSource component. The TDataSource component references the TDataSet and provides an interface to the TDataSet that data-aware components use to retrieve their data. The data-aware components are limited to using only the database functionality exposed by TDataSet through this interface. Many methods of TTable and TQuery such as TTable.ApplyRange and TQuery.ExecSQL are not accessible via this interface and are therefore never accessed by any Delphi data-aware components.

To summarize, the data-aware components such as TDBGrid and TDBEdit link to a TDataSource. The TDataSource component provides an interface to a particular TDataSet component. The TDataSet component is an abstract component that provides functionality used to access data. The TTable or TQuery components descend from the abstract TDataSet component. These components are concrete. They provide all functionality that the abstract ancestor components require. The native TTable and the TQuery components encapsulate all database functionality as far as the Delphi environment is concerned, but use the BDE to actually retrieve the data.
