---
title: Master Sp Modifyviewproperty
slug: master_sp_modifyviewproperty
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_modifyviewproperty.htm
source: Advantage CHM
tags:
  - master
checksum: 0e353d5360d611ae209dccf96dace107b9ab039d
---

# Master Sp Modifyviewproperty

sp\_ModifyViewProperty

sp\_ModifyViewProperty

Advantage SQL Engine

| sp\_ModifyViewProperty  Advantage SQL Engine |  |  |  |  |

Modifies an existing view in the data dictionary.

Syntax

sp\_ModifyViewProperty(

ViewName,CHARACTER,200,

Property,CHARACTER,200,

Value,Memo )

sp\_ModifyViewProperty(

ViewName,CHARACTER,200,

Property,CHARACTER,200,

Value,NMemo )

Parameters

| ViewName (I) | Name of the existing view to modify. |
| Property (I) | Name of a view property to set. See Remarks for allowed values. |
| Value (I) | Property value to set. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | This error will be returned if the view cannot be found. |

Remarks

This procedure modifies an existing view. The primary benefit to using this procedure over deleting and re-creating the view is that it maintains existing permissions on the view object. The following are the valid values of Property and the expected value in Value.

| usPropertyID | Description |
| COMMENT | Stores a new description for the view. |
| VIEW\_STMT | Stores a new SQL SELECT statement for the view. |

Example

After making a connection to the database, set a new password for "view1".

EXECUTE PROCEDURE sp\_ModifyViewProperty(

'View1',

'VIEW\_STMT',

'select \* from test1' );

See Also

[CREATE VIEW](master_create_view.md)

[DROP VIEW](master_drop_view.md)
