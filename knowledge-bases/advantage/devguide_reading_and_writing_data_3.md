Reading and Writing Data




Advantage Database Server 12  

     Reading and Writing Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Reading and Writing Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Reading and Writing Data Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Reading\_and\_Writing\_Data\_3 Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 18 - The .NET Data Provider > Reading and Writing Data / Dear Support Staff, |  |
| Reading and Writing Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

ADO.NET supports three mechanisms for reading data obtained through a SQL SELECT query. Which mechanism you use depends on how much data you are reading, and what you plan to do with it.

In the simplest case, if you are reading a single value from a table you can call the ExecuteScalar method of an AdsCommand.

The remaining two mechanisms permit you to read multiple fields and multiple records. If you need to be able to refer to multiple rows of data at the same time, you will likely load the data through an AdsDataAdapter into a DataTable. This approach was demonstrated earlier in this chapter in the section on executing a query. In that example, a DataTable was populated and its contents displayed in a DataGrid.

The third mechanism is to use a class that implements the IDataReader interface, and the Advantage .NET Data Provider offers two classes that implement that interface.

The AdsDataReader is a typical ADO.NET data reader implementation. Like other data readers, it provides a forward-only, readonly cursor to a result set. After obtaining an AdsDataReader by calling the ExecuteReader method of an AdsCommand, you call the Read method. If Read returns the value True, the AdsDataReader points to the first record in the result set, after which you call any of the available Get methods, such as GetString, GetBoolean, or GetDate, to read data from that record.

If there are additional records in the result set, calling Read advances the data reader to the next record. Read returns False when there are no remaining records in the result set referred to by the data reader.

The following code segment demonstrates how to read data using an AdsDataReader. This code is associated with the event handler assigned to the Get Address button shown in Figure 18-3:

private void getAddressBtn\_Click(object sender,   
  System.EventArgs e) {  
  AdsCommand getCustCommand;  
  AdsDataReader dataReader;  
  String custNo;  
   
  custNo = custNoText.Text;  
   
  if (custNo.Equals(""))   
  {  
    MessageBox.Show(this, "You must supply a customer ID");  
    return;  
  }  
   
  getCustCommand = new AdsCommand(  
    "SELECT \* FROM CUSTOMER WHERE [Customer ID] = ?",  
    connection);  
  getCustCommand.Parameters.Add(1,System.Data.DbType.Int32);  
  getCustCommand.Parameters[0].Value =   
    Int32.Parse(custNo);  
   
  dataReader = getCustCommand.ExecuteReader();  
  if (dataReader.Read())  
  {  
    oldAddressText.Text =  
      dataReader.GetString  
        (dataReader.GetOrdinal("Address"));  
  }  
  else  
  {  
    MessageBox.Show(this, "Customer " + custNo +   
      " not found");  
  }  
  dataReader.Close();  
}

Most ADO.NET developers write data using SQL queries. These may be invoked directly through an IDbCommand object, or they can be invoked through a properly configured IDbDataAdapter.

As mentioned earlier in this section, Advantage developers have an additional tool for writing data, the AdsExtendedReader. The AdsExtendedReader supports both read and write operations on a live cursor returned by a SQL SELECT statement or from a table opened directly. (Opening a table directly, by setting the AdsCommand's CommandType to TableDirect, permits you to open a table exclusively, so long as the shared=false name/value pair appears in the command's connection string.)

Since the AdsExtendedReader is unique to Advantage, and offers editing capabilities that are unique in the world of ADO.NET, the following example demonstrates how to write to a table using an AdsExtendedReader. For information on writing data using the Update method of a data adapter, refer to the .NET framework documentation.

Actually, using an AdsExtendedReader is almost as simple as using an AdsDataReader. The primary difference is that the AdsExtendedReader has many more methods than the typical data reader. After calling Read, which executes the associated SQL SELECT statement, you can insert records, delete records, read fields, write to fields, set a range, apply a filter, perform a seek, empty the table, or run almost any other operation that you would expect from a server-side cursor.

The following code demonstrates a simple write operation using an AdsExtendedReader. Like the preceding example, an AdsExtendedReader is used to retrieve a single record from the Customer table. Once retrieved, the selected customer's address is changed, and the update is written to the underlying table. This code is associated with the event handler assigned to the Set Address button shown in Figure 18-3.

private void setAddressBtn\_Click(object sender,       
  System.EventArgs e) {  
  AdsCommand getCustCommand;  
  AdsExtendedReader extendedReader;  
  String custNo;  
   
  custNo = custNoText.Text;  
   
  if (custNo.Equals(""))   
  {  
    MessageBox.Show(this, "You must supply a customer ID");  
    return;  
  }     
   
  getCustCommand = new AdsCommand(  
    "SELECT \* FROM CUSTOMER WHERE [Customer ID] = ?",  
    connection);  
  getCustCommand.Parameters.Add(1,System.Data.DbType.Int32);  
  getCustCommand.Parameters[0].Value =   
    Int32.Parse(custNo);  
   
  extendedReader = getCustCommand.ExecuteExtendedReader();  
  if (extendedReader.Read())  
  {  
    extendedReader.SetString(  
      extendedReader.GetOrdinal("Address"),  
      newAddressText.Text);  
    extendedReader.WriteRecord();  
  }  
  else  
  {  
     MessageBox.Show(this, "Customer " + custNo +   
       " not found");  
  }  
  extendedReader.Close();  
}

   
NOTE: Whether you use an AdsDataReader or an AdsExtendedReader, it is very important to call the data reader's Close method when you are done with it. You cannot use the AdsCommand object from which you created the data reader for any other queries until the data reader it returned has been closed.