Full Text Search Scalar Functions




Advantage Database Server 12  

Full Text Search Scalar Functions

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Full Text Search Scalar Functions  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Full Text Search Scalar Functions Advantage Concepts master\_Full\_text\_search\_scalar\_functions Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Full Text Search Scalar Functions  Advantage Concepts |  |  |  |  |

The scalar functions associated with full text searches include CONTAINS(), SCORE(), and SCOREDISTINCT. The CONTAINS() function takes two parameters. The first is either a field name or an asterisk (\*). The asterisk indicates that the search will be applied to all fields that have FTS indexes. The second parameter is the search condition inside quotes.

CONTAINS( fieldname, search condition )

CONTAINS( \*, search condition )

Use of the \* as the first parameter causes the search to include all fields that have FTS indexes matching the current active collation. For example, if a search is for two words, it will succeed even if the words are in different fields. For example, the following search will succeed if 'dog' is in one field and 'cat' is in another field in the same record (assuming both fields have FTS indexes that use same collation as the table's collation):

CONTAINS(\*, dog and cat)

Another potential limitation with the wild card search is that if there are FTS indexes on both ANSI fields and Unicode fields, then problem may arise if the ANSI FTS indexes and Unicode indexes were built using different index options. For example, if dog is a noise word in the ANSI FTS indexes but not in the Unicode FTS indexes, then an error will be returned when trying to perform the above search.

Note that the NEAR operator requires that the related search words be in the same field. For example, the following search will only succeed if both words are in the same field.

CONTAINS(\*, dog NEAR cat)

In SQL statements, the field name or asterisk must be qualified with a table name if multiple tables are involved and the field names are not unique. For example:

SELECT apdd.word, apdd.definition, ths.synomyms from

 apdd left outer join ths on apdd.id=ths.idd

 where contains( apdd.definition, superior )

The scoring functions SCORE() and SCOREDISTINCT() accept the same parameters as the CONTAINS() function. SCORE() returns the total count of all instances of words in the search condition that are in the text for a given record. SCOREDISTINCT() returns the number of search words that are in text. So the count for a given search word will be zero if it does not appear in the text and one if it appears one or more times. For example, if the search string is "word1 or word2" and the text is "word1 word1 word3", then SCORE() will return 2 and SCOREDISTINCT() will return 1.

In addition to accepting the same parameters as CONTAINS(), the score functions also have a second form: SCORE(n) and SCOREDISTINCT(n). In these versions, "n" refers to the nth instance of CONTAINS() in the statement. The following two SQL statements are equivalent.

SELECT \* from apdd where contains( definition, science or history )

order by score( definition, science or history ) desc

SELECT \* from apdd where contains( definition, science or history )

order by score(1) desc

In general, the scoring functions are intended for ordering result sets as in the above example, which sorts the results with the highest score at the top. However, the score functions can be used for displaying results as well. For example:

SELECT apdd.\*, score(1) as Score from apdd

where contains( definition, science or history )

order by score(1) desc

It is also possible to use the score functions in the WHERE clause to restrict results sets. For example, the following query limits the result set to exclude records that have scores less than 3.

SELECT apdd.\*, score(1) as Score from apdd

where contains( definition, science or history )

and score(1) > 2

While it is possible to use the SCORE function without any other criteria, please note that the computation of score values is not as optimized as the CONTAINS() function. Even if the FTS index contains scoring information, the score values must be computed on a record-by-record basis. The CONTAINS function, on the other hand, is evaluated (assuming an FTS index is available) with optimization techniques similar to [Advantage Optimized Filters](master_advantage_optimized_filters.htm). So while the following two queries produce equivalent result sets, the first one is much faster.

SELECT \* from apdd

where contains( definition, science or history )

and score(1) > 2

SELECT \* from apdd

where score( definition, science or history ) > 2

The first query limits the result set initially to only the records that contain the given words before any score values are computed. The second query must compute the score for every single record in the table.

The SCORE() and SCOREDISTINCT() functions can only be used with SQL statements. If they are used in a filter expression with a TAdsTable instance, an error will be returned.

The CONTAINS() scalar function can be used on fields that do not have FTS indexes, but the search will not be optimized. The search condition will be evaluated against all possible records in a linear fashion. When the condition is evaluated, the default delimiters, drop characters, and conditional drop characters are used for the evaluation. For data dictionary connections, these defaults can be specified by the developer and stored in the data dictionary. This may be useful, for example, if you are evaluating full text searches on non-indexed fields that require other delimiters than white space characters. For more information see [Full Text Search Index Options](master_full_text_search_index_options_fts.htm). For free table connections and for data dictionary connections that do not have FTS defaults specified, Advantage will use the system FTS defaults for the evaluation of CONTAINS on non-indexed fields.

When Advantage evaluates the CONTAINS condition on a non-indexed field, it does not use any noise word lists for performance reasons. This will cause differences in results only if you include noise words in the search condition. For example, the evaluation of CONTAINS( field, 'about time' ) can produce different results depending on if the field has an FTS index. If it does not have an FTS index, then the field must contain both the words 'about' and 'time' in order to pass the condition. If it does have an FTS index with the word 'about' as a noise word, then field only needs to contain the word 'time' in order to pass the condition.