Creating AEPs Using Delphi




Advantage Database Server 12  

     Creating AEPs Using Delphi

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating AEPs Using Delphi  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating AEPs Using Delphi Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_AEPs\_Using\_Delphi Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 7 - Stored Procedures > Creating AEPs Using Delphi / Dear Support Staff, |  |
| Creating AEPs Using Delphi  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You create a Windows DLL when you create an AEP in Delphi using the template provided. This template is installed when you install the Advantage TDataSet Descendant. This template is also available when you install the TDataSet Descendant for C++Builder or the TDataSet Descendant for Kylix. With Kylix, however, the template will create a shared object library.

   
NOTE: The extension of this DLL or shared object library will be .aep.  
 

Creating the AEP Project

You can use the following steps to create an AEP using Delphi:

1.        In Delphi, select File | New | Other to display the Object Repository (similar to that shown in Figure 7-2).

|  |  |
| --- | --- |
| 2. | From Delphi versions 3-7, click Projects to view the Project templates page of the Object Repository. From Delphi 2005 or Delphi 2006, select Delphi Projects. |

Figure 7-2: The Advantage Extended Procedure template shown in Delphi 2006

3.        Select the Advantage Extended Procedure as shown in Figure 7-2, and click OK. When prompted, use the displayed browser to select a directory in which this project will be stored.

The copied template is now your current project in Delphi.

   
NOTE: The steps given here for creating AEPs using Delphi are also applicable to Kylix. For C++Builder, the steps are similar, and the object properties and methods are the same, but you need to write the code in C++ instead of the Delphi language.  
 

Saving the Project Using a New Name

When you use a project template, you are using an exact copy of a project that was installed in your Object Repository. If you were to create another AEP, it would have exactly the same project name, and this could lead to confusion. Consequently, one of your first tasks should be to rename the project. To do this:

Select File | Save Project As from the main menu.

Save the project using the name AEPDemoD.dpr.

Changing the Stored Procedure Function Name

Initially the AEP template includes one stored procedure named MyProcedure. You should change the name of this procedure to something meaningful. In this case, the new procedure name will be Get10Percent. This must be done in two places in the .DPR file as described here:

1.        Search the AEPDemoD.dpr file for the line that begins function MyProcedure.

|  |  |
| --- | --- |
| 2. | Change the name of the function from MyProcedure to Get10Percent. |

|  |  |
| --- | --- |
| 3. | Locate the exports clause at the end of this unit. Change the entry for MyProcedure to Get10Percent. |

Writing the Stored Procedure

You are now ready to update the Get10Percent function and compile your project. Use the following steps:

Locate the beginning of the Get10Percent function in AEPDemoD.dpr.

Modify this procedure to look like that shown in Listing 7-2.

When you are done updating the procedure, select Project | Compile AEPDemoD.dpr from the main menu.

You are now done. Your compiled DLL, named AEPDemoD.aep, will be located in the directory where you saved your AEP project. While it is not required that you do so, we recommend that you set your output directory to the same directory where your DemoDictionary data dictionary is stored. That way, a new copy of the DLL will be written to this directory each time you compile, and it will also make debugging easier, if necessary.

Listing 7-2

   
CODE DOWNLOAD: This listing is also located in listing7-2.txt located on this book's code download (see Appendix A).  
 

function Get10Percent( ulConnectionID: UNSIGNED32;  
                      hConnection: ADSHANDLE;  
                      pulNumRowsAffected: PUNSIGNED32 ):  
                      UNSIGNED32;  
                      {$IFDEF WIN32}stdcall;{$ENDIF}  
                      {$IFDEF LINUX}cdecl;{$ENDIF}  
var  
   DM1 : TDM1;  
   InvoiceTable: TAdsTable;  
   Counter: Integer;  
   CustID: Integer;  
begin  
   
   Result := AE\_SUCCESS;  
   
   {\* Get this connection's data module from   
    the session manager. \*}  
   DM1 := TDM1( AEPSessionMgr.GetDM( ulConnectionID ) );  
   try  
      with DM1 do  
      begin  
        InvoiceTable := TAdsTable.Create(nil);  
        try  
          //Get customer's invoices  
          InvoiceTable.AdsConnection := DM1.DataConn;  
          InvoiceTable.TableName := 'invoice';  
          InvoiceTable.Open;  
          InvoiceTable.IndexName := 'customer ID';  
          tblInput.open;  
          CustID := tblInput.Fields[0].AsInteger;  
          InvoiceTable.SetRange([CustID], [CustID]);  
          tblInput.Close;  
   
          //Write 10 percent of customer IDs to output  
          tblOutput.Open;  
          InvoiceTable.First;  
          Counter := 0;  
          repeat  
            inc(Counter);  
            if Counter = 10 then  
            begin  
              Counter := 0;  
              tblOutput.Append;  
              tblOutput.Fields[0].Value :=  
                InvoiceTable.Fields[0].Value;  
              tblOutput.Post;  
            end;  
            InvoiceTable.Next;  
          until InvoiceTable.Eof;  
   
          //Generate error if no records  
          if tblOutput.IsEmpty then  
            begin  
              DataConn.Execute( 'INSERT INTO \_\_error '+  
                'VALUES ( 2500, ' +  
                QuotedStr( 'There are less than 10 ' +   
                'records for ' +  
                IntToStr(CustID) ) + ' )' );  
              Exit;  
            end;  
          pulNumRowsAffected^ := tblOutput.RecordCount;  
        finally  
          InvoiceTable.Free;  
          tblOutput.Close;  
        end;  
      end;   {\* with DM1 \*}  
   
   except  
      on E : EADSDatabaseError do  
         {\* ADS-specific error, use ACE error code \*}  
         DM1.DataConn.Execute( 'INSERT INTO \_\_error '+   
           'VALUES ( ' + IntToStr( E.ACEErrorCode ) +   
           ', ' + QuotedStr( E.Message ) + ' )' );  
      on E : Exception do  
         {\* other error \*}  
         DM1.DataConn.Execute( 'INSERT INTO \_\_error '+  
          'VALUES ( 1, ' + QuotedStr( E.Message ) + ' )' );  
   end;  
end;

If you wanted to create additional stored procedure functions in this AEP container, you would make one or more copies of the original MyProcedure function. You would then change the names of these functions so that they are unique in the project, and then add these names to your exports clause.