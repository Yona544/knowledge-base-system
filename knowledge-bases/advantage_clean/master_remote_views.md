---
title: Master Remote Views
slug: master_remote_views
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_remote_views.htm
source: Advantage CHM
tags:
  - master
checksum: bb30ef7c94da4c8915eccc379ae08317f9b73d1b
---

# Master Remote Views

Remote Views

Remote Views

Advantage and Visual FoxPro

| Remote Views  Advantage and Visual FoxPro |  |  |  |  |

Remote views use ODBC to access data that is external to Visual FoxPro. If you are already using local views in Visual FoxPro, switching to a remote view to access the same data through Advantage may be the simplest option. Note that in order to use a remote view, you must have a database open in your project. Visual FoxPro stores information about the remote view in the DBC.

When creating a remote view, it may be desirable to limit the rows that are returned from the table through a WHERE clause (the Filter tab in the View Designer provides access to this functionality). When opening a view, the default behavior is to read all records from the view. If the table is large, this can be an expensive operation.

In order to use a remote view with Advantage, you must have the Advantage ODBC driver installed. A simple way to use a remote view is to use an ODBC data source to specify connection information. You can set up an ODBC data source through the Windows Control Panel. There is usually an icon named "Data Sources (ODBC)" that provides access to the ODBC administrator. You can also start it from a command prompt with the command ODBCAD32.EXE.

If you plan to share DBF tables with Visual FoxPros native data access and Advantage at the same time, you should choose the "Compatible" option for the "Advantage Locking" choice in the Advantage ODBC driver setup dialog. If you choose "Proprietary" and are using Advantage Database Server (remote server), then Visual FoxPro will not be able to access the tables, because Advantage opens tables in a mode that allows other applications to only open the table in a read-only mode.

The ODBC setup dialog defaults to a table type setting of "Advantage". This table type is used to access Advantage proprietary format tables (ADT tables). Change this value to "Visual FoxPro".

If you do not have Advantage Database Server (remote server) available, you should make sure that only "Local Server (ALS)" is selected in the Advantage ODBC setup dialog. This will speed up the connection to Advantage. If both the remote and local option are chosen, then the ODBC driver will attempt a remote server connection that must first fail before it scales back to the local option.

Creating a Remote View

| 1. | One way to create a remote view is through the Project Manager in Visual FoxPro. Choose the Data tab, expand the Databases tree, click on the Remote Views tree and click the New button. This will show a dialog that prompts for a connection or data source. If you do not have any connections defined, you can select an ODBC data source by choosing the "Available data sources" option. Once you have selected a connection or data source, click OK and the view designer will be shown. At this point, you can choose which columns the view should contain. |

| 2. | Another way to create a remote view is with the CREATE SQL VIEW command in Visual FoxPro. For example, the following command will create a remote view named MyView that retrieves all columns from a table named test. It uses an ODBC data source named ADS. |

CREATE SQL VIEW MyView REMOTE CONNECTION ADS as select \* from test

Once the view is created, you can modify it with the view designer the same as if you created it in the project manager.

| 3. | After you have created a remote view, you can use it much like you would a normal table. For example, the commands "use MyView" and "Browse" will open the view and display the results in the Browse window. |

Making a Remote View Editable

The steps described above will create a remote view that can be used to bring data into Visual FoxPro from Advantage. In order for Visual FoxPro to be able to save any edits back to the physical table, it is necessary to provide the information that allows Visual FoxPro to generate the SQL statements to perform the updates. A simple way to do this is through the View Designer.

| 1. | Open the view designer for the remote view. For example, you can use the command "MODIFY VIEW MyView". |

| 2. | Click on the "Update Criteria" tab in the View Designer. |

| 3. | This tab shows the list of available fields. Choose the key fields that uniquely identify a record by clicking in the left-most column of the list (under the key icon). |

| 4. | Select which fields should be updatable by clicking in the second column in the field list or simply click the "Update All" button to make all fields updatable. |

| 5. | Select the "Send SQL updates" check box. If this is not selected, Visual FoxPro will not send the update statements to Advantage and edits will not be saved. |

See Also

[Getting Started with Visual FoxPro](master_getting_started_with_visual_foxpro.md)

[Cursor Adapters](master_cursor_adapters.md)

[SQL Pass Through](master_sql_pass_through.md)
