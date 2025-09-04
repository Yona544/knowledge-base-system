TAdsStringField




Advantage Database Server 12  

TAdsStringField

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsStringField  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsStringField Advantage TDataSet Descendant ade\_Tadsstringfield Advantage TDataSet Descendant > Advantage Components > TAdsStringField / Dear Support Staff, |  |
| TAdsStringField  Advantage TDataSet Descendant |  |  |  |  |

|  |  |
| --- | --- |
| [Properties](ade_tadsstringfield_properties.htm) |  |

 

The TAdsStringField is a descendant of TStringField, and contains Advantage-specific properties and methods.

Unit

AdsData

Description

TAdsStringField is the default field class used for fields of the type ftString. It is a descendant of the TStringField class, so all existing TDataSet functionality specific to TStringField is still possible when using a TAdsStringField.

You do not have to explicitly choose to use a TAdsStringField. When a table with string fields is opened a TAdsStringField object is created for each string field automatically.

The only exception to this rule is if you are using persistent fields. If you are using persistent fields, and your string field is defined as a TStringField, then you will not automatically be using a TAdsStringField. If you need access to TAdsStringField-specific properties or methods change the persistent field definition to declare the field as a TAdsStringField.

Example

The following example shows how a TField object from the datasets Fields collection can be cast to a TAdsStringField in order to access a TAdsStringField-specific property.

for i := 0 to ( CodeTable.Fields.Count - 1 ) do

begin

if ( CodeTable.Fields[i] is TAdsStringField ) and

( TAdsStringField( CodeTable.Fields[i] ).CaseInsensitive ) then

begin

Result := TRUE;

exit;

end;

end;

The as operator could be used as well. For example:

(adstable1.fields[1] as TAdsStringField).CaseInsensitive