Table Maintenance




Advantage Database Server 12  

     Table Maintenance

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Table Maintenance  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Table Maintenance Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Table\_Maintenance Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 2 - Creating Tables > Table Maintenance / Dear Support Staff, |  |
| Table Maintenance  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Depending on the type of ADS table you are working with, and whether or not you are using ADS versus ALS, there are a couple of maintenance tasks that you might have to perform periodically on tables.

For example, if you are using DBF tables, you will probably need to pack them from time to time, in order to recover space occupied by deleted records. With ADT tables, packing is not always necessary.

Similarly, if you are using ALS, there exists a real possibility that a hardware or software problem may cause one or more of a table's indexes to become corrupted. If this happens, you will have to rebuild the table's indexes. Index corruption is rare or nonexistent when you are using ADS.

The following sections describe how to perform basic table maintenance tasks from the Advantage Data Architect. Note, however, that these same tasks can be performed at runtime from a client application. See the documentation for the particular data access mechanism you are using for information on how to add these maintenance tasks to your client applications.

Packing Tables

As you have learned, records deleted from a DBF file are marked for deletion, but continue to occupy space in the underlying table. Unlike ADT tables, which reuse the space occupied by deleted records when new records are added, you must take explicit steps to recover the space occupied by deleted records with DBF files. This process is referred to as packing.

To pack a table, open it in the Table Browser, right-click and select Pack from the context menu. You must be able to obtain exclusive access to a table in order to pack it. Also, if the table has a large number of records, packing may take a while.

Although packing is a process most often associated with DBF files, you can also pack an ADT table. As with DBF tables, packing an ADT table removes all records that have been deleted. Since an ADT table can reuse deleted records automatically, packing an ADT table is usually only necessary if you have deleted a large number of records, do not plan to add many new records, and want to recover available space in the underlying ADT file.

One very specific scenario in which you may want to pack an ADS table occasionally occurs if you are using memo files. A memo file will have orphaned memo pages if a memo field's contents for a record (any binary, image, or memo data) are added and are then deleted, and that record's memo field now has no data in it. Packing an ADT table with frequent changes of this type to a memo file will recover disk space.

   
NOTE: When you delete a record with data in binary, image, or memo fields, the associated space in the memo file will be available for reuse when future data is written to the memo file.  
 

 

   
CAUTION: Packing a DBF table permanently destroys any records deleted prior to the packing, making them unrecallable. ADT table records become un-recallable when you pack the table or when newly inserted records reuse the space occupied by recently deleted records.  
 

Emptying Tables

When you empty, or zap, a table, you permanently remove all records from that table, losing the data forever. Note that you must be able to obtain exclusive access to a table in order to empty it. In order to empty a table, open it in the Table Browser, right-click and select Empty from the displayed context menu. When you do, the Table Browser will display the following warning dialog box asking you to confirm that you want to remove all data from the table:

Select Yes from the Warning dialog box. A second dialog box is displayed, asking you to repeat your confirmation. Select Yes again to permanently remove all data from the table.

Deleting Some, But Not All Records

It is possible to delete one or more records at the same time from the Table Browser without entirely emptying the table. To delete just one record, position your cursor on the record you want to delete and click the Delete button on the Table Browser navigator. When the Confirm dialog box asks you to confirm the deletion, select Yes.

To delete more than one record, use the following steps:

With the table open in the Table Browser, select the records that you want to delete. If the records you want to delete are consecutive records, select the first record in the range, depress the Shift key and then click the last record in the range. All records in the range will be highlighted. To select records that are not consecutive, hold down the Ctrl key while you click the individual records that you want to delete. Each time you click a record with the Ctrl key depressed, that record will be selected (Ctrl-click a selected record to remove the highlighting.) If some records are consecutive and others are not, begin by select the consecutive records using the click, Shift-click technique, and then select the remaining nonconsecutive records using Ctrl-click.

Once you have selected all of the records that you want to delete, right-click the Table Browser and select Delete Records (or press Ctrl-Del).

From the Confirm dialog box, select Yes to delete the highlighted records.

Restoring/Recalling Deleted Records

With DBF tables, records that have been deleted may be recoverable. The deleted records are simply marked as deleted, and can be restored, or recalled, so long as you have not packed a table since the records were deleted.

The Table Browser actually provides you with two options for recalling deleted records for DBF tables. The first is to recall a deleted record that is currently active in the Table Browser. To recall the currently active deleted record, right-click the Table Browser and select Recall Current Record from the displayed context menu.

If you want to recall all recoverable records in a DBF table, right-click the Table Browser and select Recall All Records from the context menu.

With ADT tables, you cannot recall deleted records from the Table Browser. This is consistent with deleted record management in other mainstream DBMSs (Database Management Systems). However, with Advantage 7.0 and later, you can use the ACE API AdsRecallAllRecords to programmatically recover delete records, so long as the space that they occupy in the table has not yet been reused. Specifically, if new records have been added to an ADT table since a given record was deleted, it is unlikely that that deleted record is still available in the table. (In a multiuser environment it may be difficult to recall records.) In those cases, the deleted record is unrecoverable. See the ADS help for more information on AdsRecallAllRecords.

Re-Indexing Tables

Re-indexing a table rebuilds that table's indexes from scratch. In most cases, there are three conditions under which you will need to re-index a table. First, you need to re-index a table if you have changed the ANSI collation or the localized OEM character set that your server and all of its client applications are using. The rebuilt indexes will then use the new collation sequence or OEM character set.

The second condition is when your current indexes become highly fragmented. An index can become fragmented over time if the fields involved in one or more of an index's tags, or index orders, have had unusual patterns of data. For example, if an indexed field of a large table has a great variety of different values, and then over time that same field becomes somewhat homogenous, and then later becomes varied again, the index can get fragmented.

The effect of a fragmented index is that operations using that index are slow compared to when the index was originally built. If you suspect that your database performance is being hurt by fragmented indexes, you should rebuild the indexes to restore your database's performance.

The third condition is when one or more of your index files become corrupt. This can happen when you fail to open all index files for a free table prior to editing the table. (With database tables, all index files are auto-open indexes, thereby preventing index corruption from this source.) Index files can also become corrupt if there is a failure in a workstation or the network when a client application is accessing data using the Advantage Local Server. Re-indexing rebuilds the indexes, removing any corruption in the process.

To re-index a table in the Table Browser, right-click and select Re-Index from the displayed context menu. Note that you must be able to obtain exclusive access to a table to re-index it. As a result, you may want to open the table you want to re-index using the Advanced Open feature, selecting to specifically open the table in exclusive mode, before continuing. If you chose not to, however, the Advantage Data Architect will attempt the exclusive open on your behalf when you choose to re-index. Indexes are discussed in detail in Chapter 3.

Changing a Table's Structure

A table's structure consists of its field definitions, and you design this structure based on your application's storage needs. Unfortunately, these needs tend to change over time. In a simple case, while testing your client application you might find that you did not allocate enough space for one or more of your character fields. For example, you might find that 12 characters is insufficient for your Last Name field, making it necessary for you to increase this field's size to 18 characters or more.

A more complicated situation may require you to add one or more fields to a table. As an application enters its prototype stage, you sometimes discover that data essential to the application was not considered in the original design. As a result, you may need to add one or more fields to one or more of your application's tables.

Fortunately, the Advantage Data Architect makes it easy to modify the structure of an existing table, whether you need to simply change the size or precision of an existing field, or to add fields to or remove fields from the table.

The following steps show you how to change the structure of the CUST.ADT table you created earlier in this example:

Right-click the CUST.ADT table in the Table Browser and select Properties from the displayed context menu. (You can also right-click the table node in the Connection Repository and select Properties.) The Table Designer, which you used to initially define this table's structure, is shown in the Fields tab of the Table Designer.

Select the Last Name field in the Field Names list. Change the Size value in the Field Properties list from 18 to 24.

Click Add Field. For the field name, enter Time Last Accessed.

Set Data Type to ModTime.

Drag the Time Last Accessed field to position it above the Comment field in the table structure. (To do this, press and hold down your left mouse button on the field name, move your mouse so that your mouse pointer appears over the Comments field and release your left mouse button.) The Time Last Accessed field should now appear above Comments.

Figure 2-7: The new table structure in the Table Designer

Your new table structure should look something like that shown in Figure 2-7.  
In addition to changing field definitions and adding fields, you can remove fields, as well as change the order of fields in the table's structure. To remove a field, select the field you want to remove and click the Delete Field button. To change a field's position in a table's structure, select the field whose position you want to change and drag it to a new location in the Field Names list.

When you are done, click OK to apply the changes to your table's structure.

   
NOTE: ADS also creates backup files of table, index, and memo files. They are given names identical to your original files but with the extensions .adt.bak, .adi.bak, and .adm.bak, respectively.  
 

A couple of comments about restructuring a table are in order. First, while the Advantage Data Architect will automatically attempt to gain exclusive access to a table before applying the new structure, in a multiuser environment you may want to use Advanced Open and explicitly open the table in exclusive mode before you start restructuring.

The second point is related to your client applications. Changing the structure of a table will often have an impact on the client applications that use the table. It is very important that you test all client applications following the restructuring of a table to ensure that the applications are running correctly, and to correct any problems that the restructuring may have introduced.

Adding Indexes

Indexes play a very important role in the design of Advantage tables. Not only do they permit you to view a table sorted by one or more fields, but they also are the source of much of Advantage's performance. Consequently, once you create a table, you will nearly always add one or more indexes to it.

You add one or more indexes to a table, or remove an existing index from a table in one of two ways: using the Index option in the Field Properties column of the Table Designer, or using the Additional Index Definitions page of the Table Designer. Creating and managing indexes is discussed in detail in Chapter 3.

Schemas for Table Structures

The Schema menu in the Table Designer allows you to save and reuse existing schemas of field and index definitions. To create a schema template from an existing tables table structure, display the table whose structure you want to create a schema template for in the Table Designer (select the table in the Connection Repository, right-click and select Properties) and select Schema | Save As from the Table Designer's menu. In the Save As dialog box, enter a name for the .arcschema file you want to save.

To create a new schema template, create a table with the table structure you would like to save as a template. Then instead of saving the table, save it as a schema template by selecting Schema | Save As. Enter a name for the .arcschema file in the Save As dialog box.

To create a new table using an existing schema, select File | New Table (or press Ctrl-N). Select Schema | Load to display the Load Schema dialog box. Select the desired schema template file (.arcschema file extension) and click the Save button. The table structure and indexes defined in the schema are used for the table structure and are displayed in the Table Designer. You can then make changes to the field and index definitions in the Table Designer. At this point, you can either save the table by clicking OK in the Table Designer, or you can save a new schema template using the steps just described.

You can also delete schemas you no longer want by selecting Schema | Delete from the Table Designer's menu.

Printing Table Structures

You can print out your table structure by selecting Schema | Print from the Table Designer's menu. Alternatively, you can print your table structure using a more detailed format by selecting Schema | Print from template. An Open dialog box is displayed. Select the DetailedDictionary.rtm report type (the SimpleTypes.rtm report is used with the Schema | Print option). Once you select either of these Print options, a report of the table schema is shown in a Print Preview window. Select the Printer icon to print the report.