---
title: Error 5020 Ae Invalid Path
slug: error_5020_ae_invalid_path
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5020_ae_invalid_path.htm
source: Advantage CHM
tags:
  - error
checksum: 3ec2ca0e5e81edddab1a6d210b44200155839b47
---

# Error 5020 Ae Invalid Path

5020 AE\_INVALID\_PATH

5020 AE\_INVALID\_PATH

Advantage Error Guide

| 5020 AE\_INVALID\_PATH  Advantage Error Guide |  |  |  |  |

Problem 1: The path given was not valid.

Solution 1: Specify a valid path.

 

Problem 2: This error can occur when trying to CREATE or EXECUTE an Advantage Extended Procedure on a Windows 9x/ME client. The error occurs while attempting to load the DLL that is stored on a Novell server when the name of the DLL file is longer than the 8.3 format.

Solution 2: Change the name of the DLL file to fit the 8.3 format.

 

Problem 3: This error can occur while trying to CREATE or EXECUTE an Advantage Extended Procedure when ACE32.DLL and AXCWS32.DLL are not in the Advantage Database Server's path.

Solution 3: Put ACE32.DLL and AXCWS32.DLL, and any other needed files, in Advantage Database Server's path.

 

Problem 4: This error can occur when the connection to the Advantage Data Dictionary was made using a local-drive-letter path and the table or index being added to the dictionary is not on the same drive. Advantage stores the file path of the table relative to the data dictionary file in the data dictionary. If the file path of the table cannot be converted to a relative path, this error is returned.

Solution 4a: Connect to the Advantage Data Dictionary using UNC file path and use UNC to specify the table to be added into the data dictionary.

Solution 4b: Move the table or index to the same hard drive as the Advantage Data Dictionary before adding them to the Advantage Data Dictionary.
