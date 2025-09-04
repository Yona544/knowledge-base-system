Limitations of the Automated Entity Framework Tools




Advantage Database Server 12  

Limitations of the Automated Entity Framework Tools

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Limitations of the Automated Entity Framework Tools  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - Limitations of the Automated Entity Framework Tools Advantage .NET Data Provider dotnet\_Limitations\_of\_the\_Automated\_E Advantage .NET Data Provider > Entity Framework Support > Limitations of the Automated Entity Framework Tools / Dear Support Staff, |  |
| Limitations of the Automated Entity Framework Tools  Advantage .NET Data Provider |  |  |  |  |

The Entity Data Model is made of three parts.  The first part is a storage metadata schema, which defines the layout of the data.  The second part is a conceptual schema, which defines the object model used by the application.  Finally, the mapping specification connects the conceptual schema with the storage metadata schema.

The Entity Framework provides a number of automated tools to generate an Entity Data Model from an existing database.  These automated tools read the available schema information from a database and then build a conceptual schema, a storage metadata schema and a mapping specification.  To function properly these automated tools require primary keys to be defined on all tables in the database with a constraint preventing NULL values on primary key fields.  Currently only the Advantage Proprietary (ADS\_ADT) format and the Visual FoxPro (ADS\_VFP) support both primary keys and NULL field constraints when bound to a data dictionary.

For databases that do not meet these requirements, the storage metadata schema can be implemented manually.  Once a storage metadata schema has been defined, edgmen2.exe from Microsoft can be used to generate the conceptual schema and mapping specification.  For information on writing a storage metadata schema see the MSDN.

See Also

[Entity Framework Support](dotnet_entity_framework_support.htm)

[Unsupported Entity Framework Functionality](dotnet_unsupported_entity_framework_f.htm)