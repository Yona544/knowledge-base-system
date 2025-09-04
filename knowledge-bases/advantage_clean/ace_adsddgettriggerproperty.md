---
title: Ace Adsddgettriggerproperty
slug: ace_adsddgettriggerproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddgettriggerproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: a055a3848a36793dc9e8adbf879630ab11b59be5
---

# Ace Adsddgettriggerproperty

AdsDDGetTriggerProperty

AdsDDGetTriggerProperty

Advantage Client Engine

| AdsDDGetTriggerProperty  Advantage Client Engine |  |  |  |  |

Gets a specified property from the data dictionary for a trigger.

Syntax

UNSIGNED32 AdsDDGetTriggerProperty( ADSHANDLE hObject,

UNSIGNED8 \*pucTriggerName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 \*pusPropertyLen );

Parameters

| hObject (I) | Handle of a database connection. |
| pucTriggerName (I) | The name of the trigger in the data dictionary. |
| usPropertyID (I) | The property to retrieve. (see below for possible values.) |
| pvProperty (O) | A buffer to hold the property value. |
| pusPropertyLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsDDGetTriggerProperty will retrieve the specified property of the trigger from the data dictionary.

The pucTriggerName parameter should be qualified with the table name the trigger belongs to followed by two colon characters ( :: ). For example, "Customers::AfterInsertTrig" would specify you want the property for the trigger called "AfterInsertTrig" that belongs to the "Customers" table.

The following are the valid values for usPropertyID:

| usPropertyID | Description |
| ADS\_DD\_TRIG\_EVENT\_TYPE | Type of trigger event this trigger fires on. See [AdsDDCreateTrigger](ace_adsddcreatetrigger.md) for details on event types. The flag is returned as a 4-byte (UNSIGNED32) number in pvProperty. |
| ADS\_DD\_TRIG\_TRIGGER\_TYPE | Type of trigger (before, after, etc.). See [AdsDDCreateTrigger](ace_adsddcreatetrigger.md) for details on trigger types. The flag is returned as a 4-byte (UNSIGNED32) number in pvProperty. |
| ADS\_DD\_TRIG\_CONTAINER\_TYPE | Type of trigger container. See [AdsDDCreateTrigger](ace_adsddcreatetrigger.md) for details on container types. The flag is returned as a 4-byte (UNSIGNED32) number in pvProperty. |
| ADS\_DD\_TRIG\_CONTAINER | Name of the trigger container. The container name is returned as a NULL terminated string in the pvProperty. |
| ADS\_DD\_TRIG\_CONTAINER\_W | Name of the trigger container. The container name is returned as a NULL terminated UTF-16 string in the pvProperty. |
| ADS\_DD\_TRIG\_FUNCTION\_NAME | Name of the trigger function in the container. The function name is returned as a NULL terminated string in the pvProperty. |
| ADS\_DD\_TRIG\_PRIORITY | Priority of the trigger. The priority is returned as a 4-byte (UNSIGNED32) number in pvProperty. |
| ADS\_DD\_TRIG\_OPTIONS | Bitmask of trigger options. See [AdsDDCreateTrigger](ace_adsddcreatetrigger.md) for details on options. The flag is returned as a 4-byte (UNSIGNED32) number in pvProperty. |
| ADS\_DD\_TRIG\_TABLENAME | Name of the table the trigger belongs to. The table name is returned as a NULL terminated string in the pvProperty. |
| ADS\_DD\_COMMENT | Returns the trigger description in pvProperty. The description is returned as a NULL terminated string in the pvProperty. |

See Also

[AdsDDCreateTrigger](ace_adsddcreatetrigger.md)

[AdsDDRemoveTrigger](ace_adsddremovetrigger.md)

[system.triggers](master_system_triggers.md)
