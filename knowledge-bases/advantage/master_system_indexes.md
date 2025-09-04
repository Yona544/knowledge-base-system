system.indexes




Advantage Database Server 12  

system.indexes

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| system.indexes  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - system.indexes Advantage SQL Engine master\_System\_indexes Advantage SQL > System Views > Views > system.indexes / Dear Support Staff, |  |
| system.indexes  Advantage SQL Engine |  |  |  |  |

Contains one row for each index in the database.

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | Index name. |
| Parent | Character | 200 | The name of the table the index was created on. |
| Index\_File\_Name | Character | 200 | The name of the index file where the index is located. |
| Index\_Expression | Character | 510 | The expression used to build the index. |
| Index\_Condition | Character | 510 | The conditional expression used to build the index. |
| Index\_Options | Integer | 4 | Numerical representation of the index options. |
| Index\_Key\_Length | Integer | 4 | The length of the index key. |
| Index\_FTS\_Min\_Length | Integer | 4 | The minimum length of a word for it to be included in an FTS Index. |
| Index\_FTS\_Delimiters | Memo | Variable | The delimiters used in parsing the table for the FTS index. |
| Index\_FTS\_Noise | Memo | Variable | List of all noise words excluded from the FTS index. |
| Index\_FTS\_Drop\_Chars | Memo | Variable | The list of characters that are dropped (ignored) unconditionally. |
| Index\_FTS\_Conditional\_Chars | Memo | Variable | The list of characters that are dropped (ignored) when they are on the beginning or end of a word. |
| Comment | Memo | Variable | The dictionary description of the index order. |
| Index\_Collation | Character | 40 | The name of the [dynamic collation](master_collation_support.htm) used for the index. If the index was built with one of the collations stamped into the server (ADS\_ANSI or ADS\_OEM), this field will be NULL. |