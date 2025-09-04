---
title: Master Task 6 Register Your Procedure In The Data Dictionary
slug: master_task_6_register_your_procedure_in_the_data_dictionary
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_task_6_register_your_procedure_in_the_data_dictionary.htm
source: Advantage CHM
tags:
  - master
checksum: 14b5c5ab280de92fe99e9b0634d6751db0907697
---

# Master Task 6 Register Your Procedure In The Data Dictionary

Task 6: Register Your Procedure in the Data Dictionary

Task 6: Register Your Procedure in the Data Dictionary

Advantage Concepts

| Task 6: Register Your Procedure in the Data Dictionary  Advantage Concepts |  |  |  |  |

Now that we have our AEP written its time to register our procedure in the data dictionary. Start the Advantage Data Architect (ARC).

| 1. | Select Open Database from the Database menu. |

| 2. | WINDOWS USERS: Type X:\data\aep\_tutorial.add in the Database Name edit box. |

LINUX USERS: Type ~/data/aep\_tutorial.add in the Database Name edit box.

| 3. | Click OK. |

Note If you receive a 7077 error at this point, it is because we have written this AEP to use local server connections (which we left open in the Delphi IDE), and you also have Advantage Database Server running on the machine your X: drive is mapped to. ARC is attempting a remote server connection, and if the tables are also opened by local server this open will fail with the 7077 error. To resolve this issue either unload the Advantage Database Server, or go back to your data module and add the ttAds\_Remote option to both TAdsConnection components AdsServerTypes property.

| 4. | When prompted for a login, click OK again. |

| 5. | Right-click the Stored Procedures icon in the tree view and select Add. |

| 6. | Enter all required information for the stored procedure. |

| 7. | Click OK to save the new procedure definition. |
