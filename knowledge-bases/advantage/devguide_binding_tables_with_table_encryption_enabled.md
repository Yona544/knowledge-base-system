Binding Tables with Table Encryption Enabled




Advantage Database Server 12  

     Binding Tables with Table Encryption Enabled

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Binding Tables with Table Encryption Enabled  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Binding Tables with Table Encryption Enabled Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Binding\_Tables\_with\_Table\_Encryption\_Enabled Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 4 - Understanding Dictionaries > Binding Tables with Table Encryption Enabled / Dear Support Staff, |  |
| Binding Tables with Table Encryption Enabled  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

If you enable encryption for a data dictionary after binding tables to it, you must manually encrypt each existing table using the technique demonstrated in the preceding section. However, if you enable encryption prior to adding tables, those tables will be encrypted as they are added to the data dictionary. As a result, if you are creating a data dictionary from existing tables, you can save yourself some time by enabling encryption prior to adding the tables.

Use the following steps to add four more tables to the data dictionary:

1.        Right-click the TABLES node and select Add Existing Table(s).

|  |  |
| --- | --- |
| 2. | Using the Open dialog box, navigate to the directory in which you copied the sample tables, if necessary. Then, while keeping the Ctrl key depressed, click the DEPARTMENTS.ADT, INVOICE.ADT, ITEMS.ADT, and PRODUCTS.ADT tables to select them. With these four tables selected, click Open. |

|  |  |
| --- | --- |
| 3. | The Advantage Data Architect binds these four tables to the data dictionary, encrypting them in the process. |

|  |  |
| --- | --- |
| 4. | Your data dictionary should now contain six tables, as shown in   Figure 4-6. |

Figure 4-6: Adding tables after enabling table encryption automatically encrypts the newly added tables