---
title: Arc Table Browser
slug: arc_table_browser
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_table_browser.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 0a0f4eecd9c3fdb6664af56cb1b81bd9b431cd8e
---

# Arc Table Browser

Table Browser

Table Browser

Advantage Data Architect

| Table Browser  Advantage Data Architect |  |  |  |  |

The Table Browser will be displayed after opening a table. See [Opening Tables](arc_opening_tables.md) for information on how to open a table. The Table Browser displays all record data in the current table in a grid. Memo and BLOB data can be displayed in a child window by double clicking on the desired memo/BLOB cell.

The Table Browser provides options in a quick menu (which can be invoked by right-clicking in the grid) and in the main Table menu to do the following:

- View and/or modify table and index properties

- Pack the current table

- Delete all records from the current table

- Re-index all indexes on the current table

- Recall the currently deleted records in the current table (DBF tables only)

- Recall all deleted records in the current table (DBF tables only)

- Encrypt all records in the current table

- Decrypt all records in the current table

- Go to a specific record

- Shrink default column sizes

- Refresh the dataset

The following functionality is provided at the bottom of the Table Browser window:

Navigation Bar

Allows various movements (navigation) within the grid, inserting new records, deleting existing records, flushing a pending record update, canceling a pending record update, and refreshing the contents of the current table.

Order By Pick List

Allows an active index order to be selected. If the table is a free table) or is a database table) that has no default index defined, there will no index active by default. The table data will be displayed in natural record number order, and NATURAL ORDER will be displayed in the Order By pick list. Select one of the available index orders listed to view the data in a different sorted order.

Scope

Allows a scope (range) to be set on the current indexed table. A scope allows you to view a subset of records in an index. A scope acts as a temporary view of an index, allowing extremely fast retrieval of only those records meeting the index scope range value(s). The scope values are determined based on the currently active index. The Scope option will only be active if an index has been selected in the Order By pick list. Click Clear to clear the specified scope. See [Index Scopes (Ranges)](master_index_scopes_ranges.md) for more information on scopes.

Set Filter

Allows an Advantage Optimized Filter to be set on the current table. Any valid Advantage expression can be specified for the Filter. See [Advantage Expression Engine](master_advantage_expression_engine.md) for more information on valid Advantage expressions. If the specified expression is fully optimized, a green dot will be displayed when the filter is set. If the specified expression is partially optimized, a yellow dot will be displayed when the filter is set. If the specified expression is non-optimized, a red dot will be displayed when the filter is set. The table will be filtered according to the specified expression regardless of the optimization level, however. Click Clear Filter to remove the filter on the table. See [Advantage Optimized Filters](master_advantage_optimized_filters.md) for more information on Advantage Optimized Filters and the levels of optimization.

Search

Searches for the specified value within the table by using the currently active index and performing a Seek operation. If the specified value exists within the index, the current record pointer will be positioned to the applicable record. If the specified value is found, a green dot will be displayed. If the specified value is not found, a red dot will be displayed. The Exact check box serves two purposes. If not checked (the default), a search for the partial value will be done as upon each individual keystroke. If the value is not found, the record pointer is positioned to the first record that falls after the specified value. If the Search check box is checked, the current record position is at EOF unless an exact match of the key value is specified. The Search functionality is only available if an index has been selected in the Order By pick list. See [Seek (FindKey, FindNearest, GotoKey, GotoNearest)](master_seek_movement.md) for more information on the Advantage Seek operation.

Record/Count

The current record pointer position and total number of records in the table are displayed in the lower left corner of the Table Browser.

When using the "Record/Count" option in ARC with an ADT table, it is possible for the record number to be higher than the number of records in the table.

If an index is selected then the first number is the key position in the index. Without an index active, the first number is the actual record number. If it is a freshly packed table then the record position and the record number will be the same. If there are deleted records in the table, the record number and record position may not be the same. If records have been deleted in the table then the record number can be higher than the number of records in the table.

For example, if there are ten records in a table and the first record is deleted the record number of the last record is 10 but the number of records in the table is 9.

A DBF table will not display a higher record number than the total number of records however, the first number will still be the record number when there isn't an active index. With a DBF table, total number of records includes deleted records where with ADTs, the total number of records does not include the deleted records.

To disable the record count display, go to the Tools | Arc Settings menu and select the General tab. Uncheck the option to display the record count.

Copying/Pasting Rows

To copy and paste rows into and out of ARC simply do a multiple select (shift+click) then a right-click to enter the context menu. Menu items Copy Records and Paste Records will be available to operate as necessary.

You can copy from or to Microsoft Word, Excel, and HTML Email clients. There is support for BLOB fields from ARC table to another, however with large blob fields, some data will be lost in certain versions of Microsoft Excel where the character count of individual cells has an upper bounds, if copying to and from ARC tables though there are no known issues.

When pasting into a table which has a different structure than the source table you will be presented with a field mapping dialog box. See [Field Mapping Utility](arc_field_mapping_utility.md) for more information on how to use this functionality.
