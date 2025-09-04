Creating Triggers in VB.NET with Visual Studio .NET




Advantage Database Server 12  

     Creating Triggers in VB.NET with Visual Studio .NET

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating Triggers in VB.NET with Visual Studio .NET  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating Triggers in VB.NET with Visual Studio .NET Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_Triggers\_in\_VB\_NET\_with\_Visual\_Studio\_NET Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 8 - Triggers > Creating Triggers in VB.NET with Visual Studio .NET / Dear Support Staff, |  |
| Creating Triggers in VB.NET with Visual Studio .NET  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You create triggers in VB.NET using the same steps as outlined in the earlier section "Creating Triggers in C# with Visual Studio .NET." There are only two differences:

•        When the New Project dialog box is displayed, set Project Name (VS 2003) or Name (VS 2005) to TriggerVB instead of TriggerCS.

|  |  |
| --- | --- |
| • | Your trigger method is implemented in VB for .NET instead of C#. |

Modify your trigger method to look like the code shown in Listing 8-5:

Listing 8-5

   
CODE DOWNLOAD: This listing is also located in listing8-5.txt with this book's code download (see Appendix A).  
 

Public Function GenGuidId(ByVal ulConnectionID As Int32, \_  
                          ByVal hConnection As Int32, \_  
                          ByVal strTriggerName As String, \_  
                          ByVal strTableName As String, \_  
                          ByVal ulEventType As Int32, \_  
                          ByVal ulTriggerType As Int32, \_  
                          ByVal ulRecNo As Int32) As Int32   
'Do not change prototype  
Dim Conn As AdsConnection  
Dim Command As AdsCommand  
Dim CommandNew As AdsCommand  
Dim ExtReader As AdsExtendedReader  
Dim DataReader As AdsDataReader  
Dim MyGuid As Guid  
Dim S As String  
   
Try  
  Conn = New AdsConnection("ConnectionHandle=" & \_  
    hConnection)  
  Conn.Open()  
  Command = Conn.CreateCommand  
  CommandNew = Conn.CreateCommand  
   
  Command.CommandText = "SELECT \* FROM \_\_new"  
  DataReader = Command.ExecuteReader  
  'Get a cursor to the trigger table  
  CommandNew.CommandText = "SELECT \* FROM " + \_  
    "[" + strTableName + "]"     
  ExtReader = CommandNew.ExecuteExtendedReader  
   
  'Insert new blank record  
  ExtReader.AppendRecord  
  'Get the GUID  
  MyGuid = Guid.NewGuid  
  S = MyGuid.ToString  
  'read from \_\_new  
  DataReader.Read  
  If (DataReader.IsDBNull(0)) Then  
    ExtReader.SetString(0, S)  
  Else  
    ExtReader.SetString(0, DataReader.GetString(0))  
  End If  
   
  'load remaining data  
  For i As Int16 = 1 To DataReader.FieldCount - 1  
    If Not DataReader.IsDBNull(i) Then  
      ExtReader.SetValue(i, DataReader.GetValue(i))  
    End If  
  Next i  
   
  ExtReader.WriteRecord  
  ExtReader.Close  
  DataReader.Close  
Catch Ex As Exception  
  Dim ErrCommand As IDbCommand  
   
  ' Handle any exceptions here  
  ErrCommand = Conn.CreateCommand  
  ErrCommand.CommandText = "INSERT INTO \_\_error " + \_  
    "VALUES( 0, " & Ex.Message & "' )"  
  ErrCommand.ExecuteNonQuery()  
Finally  
  ' Always return zero.  
  GenGuidId = 0  
End Try  
End Function  'GenGuidId