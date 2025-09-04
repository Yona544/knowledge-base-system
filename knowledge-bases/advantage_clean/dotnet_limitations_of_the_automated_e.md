---
title: Dotnet Limitations Of The Automated E
slug: dotnet_limitations_of_the_automated_e
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_limitations_of_the_automated_e.htm
source: Advantage CHM
tags:
  - dotnet
checksum: faf7d2fbeeaaef6219784c480156153fdaa6ee4e
---

# Dotnet Limitations Of The Automated E

Limitations of the Automated Entity Framework Tools

Limitations of the Automated Entity Framework Tools

Advantage .NET Data Provider

| Limitations of the Automated Entity Framework Tools  Advantage .NET Data Provider |  |  |  |  |

The Entity Data Model is made of three parts.  The first part is a storage metadata schema, which defines the layout of the data.  The second part is a conceptual schema, which defines the object model used by the application.  Finally, the mapping specification connects the conceptual schema with the storage metadata schema.

The Entity Framework provides a number of automated tools to generate an Entity Data Model from an existing database.  These automated tools read the available schema information from a database and then build a conceptual schema, a storage metadata schema and a mapping specification.  To function properly these automated tools require primary keys to be defined on all tables in the database with a constraint preventing NULL values on primary key fields.  Currently only the Advantage Proprietary (ADS\_ADT) format and the Visual FoxPro (ADS\_VFP) support both primary keys and NULL field constraints when bound to a data dictionary.

For databases that do not meet these requirements, the storage metadata schema can be implemented manually.  Once a storage metadata schema has been defined, edgmen2.exe from Microsoft can be used to generate the conceptual schema and mapping specification.  For information on writing a storage metadata schema see the MSDN.

See Also

[Entity Framework Support](dotnet_entity_framework_support.md)

[Unsupported Entity Framework Functionality](dotnet_unsupported_entity_framework_f.md)
