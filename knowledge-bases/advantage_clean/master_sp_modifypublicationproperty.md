---
title: Master Sp Modifypublicationproperty
slug: master_sp_modifypublicationproperty
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_modifypublicationproperty.htm
source: Advantage CHM
tags:
  - master
checksum: 21c4feb4f96cc74545f5d94679607483a6a661e9
---

# Master Sp Modifypublicationproperty

sp\_ModifyPublicationProperty

sp\_ModifyPublicationProperty

Advantage SQL Engine

| sp\_ModifyPublicationProperty  Advantage SQL Engine |  |  |  |  |

Set the property of an existing publication in the data dictionary.

Syntax

sp\_ModifyPublicationProperty(

PublicationName,CHARACTER,200,

Property,CHARACTER,200,

Value,Memo )

 

Parameters

| PublicationName (I) | The name of the publication in the database. |
| Property (I) | Name of the property to set. See Remarks for allowed values. |
| Value (I) | Value to be stored in the data dictionary in string format. |

Special Return Codes

| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in Property is not a valid publication property, or the specified property cannot be modified. |
| AE\_INVALID\_OBJECT\_NAME | The publication specified by PublicationName cannot be located in the data dictionary. |

Remarks

sp\_ModifyPublicationProperty sets one property for the specified publication in the database. The new property overwrites the existing property in the data dictionary. The following are the valid values for Property.

| Property | Description |
| COMMENT | Changes the publication description. |
| OPTIONS | This is reserved for future use. |
| USER\_DEFINED\_PROP | Changes the user defined publication property. The user-defined property is set, read, and interpreted by the application. It is not used by Advantage. |

Example

EXECUTE PROCEDURE sp\_ModifyPublicationProperty( 'mypub', 'comment',

'this is a test publication' )

See Also

[sp\_CreatePublication](master_sp_createpublication.md)

[system.publications](master_system_publications.md)
