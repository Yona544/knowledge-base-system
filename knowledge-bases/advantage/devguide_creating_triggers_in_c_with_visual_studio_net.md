Creating Triggers in C# with Visual Studio .NET




Advantage Database Server 12  

     Creating Triggers in C# with Visual Studio .NET

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating Triggers in C# with Visual Studio .NET  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating Triggers in C# with Visual Studio .NET Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_Triggers\_in\_C\_with\_Visual\_Studio\_NET Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 8 - Triggers > Creating Triggers in C# with Visual Studio .NET / Dear Support Staff, |  |
| Creating Triggers in C# with Visual Studio .NET  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

When you create a trigger using C# with Visual Studio .NET, you begin with a template that is automatically installed when you install the Advantage .NET Data Provider.

Creating the Trigger Project

Use the following steps to create a new trigger project in Visual Studio .NET using the trigger template installed with the Advantage .NET Data Provider:

1.        Begin by selecting File | New | Project. Visual Studio responds by displaying the New Project dialog box. In the Project Types tree view, select Visual C# Projects. The available templates are displayed in the Templates pane (Visual Studio 2003) or the Windows pane (Visual Studio 2005), which appears to the right of the Project Types tree view, as shown in Figure 8-4.

Figure 8-4: The New Project dialog box

2.        Select the Advantage Trigger template.

|  |  |
| --- | --- |
| 3. | Set Project Name (VS 2003) or Name (VS 2005) to TriggerCS. |

|  |  |
| --- | --- |
| 4. | Next, use the Browse button to choose the directory to which you want to save this project. |

|  |  |
| --- | --- |
| 5. | Click OK to continue. |

|  |  |
| --- | --- |
| 6. | Your new C# trigger project should now be open in Visual Studio, as shown in Figure 8-5. |

Figure 8-5: The new C# Project in Visual Studio

Renaming the Trigger Method

The trigger project created from the template contains a method named MyFunction that you use as the basis for your trigger. One of the first things you need to do is change the name of this trigger to something that better reflects what the trigger does.

Use the following steps to assign a new name to your trigger:

1.        Locate the MyFunction implementation in the editor.

|  |  |
| --- | --- |
| 2. | Change the name of this method to GenGuidID. |

Writing the Trigger

You are now ready to modify the trigger method and compile your project. Use the following steps:

1.        Modify your trigger method to look like that shown in Listing 8-4.

|  |  |
| --- | --- |
| 2. | When you are done updating the methods, select Build | Build TriggerCS from Visual Studio for .NET's main menu. |

|  |  |
| --- | --- |
| 3. | If the project compiled correctly, set your Solutions Configuration to Release, and select Build | Build TriggerCS again. |

You are now done. Your compiled DLL, named TriggerCS.DLL, will be located in the bin\Release directory under where your project is located.

Listing 8-4

   
CODE DOWNLOAD: This listing is also located in listing8-4.txt with this book's code download (see Appendix A).  
 

public Int32 GenGuidID(Int32 ulConnectionID,  
                       Int32 hConnection,       
                       String strTriggerName,   
                       String strTableName,     
                       Int32 ulEventType,       
                       Int32 ulTriggerType,     
                       Int32 ulRecNo)           
{  
  AdsConnection oConn =   
    new AdsConnection("ConnectionHandle=" +   
    hConnection.ToString());  
  AdsCommand oCommand;  
  AdsCommand oCommandNew;  
  AdsExtendedReader oExtReader;  
  AdsDataReader oDataReader;  
  Guid myGuid = Guid.NewGuid();  
  String s = myGuid.ToString();  
  try  
  {  
    oConn.Open();  
    oCommand = oConn.CreateCommand();  
    oCommandNew = oConn.CreateCommand();  
   
    oCommand.CommandText = "SELECT \* FROM \_\_new";  
    oDataReader = oCommand.ExecuteReader();  
    //Get a cursor to the trigger table  
    oCommandNew.CommandText = "SELECT \* FROM "+  
      "[" + strTableName + "]";  
    oExtReader = oCommandNew.ExecuteExtendedReader();  
   
    //insert new, blank record  
    oExtReader.AppendRecord();  
    oDataReader.Read();  
    if (oDataReader.IsDBNull(0))  
      { oExtReader.SetString(0, s); }  
      else  
      { oExtReader.SetString(0, oDataReader.GetString(0));}  
   
    for (Int16 i = 1;   
       i < oDataReader.FieldCount - 1; ++i)   
      { if (! oDataReader.IsDBNull(i))  
        {  
          oExtReader.SetValue(i, oDataReader.GetValue(i));  
         }  
      }  
   
    oExtReader.WriteRecord();  
    oExtReader.Close();  
    oDataReader.Close();  
  }  
  catch (Exception e)  
  {  
    AdsCommand oErrCommand = oConn.CreateCommand();  
    oErrCommand.CommandText = "INSERT INTO \_\_error " +  
      "VALUES( 0, '" + e.Message + "' )";  
    oErrCommand.ExecuteNonQuery();  
  }  
   
  // Result is currently reserved and not used.   
  //Always return zero.  
  return 0;  
   
}  // GenGuidID

Registering the Trigger

When you compile your project with Visual Studio, it registers your .NET class library in the Windows Registry on your development machine. If your data dictionary is on this same machine you are ready to configure and test your trigger.

If you are running ADS as a remote server, and your data dictionary is on a machine other than the one where you compiled your .NET project, you must install the .NET class library before you can configure the trigger in the data dictionary. The same process must be used if you want to move your trigger executable from the directory to which the Visual Studio compiled it to the directory in which your data dictionary is stored, even if this is on the same machine.

This installation is performed using the regasm.exe utility, which is installed as part of the .NET framework. Since you cannot run the .NET class library without having installed the .NET framework, this utility should be on any machine on which you will run .NET triggers.

   
NOTE: Depending on who is going to use your triggers, and how you are going to distribute them, you may want to sign and strongly name your .NET assemblies. Refer to the .NET Framework SDK (software development kit) for more information on signing and strong names.  
 

The following steps describe how to install your .NET class library:

1.        Copy your .NET class library to the directory in which your data dictionary resides.

|  |  |
| --- | --- |
| 2. | Open a command (CMD.EXE) window and navigate to the directory into which you copied your class library. |

|  |  |
| --- | --- |
| 3. | If regasm.exe is in a directory on your DOS path, you can register your library using a command similar to the following: |

regasm TriggerCS.dll /codebase

   
NOTE: If regasm is not on your DOS path, you can enter the fully qualified path to regasm or execute regasm from the SDK Command Prompt, which automatically includes the framework and SDK directories on the DOS path. The SDK Command Prompt ships with both Visual Studio and the .NET Software Developers Kit.  
 

The use of the /codebase command-line option is required here because you have not installed your trigger assembly in the global assembly cache (GAC). If you did register your .NET assembly in the GAC, you do not have to perform the preceding steps. While storing your class library in the GAC permits you to share it, sharing is really not an advantage in this case. Placing your trigger in the same directory as your data dictionary ensures that you do not introduce version control problems with triggers that are used in more than one data dictionary.

Also, when you use the /codebase command-line option, unless you have signed your compiled library, you will see several lines of messages warning you that you are registering an assembly that is not signed, and that it does not use a strong name. Giving your assembly a strong name and signing it are options that you may want to consider. Those topics, however, are beyond the scope of this book.

   
TIP: You can unregister a .NET class library using the same command line, replacing /codebase with /unregister as the command-line option. In fact, if you must relocate, update, or replace a trigger, it is strongly recommended that you first unregister the old version before registering the updated version. Otherwise you may end up with multiple entries in your Windows Registry.