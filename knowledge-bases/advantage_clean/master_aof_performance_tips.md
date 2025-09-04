---
title: Master Aof Performance Tips
slug: master_aof_performance_tips
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_aof_performance_tips.htm
source: Advantage CHM
tags:
  - master
checksum: 7725519c3ed46642d485c3941a9276d4aac90b66
---

# Master Aof Performance Tips

AOF Performance Tips

AOF Performance Tips

Advantage Concepts

| AOF Performance Tips  Advantage Concepts |  |  |  |  |

The amount of time required to build the Advantage Optimized Filter depends on the number of index pages that must be read. For example, the filter "lastname = 'Elliot'" would likely be built very quickly because very few (possibly only one) index pages would need to be read. On the other hand, the filter "lastname != 'Elliot'" would take longer to build because most of the index pages would need to be read. By using the logical NOT operator, a developer can speed up the AOF builds. For example, the filter ".NOT. (lastname = 'Elliot')" would build faster than "lastname != 'Elliot'" because the server would only read the index pages containing 'Elliot' and then invert the resulting array of bits. Another example is "lastname > 'C'" versus ".NOT. (lastname <= 'C')". Assuming an even distribution of last names beginning with each letter, the latter filter will build faster because the server would read fewer index pages.

Developers can speed up the filtering of deleted records through the use of indexes built on "DELETED()". This applies to both ADT and DBF tables. With ADTs, the DELETED() index should be a [binary index](master_binary_indexes.md). With a DBF table, it can use either a traditional index or a binary index, but a binary index will probably produce better performance.

If a table has the index "DELETED()" built, then the AOF engine will automatically use that index to optimize the filtering of deleted records. For example, consider the following two operations using the Advantage Client Engine API:

ulRetCode = AdsShowDeleted( False );

ulRetCode = AdsSetAOF( hTable, "lastname='Smith'", ADS\_RESOLVE\_DYNAMIC );

If the table has an index built on "DELETED()", the AOF engine will automatically add "AND !DELETED()" to the filter expression, which will cause deleted records to be removed from the AOF. If there is not an index built on "DELETED()", "AND !DELETED()" is not added to the index expression, so deleted records will still be in the AOF. The server will filter out the deleted records resulting in the same set of records that would occur with an index on "DELETED()" but there may be a loss in performance. Note that if you change the "show deleted records" setting after building the AOF on a DBF table, you should rebuild the AOF, otherwise the AOF will still filter the deleted records. With ADT tables, deleted records are never visible to the application, so rebuilding the AOF is not necessary.

The AOF engine does not use custom indexes for optimization. In general, it also does not use conditional indexes. When filtering deleted records in DBF tables, the AOF engine will use conditional indexes with conditions of "!DELETED()". With DBF tables, unique indexes are not used for optimization. With ADT files, unique indexes are used for optimization because Advantage enforces the unique attribute and does not allow an ADT to contain records with duplicate keys for indexes with the unique attribute.

For an expression to be optimized, the left-hand side of the operator must match an index expression. If it is on the right side of the operator, it will not be optimized. For example, "'Smith'=lastname" will not be optimized. This should be coded as "lastname='Smith'". In addition, the right hand side of the operator cannot vary by record. For example, the filter "lastname<firstname" will not be optimized because the right hand side of the operator contains a field value. You can get around this limitation by creating an index of the form "(lastname<firstname)". A filter of the form "(lastname<firstname)=.T." will then be fully optimized.
