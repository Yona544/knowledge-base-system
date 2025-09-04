AX\_SetCollation()




Advantage Database Server 12  

AX\_SetCollation()

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AX\_SetCollation()  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - AX\_SetCollation() Advantage Visual Objects and Vulcan.NET RDD vo\_Ax\_setcollation Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Advanced  Functions > AX\_SetCollation() / Dear Support Staff, |  |
| AX\_SetCollation()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Syntax

AX\_SetCollation( strCollation AS STRING )

Parameters

|  |  |
| --- | --- |
| <strCollation> | Collation language for the RDD to use. |

 

Returns

The previous collation setting.

Description

This function specifies which collation language to use when opening tables, opening cursors, or creating tables. By default, no collation language is set and the client will use the language set by the Advantage Database Server.

Note Collation languages are only valid with ADT and VFP tables. For all other table types, the collation language is ignored.

See Also

[AdsSetCollation](ace_adssetcollation.htm)

[AdsOpenTable90](ace_adsopentable90.htm)

[AdsCreateTable90](ace_adscreatetable.htm)