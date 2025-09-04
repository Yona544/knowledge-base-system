AdsSetExact22




Advantage Database Server 12  

AdsSetExact22

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetExact22  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetExact22 Advantage Client Engine ace\_Adssetexact22 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetExact22  Advantage Client Engine |  |  |  |  |

Affects how string comparisons are performed with certain relational operators

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetExact22 (ADSHANDLE hObj,  UNSIGNED16 bIgnoreSpaces); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of a table or connection. If this is 0, the result is the same as calling AdsSetExact. |
| bIgnoreSpaces (I) | A non-zero value causes string comparisons with certain relational operators to ignore trailing spaces. The default value for connections is determined by the global value set by AdsSetExact. The default value for tables is determined by the connection under which the table is opened or created. |

Remarks

The AdsSetExact22 setting affects how string comparisons are performed with the relational operators =, >, <, >=, and <=. The exact equal operator ("==") is not affected by this setting. In general, if the AdsSetExact22 setting is True, trailing spaces are ignored during the comparison. The AdsSetExact22 setting is more complex and affects the various relational operators differently. See [Expression Engine Operators](master_expression_engine_operators.htm) for detailed information on how the AdsSetExact22 setting affects relational operators.

If a table handle is specified in hObj, AdsSetExact22 will only affect string comparisons in traditional record filters set via AdsSetFilter, and string comparisons in Advantage Optimized Filters set via AdsSetAOF set for the specified table in the future. Changing the set exact setting for a table has no immediate effect on string comparisons in an existing record filter or an existing AOF. Changing the set exact setting for a table also has no effect on string comparisons performed in existing index expressions or on string comparisons performed in newly created indexes on the specified table.

If a connection handle is specified in hObj, AdsSetExact22 will affect string comparisons in all tables currently opened on this connection, and all string comparisons in tables opened in the future on this connection. Changing the exact setting for a connection has an immediate effect on string comparisons in existing traditional record filters set via AdsSetFilter on tables on this connection, but has no effect on existing Advantage Optimized Filters set via AdsSetAOF until AdsRefreshAOF is called. Changing the set exact setting for a connection also affects string comparisons in index expressions in all indexes created on tables opened on the specified connection.

If 0 (zero) is specified in hObj, AdsSetExact22 is equivalent to AdsSetExact that affects all tables on all connections.

Note AdsSetExact22 expands the functionality available in AdsSetExact with the addition of a parameter for specifying a table or connection. Since a new parameter was added, a new API had to be created. The "22" indicates the Advantage Client Engine version (i.e., version 2.2) in which this new supplementary API was first available.

Note AdsSetExact22 does not affect [AdsSeek](ace_adsseek.htm).

Example

[Click Here](ace_more_examples.htm#adssetexact22_example)

See Also

[AdsGetExact22](ace_adsgetexact22.htm)

[AdsSetFilter](ace_adssetfilter.htm)

[AdsSetAOF](ace_adssetaof.htm)

[AdsSetExact](ace_adssetexact.htm)