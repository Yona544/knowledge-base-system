---
title: Devguide Types Of Index Orders
slug: devguide_types_of_index_orders
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_types_of_index_orders.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 89f2c44ae1b6f2c501ba0e052e02cd5e1b47634e
---

# Devguide Types Of Index Orders

Types of Index Orders

     Types of Index Orders

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Types of Index Orders  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

ADT tables support four types of index orders. These are expression indexes, conditional indexes, custom indexes, and FTS indexes. Each of these types is described in the following sections.

Expression Indexes

An expression index is a simple index order that consists of one key for each record. As is the case with all other ADT index orders, with the exception of FTS indexes, the value of each key is defined by an index key expression.

A common type of index key expression is one that is based on one or more fields of a table. For example, assuming that there is a table that includes a field named Country, the following index key expression builds an index order based on this field:

Country

When building an index key expression on two or more fields of an ADT table, you separate the field names with a semicolon. For example, the following index key expression defines an index based on the Invoice Number and Part Number fields:

Invoice Number;Part Number

For DBF index files, this same expression index would be represented something like the following:

INVNUM + PARTNO

   
NOTE: For the preceding DBF index order to meaningful, both INVNUM and PARTNO would need to be string fields. If they were numeric fields, it would be necessary to use the expression engine STR function to convert them to strings before concatenating their values. The resulting expression would look like STR(INVNUM) + STR(PARTNO). If the fields were not converted to a string, the resulting expression would be the sum of the INVNUM and PARTNO fields, which would only be useful if you want to sort or search the corresponding table based on the sum of INVNUM and PARTNO, an otherwise meaningless value. This conversion is not necessary for ADT tables when a semicolon is used to concatenate fields. With ADT index order expressions, a semicolon can concatenate expressions of differing types. For example, a string field can be concatenated with an integer field.  
 

While expression indexes based on one or more fields are the most common, these indexes can also include more complicated expressions. For example, they can include two or more expressions, as well as basic arithmetic, string, and Boolean operators. These operators include the following:

+        -        \*        /        AND        OR        NOT

In addition, expressions can make use of a variety of functions supported by the Advantage expression engine. The following is the list of these functions as of this writing:

ABS, ALLTRIM, AT, CHR, COLLATE, CTOD, CTOT, CTOTS, DATE, DAY, DELETED, DESCEND, DTOC, DTOS, EMPTY, I2BIN, IF, IIF, L2BIN, LEFT, LEN, LOWER, LOWERW, LTRIM, MAX, MIN, MONTH, NOW, PAD, PADC, PADL, PADR, RAT, RECNO, REVERSE, RIGHT, ROUND, RTRIM, SPACE, STOD, STOTS, STR, STRZERO, SUBSTR, TIME, TODAY, TRANSFORM, TRIM, TSTOD, UPPER, UPPERW, VAL, YEAR

Consider this: expression indexes on character fields are case-sensitive (as opposed to cicharacter fields, which are case-insensitive). To create an expression index that can be used to sort and search a character field without regard to case, you can use the UPPER function (or LOWER function). The following expression defines an index that can be used to create a case-insensitive filter on a character field named Last Name:

UPPER(Last Name)

It is important to note, however, that with an index like this, your filter expression or SQL SELECT WHERE clause must also make use of the UPPER function. Otherwise, the selection operation will not be optimized. More about this is said later in this chapter.

In addition to their other features, expression indexes can be descending indexes and they can be unique. When you make a descending expression index active, the records in your table are sorted in descending order.

What a unique expression index does depends on whether the associated table is an ADT table or a DBF table. With DBF tables, a unique index contains one key for each distinct value on the index expression, but the index does not enforce uniqueness among records. For example, if you define a unique index on a DBF table field named Customer ID, it is still possible for this table to contain two different records that have the same value in the Customer ID field. However, when this index is active, only one of those records would be accessible. (This behavior is similar to a SQL SELECT statement that uses the DISTINCT keyword.)

By comparison, a unique index on an ADT table enforces uniqueness. For example, if you have a unique index on the Customer ID field of an ADT table, an attempt to write another record to this table using the same Customer ID value as one that already exists in the table will fail (an exception will be raised and the new record will not be inserted).

Expression indexes are the workhorse indexes of your database applications. In fact, conditional and custom index orders are really just special cases of expression indexes. In short, expression indexes provide you with ordered, high-speed access to your tables records based on index key expressions.

Conditional Indexes

A conditional index is similar to an expression index. The major difference is that while an expression index has a key for every record in the underlying table, a conditional index may not.

There are two parts to a conditional index. These are the index key expression and the condition expression. The index key expression serves the same purpose as in an expression index. Specifically, it defines the contents of the index key, which is used both for sorting and for high-speed access to the underlying records.

The second part is the condition expression. The condition expression is a Boolean expression, and it typically compares values in one or more fields to one or more expressions. A conditional index has one key for each record where the condition evaluates to a Boolean True.

When a conditional index is made the current index of a table, only those records for which there are index keys appear visible in the table. Those records appear in order of the index key expression. For example, if you want to create an index that includes only customers from the USA, and you want those records to be sorted by Customer ID, you define the index key expression as:

Customer ID

and the condition expression as:

Country='USA'

At first glance, conditional indexes sound appealing. But in practice, there are more flexible mechanisms for achieving the same result. For example, you can use a SQL SELECT statement to select a subset of records as well as to sort the records that are displayed. Since SQL SELECT queries can contain parameters in their WHERE clauses, the Boolean expression that selects the subset of records can be controlled at runtime. By comparison, the Boolean expression employed by a conditional index is fixed when the index is created.

An even more flexible solution is to use an expression index in conjunction with a scope (sometimes called a range) or a filter. Like a conditional index, a scope on an expression index can limit which records appear in the table, as well as provide a sorted view of the records that do appear. Filters provide a similar feature, and while slightly slower than scopes, provide for more flexible expressions than scopes. Specifically, a filter expression can include more fields than are contained in the index key expression.

This discussion is not meant to suggest that you should avoid conditional indexes. Indeed, they are high-performance indexes with many valuable characteristics. However, there are alternatives. Which indexes and filtering mechanisms are best for your application depends on the nature of your data and how you need to access it.

Custom Indexes

A custom index is an initially empty index whose keys are added at runtime. For example, you can have a custom index named ShowCustomers. You can then add keys for each customer that you want displayed in the table when the index is applied. As is the case with the other indexes discussed in this section, the keys of a custom index are defined using an index key expression.

You add a custom key using the ACE (Advantage Client Engine) API by calling AdsAddCustomKey. This method adds a key to the custom index that references the current record of a table. Similarly AdsDeleteCustomKey removes a key for the current record from the custom index. Some of the other Advantage data access mechanisms provide additional functions for adding and remove keys from a custom index.

While a custom index might sound like a useful tool, you need to be careful when using a custom index in a multiuser environment. Specifically, all client applications that are using the same custom index can add or remove keys from that index, so long as the index is opened in a shared mode. Also, keys that are added to a custom index are based on the data in the associated record at the time that the key was added. Subsequent changes to the associated records will have no effect on the custom index, even if those changes make the record inconsistent with the indexs purpose.

FTS Indexes

FTS indexes enable high-speed searches of text-based fields in ADT and FoxPro DBF tables. (Clipper NTX indexes do not support FTS indexes.) Unlike the other indexes introduced in this section, the keys of an FTS are not based on an index key expression. Instead, they are based on the words of the text-based field on which they are built.

Each FTS index applies to only a single text-based field. You can create an FTS index on any of the following field types: BINARY, CHARACTER, MEMO, RAW (ADT tables only), IMAGE, and VARCHAR.

   
NOTE: VarChar character fields have been deprecated so while they are supported with Advantage tables, using them is discouraged.  
 

FTS indexes are used by filter expressions and the WHERE clause of SQL SELECT statements to select records based on their text content. These filter expressions must use the CONTAINS scalar function, and WHERE clauses must contain one or more of the following scalar functions: CONTAINS, SCORE, and SCOREDISTINCT. See the section "Full Text Search Indexes" later in this chapter for in-depth coverage of these indexes.
