Data Type Independent Expression Concatenation Operator




Advantage Database Server 12  

Data Type Independent Expression Concatenation Operator

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data Type Independent Expression Concatenation Operator  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Data Type Independent Expression Concatenation Operator Advantage Concepts master\_Data\_type\_independent\_expression\_concatenation\_operator Advantage Concepts > Advantage File Formats > Advantage Proprietary File Format > Data Type Independent Expression Concatenation Operator / Dear Support Staff, |  |
| Data Type Independent Expression Concatenation Operator  Advantage Concepts |  |  |  |  |

Advantage proprietary files support a concatenation operator ; (a semi-colon) that can be used in index and filter expressions. This operator allows any data to be concatenated regardless of data type. For example, if two fields exist that are named DATE\_FIELD and CHAR\_FIELD, an index can be built with the [key](javascript:hhpopuplink.TextPopup(popid_44303104X,FontFace,-1,-1,-1,-1)) expression "DATE\_FIELD; CHAR\_FIELD". The equivalent index expression for a DBF table would be "DTOS( DATE\_FIELD ) + CHAR\_FIELD", which concatenates the characters that are the result of the DTOS function call, and the data stored in the character field.

If you prefer to concatenate fields of different data type in index and filter expressions without having to use functions to convert the fields to the same data type, you will want to use the [Advantage Proprietary Format](master_advantage_proprietary_format.htm) and the data type independent concatenation operator.

It is also possible to use the binary concatenation operator when using DBF tables opened with the Visual FoxPro (VFP) table type. However, this will produce an index that is not compatible with Visual FoxPro. One benefit to using the binary concatenation operator is that it produces keys that are more useful for optimization when the fields involved can hold [NULL values](master_support_for_null_values.htm). For example, if a key expression is "lastname+firstname", and one or both fields can hold NULL values, that index cannot be used for certain optimizations (e.g., Advantage Optimized Filters) because the result of the key is NULL if either value is NULL. Using the key expression "lastname;firstname" produces an index that can be used for more optimizations.