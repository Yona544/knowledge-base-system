Known Problems




Advantage Database Server 12  

Known Problems

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Known Problems  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - Known Problems Advantage .NET Data Provider dotnet\_Known\_problems Advantage .NET Data Provider > Introduction > Known Problems / Dear Support Staff, |  |
| Known Problems  Advantage .NET Data Provider |  |  |  |  |

When creating table adapter objects for linked tables (e.g., drag and drop a table from the Visual Studio Server Explorer onto a DataSet), the link name is not included in the generated UPDATE, DELETE, and INSERT statements. In order to use the generated statements, you must add the link name to the table in the SQL statements. For example, change [mytable] to mylink].[mytable]

When creating table adapter objects for stored procedures (e.g., drag and drop a stored procedure from the Visual Studio Server Explorer onto a DataSet), the data types for the input parameters are not generated correctly. All of the parameter types are set to type System.Object. The data provider will infer the type from the data. However, if there is any ambiguity, it might be best to specifically set the parameter type by editing the input parameters collection for the table adapter Fill Query.