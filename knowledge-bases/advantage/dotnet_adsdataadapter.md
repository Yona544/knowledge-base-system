AdsDataAdapter




Advantage Database Server 12  

AdsDataAdapter

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataAdapter  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataAdapter Advantage .NET Data Provider dotnet\_Adsdataadapter Advantage .NET Data Provider > AdsDataAdapter Class > Overview / Dear Support Staff, |  |
| AdsDataAdapter  Advantage .NET Data Provider |  |  |  |  |

Full Name: Advantage.Data.Provider.AdsDataAdapter

Implements: System.Data.IDbDataAdapter, System.Data.IDataAdapter

Inherits: System.Data.Common.DbDataAdapter

[Constructors](dotnet_adsdataadapter_constructors.htm)

[Properties](dotnet_adsdataadapter_properties.htm)

[Methods](dotnet_adsdataadapter_methods.htm)

[Events](dotnet_adsdataadapter_events.htm)

An AdsDataAdapter object represents a set of data commands and a database connection that are used to fill a DataSet and update an Advantage database.

The AdsDataAdapter serves as a bridge between a DataSet and Advantage Database Server or Advantage Local Serer for retrieving and saving data. The AdsDataAdapter provides this bridge by mapping Fill, which changes the data in the DataSet to match the data in the data source, and Update, which changes the data in the data source to match the data in the DataSet, using the appropriate Advantage SQL statements against the data source.

The AdsDataAdapter also includes the [SelectCommand](dotnet_adsdataadapter_selectcommand.htm), [InsertCommand](dotnet_adsdataadapter_insertcommand.htm), [DeleteCommand](dotnet_adsdataadapter_deletecommand.htm), [UpdateCommand](dotnet_adsdataadapter_updatecommand.htm), and [TableMappings](dotnet_adsdataadapter_tablemappings.htm) properties to facilitate the loading and updating of data. You can use [AdsCommandBuilder](dotnet_adscommandbuilder.htm) to fill in these properties automatically for Advantage SQL statements that produce live cursors. For static cursors, it is necessary to set these properties explicitly.

Example

The following example shows how the UpdateCommand might be assigned to handle updating a static cursor that is the result of a left outer join. The InsertCommand and DeleteCommand could be assigned similarly.

AdsConnection conn = new AdsConnection( "data source = c:\\data" );

conn.Open();

 

// create a data adapter that results in a static cursor (cannot

// use AdsCommandBuilder in this case)

AdsDataAdapter da = new AdsDataAdapter( "select e.[employee number], " +

"e.[first name], e.[last name], e.salary, d.[department name] " +

"from employee e left outer join departments d on " +

"d.[department code] = e.[department code]", conn );

 

// create an update command that will handle updates to the

// employee portion of the result set.

da.UpdateCommand = new AdsCommand( "", conn );

da.UpdateCommand.CommandText = "update employee set " +

"[Employee Number] = :EmployeeNumber, " +

"[First Name] = :FirstName, " +

"[Last Name] = :LastName, " +

"[Salary] = :Salary " +

"where [Employee Number] = :EmpNumOrig";

 

 

// create the necessary parameters to map columns in the

// result set to the UPDATE statement.

da.UpdateCommand.Parameters.Add( "EmployeeNumber", DbType.Int32, -1,

"Employee Number" );

da.UpdateCommand.Parameters.Add( "FirstName", DbType.String, -1,

"First Name" );

da.UpdateCommand.Parameters.Add( "LastName", DbType.String, -1,

"Last Name" );

da.UpdateCommand.Parameters.Add( "Salary", DbType.Double, -1,

"Salary" );

 

// get the reference to this one - need to change the source version

// in order to specify the correct row for where clause (in case

// employee number is changed)

AdsParameter param;

param = da.UpdateCommand.Parameters.Add( "EmpNumOrig", DbType.Int32,

-1, "Employee Number" );

param.SourceVersion = DataRowVersion.Original;

 

 

DataSet ds = new DataSet();

 

da.Fill( ds, "test" );

 

// give someone a raise

double salary = (double)ds.Tables["test"].Rows[0]["Salary"];

salary \*= 1.05;

ds.Tables["test"].Rows[0]["Salary"] = salary;

 

// perform other update to the dataset

 

// send the update(s) to the server

da.Update( ds, "test" );

 

da.Dispose();

conn.Close();