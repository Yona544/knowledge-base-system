---
title: Ace Adsddremovetable
slug: ace_adsddremovetable
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddremovetable.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 436bb9bd755369c91881dc83c2a3e772c0f9f6ec
---

# Ace Adsddremovetable

AdsDDRemoveTable

AdsDDRemoveTable

Advantage Client Engine

| AdsDDRemoveTable  Advantage Client Engine |  |  |  |  |

Disassociates a table with the data dictionary.

Syntax

UNSIGNED32 AdsDDRemoveTable( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucTableName,

UNSIGNED16 usDeleteFiles );

Parameters

| hAdminConn (I) | Handle of a database connection). |
| pucTableName (I) | Name of the table identifying the table object in the data dictionary. |
| usDeleteFiles (I) | If this parameter is non-zero, the physical files will be deleted permanently. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | The pucTableName does not identify a table object in the data dictionary. |

Remarks

AdsDDRemoveTable disassociates a table, its memo file and its index files with the database defined in the data dictionary. It can also optionally delete the table, memo and index files permanently. After an ADT table is disassociated with the data dictionary, it becomes a free table) and can then be opened through a regular non-data dictionary bound free connection).

DROP permissions on the table are required to remove a table from a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note AdsDDRemoveTable requires an exclusive open of the table. An error will be returned if the table cannot be opened exclusively. If the table is the parent of any referential integrity in the data dictionary, the function will return an error.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

Remove the "Customer Information" table from the data dictionary and delete the files at the same time.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

AdsDDRemoveTable( hDD, "Customer Information", TRUE );

AdsDDClose( hDD );

See Also

[AdsDDAddTable](ace_adsddaddtable.md)

[AdsOpenTable](ace_adsopentable.md)

[AdsConnect60](ace_adsconnect60.md)
