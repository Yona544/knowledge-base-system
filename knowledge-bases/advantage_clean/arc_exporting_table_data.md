---
title: Arc Exporting Table Data
slug: arc_exporting_table_data
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_exporting_table_data.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: c7bf7089b2a4c0d07ff5d45ce1ecdc80837f891c
---

# Arc Exporting Table Data

Exporting Table Data

Exporting Table Data

Advantage Data Architect

| Exporting Table Data  Advantage Data Architect |  |  |  |  |

Use the Advantage Data Architect export functionality to export a table's data into a new Advantage table, into an existing Advantage table, or into another file format such as MS Excel, HTML, or a comma-delimited text (CSV) file.

To export data from an open table or query:

| 1. | Open a table or query. See [Opening Tables](arc_opening_tables.md) for more information. |

| 2. | Right-click anywhere on the opened table's grid. |

| 3. | Select the file format in which to export. Available options are: |

- Export into a new Advantage table of the same table type as the original (ADT/ADI/ADM, DBF/CDX/FPT, or DBF/NTX/DBT)

- Export into an existing Advantage table of the same table type as the original (ADT/ADI/ADM, DBF/CDX/FPT, or DBF/NTX/DBT)

- Export into another file format, including:

- HTML

- Microsoft Word

- Microsoft Excel

- Text

- Rich Text

- Comma-Delimited Text (CSV)

- Tab-Delimited Text

- Data Interchange Format (DIF)

- SYLK Format

- the Windows Clipboard

To export data from a table in the Connection Repository:

| 1. | Open a database. See [Opening a Database](arc_opening_a_database2.md) for more information. |

| 2. | Expand the list of available tables |

| 3. | Right-click on the desired table and select Export. |

| 4. | Select the file format in which to export. Available options are: |

- Export into a new Advantage table of the same table type as the original (ADT/ADI/ADM, DBF/CDX/FPT, or DBF/NTX/DBT)

- Export into an existing Advantage table of the same table type as the original (ADT/ADI/ADM, DBF/CDX/FPT, or DBF/NTX/DBT)

- Export into another file format, including:

- HTML

- Microsoft Word

- Microsoft Excel

- Text

- Rich Text

- Comma-Delimited Text (CSV)

- Tab-Delimited Text

- Data Interchange Format (DIF)

- SYLK Format

- the Windows Clipboard

Exporting data into a new or existing Advantage table will copy the table data and memo data, and it will copy the data in indexed order if an index is active. When exporting into a new Advantage table, a table and memo file (if applicable) will be created, but no index file(s) will be created. When exporting into an existing Advantage table, if the destination table is of a different field structure than the source table, only those columns of the same name will attempted to be exported into the destination table.
