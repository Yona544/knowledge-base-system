---
title: Devguide Installing Aeps
slug: devguide_installing_aeps
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_installing_aeps.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 18af3069fb4d2c2256addd94274af974befff1ce
---

# Devguide Installing Aeps

Installing AEPs

     Installing AEPs

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Installing AEPs  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Like all other objects in a data dictionary, you can install stored procedures using a number of techniques. For example, they can be installed using Advantage SQL or direct calls to the ACE (Advantage Client Engine) API. Typically, you use these techniques if you need to install an AEP at runtime.

Most of the time, however, installing an AEP is part of the overall design process of your data dictionary, which means that you do it at design time. In these cases, you install an AEP using the Advantage Data Architect.

Use the following steps to install your AEPs using the Advantage Data Architect:

1.        Right-click the STORED PROCS node in DemoDictionary connection and select Create. The Advantage Data Architect responds by displaying the Stored Procedure dialog box (shown earlier in this chapter in Figure 7-1).

| 2. | Set Name to the name you want to use to refer to your AEP. If you are installing one of the AEPs that you created by following the steps provided earlier in this chapter, set Name to DelphiGet10Percent, CSGet10Percent, or VBGet10Percent, depending on which development tool you used to create the AEP. |

| 3. | In Parameters, set Name to CustID, Type to input, and DataType to integer. |

| 4. | Press the Down Arrow to create a new parameter. Set Name to InvoiceNo, Type to output, DataType to character, and Size to 12. |

| 5. | If you are installing the Delphi AEP container (or any AEP container you created as a standard Windows DLL or shared object library), select the Windows DLL or Linux Share Object tab. If you created your AEP container as a COM server or a .NET class library, select the .NET Assembly or COM Object tab.     Next, you follow either step 6 or step 7. |

| 6. | If you are on the Windows DLL or Linux Share Object pane, set the Advantage Extended Procedure File field to the AEP container filename (AEPDemoD.aep, for example). Most Advantage developers prefer to store their DLLs (or shared object libraries) in the same directory in which they have stored their data dictionary. While this is the recommended approach, you can actually store your DLLs or shared object libraries in any directory on the same share as the data dictionary. If you do store the DLLs or shared object libraries in a directory other than the one in which your data dictionary is stored, we recommend that you refer to the libraries using a UNC (universal naming convention) path, rather than a DOS or Linux path.  Also, enter the name of the stored procedure function in the Stored Procedure Name field (for example, Get10Percent). |

| 7. | If you are on the .NET Assembly or COM Object pane, set Advantage AEP Program ID (ProgID) to the ProgID of the managed assembly or COM server. The ProgID is a value registered under the HKEY\_CLASSES\_ROOT key of the Windows Registry. So long as the COM server or .NET class library has been registered on the machine on which the Advantage Data Architect is running, you can click the Browse button to the right of the Advantage AEP Program ID (ProgID) field to see a list of the registered ProgIDs, as shown in Figure 7-5. Normally, the ProgID for a registered .NET class library is the combination of the .NET project name plus the AEP class name, separated by a period. For example, for the AEPDemoCS project, the ProgID is likely to be AEPDemoCS.aep\_procedures. (If you click the Browse button and your Select ProgID window appears blank, you will need to scroll down one or more pages before the available ProgIDs become visible.)     Also, enter the name of the stored procedure function in the Stored Procedure Name field (for example, Get10Percent). |

Figure 7-5: Select from the list of the registered Program IDs

8.        When you are done, click OK to save the stored procedure object.

| 9. | If your data dictionary requires login and checks user rights, you need to grant execute privileges to each of the groups and users that need to be able to execute the stored procedure. For groups, right-click the node for the group in the data dictionary connection and select Properties. Click the Permissions button, set the combo box to Procedure, and then enable the Execute checkbox for each stored procedure that the group's members need to execute. Click OK to close the Permissions dialog box, and then click OK to close the Group dialog box, saving your new permissions. |

| 10. | For each user who does not belong to a group from which they will inherit the rights to execute your stored procedures, right-click the user's node and select Properties. Click Permissions, select Procedure from the combo box, and then check the Execute checkbox next to each procedure that this user needs to be able to execute. Click OK to close the Permissions dialog box, and click OK once again to close the User dialog box. |

   
CAUTION: You cannot include spaces in either input parameter or output parameter names. If you attempt to define a parameter whose name includes at least one space, the stored procedure object cannot be created.  
 

There are several points that need to be made concerning stored procedures. First, the input and output parameters that you define using the Stored Procedure dialog box are used to define the structures of the \_ \_input and \_ \_output tables that you work with in your stored procedure implementation. In particular, the order of the parameters defines the order of the resulting fields in the \_ \_input and \_ \_output tables. If the access mechanism that you are using references fields by their ordinal position, it is up to you to ensure that the order of the parameters in your stored procedure object definition matches the references you use in your stored procedure code.
