Advantage Proprietary File Format Specifications




Advantage Database Server 12  

Advantage Proprietary File Format Specifications

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Proprietary File Format Specifications  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Advantage Proprietary File Format Specifications Advantage Concepts master\_Advantage\_proprietary\_file\_format\_specifications Advantage Concepts > Advantage File Formats > Advantage Proprietary File Format Specifications / Dear Support Staff, |  |
| Advantage Proprietary File Format Specifications  Advantage Concepts |  |  |  |  |

|  |  |
| --- | --- |
| Description | Length |
| Maximum number of index orders per compound index file | 256 |
| Maximum number of index files open per table | 15 |
| Maximum table size |  |
| Windows with NTFS | 16 exabytes (18,446,744,073,709,551,616 bytes) |
| Windows with FAT32 | 4 gigabytes (4,294,967,296 bytes) |
| Linux | 8 exabytes (9,223,372,036,854,775,807 bytes) |
| Maximum index file size |  |
| Windows with NTFS | 4 gigabytes multiplied by (Index Page Size) : Max 35 terabytes |
| Windows with FAT32 | 4 gigabytes (4,294,967,296 bytes) |
| Linux | 4 gigabytes multiplied by (Index Page Size) : Max 35 terabytes |
| Maximum memo file size |  |
| Windows with NTFS | 4 gigabytes multiplied by (Memo Page Size) : Max 4 terabytes |
| Windows with FAT32 | 4 gigabytes (4,294,967,296 bytes) |
| Linux | 4 gigabytes multiplied by (Memo Page Size) : Max 4 terabytes |
| Maximum database size | No maximum - limited by disk space only |
| Maximum number of records per table | 2 billion. |
| Maximum record length | 65530 bytes |
| Maximum field name length | 128 characters |
| Maximum index order name length | 128 characters |
| Characters allowed in field names | Any character value except 0 (NULL), ; (a semi-colon), or , (a comma) |
| Characters allowed in index order names | Any character value except 0 (NULL), ; (a semi-colon), or , (a comma) |
| Maximum amount of data per binary/image/BLOB field | 4 gigabytes |
| Maximum traditional record filter expression text length | 65,534 characters |
| Maximum Advantage Optimized Filter (AOF) expression text length | 65,534 characters |
| Maximum number of transactions | Limited by memory |
| Maximum number of connections | Limited by memory |
| Maximum number of files opened simultaneously | Limited by memory |
| Maximum number of tables opened per connection | Limited by memory |
| Maximum number of locks | Limited by memory |

|  |  |
| --- | --- |
| Maximum length of key expression text and maximum length of conditional expression text | 512 bytes\*\* |
| Maximum length of evaluated key expression | 4082 bytes\*\*\* |

 

\*\* The combined length of the index key expression text and conditional expression text must not be longer than 512 bytes.

\*\*\* The maximum length of an ADI index key is limited by the index page size. Refer to [Index Key Size and Page Size Relationships](master_index_key_size_and_page_size_relationships.htm) for the specific equations.

The maximum number of fields per table depends on field name lengths, and can be calculated by: 65135 / ( 10 + AverageFieldNameLength ). For example, if the average field name length is:

10 - then the maximum number of fields per table is 3256 fields

20 - then the maximum number of fields per table is 2171 fields

30 - then the maximum number of fields per table is 1628 fields.