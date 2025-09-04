---
title: Arc Creating Or Modifying A Package
slug: arc_creating_or_modifying_a_package
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_creating_or_modifying_a_package.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 8dd58f8798185ff4a8bb5e07ee929fa6c859be47
---

# Arc Creating Or Modifying A Package

Creating or Modifying a Package

Creating or Modifying a Package

Advantage Data Architect

| Creating or Modifying a Package  Advantage Data Architect |  |  |  |  |

Packages allow developers to create independent name spaces for UDFs. The Connection Repository will allow you to add packages to your database.

To create or modify a package, open a database. See [Opening a Database](arc_opening_a_database2.md) for details. You must be logged into the database as a user with the CREATE PACKAGE or ALTER permission to add or modify packages.

To add a new package, from the tree view within the Connection Repository, right-click the FUNCTION icon and select Create Package.

To modify a package, from the tree view within the Connection Repository, right-click on the package and select Properties.

Package Field Descriptions

Name (required)

Enter the name for the package. This will be the name space for all UDFs in the package.

OK

Click OK to add the package to the database. If you are modifying an existing package, clicking OK alters the package.

Cancel

Cancels the current operation and exits the screen.

See Also

[Deleting a Package](arc_deleting_a_package.md)
