---
title: Master Task 4 Register Your Trigger In The Database
slug: master_task_4_register_your_trigger_in_the_database
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_task_4_register_your_trigger_in_the_database.htm
source: Advantage CHM
tags:
  - master
checksum: f98910ee5013f3821712545ae35bc1ab4b2cfb08
---

# Master Task 4 Register Your Trigger In The Database

Task 4: Register Your Trigger in the Database

Task 4: Register Your Trigger in the Database

Advantage Concepts

| Task 4: Register Your Trigger in the Database  Advantage Concepts |  |  |  |  |

The final step in trigger creation is to register your trigger with the database.

| 1. | Open ARC. |

| 2. | Select Database -> Open Database from the main menu. |

| 3. | Enter "c:\data\trig\_tutorial.add" as the database name. |

| 4. | Set the Advantage Connection Type to local or remote (depending on which server type you are using). |

| 5. | Click the Open button. |

| 6. | Click the OK button at the login prompt. |

| 7. | Expand the tables tree item. |

| 8. | Expand the orders table tree item. |

| 9. | Highlight the triggers tree item. |

| 10. | Set the Trigger Type to AFTER. |

Take the appropriate steps below depending on your development environment:

Borland Delphi/Kylix

| 1. | Select the Windows DLL or Linux Shared Object tab. |

| 2. | Enter "c:\data\AdsTrigs.dll" as the Container Path and Filename. |

| 3. | Enter "MyFunction" as the Function Name. |

| 4. | Click the Save button. |

| 5. | Enter "t1" as the trigger name. |

| 6. | Click the OK button. |

Microsoft Visual Studio .NET

| 1. | Select the COM Object or .NET Assembly tab. |

| 2. | Enter "AdsTrigs.trig\_functions" as the Program ID. |

| 3. | Enter "MyFunction" as the Function Name. |

| 4. | Click the Save button. |

| 5. | Enter "t1" as the trigger name. |

| 6. | Click the OK button. |
