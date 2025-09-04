Index Files (CDX, IDX, NTX)




Advantage Database Server 12  

Index Files (CDX, IDX, NTX)

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Index Files (CDX, IDX, NTX)  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Index Files (CDX, IDX, NTX) Advantage Concepts master\_Index\_files\_cdx\_idx\_ntx\_ Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Index Files (CDX, IDX, NTX)  Advantage Concepts |  |  |  |  |

Single Order Index Files (IDX, NTX)

The Advantage Database Server supports single order Xbase index files in the IDX and NTX formats. The syntax to build these two index file types is identical. Only the internal file formats are different. IDX index files are a FoxPro defined index format while NTX index files are a CA-Clipper defined format.

The index format is determined by the database driver used in your application. For example, the Advantage NTX driver will build NTX indexes. For IDX indexes, use the Advantage CDX driver.

IDX index files save disk space and will increase the speed of an operation when accessing large data sets. Key data is stored in a compressed format. An IDX index can be up to 90% smaller than an equivalent NTX index. The amount of compression depends on the number of duplicate keys, trailing blanks in the character keys, and blank keys in the index.

Multiple Order (Compound) Index Files (CDX)

The Advantage Database Server supports multiple order (compound) Xbase index files in the CDX format. CDX index files are a FoxPro defined index format. A "tag" is a single index order within a CDX. A tag is essentially identical to a single order IDX index file and supports all of the same features. Once a compound index file is opened, all tags contained in the file are automatically updated as the records are changed. By default, the first tag in the compound index file (in order of creation) is the active tag when the index file is explicitly opened. A tag name in a CDX index file is limited to 10 characters in length and may only contain the letters 'a'-'z' and 'A'-'Z', digits '0'-'9', and the underscore '\_' character.

Structural CDX

A structural CDX is also known as an "auto-open" index file. A CDX is considered a "structural" index file when the index file has the same base name and resides in the same directory as the table. The structural CDX will be opened automatically when the table is opened and cannot be closed as long as the table is open.

Non-structural CDX

All CDX index files that do not have the same base file name as the corresponding table is considered "non-structural" and will not be automatically opened when the table is opened.

See Also

[Xbase File Format Specifications](master_xbase_file_format_specifications.htm)