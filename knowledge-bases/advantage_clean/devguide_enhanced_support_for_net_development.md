---
title: Devguide Enhanced Support For Net Development
slug: devguide_enhanced_support_for_net_development
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_enhanced_support_for_net_development.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: d6f9fe124a3e417b28c31b04e049b52676004c68
---

# Devguide Enhanced Support For Net Development

Enhanced Support for .NET Development

     Enhanced Support for .NET Development

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Enhanced Support for .NET Development  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Advantage 8 now includes support for ADO.NET 2.0, in addition to the ADO.NET 1.1 support found in version 7. In both the .NET 1.1 and 2.0 versions, the AdsExtendedReader has been improved, providing methods for detecting record and table locks, as well as a property that you can use to determine the relative record position for the currently selected index. In the 8.1 release, the Advantage .NET Data Provider also includes methods for obtaining additional information about the active index.

Many additional updates are available in the ADO.NET 2.0 Advantage .NET Data Provider. For example, the Advantage .NET Data Provider for Advantage 8 now includes the AdsHelper class. The AdsHelper class provides the same convenience as that provided to MS SQL Server developers through the Microsoft Data Access Application Block for .NET 2.0, simplifying the process of using parameterized queries and stored procedures, populating DataSets, and generating DataReaders.

Consistent with the native .NET data providers in the 2.0 framework, the Advantage .NET Data Provider for ADO.NET 2.0 includes data factory support through the AdsFactory class. This class permits you to write more portable code, which is useful if your client applications must support multiple databases.

Also consistent with the native 2.0 data access classes, classes in the Advantage .NET Data Provider for ADO.NET 2.0 descend from abstract base data access classes supplied in the System.Data.Common namespace. Like the data factory, these base classes permit their descendants, such as AdsConnection and AdsCommand, to be used polymorphically, again permitting you to write more portable code.

Finally, Advantage now supports ambient transactions through the System.Transaction.TransactionScope class. Once you create a TransactionScope, all subsequent connections to Advantage through the Advantage .NET Database Provider enlist the services of the TransactionScope, which you can then use to commit or roll back updates to your data.
