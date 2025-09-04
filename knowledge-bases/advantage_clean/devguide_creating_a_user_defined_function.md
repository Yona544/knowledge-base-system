---
title: Devguide Creating A User Defined Function
slug: devguide_creating_a_user_defined_function
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_a_user_defined_function.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 02e8dfad923ff18bd0ef90c46bfa89c3baee1681
---

# Devguide Creating A User Defined Function

Creating a User Defined Function

     Creating a User Defined Function

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating a User Defined Function  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You can create user defined functions either by calling the CREATE FUNCTION SQL statement or interactively using the Advantage Data Architect. Since user defined functions are typically created at design time, you will most likely create your user defined functions with the Advantage Data Architect.

You create a function in a package by right-clicking the package in which you want the function to appear and selecting Create Function. If you want to create a stand-alone function (one without a package), right-click the FUNCTION node of the data dictionary and select Create Function.

Use the following statements to create the RandomRange function in the Math package:

1.        From your active and connected DemoDictionary connection, right-click the Math package node under the FUNCTION node and select Create Function. The Advantage Data Architect responds by displaying the Function dialog box, shown in Figure 13-2.

| 2. | At Name at the top of the dialog box, enter RandomRange. |

| 3. | In the Parameters section, change the DataType of ReturnValue to integer. |

| 4. | Click the + button to the right of Parameters to add a new parameter. The new parameter will be inserted in the top position in the Parameters section. |

| 5. | Set Name to StartRange, type to input, and DataType to integer. |

| 6. | Move your cursor to the ReturnValue parameter and click the + button again. |

Figure 13-2: The Function dialog box

7.        The new parameter is inserted above ReturnValue and below StartRange. Set Name to EndRange, Type to input, and DataType to integer.

| 8. | In the SQL pane, enter the following three lines of code: |

DECLARE Range Integer;  
Range = (EndRange - StartRange) + 1;  
RETURN (RAND() \* Range) + StartRange;

9.        Your user defined function should now look something like that shown in Figure 13-3. Click OK to close the Function dialog box and save your new user defined function.

Figure 13-3: The Function dialog box and the RandomRange function

   
NOTE: This function could have contained a single line of code. This line would look like the following  
RETURN (RAND() \* (EndRange StartRange 1)) + StartRange  
We used three lines in this example to make the function more readable.
