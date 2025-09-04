Connecting to Data




Advantage Database Server 12  

     Connecting to Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Connecting to Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Connecting to Data Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Connecting\_to\_Data Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 15 - Using Advantage from Delphi > Connecting to Data / Dear Support Staff, |  |
| Connecting to Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You connect to a data dictionary or a directory in which free tables are located using an AdsConnection component. AdsConnection is very similar to the VCL's Database component, located on the BDE page of the Tool Palette. At a minimum, you must set a property of this AdsConnection component to describe where the data dictionary or free tables are located, after which you set the IsConnected property to True (or call the Connect method). If you are connecting to a data dictionary that requires a login, and you do not want the user to have to enter their user name, you must also set the Username and Password properties of this component.

There are two ways to indicate the location of your data. The easiest way, if you have a connection defined for your data dictionary or free table directory, is to set the Alias name property of the AdsConnection to a defined connection. Connections are defined in the ADS.INI file, which can be stored in the same directory as your client application (under Windows), or anywhere on your search path. (When you use the Advantage Data Architect, the ADS.INI file is stored in the Windows directory by default.)

Alternatively, you can set the ConnectPath of the AdsConnection to a path, preferably a UNC path (which can include an IP address if Advantage is installed on a machine with a fixed IP address). The benefit of using an ADS.INI file is that you can change the directory in which Advantage looks for your data by changing an entry in the ADS.INI file. By comparison, if your data directory is hard-coded in your application, changing your data directory involves recompiling and redistributing your client application.

   
TIP: Some developers who do not want to use the ADS.INI file assign the ConnectPath property of the AdsConnection object at runtime, assigning to it a directory relative to the application's directory. You can obtain the application's directory path by calling the ExtractFilePath function, passing Application.ExeName to it.  
 

If you set the IsConnected property of the AdsConnection to True at design time, and a user name and password are supplied (if necessary), you will have an active connection within the Delphi IDE, and the connection will be reestablished at runtime once the AdsConnection is created and initialized (given that the StoredConnected property is set to True). If IsConnected is set to False at design time, the AdsConnection component will establish a connection at runtime once either the IsConnected property is explicitly set to True or any TDataSets that use the AdsConnection attempt to open or execute.

If you set the Username and Password properties prior to connecting an AdsConnection, set the LoginPrompt property to False. If LoginPrompt is True, the user will be prompted for their user name and password.

   
TIP: If LoginPrompt is set to True, but no login dialog box is displayed, you must add the DBLogDlg unit to your unit's uses clause.  
 

In the Delphi\_TDataSet project, the Alias property of the AdsConnection is set to DemoDictionary (the connection name you defined for the DemoDictionary data dictionary in Chapter 4), the user name is set to adsuser, the password is set to password, and the LoginPrompt is set to False. With these settings in place, you will not be prompted for a user name or password when connecting to the data dictionary.

   
NOTE: If you have difficulty connecting, it might be because you have other client applications, such as the Advantage Data Architect, connected using a local connection. Ensure that all clients connecting to the database use the same type of connection. You control the type of connections attempted by an AdsConnection using the AdsServerTypes property.