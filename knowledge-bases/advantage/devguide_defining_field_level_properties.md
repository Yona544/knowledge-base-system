Defining Field-Level Properties




Advantage Database Server 12  

     Defining Field-Level Properties

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Defining Field-Level Properties  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Defining Field-Level Properties Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Defining\_Field\_Level\_Properties Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 5 - Constraints and RI > Defining Field-Level Properties / Dear Support Staff, |  |
| Defining Field-Level Properties  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You define field-level properties using the Fields page of the Table Designer. Figure 5-1 shows the Fields page of the Table Designer for the CUSTOMER table in the DemoDictionary data dictionary.

Figure 5-1: The Fields page of the Table Designer

   
NOTE: The steps for creating the DemoDictionary data dictionary are described in Chapter 4. If you did not create this data dictionary, and want to follow along with the examples in this chapter, you should return to Chapter 4 and create this data dictionary before continuing.  
 

As you learned in Chapter 2, the Fields page of the Table Designer serves several purposes. First, it displays a list of the fields of the associated table, ordered by the table's structure. When you select one of the fields from this list, you can view its metadata, including its name, its type, its width (in bytes), and its precision (where applicable).

The second purpose is to permit you to change the table's structure. You can add and remove fields, change the order of fields in the table's structure, and modify the data type of fields.

The third purpose is to permit you to modify individual field properties. These properties include index, NULL valid, default value, description, and field-level constraints. These properties are described in the following sections.

The Index Property

The Index property permits you to effortlessly create single-field expression indexes on most field types. No index is created when Index is set to No. Set Index to Yes to create a single-field expression index on the field.

When you set Index to Unique, a single-field expression index is also created on the field. This index is also a unique index. Set Index to Primary to create a single-field expression index that is also designated as the primary index of the table. The designated primary index is used by the replication and referential integrity features of a data dictionary.

The NULL Valid Property

The NULL Valid property controls whether the field is a required field or not. When you set NULL Valid to No, an exception is raised if the client attempts to post a record to the table where this field has not been assigned a value. The default value for NULL Valid is Yes.

The Default Value Property

The Default Value property permits you to define a default value for a field. When a new record is being inserted, fields that have not been assigned a value will be assigned the default value. If no default value is specified, fields that are not assigned a value when the record is being inserted will contain the value of NULL.

Imagine, for instance, that you have a sales rep table, and that one of the fields of the sales rep table is the code for the office to which the employee is assigned. You may define that the default value for the office field is a value (say 100) that indicates that no office has yet been assigned. In a situation like this one, this default value would be a valid key field in the related table that contains information about offices.

The Description Property

You can use the Description property to store a description for each field in the table. While adding a description to each field is optional, you can use this feature within your client applications to provide data-driven help about each field.

The value of the Description field, as well as all other properties of fields, can be queried at runtime by your client applications. For example, if a user asks for a field description, you can dynamically determine which field and which table the user is interested in, and extract the description from the system.columns system table. The following is an example of a parameterized query that will return the contents of the Description property for a given field and table:

SELECT [Comment] FROM system.columns   
  WHERE [Parent] = :Table AND [Name] = :Field

Field-Level Constraints

The field-level constraints are pretty self-explanatory. The Minimum Value and Maximum Value fields define the acceptable range for data. Fields containing data that exceed either of these limits are rejected. If no minimum or maximum value is set, the data type of the field will define the field's limits.

When a record cannot be posted because at least one field's field-level constraint is violated, Advantage generates an error that includes the Advantage error code as well as a description of the error. For example, if you set a minimum value of 0 for a field named Retail Price, and then a client application attempts to post a record where the Retail Price value is a negative number, Advantage will generate an error message similar to the one shown here:

When you configure at least one of the field-level constraints for a particular field, you have the option of providing a custom error message that will be displayed in place of the descriptive text that Advantage would have added to the error message. For example, if you assign the text Retail Price must be a positive value to the Failed Validation Message field, attempting to post a record with a negative retail price will produce this error message:

How Field-Level Constraints Are Applied

After you assign one or more constraints to a table's fields, you click the OK button on the Table Designer to apply your changes. What happens next depends on whether existing data in your table conforms to the new constraints or not. If all of your existing data is consistent with your constraints, everything will be fine. Your table will remain intact with all of its data.

If one or more of your existing records violate one or more of the constraints that you have applied, those records are removed from your table and placed into a temporary table. Furthermore, that temporary table is displayed in a special dialog box. A message that appears along the top of this dialog box indicates that it contains records that were removed due to constraint violations, as shown in Figure 5-2.

Figure 5-2: Records that violate newly added constraints are placed into a temporary table

What you do if constraints remove one or more records from a table depends on how you view the records that were removed. If those removed records really are invalid, and you no longer want them, click the Discard button. The records will be deleted and the dialog box will close.

On the other hand, if you do not want to lose these records, you have two choices. If the new constraints are correct, you can fix each record that you want to keep and then click Save to return the updated records back to the original table.

The second choice is to export these records to a new or existing table. At a minimum, this saves a copy of your records, permitting you to decide how to deal with these records later. For example, after doing some research, you might delete the records that you know are bad, fix the records that are good, and even make adjustments to one or more of your constraints. You can then insert the saved good records back into the original table (using an INSERT query, for example). The most important aspect of exporting to a new or existing table is that you can take your time to decide which records or constraints need adjustment.

Field-Level Constraint Example

The following steps demonstrate how to add field-level constraints to a table:

Right-click the PRODUCTS table under the TABLES node of the DemoDictionary connection in the Connection Repository, and select Properties.

Select the Product Code field in the Field Names list, and then set the NULL Valid property to No.

Select the Retail Price field in the Field Names list. Set the NULL Valid property to No, and set the Minimum Value property to 0.

Finally, at Failed Validation Message, enter Retail Price must be a positive value and press Enter. Your screen should look similar to that shown in Figure 5-3.

Click OK to close the Table Designer and apply the new constraints. Since no data in the Product table violated any of the new constraints, the constraints are applied without removing records from the Products table.

Figure 5-3: New constraints added to the Retail Price field of the Products table