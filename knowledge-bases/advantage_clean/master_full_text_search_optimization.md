---
title: Master Full Text Search Optimization
slug: master_full_text_search_optimization
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_full_text_search_optimization.htm
source: Advantage CHM
tags:
  - master
checksum: 938afa5effd27a9733c381f70c86ba1fb617a904
---

# Master Full Text Search Optimization

Full Text Search Optimization

Full Text Search Optimization

Advantage Concepts

| Full Text Search Optimization  Advantage Concepts |  |  |  |  |

Search conditions that use only search words combined with the logical operators AND and OR are fully optimized (assuming an FTS index exists on the field being searched). For example, the following query is fully optimized:

SELECT \* FROM apdd

where contains( definition, science and (history or proof) )

Some search conditions require low-level searches of the data to fully resolve them. These searches return an initial optimized result set that must then be searched to determine which records fully meet the condition. The specific cases that require this post-processing step include the following:

- Use of the NEAR operator. The FTS indexes do not contain location (proximity) information. Thus, when the NEAR operator is used, the initial optimized search can verify that the words exist, but then the post-processing step must examine the physical data to determine if the words are "near" each other.

- Use of multi-word phrases. As with the NEAR operator, the initial optimized search can narrow down the result set to records that contain the words in the phrase, but the post-processing step must be performed to determine if the words actually form the given phrase in each record.

- Searches for words that exceed the maximum word length of the FTS index. The initial optimized search can narrow the result set down to the records that contain the first portion of the search word (up to the maximum word length, which is effectively the key length of the index). If the maximum word size of the index is, for example, 10 and a search for a word of more than 10 characters is performed, then the initial search will find records that have words where the first 10 characters match. The post-processing step will eliminate the records that do not fully match.

Note that substring and post-fix searches do not require post-processing. Although they are not nearly as efficient as prefix and exact match searches, they are fully resolved in the initial result set.

Finally, some search conditions cannot be optimized. Search conditions that use the NOT operator on a sub-condition that requires post-processing cannot be optimized. For example, the following query cannot be optimized because it uses the logical NOT operation on a partially optimized sub-condition.

SELECT \* FROM apdd

where contains( definition, not (species near snake) )

It is also possible that a CONTAINS() function must be evaluated by searching the physical data when the entire expression cannot be optimized. For details on this see Advantage Optimized Filters. In general, though, the expression logical OR operator (not the FTS OR operator) is the most common cause of this. The following statement is an example of this:

SELECT \* FROM apdd

where contains( definition, 'polite recognition' )

or id = 36

If the field "id" is not indexed, then the entire expression "contains( ) or id = 36" cannot be optimized. This means that every record in the table must be evaluated against the entire expression including the CONTAINS() evaluation, which can be expensive. If the field "id" has an index on it and the field "definition" has an FTS index, then the entire statement will be optimized.
