Create an Entity Model




Advantage Database Server 12  

Create an Entity Model

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Create an Entity Model  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - Create an Entity Model Advantage .NET Data Provider dotnet\_Create\_an\_Entity\_Model Advantage .NET Data Provider > Entity Framework Support > Entity Framework Quick Start > Create an Entity Model / Dear Support Staff, |  |
| Create an Entity Model  Advantage .NET Data Provider |  |  |  |  |

Create the Entity Data Model

The Entity Data Model (EDM) is a set of entity to table mappings used to map data from tables to objects.

|  |  |
| --- | --- |
| 1. | Start Visual Studio 2008 and create a new C# Windows Forms Application with a project name of EFDemo. |

|  |  |
| --- | --- |
| 2. | In the Solution Explorer select the EFDemo project, right-click, and then select Add | New Item |

|  |  |
| --- | --- |
| 3. | Select ADO.NET Entity Data Model in Templates. |

If you do not see ADO.NET Entity Data Model as a template option, you will need to install .NET 3.5 SP1 or newer. You also need to verify that the project you created is targeting .NET version 3.5 or newer. To check this, go to Project | <ProjectName> Properties | Application Tab | Target Framework

|  |  |
| --- | --- |
| 4. | For the Name enter EFDemo.edmx |

|  |  |
| --- | --- |
| 5. | Click Add. |

|  |  |
| --- | --- |
| 6. | When the Entity Data Model wizard appears, select Generate from database and click Next. |

|  |  |
| --- | --- |
| 7. | A new connection to the database will need to be created, click New Connection. |

|  |  |
| --- | --- |
| 8. | In the Connection Properties dialog, click the Change button. |

|  |  |
| --- | --- |
| 9. | Select Advantage Database Server and click OK. |

|  |  |
| --- | --- |
| 10. | For (Data Source) enter c:\example\EFDemo.add. |

|  |  |
| --- | --- |
| 11. | For UserID enter AdsSys. |

|  |  |
| --- | --- |
| 12. | For TrimTrailingSpace select True. |

|  |  |
| --- | --- |
| 13. | If you do not have the Advantage Database Server running on your development PC, then set the ServerType property to LOCAL. |

|  |  |
| --- | --- |
| 14. | Click OK. |

|  |  |
| --- | --- |
| 15. | Ensure that Save entity connection settings in App.Config as: is checked and set the value to EFDemoEntities. |

|  |  |
| --- | --- |
| 16. | Select Next. |

|  |  |
| --- | --- |
| 17. | Ensure that all tables are selected and the click Finish to complete the wizard. |

The entity data model of the example database has been created and will be displayed.

See Also

[Entity Framework Quick Start Overview](dotnet_entity_quick_start_overview.htm)

[Create the sample database](dotnet_create_sample_database.htm)

[Display Records using LINQ](dotnet_display_records_using_linq.htm)