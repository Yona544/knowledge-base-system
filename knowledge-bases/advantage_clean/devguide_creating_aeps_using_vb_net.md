---
title: Devguide Creating Aeps Using Vb Net
slug: devguide_creating_aeps_using_vb_net
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_aeps_using_vb_net.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: f2447df4e405da8266b34e6733fb9ad97e58ee9a
---

# Devguide Creating Aeps Using Vb Net

Creating AEPs Using VB.NET

     Creating AEPs Using VB.NET

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating AEPs Using VB.NET  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You create an AEP using VB for .NET using the same steps as outlined in the previous section "Creating AEPs Using C# with Visual Studio .NET." There are only two differences:

•        When the New Project dialog box is displayed, set Project Name or Name to AEPDemoVB7 instead of AEPDemoCS.

| • | Your AEP is implemented in VB.NET instead of C#. Implement your Get10Percent method using the code shown in Listing 7-4. |

Listing 7-4

   
CODE DOWNLOAD: This listing is also located in listing7-4.txt, located with this book's code download (see Appendix A).  
 

Public Function Get10Percent(ByVal ulConnectionID \_  
  As Int32, \_  
  ByVal hConnection As Int32, \_  
  ByRef ulNumRowsAffected As Int32) As Int32  
   
  Dim oStateInfo As StateInfo  
  Dim oCommand As IDbCommand  
  Dim oReader As IDataReader  
  Dim Adapter As AdsDataAdapter  
  Dim DS As DataSet  
  Dim Table As DataTable  
  Dim custID As Int32  
  Dim Counter As Int32  
  Dim oneOrMoreRows As Boolean  
  Try  
    ' Get this client's state information   
    'before doing anything  
    SyncLock colClientInfo  
      oStateInfo = colClientInfo.Item(CStr(ulConnectionID))  
    End SyncLock  
   
    ' Create command object to use  
    oCommand = oStateInfo.DataConnection.CreateCommand  
    oCommand.CommandText = "SELECT \* FROM \_\_input"  
    oReader = oCommand.ExecuteReader  
    oReader.Read()  
    custID = oReader.GetInt32(0)  
    'Close DataReader before connection can be reused  
    oReader.Close()  
   
    oCommand = oStateInfo.DataConnection.CreateCommand  
    DS = New DataSet  
    Adapter = New AdsDataAdapter( \_  
      "SELECT [Invoice No] FROM invoice " + \_  
      "WHERE [Customer ID] = " + custID.ToString(), \_  
      oStateInfo.DataConnection)  
    Adapter.Fill(DS, "invoices")  
    Table = DS.Tables("invoices")  
   
    Counter = 0  
    oneOrMoreRows = False  
    Dim i As Int32  
    For i = 0 To (Table.Rows.Count - 1)  
      Counter = Counter + 1  
      If Counter = 10 Then  
        oCommand.CommandText = \_  
          "INSERT INTO \_\_output  VALUES ('" + \_  
          Table.Rows(i).ItemArray(0).ToString() + "')"  
        oCommand.ExecuteNonQuery()  
        Counter = 0  
        oneOrMoreRows = True  
      End If  
    Next  
   
    If Not oneOrMoreRows Then  
      oCommand.CommandText = "INSERT INTO \_\_error " + \_  
        "VALUES( 2500, 'Less than 10 records for " + \_  
        "custID.ToString + "')"  
      oCommand.ExecuteNonQuery()  
    End If  
   
  Catch Ex As Exception  
    Dim oErrCommand As IDbCommand  
    oErrCommand = oStateInfo.DataConnection.CreateCommand  
    oErrCommand.CommandText = "INSERT INTO \_\_error " + \_  
      "VALUES( 1, '" + Ex.Message + "' )"  
    oErrCommand.ExecuteNonQuery()  
  Finally  
    Get10Percent = 0  
  End Try  
   
  End Function 'Get10Percent
