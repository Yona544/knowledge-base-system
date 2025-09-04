---
title: Crystal Known Issues
slug: crystal_known_issues
product: Advantage Database Server
component: Crystal Reports
version: "12"
category: API
original_path_html: crystal_known_issues.htm
source: Advantage CHM
tags:
  - crystal
  - crystal-reports
checksum: 54717e454760017e2bac433707721b1264502461
---

# Crystal Known Issues

Known Issues

Known Issues

Crystal Reports

| Known Issues  Crystal Reports |  |  |  |  |

Crystal 11 and newer

- Reports created with previous versions of the Advantage Crystal Reports Driver that use INNER joins may not function correctly. When opened with the new Crystal driver, the report might switch the INNER joins to LEFT OUTER joins. To work around this issue:

| 1. | Open the report in the Crystal IDE. |

| 2. | Select 'Database Expert...' from the 'Database' menu option. |

| 3. | Select the 'Links' tab. |

| 4. | Right-click on each link and select 'Link Options...' |

| 5. | Select the correct join type. |

| 6. | Save the report. |
