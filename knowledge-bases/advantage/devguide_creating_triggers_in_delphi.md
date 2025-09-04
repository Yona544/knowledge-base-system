Creating Triggers in Delphi




Advantage Database Server 12  

     Creating Triggers in Delphi

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating Triggers in Delphi  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating Triggers in Delphi Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_Triggers\_in\_Delphi Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 8 - Triggers > Creating Triggers in Delphi / Dear Support Staff, |  |
| Creating Triggers in Delphi  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You create a Windows DLL when you create a trigger project in Delphi using the template provided by Advantage. This template is installed when you install the Advantage TDataSet Descendant. Templates are also available when you install the TDataSet Descendant for C++Builder and for Kylix. With Kylix, however, the template will create a shared object library.

Creating the Trigger Project

Use the following steps to create a trigger:

Select File | New | Other from Delphi's main menu to display the Object Repository shown in Figure 8-3.

Select the Advantage tab (in Delphi versions 3-7) or the Delphi Projects tab (in Delphi 2005 or Delphi 2006) from the Object Repository.

Figure 8-3: The Object Repository in Delphi

Select the Advantage Trigger template and click OK. When prompted, save this project to a directory where you want to store the source files.

Saving the Project Using a New Name

Delphi projects created from a project template are an exact copy of an existing project that has been added to the Object Repository. In case you ever plan to create more than one trigger project, it is a good idea to rename this project to something that is unique. The following steps show you how:

1.        From Delphi's main menu, select File | Save Project As.

|  |  |
| --- | --- |
| 2. | Using the Save dialog box, set File Name to TriggerD. |

|  |  |
| --- | --- |
| 3. | Click Save. |

Renaming the Trigger Function

The trigger project created from the template contains a function named MyFunction that you use as the basis for your trigger. Change the name of this trigger to something that better reflects what the trigger does. You must also change the exports clause, updating the name of the trigger function that appears there initially.

Use the following steps to change the name of MyFunction:

1.        Locate the MyFunction implementation in the editor.

|  |  |
| --- | --- |
| 2. | Change the name of this function to GenGuidID. |

|  |  |
| --- | --- |
| 3. | Locate the exports clause and change MyFunction to GenGuidID. Your complete exports clause will look something like the following: |

exports  
  GenGuidID;

Writing the Trigger Function

You are now ready to modify the trigger function and compile your project. Use the following steps:

Modify your trigger function to look like that shown in Listing 8-3.

When you are done updating the function, select Project | Compile TriggerD.dpr from the main menu.

You are now done. Your compiled DLL, named TriggerD.DLL, will be located in the directory where you saved your trigger project. While it is not required that you do so, we recommend that you copy TriggerD.DLL to the same directory where your DemoDictionary data dictionary is stored.

Listing 8-3

   
CODE DOWNLOAD: This listing is also located in listing8-3.txt on this book's code download (see Appendix A).  
 

function GenGuidID  
(  
  ulConnectionID : UNSIGNED32;  
  hConnection    : ADSHANDLE;  
   
  pcTriggerName  : PChar;  
  pcTableName    : PChar;  
  ulEventType    : UNSIGNED32;  
  ulTriggerType  : UNSIGNED32;  
  ulRecNo        : UNSIGNED32  
) : UNSIGNED32;  
{$IFDEF WIN32}stdcall;{$ENDIF}  
{$IFDEF LINUX}cdecl;{$ENDIF}  
var  
  //This variable was in the original template  
  oConn  : TAdsConnection;  
   
  //These variables were added  
  oTable: TAdsTable;  
  oNewTable: TAdsTable;  
  GUID1 : TGUID;  
  GUIDStr: String;  
  i: Integer;  
   
begin  
  Result := 0;  
   
  //This code was part of the original template  
  oConn := TAdsConnection.CreateWithHandle( nil,  
    hConnection);  
   
  //This table will point to the table  
  //to which the trigger is assigned  
  oTable := TAdsTable.Create(nil);  
   
  //This table will point to the  
  //single record that is being inserted data  
  oNewTable := TAdsTable.Create(nil);  
   
  try  
    try  
   
      //Hook up both AdsTables to the connection  
      //that was passed to the trigger  
      oTable.AdsConnection := oConn;  
      oNewTable.AdsConnection := oConn;  
   
      //Hook the AdsTables to the  
      //appropriate underlying table  
      oNewTable.TableName := '\_\_new';  
      oTable.TableName := pcTableName;  
   
      //Open the tables  
      oTable.Open;  
      oNewTable.Open;  
   
      //Add a new record to the table to which  
      //the trigger is assigned. This new  
      //record will be the 'inserted' record.  
      oTable.Append;  
   
      //Generate a GUID as a string  
      if CreateGUID(GUID1) = 0 then  
        GUIDStr := GUIDToString(GUID1);  
   
      //If the first field has not already been assigned  
      //a value, insert the GUID string  
      if (oNewTable.Fields[0].AsString = '') or  
         (oNewTable.Fields[0].IsNull) then  
        oTable.Fields[0].AsString := GUIDStr  
      else  
        oTable.Fields[0].Value := oNewTable.Fields[0].Value;  
   
      //Now iterate through the remaining fields  
      //and insert the data. Only do this   
      //for non-null fields  
      for i := 1 to Pred(oTable.FieldCount) do  
        if not oNewTable.Fields[i].IsNull then  
          oTable.Fields[i].Value :=   
            oNewTable.Fields[i].Value;  
   
      //Post the data.  
      oTable.Post;  
   
      //All done. Goto the finally clause and clean-up.  
    except  
      on E : EADSDatabaseError do  
        SetError( oConn, E.ACEErrorCode, E.message );  
      on E : Exception do  
        SetError( oConn, 0, E.message );  
    end;  
   
  finally  
    //Close and free the tables.  
    //Also free the connection object  
    oTable.Close;  
    oNewTable.Close;  
    oConn.Free;  
    oTable.Free;  
    oNewTable.Free;  
  end;  
end;