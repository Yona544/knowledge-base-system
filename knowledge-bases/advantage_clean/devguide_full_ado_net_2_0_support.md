---
title: Devguide Full Ado Net 2 0 Support
slug: devguide_full_ado_net_2_0_support
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_full_ado_net_2_0_support.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: aec15845730643865728122b1b348ff4cc829169
---

# Devguide Full Ado Net 2 0 Support

Full ADO.NET 2.0 Support

     Full ADO.NET 2.0 Support

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Full ADO.NET 2.0 Support  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

There are few .NET data providers that fully support the updated ADO.NET framework, and Advantage is one of them. To begin with, the primary Advantage .NET data provider classes descend from the newly introduced base classes, including DbConnection, DbCommand, DbDataAdapter, and so forth. Furthermore, Advantage provides an implementation of the DbFactory class, AdsFactory, which you can use to write more portable code.

Additional ADO.NET features supported by Advantage include support for ambient transactions through the System.Transaction.TransactionScope class. Using a TransactionScope, all subsequent connections to Advantage through the Advantage .NET Database Provider enlist the services of the TransactionScope, which you can then use to commit or roll back updates to your data.

Another new class in the Advantage .NET 2.0 Data Provider is the AdsConnectionStringBuilder. This class provides your code with help building a connection string by exposing properties that map to the connection string parameters. After setting its properties, you can read the correctly formatted connection string from the AdsConnectionStringBuilder's ConnectionString property.

You can also assign a valid connection string to the ConnectionString property, and then read the individual connection parameters from the AdsConnectionStringBuilder's properties.
