BLOB Functions




Advantage Database Server 12  

BLOB Functions

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| BLOB Functions  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - BLOB Functions Advantage Visual Objects and Vulcan.NET RDD vo\_Blob\_functions Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Advanced  Functions > BLOB Functions / Dear Support Staff, |  |
| BLOB Functions  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Any data types, such as arrays, characters and BLOBs can be stored in an .fpt memo field. The term "BLOB" is an acronym for Binary Large Object, which means any type of binary data, not just plain ASCII text that would normally be associated with memo fields. This allows for large amounts of any data type to be saved into a memo field for quick reference. A common use of this feature is to save user interface screens into the field rather than generating a fresh screen with code. Also, graphic images may be cut and pasted from the Clipboard to a memo field. This can provide significant performance gains, depending on your application. Advantage provides two functions for BLOBs, one that writes a BLOB contained in a memo field to a file, and one that stores the contents of a file into a memo field.

[AX\_BLOB2File()](vo_ax_blob2file.htm)

[AX\_File2BLOB()](vo_ax_file2blob.htm)