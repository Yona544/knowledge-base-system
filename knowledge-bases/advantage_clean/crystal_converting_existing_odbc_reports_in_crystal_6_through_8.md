---
title: Crystal Converting Existing Odbc Reports In Crystal 6 Through 8
slug: crystal_converting_existing_odbc_reports_in_crystal_6_through_8
product: Advantage Database Server
component: Crystal Reports
version: "12"
category: API
original_path_html: crystal_converting_existing_odbc_reports_in_crystal_6_through_8.htm
source: Advantage CHM
tags:
  - crystal
  - crystal-reports
checksum: 080121074f16d87265a7903c858e0c7698f950b2
---

# Crystal Converting Existing Odbc Reports In Crystal 6 Through 8

Converting Existing ODBC Reports in Crystal 6 through 8

Converting Existing ODBC Reports in Crystal 6 through 8

Crystal Reports

| Converting Existing ODBC Reports in Crystal 6 through 8  Crystal Reports |  |  |  |  |

Note: Crystal Reports versions 6 through 8 are no longer supported. The following help topic has been left in place as a courtesy for those that are still working with these unsupported versions.

To convert an existing ODBC report to use the Advantage driver:

| 1. | Open the report. |

| 2. | Choose 'Database' from the main menu. |

| 3. | Choose 'Convert Database Driver...' from the Database menu. |

| 4. | Check the 'Convert Database Driver on next Refresh' check box. |

| 5. | Find and select pdsads.dll in the drop-down list. |

| 6. | Click OK. |

| 7. | If the Advantage Alias dialog does not appear immediately, press the F5 key to force a refresh. |

| 8. | You will be prompted for an Advantage alias to use in this report. Either select an existing alias from the list provided, or click New to create a new alias. |

Note If converting from a Paradox ODBC datasource do not check the 'Converting Report From BDE Driver' checkbox. That check box is only for reports that were previously using pdbbde.dll.

| 9. | Click OK. |

| 10. | Crystal may report that the base tables have changed and ask if you want to fix up the report. Click Yes for each table. |

| 11. | If you have modified the original SQL statement in your report for some reason (possibly to make it work with the Advantage ODBC Driver, for example), it is best to restore the statement to its original format. To do this: |

| a. | Choose 'Database' from the main menu. |

| b. | Choose 'Show SQL Query...' from the Database menu. |

| c. | Click Reset. |

| d. | Refresh the report data (press F5). |
