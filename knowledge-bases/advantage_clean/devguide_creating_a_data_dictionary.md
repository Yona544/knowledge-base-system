---
title: Devguide Creating A Data Dictionary
slug: devguide_creating_a_data_dictionary
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_a_data_dictionary.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 87a36462ec969b2185ac04501f7d3e6a2a417a4d
---

# Devguide Creating A Data Dictionary

Creating a Data Dictionary

 

     Creating a Data Dictionary

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating a Data Dictionary  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Like tables and indexes, data dictionaries can be created at runtime from your client applications. However, most developers will create their data dictionaries at design time as part of their overall database design process. You use the Advantage Data Architect to create data dictionaries at design time.

The following steps demonstrate how to create a data dictionary. This data dictionary will be used in this and future chapters to demonstrate data dictionary features.

Select Connection | Create New Data Dictionary from the Advantage Data Architect main menu. In response, the Advantage Data Architect opens the Data Dictionary dialog box, shown in Figure 4-1. You are only required to provide information for the fields that appear in bold font. However, most developers provide additional information.

Figure 4-1: The Data Dictionary dialog box

At the Name field, enter DemoDictionary. This name is used for the data dictionary files, as well as the corresponding connection that will appear in the Connection Repository.

Set Server Type to Remote Server. This setting instructs the Advantage Data Architect to attempt to connect to this data dictionary using ADS. This setting does not affect how you access your data dictionary from client applications. (Your client application's connection-specific settings control this.) For example, even with Server Type set to Remote Server for this connection, your client applications may use ALS to work with the objects of this data dictionary.

   
NOTE: While different clients can use different server types, Advantage requires all clients simultaneously connected to a data dictionary to be using the same connection method. Trying to mix connection types will produce a 7077 error.  
 

Leave the AdsSys Password and Verify AdsSys Password fields blank. In other words, at least for now, the data dictionary will have a blank password. Having a blank password for a data dictionary is useful during development, permitting you to avoid having to enter a password every time you open a connection to the data dictionary. However, it is very important that you assign a good, strong, and not easily guessable password before you deploy your data dictionary.

At Database, enter the path of the directory where you stored the downloaded sample database tables and code. If you use the directory name suggested in Appendix A, this will be the c:\AdsBook directory. When you complete the creation of the data dictionary, Advantage will actually create three files: DemoDictionary.ADD, DemoDictionary.AI, and DemoDictionary.AM. Only the ADD and AM files should be deployed. ADS will re-create the AI file the first time it accesses the data dictionary. If you were to deploy the AI file, and there are collation sequence differences between the ADS server to which you are deploying and the server against which the ADD file was created, you will have problems.

Leave the Default and Temp directories blank. When blank, the default directory (the directory where tables are created by default) and the temp directory (the directory in which temporary files are stored) will be the same as the directory in which the data dictionary files are stored.

Set Major version to 1 and Minor version to 0. These values, which are optional, are useful if you ever need to detect different versions of your data dictionaries.

Click the Description tab of the Data Dictionary dialog box. In the description field, enter Sample Advantage data dictionary.

Click the Security tab of the Data Dictionary dialog box. Enable the Encrypt Data Dictionary Files checkbox. Encrypting a data dictionary is something that you can do only when you first create it. Leave the remaining options unchecked. We will address the remaining options in the user access and encryption sections later in this chapter.

Click OK to create your new data dictionary and the DemoDictionary connection.

You have now created a new connection in the Connection Repository. This connection, named DemoDictionary, points to your new data dictionary, which is named DemoDictionary.ADD. The Advantage Data Architect should now look similar to the image shown in Figure 4-2.

Figure 4-2: The new connection in the Advantage Data Architect

   
NOTE: Passwords for data dictionaries are case-sensitive. If you attempt to access this data dictionary using the administrative user name, and the Advantage Data Architect reports that your user name and/or password are not correct, check to see if your caps lock key is on.  
 

As you can see in Figure 4-2, the newly created connection is also connected, which means that you can immediately begin adding objects to your data dictionary. Before you do, however, let's discuss data dictionary passwords.

For ease of use, we did not assign a password to this data dictionary. We mentioned in the preceding steps that this was done for convenience --permitting you to use the data dictionary without having to enter a password each time you access it. However, as the DemoDictionary connection is currently configured, it will still nonetheless challenge you for a password each time you attempt to activate the connection.

Use the following steps to demonstrate this:

Close the Advantage Data Architect.

Now, open it again. Since the DemoDictionary was connected when you closed the Advantage Data Architect, it will attempt to reconnect upon loading. However, due to the default connection properties, Advantage Data Architect will challenge you for a password, displaying the following dialog box.

Since there is no password, click OK to continue. The Advantage Data Architect will open the DemoDictionary connection using the blank password.

Blank passwords save you time during development, but it is a waste of time to be asked for a password when one does not exist. What you need to do is to configure the DemoDictionary connection to permit blank passwords. Use the following steps to do this:

Right-click the DemoDictionary connection in the Connection Repository and select Connection Properties.

From the Connection Properties dialog box, set Blank Password to yes, as shown in Figure 4-3.

Click OK to save your new connection settings.

Figure 4-3: Use the Connection Properties dialog box to change the properties of connections in the Connection Repository

When you first create a data dictionary, it contains only a single definitiona user named ADSSYSwhich is the data dictionary administrator's user name. This ADSSYS user name cannot be changed. Defining users and groups is discussed later in this chapter.
