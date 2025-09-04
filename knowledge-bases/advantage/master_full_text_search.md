Full Text Search




Advantage Database Server 12  

Full Text Search

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Full Text Search  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Full Text Search Advantage Concepts master\_Full\_text\_search Advantage Concepts > Advantage Functionality > Full Text Search / Dear Support Staff, |  |
| Full Text Search  Advantage Concepts |  |  |  |  |

Overview

Advantage has a server-side full text search engine (FTS) that allows developers to write applications that perform very fast searches of free format text data. Full text searches (also known as content searches) use intuitive search conditions consisting of words and phrases optionally combined with logical operators (AND, OR, NOT, NEAR) to search character, memo, and BLOB fields. The search conditions can be specified directly by end users and used in SQL WHERE clauses and record filters to produce result sets.

To optimize the full text searches, Advantage maintains content indexes specified by the developer. The indexes are in a compressed format; therefore the actual index size can be much smaller than the physical data. It is possible to perform full text searches on non-indexed data, but this requires a physical search of the record data and can be much slower. Content indexes can be built on Advantage proprietary (ADS\_ADT) and on FoxPro compatible (ADS\_CDX and ADS\_VFP) tables. Content indexes are not supported with CA-Clipper (ADS\_NTX) table types. As a result, is possible to perform full text searches on CA-Clipper tables, but the searches will not be optimized.

The interface functions for the full text search engine integrate seamlessly with other Advantage functionality. The scalar function CONTAINS() is used to specify the search condition and the field to be searched. It can be used inside SQL statements and in traditional Xbase-style record filters. For example, CONTAINS( definition, knowledge and complicity ) would return records where the given field contains both words "knowledge" and "complicity". This can be used directly in a filter condition or an SQL statement. For example:

SELECT \* FROM apdd

where contains( definition, knowledge and complicity )

The CONTAINS() scalar function can be combined in the statement with other SQL conditions. The following is a simple example of this:

SELECT \* FROM apdd

where contains( definition, (knowledge complicity) or (knowledge condensed) )

AND lcase( word ) <> accomplice

See Also

[FTS Quick Start](master_fts_quick_start.htm)

[Full Text Search Details](master_full_text_search_details.htm)