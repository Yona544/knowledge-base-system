---
title: Ade Gettriggerproperty
slug: ade_gettriggerproperty
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_gettriggerproperty.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a413450397d822e2cd810006a5d1a5076b3c40bf
---

# Ade Gettriggerproperty

GetTriggerProperty

TAdsDictionary.GetTriggerProperty

Advantage TDataSet Descendant

| TAdsDictionary.GetTriggerProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Gets a specified property from the data dictionary for a trigger.

Syntax

procedure TAdsDictionary.GetTriggerProperty( strTriggerName : string;

usPropertyID : UNSIGNED16;

pvProperty : pointer;

var usPropertyLen : UNSIGNED16 );

Parameters

| strTriggerName (I) | The name of the trigger in the data dictionary. |
| usPropertyID (I) | The property to retrieve. (see below for possible values.) |
| pvProperty (O) | A buffer to hold the property value. |
| usPropertyLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

GetTriggerProperty will retrieve the specified property of the trigger from the data dictionary.

The strTriggerName parameter should be qualified with the table name the trigger belongs to followed by two colon characters ( :: ). For example, "Customers::AfterInsertTrig" would specify you want the property for the trigger called "AfterInsertTrig" that belongs to the "Customers" table.

The following are the valid values for usPropertyID:

| usPropertyID | Description |
| ADS\_DD\_TRIG\_EVENT\_TYPE | Type of trigger event this trigger fires on. See [CreateTrigger](ade_createtrigger.md) for details on event types. The flag is returned as a 4-byte (UNSIGNED32) number in pvProperty. |
| ADS\_DD\_TRIG\_TRIGGER\_TYPE | Type of trigger (before, after, etc.). See [CreateTrigger](ade_createtrigger.md) for details on trigger types. The flag is returned as a 4-byte (UNSIGNED32) number in pvProperty. |
| ADS\_DD\_TRIG\_CONTAINER\_TYPE | Type of trigger container. See [CreateTrigger](ade_createtrigger.md) for details on container types.The flag is returned as a 4-byte (UNSIGNED32) number in pvProperty. |
| ADS\_DD\_TRIG\_CONTAINER | Name of the trigger container. The container name is returned as a NULL terminated string in the pvProperty. |
| ADS\_DD\_TRIG\_FUNCTION\_NAME | Name of the trigger function in the container. The function name is returned as a NULL terminated string in the pvProperty. |
| ADS\_DD\_TRIG\_PRIORITY | Priority of the trigger. The priority is returned as a 4-byte (UNSIGNED32) number in pvProperty. |
| ADS\_DD\_TRIG\_OPTIONS | Bitmask of trigger options. See [CreateTrigger](ade_createtrigger.md) for details on options. The flag is returned as a 4-byte (UNSIGNED32) number in pvProperty. |
| ADS\_DD\_TRIG\_TABLENAME | Name of the table the trigger belongs to. The table name is returned as a NULL terminated string in the pvProperty. |
| ADS\_DD\_COMMENT | Returns the trigger description in pvProperty. The description is returned as a NULL terminated string in the pvProperty. |

See Also

[CreateTrigger](ade_createtrigger.md)

[RemoveTrigger](ade_removetrigger.md)
