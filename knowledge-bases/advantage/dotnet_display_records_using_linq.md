Display Records using LINQ




Advantage Database Server 12  

Display Records using LINQ

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Display Records using LINQ  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - Display Records using LINQ Advantage .NET Data Provider dotnet\_Display\_Records\_using\_LINQ Advantage .NET Data Provider > Entity Framework Support > Entity Framework Quick Start > Display Records using LINQ / Dear Support Staff, |  |
| Display Records using LINQ  Advantage .NET Data Provider |  |  |  |  |

Display Database Records using LINQ

The following task will display the Customers table in a GridView.

|  |  |
| --- | --- |
| 1. | Select Data | Show Data Sources. |

|  |  |
| --- | --- |
| 2. | Click Add New Data Source in the Data Sources window. |

|  |  |
| --- | --- |
| 3. | Select Object click Next. |

|  |  |
| --- | --- |
| 4. | Expand EFDemo and select Customers and click Finish. |

|  |  |
| --- | --- |
| 5. | Double-click Form1.cs from the Solution Explorer Window. |

|  |  |
| --- | --- |
| 6. | Drag the Customers object from the Data Sources window and drop it on Form1. |

|  |  |
| --- | --- |
| 7. | Double click Form1 to open the code editor. |

|  |  |
| --- | --- |
| 8. | In the Load event of the forum add the following code: |

// Create an ObjectContext instance based on EFDemo.EFDemoEntities  
           var ADSEntities = new EFDemo.EFDemoEntities();  
   
           // Retrieve the list of customers using LINQ  
           var customers = from c in ADSEntities.Customers  
                           orderby c.City  
                           select c;  
   
           // Bind the customers object to the data grid  
           customersBindingSource.DataSource = customers;

9.  Run the project by pressing F5.  The form will contain the customers information ordered by city.

 

Additional Resources and Tutorials

[Microsoft MSDN Entity Framework Getting Started Guide](http://msdn.microsoft.com/en-us/library/bb386876.aspx)

[Microsoft Entity Framework Quickstart](http://msdn.microsoft.com/en-us/library/bb399182.aspx)

See Also

[Entity Framework Quick Start Overview](dotnet_entity_quick_start_overview.htm)

[Create the sample database](dotnet_create_sample_database.htm)

[Create the Entity Data Model](dotnet_create_an_entity_model.htm)