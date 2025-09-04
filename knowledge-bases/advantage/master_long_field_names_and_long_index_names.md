Long Field Names and Long Index Names




Advantage Database Server 12  

Long Field Names and Long Index Names

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Long Field Names and Long Index Names  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Long Field Names and Long Index Names Advantage Concepts master\_Long\_field\_names\_and\_long\_index\_names Advantage Concepts > Advantage File Formats > Advantage Proprietary File Format > Long Field Names and Long Index Names / Dear Support Staff, |  |
| Long Field Names and Long Index Names  Advantage Concepts |  |  |  |  |

Field names and index order names in the Xbase file format are limited to 10 characters in length. However, if you are using Visual FoxPro (VFP) tables in a data dictionary, field names can be up to 128 characters in length. Note, though, that the field names stored in the physical table are still only 10 characters so if the table becomes separated from the dictionary without using a standard method for removing tables from dictionaries (e.g., SQL, Advantage Client Engine API, or Advantage Data Architect), then the associated indexes might not be valid. This is because when long field names are used with Visual FoxPro tables, the index key expressions include the long name, so those key expressions would no longer match the table.

Field names and index order names in the Advantage proprietary file format can be up to 128 characters in length. Because the long field names are stored in the table itself, there are fewer potential problems if a table is inadvertently separated from the dictionary. If you have the need for field names or index order names longer than 10 characters, you may want to choose the Advantage proprietary file format.