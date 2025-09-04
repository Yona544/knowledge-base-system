---
title: Devguide Enabling Table Encryption
slug: devguide_enabling_table_encryption
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_enabling_table_encryption.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: c0de16bb0ac8e9da2c58bd5e16f16fa679ce6264
---

# Devguide Enabling Table Encryption

Enabling Table Encryption

     Enabling Table Encryption

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Enabling Table Encryption  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Before you can encrypt the tables of your data dictionary, you must enable table encryption for your database tables and define the encryption password. Use the following steps to enable table encryption for DemoDictionary:

1.        Right-click the DemoDictionary connection in the Connection Repository and select Properties. Select the Security tab to Display the Security page of the of the Data Dictionary dialog box.

| 2. | Enable the Encrypt New Tables checkbox in the Encryption section, as shown in Figure 4-5. |

| 3. | Next, click the Table Encryption Password button to display the Password dialog box. |

| 4. | At New Password, enter password. Click OK when you are done. |

| 5. | Now click OK on the Data Dictionary dialog box to save the data dictionary's properties. |

Figure 4-5: The Security page of the Data Dictionary dialog box

   
NOTE: The table encryption password and your data dictionary administrator's password are independent and serve different purposes. The table encryption password provides the key for encrypting your data. The data dictionary administrator's password provides you with administrative access to the data dictionary. We are using the word password for tables and a blank password for the data dictionary (and also configured the connection properties of the data dictionary to accept a blank password) merely as a convenience, reducing the number of passwords that you have to remember while working with the examples in this book. Typically, you want to use two different passwords for table encryption and administrative access, as well as use passwords that are much more difficult to guess.
