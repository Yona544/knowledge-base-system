Replication Example




Advantage Database Server 12  

     Replication Example

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Replication Example  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Replication Example Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Replication\_Example Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 10 - Replication > Replication Example / Dear Support Staff, |  |
| Replication Example  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The following sections provide you with steps to implement replication for a simple unidirectional strategy. This example makes use of the DemoDictionary as the source data dictionary, and the restored backup you created in the preceding chapter as the target.

As mentioned in the beginning of this chapter, replication requires that ADS be on both the source and target, and also requires a replication license for the source. The two-user developer edition that accompanies this book is ADS, and it includes a replication license for testing purposes. Since both the source and the target are on your machine (as we are assuming in this book), you have met the necessary requirements to demonstrate replication.

Creating the Publication

Use the following steps to create a publication:

1.        From the DemoDictionary connection, right-click PUBLICATIONS and select Create.

|  |  |
| --- | --- |
| 2. | Leave Primary Key selected and click Next. |

|  |  |
| --- | --- |
| 3. | On the Select Tables to Publish page of the Advantage Publication Wizard, uncheck the checkbox next to TriggerTest. Click Next. |

|  |  |
| --- | --- |
| 4. | On the Enter Publication Name and Description page of the Advantage Publication Wizard, leave Publication Name set to DemoDictionary. Click Next. |

|  |  |
| --- | --- |
| 5. | Review the information displayed on the Complete Publication page of the Advantage Publication Wizard and then click Finish. |

|  |  |
| --- | --- |
| 6. | When the publication is complete, click Close to close both the Creating Publications and Articles dialog box and the Advantage Publication Wizard. |

You are now ready to configure the publication.

Configuring the Publication

Use the following steps to configure your publication:

1.        Right-click the DemoDictionary publication and select Properties from the displayed context menu.

|  |  |
| --- | --- |
| 2. | Select each table in turn and inspect which of its fields are used to identify its records. Check or uncheck fields as follows. For all tables except the ITEMS table, only the first field in the Row Identifiers list should be checked. For the ITEMS table, the first two fields should be checked. No filters are needed for this replication. When you are done configuring the publication, click OK to close the Publication dialog box. |

Your new publication is ready. In the next section you will create a subscription that will use this publication.

Creating the Subscription

Use the following steps to create a subscription for your publication:

1.        Right-click the SUBSCRIPTIONS node of the DemoDictionary connection and select Create.

|  |  |
| --- | --- |
| 2. | At Name, enter One-Way. Set Publication to DemoDictionary. For the Path field in the Target Database section, use the Browse button to select the restored backup that you created in Chapter 9. If you used the directory structures suggested in this book, this data dictionary should be located in c:\AdsBook\Restore. |

|  |  |
| --- | --- |
| 3. | Next, set User Name to ADSSYS and leave Password blank (assuming that you are using a blank password. Otherwise, enter the ADSSYS password at Password). |

|  |  |
| --- | --- |
| 4. | Click Advanced to display the Advanced page of the Subscription dialog box. |

|  |  |
| --- | --- |
| 5. | Leave Queue Table set to One-Way.adt. |

|  |  |
| --- | --- |
| 6. | Leave Target Connection set to Advantage Remote Server, and enable the option Ignore Replication Failures. |

|  |  |
| --- | --- |
| 7. | Click OK to save the subscription. |

The subscription is now active. Any changes you make to the replicated tables of the DemoDictionary connection are forwarded to the duplicate database.

If you want to later suspend this subscription, right-click the One-Way node under the SUBSCRIPTIONS node and select Properties. Place a checkmark in the Disable Subscription checkbox and click OK to save the change.

Observing Replication

Use the following steps to see the effects of replication on your target data dictionary tables:

Create a new connection to the restored data dictionary that you created in Chapter 9. To do this, select Connection | Create New Connection from the Advantage Data Architect's main menu.

From the New Connection dialog box, select Browse for Dictionary File from the ConnectionPath dropdown menu.

Browse to the directory in which the restored DemoDictionary.ADD is stored. If you used the suggested directory, this will be c:\AdsBook\Restore. Select DemoDictionary.ADD from this directory and click Open.

DatabaseName will automatically be set to DemoDictionary. Since you already have a connection with this name, you must change this value. At DatabaseName, enter RestoreDD.

Set ServerType to remote and BlankPassword to yes. Your New Connection dialog box should look something like the Connection Properties dialog box shown in Figure 10-13.

Figure 10-13: The Connection Properties dialog box shows settings for the database replication example

Click OK to save the new RestoreDD connection.

Connect to the DemoDictionary connection (if not already connected) and open the DEPARTMENTS table.

Connect to the RestoreDD connection and open the DEPARTMENTS table.

Return to the DemoDictionary DEPARTMENTS table and insert a new record. Set Department Code to 200 and Department Name to New Department. Click the Post button in the Navigator, or simply navigate off of the new record to post it.

Select the DEPARTMENTS table from the RestoreDD connection, and click the Refresh button in the Navigator (or press the F5 key). The new record should appear.

Return to the DemoDictionary DEPARTMENTS table. Change the new department name from New Department to Service. Click the Post button in the Navigator to post this new change.

Click the Refresh button on the RestoreDD DEPARTMENTS Table Browser. The changed department name now appears.

Return to the DemoDictionary DEPARTMENTS and delete the newly created record.

Click the Refresh button on the RestoreDD DEPARTMENTS Table Browser. The new record is no longer in the table.

Close both of the table browsers.

Right-click the subscription One-Way in the DemoDictionary connection and select Properties (or double-click the One-Way subscription). Check the Disable Subscription checkbox. Click OK to save your change.

   
WARNING: You should disable the One-Way subscription, as described in step 16 of the preceding example, in order to prevent potential problems as you work through the examples in this book. Replication is something that is often applied to a production database. Having replication enabled for a database that you are testing may produce errors that are difficult to resolve.