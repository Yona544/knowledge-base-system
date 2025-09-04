---
title: Devguide Creating Aeps Using C With Visual Studio Net
slug: devguide_creating_aeps_using_c_with_visual_studio_net
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_aeps_using_c_with_visual_studio_net.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 83d9aa7db19010ff897ecdaa731d19ab8d7b98a9
---

# Devguide Creating Aeps Using C With Visual Studio Net

Creating AEPs Using C# with Visual Studio .NET

     Creating AEPs Using C# with Visual Studio .NET

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating AEPs Using C# with Visual Studio .NET  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

When you create an AEP using C# with Visual Studio .NET, you begin with a template that is installed when you install the Advantage .NET Data Provider. You'll see how to do this next.

   
CODE DOWNLOAD: A sample template for Delphi for .NET is available on the code download (see Appendix A).  
 

Creating the AEP Project

Use the following steps to create a new AEP project in Visual Studio using the AEP template:

Begin by selecting File | New | Project. Visual Studio responds by displaying the New Project dialog box. In the Project Types tree view, select Visual C# Projects. The available templates are displayed in the Templates pane (Visual Studio 2003) or the Windows pane (Visual Studio 2005), which appears to the right of the Project Types tree view, as shown in Figure 7-3.

Figure 7-3: The Advantage AEP in Visual Studio 2005

Select the Advantage AEP template.

Set Project Name (2003) or Name (2005) to AEPDemoCS.

Next, use the Browse button to choose the directory in which you want to save this project.

Click OK to continue.

Your new C# AEP project should now be open in Visual Studio, as shown in Figure 7-4.

Figure 7-4: The new C# Project in Visual Studio

Renaming the Stored Procedure

Like with the templates used to create AEPs in Delphi, the AEP template for C# creates a project that contains one stored procedure named MyProcedure. The following steps show you how to rename this procedure:

1.        Locate the public method MyProcedure in the public aep\_procedures class.

| 2. | Change the name of the method from MyProcedure to Get10Percent. |

   
NOTE: It is not necessary to change the name of the aep\_procedures class, although you can do so if you like. Since the aep\_procedures class is declared in the namespace associated with your project, it will be unique from any other aep\_procedures classes that you create for other .NET AEPs, so long as they are defined in different namespaces. In Visual Studio, the project name defines the namespace, which is AEPDemoCS in this case.  
 

Writing the Stored Procedure

You are now ready to update and compile your AEP project as a .NET class library. Use the following steps:

1.        Locate the Get10Percent method in the aep\_procedures class.

| 2. | Modify this method to look like that shown in Listing 7-3. |

| 3. | Select Build | Build AEPDemoCS. |

Once you build, the file AEPDemoCS.dll will appear in the debug or release directory of your project's directory.

Listing 7-3

   
CODE DOWNLOAD: This listing is also located in listing7-3.txt, located on this book's code download (see Appendix A).  
 

public Int32 Get10Percent( Int32 ulConnectionID,  
  Int32 hConnection,  
  ref Int32 ulNumRowsAffected )  
{  
  StateInfo         oStateInfo;  
  IDbCommand      oCommand;  
  IDataReader   oReader;  
   
  AdsDataAdapter Adapter;  
  DataSet DS;  
  DataTable Table;  
  Int32  custID;  
  Int32 counter;  
  Boolean oneOrMoreRows;  
   
  lock( colClientInfo )  
    oStateInfo = (StateInfo)(colClientInfo[ulConnectionID]);  
   
  try  
  {       
    oCommand = oStateInfo.DataConn.CreateCommand();  
    oCommand.CommandText = "SELECT \* FROM \_\_input";  
    oReader = oCommand.ExecuteReader();  
    oReader.Read();  
    custID = oReader.GetInt32(0);  
    //Close DataReader before connection can be reused  
    oReader.Close();  
   
    oCommand = oStateInfo.DataConn.CreateCommand();  
    DS = new DataSet();  
    Adapter = new AdsDataAdapter(  
      "SELECT [Invoice No] FROM INVOICE " +  
      "WHERE [Customer ID] = " + custID.ToString(),  
      oStateInfo.DataConn);   
    Adapter.Fill(DS, "INVOICES");  
    Table = DS.Tables["INVOICES"];  
     
    counter = 0;  
    oneOrMoreRows = false;  
    for (int i = 0; i<= (Table.Rows.Count-1)  ; i++)  
    {  
      counter++;  
      if (counter == 10)   
      {  
        oCommand.CommandText =   
          "INSERT INTO \_\_output  VALUES ('"  
          + Table.Rows[i].ItemArray[0].ToString() + "')";  
        oCommand.ExecuteNonQuery();  
        counter = 0;  
        oneOrMoreRows = true;  
      }  
    }  
   
    if (! oneOrMoreRows)   
    {         
      oCommand.CommandText = "INSERT INTO \_\_error " +  
        "VALUES( 2500, 'Less than 10 records for "+  
        custID.ToString()+"' )";  
      oCommand.ExecuteNonQuery();  
    }  
  }   
  catch( Exception e )  
  {  
    IDbCommand  oErrCommand =   
      oStateInfo.DataConn.CreateCommand();  
    oErrCommand.CommandText = "INSERT INTO \_\_error "+  
      "VALUES( 1, '" + e.Message + "' )";  
    oErrCommand.ExecuteNonQuery();  
  }  
   
  return 0;  
   
}   // Get10Percent

Registering the Stored Procedure

When you compile your project with Visual Studio, it registers your .NET class library in the Windows Registry on your development machine. If your data dictionary is on this same machine, you are ready to install and test your AEP.

If you are running ADS as a remote server, and your data dictionary is on a machine other than the one where you compiled your .NET project, you must install the .NET class library before you can register the AEP in the data dictionary. This installation is performed using the regasm.exe utility, which is installed as part of the .NET framework. Since you cannot run the .NET class library without having installed the .NET framework, this utility should be on any machine on which you will run .NET AEPs.

   
NOTE: Depending on who is going to use your AEPs, and how you are going to distribute them, you may want to sign and strongly name your .NET assemblies. Refer to the .NET Framework SDK (software development kit) for more information on signing and strong names.  
 

The following steps describe how to install your .NET class library:

Copy your .NET class library to the directory in which your data dictionary resides.

Open a command (CMD.EXE) window and navigate to the directory into which you copied your class library.

If regasm.exe is in a directory on your DOS path, you can register your library using a command similar to the following:

regasm AEPDemoCS.dll /codebase

If regasm is not on your DOS path, you must enter the fully qualified path to regasm. (If you do not know where regasm.exe is stored, use the Windows Explorer's searching capabilities to find it.) The command might look something like the following:

c:\Windows\Microsoft.NET\Framework\v1.1.4322\regasm  
AEPDemoCS.dll /codebase

 for .NET 1.1, or the following for .NET 2.0:

C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\regasm  
AEPDemoCS.dll /codebase

   
NOTE: The preceding command-line entries must be entered as a single command (in one line). It appears on two lines here because of the limited line space in this book.  
 

The use of the /codebase command-line option is required here because you have not stored your AEP class library in the GAC (global assembly cache). If you did register your .NET executable in the GAC, you do not have to perform the preceding steps. While storing your class library in the GAC permits you to share it, sharing is really not an advantage in this case. Placing your AEP in the same directory as your data dictionary ensures that you do not introduce version control problems with AEPs that are used in more than one data dictionary.

Also, when you use the /codebase command-line option, unless you have signed your compiled library, you will see several message lines warning you that you are registering an assembly that is not signed, and that does not use a strong name. Giving your assembly a strong name and signing it are options you might want to consider. Those topics, however, are beyond the scope of this book. For information on strongly named and signed assemblies, refer to the online documentation in Visual Studio .NET.

   
TIP: You can unregister a .NET class library using the same command line, replacing /codebase with /unregister as the command-line option. In fact, if you must update or replace an AEP container, it is strongly recommended that you first unregister the old version before registering the updated version. Otherwise, you may get multiple ProgID entries in your Windows Registry.
