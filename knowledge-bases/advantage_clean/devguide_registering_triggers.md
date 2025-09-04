---
title: Devguide Registering Triggers
slug: devguide_registering_triggers
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_registering_triggers.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 2222387dab8f32ba4b1f6e406c1110dd126e4067
---

# Devguide Registering Triggers

Registering Triggers

     Registering Triggers

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Registering Triggers  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You already registered the two SQL script-based triggers into your data dictionary. Use the following steps to register one of your compiled triggers:

1.        Right-click TriggerTest under the TABLES node and select Triggers.

| 2. | Set Trigger Type to INSTEAD OF, and Event Type to INSERT. |

| 3. | If your trigger container is a Windows DLL or a shared object file, click the Windows DLL or Linux Shared Object tab. Click the browse button to the right of the Container Path and Filename field, and use the displayed Open dialog box to select your trigger library. If you created the Delphi trigger earlier in this chapter, select TriggerD.dll and click Open. Set Function Name in Container to GenGuidID. Your Triggers dialog box should look something like that shown in   Figure 8-6. |

Figure 8-6: Installing a Windows DLL Trigger

4.        If your trigger library is a .NET assembly, click the COM Object or .NET Assembly tab. Click the Browse button to the right of the Program ID (ProgID) field to display the Select ProgID dialog box. Scroll down to locate your registered trigger assembly and then click OK. (Note that the first few pages of the Select ProgID dialog box may contain blank values.). Set Method Name in Class to GenGuidID. Your Triggers dialog box should look something like that shown in Figure 8-7.

| 5. | Leave the first two checkboxes in the Options section checked, meaning that your triggers will have access to the old and new values, and will include memo BLOB data. Uncheck the "Use implicit transactions to maintain data integrity" option. |

| 6. | Click OK to save your trigger. The Advantage Data Architect will respond by displaying the Trigger Name dialog box. Set the trigger name to GenKey and click OK. |

Figure 8-7: Installing a .NET trigger
