Opening Tables




Advantage Database Server 12  

Opening Tables

Advantage Data Architect

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Opening Tables  Advantage Data Architect |  |  | Feedback on: Advantage Database Server 12 - Opening Tables Advantage Data Architect arc\_Opening\_tables Advantage Data Architect > Tables > Opening Tables / Dear Support Staff, |  |
| Opening Tables  Advantage Data Architect |  |  |  |  |

Once you have established a connection in the Connection Repository, you can open a table by double-clicking on the table in the Connection Repository tree view, or by right-clicking on a table and selecting Open.

You can also open a table that is not associated with a Connection Repository connection by following the steps below:

Choose File | Open Table from the menu or click Open Table on the toolbar.

To open a free table:

Select Alias or Path to specify the alias or path to the directory that contains the [free table](javascript:hhpopuplink.TextPopup(popid_607755236X,FontFace,-1,-1,-1,-1)) to be opened. If Alias is chosen, the [free connection](javascript:hhpopuplink.TextPopup(popid_1109492976,FontFace,-1,-1,-1,-1)) alias may be chosen from the drop-down list. If Path is chosen, the path to the directory that contains the free tables can be entered by hand or can be selected via the Browse option. The File(s) name should be the free table you want to open.

If the free table is encrypted, you will be prompted for the password. Note that it is possible to specify passwords in the ExtraConnectString property in the connection repository for the current connection.  For example, provide it as "EncryptionPassword=table1=password1,table2=password2;"  Or if all free tables use the same password, "EncryptionPassword=freetablepassword;".  Note, though, that this information is persisted in the ads.ini file on disk without any encryption. So anyone with access to the machine can view the passwords.

To open a database table (in the Advantage Data Dictionary):

To open a [database table](javascript:hhpopuplink.TextPopup(popid_201684107,FontFace,-1,-1,-1,-1)) that is a member of an Advantage Data Dictionary, select Alias or Dictionary to specify the alias or data dictionary name of the data dictionary file (\*.add). For example, if a database table is part of the Advantage Data Dictionary sampledb, the Dictionary option can be selected and the dictionary path would be something like c:\data\sampledb.add. The File(s) drop-down list files will be populated with all of the database tables and views that are contained in the Advantage Data Dictionary.

After selecting OK, the [Table Browser](arc_table_browser.htm) will be displayed.