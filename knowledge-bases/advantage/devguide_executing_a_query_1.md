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
| Executing a Query  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Executing a Query Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Executing\_a\_Query\_1 Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 16 - Advantage and Java > Executing a Query / Dear Support Staff, |  |
| Executing a Query  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You can execute a query against ADS by calling any one of a number of methods of a java.sql.Statement instance, including execute, executeQuery, and executeUpdate. The execute method returns True if the statement returns a result, False if it does not, and throws an exception if the statement fails. The execute method is best when you do not know ahead of time if the statement returns a result set. Call executeQuery when you know that a result set will be returned, and executeUpdate when you know that one will not be returned.

The following event handler demonstrates the execution of a query that returns a result set. This event handler is associated with the Execute SELECT button (shown in Figure 16-1):

void executeSelect\_actionPerformed(ActionEvent e) {  
  try {  
    ResultSet rs = stmt.executeQuery(selectText.getText());  
    if (isRSEmpty(rs)) {  
      JOptionPane.showMessageDialog(this,  
       "No records in result set");  
      return;  
    }  
    jTable1.setModel(new ResultTableModel(rs));  
  }  
  catch (Exception e1) {  
    System.err.println( e1.getMessage());  
  }  
}

Since this is the first event handler from this project that we've inspected, there are two characteristics that need to be introducedspecifically, the isRSEmpty method and the use of the ResultTableModel class. Both of these are declared in the MainFrame.java file.

The isRSEmpty method is called by many of the event handlers in this application to determine whether or not there are records in the ResultSet returned by executeQuery. This method was added to the MainFrame class declaration as a public static method. The following is the implementation of this method:

public static boolean isRSEmpty(ResultSet rs) {  
  try {  
    return ! rs.first();  
  }  
  catch (Exception e1) {  
    System.err.println( e1.getMessage());  
    return false;  
  }  
}

The second item of interest is the class ResultTableModel. This class extends the abstract class AbstractTableModel, and it is used to create a model that can be used by the JTable class to display the contents of the result set. (Java swing classes employ a model-view architecture. The view is supplied by the visual component, and the model is responsible for handling the data.) At a minimum, ResultTableModel must override getColumnCount, getRowCount, and getValueAt. In this case, getColumnName is also overridden.

The following code implements the ResultTableModel class:

class ResultTableModel  
  extends javax.swing.table.AbstractTableModel {  
  Object obj [] [];  
  int rows, columns;  
  ResultSetMetaData rsMeta;  
   
  public ResultTableModel (ResultSet rs) {  
    try {  
      if (rs == null) {  
        rows = 0;  
        columns = 0;  
        obj = new Object[0][0];  
        return;  
      }  
      rsMeta = rs.getMetaData();  
      //get column count  
      columns = rsMeta.getColumnCount();  
      //calculate number of rows  
      rows = 0;  
      rs.first();  
      do {  
        rows++;  
      } while (rs.next());  
      //set array dimension  
      obj = new Object [rows][columns];  
      //load data  
      rs.first();  
      rows = 0;  
      do {  
        for (int j = 0; j <= (columns-1); j++) {  
          obj[rows][j] = rs.getString(j+1);  
        }  
        rows++;  
      } while (rs.next());  
    } catch (Exception e1) {  
    System.out.println(e1.getMessage());  
    }  
  }  
   
    public int getColumnCount() {  
          return columns;  
    }  
   
      public int getRowCount() {  
          return rows;  
      }  
   
      public String getColumnName(int col)  {  
        String res = "";  
        if (rsMeta == null) {  
          return res;  
        }  
        try {  
          res = rsMeta.getColumnName(col+1);  
        }  
        catch (Exception e1) {  
          System.out.println(e1.getMessage());  
        }  
        return res;  
      }  
   
      public Object getValueAt(int row, int col) {  
          return obj[row][col];  
      }  
} //ResultTableModel class

As you can see in this code, the constructor of ResultTableModel is passed the ResultSet. This ResultSet is used to obtain a ResultSetMetaData object, which is then used to determine the number of columns in the ResultSet. This ResultSetMetaData object is also used to obtain the column names from within the getColumnName method.

Next, the ResultSet is navigated in order to count how many records the ResultSet contains. Finally, a two-dimensional array of Object is declared and populated with the rows and columns of the ResultSet.

Admittedly, this code is somewhat inefficient, in that it necessitates the retrieval of all of the records in the ResultSet, which is a time-consuming task when many records are involved. Consequently, this is not the type of TableModel that would be appropriate for every application. But for this sample Java project, it works just fine.

ResultTableModel is used to populate the JTable instance, a grid control that appears in the JFrame. Figure 16-2 shows this JTable populated with the results of a SQL SELECT statement.

Figure 16-2: The JTable obtains its data from ResultTableModel