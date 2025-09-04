Executing a Query




Advantage Database Server 12  

     Executing a Query

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Executing a Query  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Executing a Query Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Executing\_a\_Query\_3 Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 18 - The .NET Data Provider > Executing a Query / Dear Support Staff, |  |
| Executing a Query  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You execute a query that returns a result set using an AdsCommand. There are numerous overloaded methods for doing this. The following code segment demonstrates one of these, where a query string and an open connection are passed as parameters to an AdsDataAdapter's constructor. Within this constructor, the query string is assigned to an internally created AdsCommand object that is associated with the SelectCommand property of the AdsDataAdapter, which performs the query execution. The Fill method is then invoked on this AdsDataAdapter, which causes the result set to be loaded into a DataTable of a DataSet.

This DataTable is then used to display the resulting data in a DataGrid, as shown in Figure 18-4. The following code demonstrates the execution of a query entered by the user into the TextBox named selectText. This method is associated with the Execute SELECT button which is shown earlier in Figure 18-3:

private void executeSELECTBtn\_Click(object sender,   
  System.EventArgs e) {  
  IDataAdapter adapter ;  
  adapter = new AdsDataAdapter(selectText.Text, connection);  
  DataSet ds = new DataSet();  
  adapter.Fill(ds);  
  DataTable dt = ds.Tables[0];  
  dataGrid1.DataSource = dt;  
}

Figure 18-4: The results of a SELECT query displayed in a data grid

Notice that the AdsDataAdapter that is created is assigned to a variable of type IDataAdapter. IDataAdapter is the interface that all data adapters implement. While we could have just as well assigned this object to a variable of type AdsDataAdapter, assigning it to an interface variable makes our code more portable, since any IDataAdapter implementing class can be assigned to this variable. This technique is used in this chapter, whenever no Advantage .NET Data Provider functionality is specifically needed. When we need a feature specific to an AdsDataAdapter, our variable is of that class type.

If you need to execute a query that does not return a record set, call the ExecuteNonQuery method of an AdsCommand object. The use of an AdsCommand object to execute a query that does not return a recordset is demonstrated later in this chapter.