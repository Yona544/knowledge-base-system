Task 2: Create a Simple Browser




Advantage Database Server 12  

Task 2: Create a Simple Browser

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Task 2: Create a Simple Browser  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Task 2: Create a Simple Browser Advantage TDataSet Descendant ade\_Task\_2\_create\_a\_simple\_browser Advantage TDataSet Descendant > Developing and Distributing Applications > Developing a Sample Advantage-Enabled Delphi Application > Task 2: Create a Simple Browser / Dear Support Staff, |  |
| Task 2: Create a Simple Browser  Advantage TDataSet Descendant |  |  |  |  |

This task involves creating a simple application that can browse a database table. This browser will be the foundation for this sample application, so leave extra room on the form for components that will be added later.

Start a New Application

Open Delphi and select New Application from the File the menu.

Set Project Search Path

|  |  |
| --- | --- |
| · | Select Options from the Project menu. |

|  |  |
| --- | --- |
| · | Select the Directories/Conditionals tab. |

|  |  |
| --- | --- |
| · | If the installation program has not modified the search path to include your Advantage directory, enter the path to your TDataSet Descendant files in the Search Path edit box (the default directory is C:\Program Files\Advantage X.x\TDataSet\Delphi?\Win32). |

Note If you wish to set the same path to your TDataSet Descendant files for all projects, enter the path in the Delphi Environment Library. To access the Delphi Environment Library, choose Environment Options from the Tools menu and click the Library tab.

Change Window Caption

|  |  |
| --- | --- |
| · | Select Form1. |

Object Inspector:

Caption - My First Advantage-Enabled Application

Add DataSource

|  |  |
| --- | --- |
| · | Choose the Data Access tab on the Delphi Component Palette. |

|  |  |
| --- | --- |
| · | Select a DataSource component and place it on Form1. |

Object Inspector:

Name - dsCustomer

Figure 1Browser Layout

Add Data-Aware Controls

|  |  |
| --- | --- |
| · | Choose the Data Controls tab on the Delphi Component Palette. |

|  |  |
| --- | --- |
| · | Select a DBGrid component and place it on Form1. |

Object Inspector:

DataSource - dsCustomer

|  |  |
| --- | --- |
| · | Select a DBNavigator component and place it on Form1. |

Object Inspector:

DataSource - dsCustomer

Add DataSet Component

|  |  |
| --- | --- |
| · | Choose the Advantage tab from the Delphi Component Palette. |

|  |  |
| --- | --- |
| · | Select an AdsConnection component and place it on Form1. |

Object Inspector:

Name - cnCustomer

ConnectPath - X:\Ads\Data

|  |  |
| --- | --- |
| · | (Optional) If you want to use the Advantage Local Server instead of the Advantage Database Server, you will need to configure your application to attempt an Advantage Local Server connection. This is most easily accomplished by modifying the AdsServerTypes property accordingly. For more information on the possible AdsServerTypes combinations, see [Advantage Server Types](master_advantage_server_types.htm) |

Object Inspector:

AdsServerTypes - stADS\_LOCAL - True

|  |  |
| --- | --- |
| · | Select an AdsTable component and place it on Form1. |

Object Inspector:

Name - tblCustomer

AdsConnection - cnCustomer

TableName - Customer.adt

Link DataSource to DataSet

|  |  |
| --- | --- |
| · | Select the dsCustomer DataSource object in Form1. |

Object Inspector:

DataSet - tblCustomer

Figure 2Data Component Hierarchy

It is now possible, at design-time, to open the table and fill the grid. To do this, select tblCustomer and change its Active property to True. The table will be opened and your grid will fill with data. If you do not see any records in your grid, or if you receive an error, carefully re-trace each step above. After verifying your table setup is correct change the Active property back to False.

Add Open/Close Functionality

|  |  |
| --- | --- |
| · | Choose the Standard tab on the Delphi Component Palette. |

|  |  |
| --- | --- |
| · | Select a GroupBox component and place it on Form1. |

|  |  |
| --- | --- |
| · | Choose the Standard tab on the Delphi Component Palette. |

|  |  |
| --- | --- |
| · | Select a Button component and place it in the Table groupbox on Form1. |

|  |  |
| --- | --- |
| · | Double-click the Open/Close button and add the following code to the OnClick event handler: |

procedure TForm1.btnOpenCloseClick(Sender: TObject);  
begin  
  tblCustomer.Active := not tblCustomer.Active;  
end;

Add Exit Button

|  |  |
| --- | --- |
| · | Choose the Standard tab on the Delphi Component Palette. |

|  |  |
| --- | --- |
| · | Select a Button component and place it in the bottom right corner of Form1. |

Object Inspector:

Name - btnExit

Caption - Exit

|  |  |
| --- | --- |
| · | Double-click the Exit button and add the following code to the OnClick event handler: |

procedure TForm1.btnExitClick(Sender: TObject);  
begin  
  Close;   
end;

Save and Run

|  |  |
| --- | --- |
| · | Select Save All from the File menu. |

|  |  |
| --- | --- |
| · | Select Run from the Run menu, or press the [F9] key to build and run your application. |