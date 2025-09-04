---
title: Master Aof Optimization
slug: master_aof_optimization
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_aof_optimization.htm
source: Advantage CHM
tags:
  - master
checksum: 311dcfe4c26abebd3411165623dc945d15ecf3ee
---

# Master Aof Optimization

AOF Optimization

AOF Optimization

Advantage Concepts

| AOF Optimization  Advantage Concepts |  |  |  |  |

Three levels of optimization are available for AOFs. AOFs can be fully optimized (ADS\_OPTIMIZED\_FULL), partially optimized (ADS\_OPTIMIZED\_PART), or not optimized (ADS\_OPTIMIZED\_NONE). For example, the filter expression "lastname = Smith .AND. firstname = John" will be fully optimized if indexes exist on "lastname" and "firstname". If an index exists on only one of those fields, the filter will be partially optimized. If no index exists for either field, the filter will not be optimized. The following rules apply when using logical operators. The columns labeled Optimization Level refer to a simple expression (e.g., "lastname = Smith") or multiple simple expressions joined by logical operators (e.g., "lastname = Smith" .AND. firstname = John").

| Optimization Level | Operator | Optimization Level | Resulting Optimization Level |
| Full | .AND. | Full | Full |
| Full | .AND. | Not Optimized | Partial |
| Full | .AND. | Partial | Partial |
| Partial | .AND. | Partial | Partial |
| Partial | .AND. | Not Optimized | Partial |
| Not Optimized | .AND. | Not Optimized | Not Optimized |
| Full | .OR. | Full | Full |
| Full | .OR. | Not Optimized | Not Optimized |
| Full | .OR. | Partial | Partial |
| Partial | .OR. | Partial | Partial |
| Partial | .OR. | Not Optimized | Not Optimized |
| Not Optimized | .OR. | Not Optimized | Not Optimized |
|  | .NOT. | Full | CDX Full, ADI Partial |
|  | .NOT. | Partial | Not Optimized |
|  | .NOT. | Not Optimized | Not Optimized |

For example, consider the filter expression:

hiredate > CTOD(1/19/90) .OR. ( hiredate > CTOD(1/18/85) .AND. deptnum = 15)

If field "hiredate" is indexed and field "deptnum" is not, the expression will be partially optimized. Each simple expression involving field "hiredate" will be fully optimized but the simple expression involving field "deptnum" will not be optimized. The expression can be viewed as:

Full .OR. (Full .AND. Not Optimized)

This then resolves to:

Full .OR. Partial

The final result is partial optimization.

For a simple expression to be fully optimized, the left operand of the expression must, in general, match an existing index expression exactly. For example, if the only index on a table is "UPPER(lastname)", the AOF expression "lastname = Smith" will not be optimized, but "UPPER(lastname)=SMITH" will be fully optimized. The following are other cases where an exact match is not needed:

- If the function YEAR( fldname ) is used in an AOF expression, Advantage will use indexes of the form "fldname" or "DTOS( fldname )" to optimize the expression. For example, the filter "YEAR( doh )=1990" will be optimized if either an index of the form "doh" or "DTOS( doh )" exists.

- If the function EMPTY( fldname ) is used as an AOF expression, Advantage will use indexes built on "fldname" to optimize the expression. For example, the filter "EMPTY( lastname )" will be optimized if the index "lastname" exists.

When a filter is partially optimized or not optimized, each bit set in the AOF indicates that the corresponding record may or may not be in the filter. Each bit that is cleared indicates that the record is definitely not in the AOF. Thus, for each bit set for a partial or non-optimized filter, Advantage must read the actual record and evaluate some portion of the filter expression against the record to determine whether or not the record passes the AOF condition.

Many of the Visual FoxPro (VFP) compatible collations include support for expansion characters, which are single-byte characters that actually collate to more than one character. For example, the character Æ (0xC6) expands to the characters AE (0x4145) in some collations. Because of the way Visual FoxPro keys are constructed, it is possible for some key values involving these expansion characters to require more bytes than will fit in the index. For these data-dependent situations, it is possible for an AOF to be partially optimized when a similar appearing AOF is fully optimized. The correct result will be returned, but it may require some additional post-processing of the filter. This rare situation can be avoided if necessary by increasing the field width, which will result in producing longer index keys.

Multiple-Field Indexes

Multiple-field (sometimes called multi-segment or composite) indexes are utilized by the AOF engine in some cases for optimization. Normally, the first field of a multiple-field index can be used the same as a single field index on that same field. For example, the index "lastname;firstname" can be used to optimize the filter "lastname='Smith'". This multiple-field index can also be used to optimize the filter "lastname='Smith' and firstname='John'". The AOF engine will attempt to fully utilize multiple-field indexes for conditions that involve strict equality (= operator) and are combined with the logical AND operator. For example, the following filter expressions will not fully utilize the index expression "lastname;firstname". Only the comparison involving lastname can utilize that index in the following examples:

lastname = 'Smith' and firstname > 'X' (because of the > operator)

lastname < 'S' and firstname = 'John' (because of the < operator)

lastname = 'Smith' OR firstname = 'John' (because of the OR operator)

Note also that the exact setting must be set to TRUE (see [Expression Engine Operators](master_expression_engine_operators.md) for more information about the exact setting) in order to use multiple-field indexes on character fields. When the exact setting if set to FALSE, then filters such as "lastname='S' and firstname = 'J'" will match all records where lastname starts with "S" and firstname starts with "J". The corresponding index keys are not consecutive in an index of the form "lastname;firstname", therefore the AOF engine will not use both fields of that index for optimization. When using SQL statements, the exact setting is TRUE by definition. The SQL statement "SELECT \* from employee where lastname = 'S'" is defined to find only records where the lastname field has exactly the value "S" (as opposed to all records where lastname begins with "S").

Multiple-field CDX indexes are created with the use of the + operator. For example, the index expression "lastname+firstname" specifies an index that is the concatenation of the two fields. Note that two numeric fields combined with the + operator in an index are numerically summed, thus resulting in an index that is probably not useful for very many situations. The AOF engine does not use such indexes. Multiple-field ADT indexes must be created with the binary concatenation operator (;) in order for them to be utilized by the AOF engine. This is because ADT fields can be NULL, and the + operator propagates the NULL value. In other words, if either field of the index "lastname+firstname" is NULL, then the entire result will be NULL. Thus, the AOF engine cannot use those indexes. If you are using Visual FoxPro (VFP) tables, it is possible to use the binary concatenation operator to gain these optimization advantages; however, these indexes will not be compatible with Visual FoxPro.
