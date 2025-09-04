Index Files (ADI)




Advantage Database Server 12  

Index Files (ADI)

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Index Files (ADI)  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Index Files (ADI) Advantage Concepts master\_Index\_files\_adi Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Index Files (ADI)  Advantage Concepts |  |  |  |  |

The Advantage Database Server supports a proprietary multiple order (compound) ADI index file. A "tag" is a single index order within an ADI. ADI index orders save disk space and will increase the speed of an operation when accessing large data sets. Key data is stored in a compressed format. Once an ADI index file is opened, all tags contained in the file are automatically updated as the records are changed. By default, the first tag in the ADI index file (in order of creation) is the active tag when the index file is explicitly opened. A tag name in an ADI index file is limited to 128 characters in length and may contain any character value except 0 (NULL), ';' (a semi-colon), or ',' (a comma).

Auto-Open ADI

An ADI index that is associated with a [free table](javascript:hhpopuplink.TextPopup(popid_23765432X,FontFace,-1,-1,-1,-1)) is considered an "auto-open" index file when the index file has the same base name and resides in the same directory as the table. The auto-open ADI will be opened automatically when the table is opened and cannot be closed as long as the table is open. All ADI indexes that are associated with [database tables](javascript:hhpopuplink.TextPopup(popid_484727561X,FontFace,-1,-1,-1,-1)) are auto-open indexes as those indexes are opened when the database table is opened.

Non-Auto-Open ADI

All ADI index files that are associated with a [free table](javascript:hhpopuplink.TextPopup(popid_23765432X,FontFace,-1,-1,-1,-1)) that do not have the same base file name as the corresponding table are considered "non-auto-open" and will not be automatically opened when the table is opened.

See Also

[Advantage Proprietary File Format Specifications](master_advantage_proprietary_file_format_specifications.htm)