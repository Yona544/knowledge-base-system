---
title: Master Table Data Caching
slug: master_table_data_caching
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_table_data_caching.htm
source: Advantage CHM
tags:
  - master
checksum: 56d9da2b8a18b0bf6eac68eb8ed32db119acdf7f
---

# Master Table Data Caching

Table Data Caching

Table Data Caching

Advantage Database Server

| Table Data Caching  Advantage Database Server |  |  |  |  |

Table Data Caching is a feature that enables the caching of table data in the Advantage caching system.  Caching (keeping data in memory) frequently used data can help speed up operations that use the data.  This feature is intended for use with small tables which contain data that is used often and shared among multiple users.  For example, a lookup table of zip codes that is used often but rarely updated.  Typically Advantage will only cache index data or temporary file data because that data can be restored or re-created in the event of a catastrophic failure.  Caching updates to table data is much more risky as that data cannot be automatically restored.  It is for that reason that you must be very careful when enabling this feature. It is highly recommended that this feature only be used with tables that are backed up on a regular basis.  Table data caching is enabled via a dictionary property for dictionary bound tables.  In Advantage Data Architect the caching mode is configurable in the Table Designer (table properties tab).  For free tables caching is enabled via the AdsOpenTable90 and AdsCreateTable90 APIs (in Delphi caching on free tables is enabled via the TAdsTableOptions in the TAdsDataSet class).

Effects on the Advantage Caching System

The Advantage caching system is designed to keep the most recently used data cached in order to speed up future uses of that data.  If table caching is enabled and the cache is filled with table data that is not used very often, the overall performance of the system will suffer.  With this in mind, it is highly recommended that only tables that are small and used often & by multiple users have caching enabled on them.

Limitations

Table data caching is limited to tables opened with [Advantage Proprietary Locking](master_advantage_proprietary_locking.md) only.  This is because compatible locking is used when sharing data with non-Advantage applications and caching reads or writes to shared data will produce undesired results.

ERR\_LOST\_CACHED\_UPDATES

In the case of a catastrophic failure or improper shutdown of Advantage, a table might not get some updates that were cached in memory.  If this happens to an ADT, DBF, or ADM file, a 7155 (ERR\_LOST\_CACHED\_UPDATES) will be logged to the Advantage error log the next time the file is opened.  This error will continue to be logged each time the file is opened until an update is made to the table.  If you see this error in your error log, the table it is associated with almost certainly has some logical or physical corruption.  It is then recommended that the table be restored with a recent backup.

Open/Create Table Options

The [AdsOpenTable90](ace_adsopentable90.md) and [AdsCreateTable90](ace_adscreatetable.md) APIs now support two options to enable table data caching. ADS\_CACHE\_READS and ADS\_CACHE\_WRITES can be passed in to enable read or write caching on the table.  These options are for use with free tables and will be ignored by dictionary bound tables. To enable table data caching on dictionary bound tables see the dictionary table property discussed below.  In Delphi, these open and create table options are enabled via the TAdsTableOptions in the TAdsDataSet class.

Data Dictionary Table Caching Property

A new dictionary table property ([ADS\_DD\_TABLE\_CACHING](master_sp_modifytableproperty.md)) has been added to automatically enable caching on a table when it is opened.  This property can be set on the Table Properties tab in the table designer of Advantage Data Architect.  By default this setting is disabled and set to None.  Setting it to Reads will enable caching of table reads.  Setting it to Writes will enable both caching of reads and writes to the table.  Note that database ALTER permissions are required to view or modify this property.  This is because modifying this property can affect the system as a whole and should only be accessed by a true administrator of the database.

See Also

[sp\_ModifyTableProperty](master_sp_modifytableproperty.md)

[AdsDDSetTableProperty](ace_adsddsettableproperty.md)

[AdsDDGetTableProperty](ace_adsddgettableproperty.md)

[AdsOpenTable90](ace_adsopentable90.md)

[AdsCreateTable90](ace_adscreatetable.md)
