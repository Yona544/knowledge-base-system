---
title: Ace Adsddgetviewproperty
slug: ace_adsddgetviewproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddgetviewproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: fbfd4ceed96f58b030cb37c6ad9c96a3be56945b
---

# Ace Adsddgetviewproperty

AdsDDGetViewProperty

AdsDDGetViewProperty

Advantage Client Engine

| AdsDDGetViewProperty  Advantage Client Engine |  |  |  |  |

Retrieves VIEW properties from an Advantage Data Dictionary. See [Advantage SQL Engine](master_advantage_sql_engine.md) for more specific VIEW documentation.

Syntax

UNSIGNED32 AdsDDGetViewProperty( ADSHANDLE hDBConn,

UNSIGNED8 \*pucViewName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 \*pusPropertyLen );

Parameters

| hDBConn (I) | Handle of a database connection). |
| pucViewName (I) | View to retrieve property. |
| usPropertyID (I) | Property to retrieve. |
| pvProperty (O) | Return property to this pointer. |
| pusPropertyLen (I/O) | pvProperty buffer length on input, number of bytes returned on output. |

Remarks

AdsDDGetViewProperty returns a VIEW property from an Advantage Data Dictionary. The following values can be passed in the usPropertyID parameter:

| ADS\_DD\_VIEW\_STMT | Retrieves the view SQL statement from the dictionary. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.  Returns data as ANSI encoded text. |
| ADS\_DD\_VIEW\_STMT\_W | Retrieves the view SQL statement from the dictionary. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.  Returns data as UTF-16 encoded text. |
| ADS\_DD\_VIEW\_STMT\_LEN | Retrieves the length of the view SQL statement. Can be used to allocate a buffer before calling AdsDDGetViewProperty with the ADS\_DD\_VIEW\_STMT option. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_COMMENT | Retrieves the optional comment set when creating the view. |

Example

UNSIGNED8 aucBuff[256];

 

usLen = sizeof( aucBuff );

AdsDDGetViewProperty( hConn, "myview", ADS\_DD\_VIEW\_STMT, aucBuff, &usLen );

See Also

[AdsDDAddView](ace_adsddaddview.md)

[AdsDDRemoveView](ace_adsddremoveview.md)

[AdsDDSetViewProperty](ace_adsddsetviewproperty.md)

[system.views](master_system_views.md)
