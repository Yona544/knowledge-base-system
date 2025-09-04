---
title: Devguide Defining Server Side Aliases
slug: devguide_defining_server_side_aliases
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_defining_server_side_aliases.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: ed8328abe68f66728caa1b426a574ef144b4ad95
---

# Devguide Defining Server Side Aliases

Defining Server-Side Aliases

     Defining Server-Side Aliases

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Defining Server-Side Aliases  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Server-side aliases are defined in an INI file named AdsServer.ini. This file needs to be placed on the server in the same directory used for the error log file. See "The Error Table" section earlier in this appendix for steps on how to locate this directory.

AdsServer.ini is not created for you automatically. If you want to use server-side aliases, you have to create this file using an editor, such as NotePad.exe or emacs.

Within AdsServer.ini, you define your server-side aliases in a section named ServerAliases. Within this section, you can define one or more name/value pairs, where the name is the server-side alias and the value is either a local drive path or UNC (Universal Naming Convention) path. In many instances, you will include the full path for the data dictionary or free tables, though a partial path is also acceptable.

Here is a sample of what an AdsServer.ini file might look like:

[ServerAliases]  
demopath=share\AdsBook  
restorepath=c:\adsdata\restore

From your client application, you include the alias as part of your connection string. For example, consider the partial C# code for connecting to the server using the Advantage Data Provider for .NET:

public void InitializeDataComponent()  
{  
  dataPath = "\\\\dataserver\\share\\AdsBook\\" +  
    "\\DemoDictionary.add";  
  connection1 = new AdsConnection("Data Source=" +   
    dataPath + ";user ID=adsuser;password=password;"+  
    "ServerType= REMOTE | LOCAL;" +  
    "FilterOptions=RESPECT\_WHEN\_COUNTING;" +  
    "TrimTrailingSpaces=True");  
  connection1.Open();

Given the server-side alias named demopath shown earlier, you can change the dataPath variable to the following:

public void InitializeDataComponent()  
{  
  dataPath = "\\\\dataserver\\demopath\\DemoDictionary.add";  
  connection1 = new AdsConnection("Data Source="+   
    dataPath + ";user ID=adsuser;password=password;"+  
    "ServerType= REMOTE | LOCAL;" +  
    "FilterOptions=RESPECT\_WHEN\_COUNTING;" +  
    "TrimTrailingSpaces=True");  
  connection1.Open();

When ADS reads the demopath part of the connection string, it replaces it with share\AdsBook before continuing.
