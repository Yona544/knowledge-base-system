Task 9: Add FindKey/FindNearest Functionality




Advantage Database Server 12  

Task 9: Add FindKey/FindNearest Functionality

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Task 9: Add FindKey/FindNearest Functionality  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Task 9: Add FindKey/FindNearest Functionality Advantage TDataSet Descendant ade\_Task\_9\_add\_findkey\_findnearest\_functionality Advantage TDataSet Descendant > Developing and Distributing Applications > Developing a Sample Advantage-Enabled Delphi Application > Task 9: Add FindKey/FindNearest Functionality / Dear Support Staff, |  |
| Task 9: Add FindKey/FindNearest Functionality  Advantage TDataSet Descendant |  |  |  |  |

In this task you will add the ability to your application to do a FindKey or FindNearest. FindKey/FindNearest are in general very fast, but they require an index on the key in question. See [Seek](master_seek_movement.htm) for more information.

Add Find GroupBox

|  |  |
| --- | --- |
| · | Choose the Standard tab on the Delphi Component Palette. |

|  |  |
| --- | --- |
| · | Select a GroupBox component and place it on Form1. |

Object Inspector:

Name - grpbxFind

Caption - Find

Figure 11 - Browser with the New Find GroupBox ... completing your sample application

Add Find Edit Box and Exact Checkbox

|  |  |
| --- | --- |
| · | Choose the Standard tab on the Delphi Component Palette. |

|  |  |
| --- | --- |
| · | Select an Edit component and place it in the Find groupbox. |

Object Inspector:

Name - ebFindValue

Text - " (empty string)

|  |  |
| --- | --- |
| · | Select a CheckBox component and place it in the Find groupbox. |

Object Inspector:

Name - chkbxExact

Caption - Exact

Add Find Button and Code

|  |  |
| --- | --- |
| · | Choose the Standard tab on the Delphi Component Palette. |

|  |  |
| --- | --- |
| · | Select a Button component and place it in the Find groupbox. |

Object Inspector:

Name - btnFind

Caption - Find

|  |  |
| --- | --- |
| · | Double-click the Find button and add the following code to the OnClick event handler: |

procedure TForm1.btnFindClick(Sender: TObject);  
begin  
  if chkbxExact.Checked then   
    tblCustomer.FindKey( [ebFindValue.Text] )   
  else   
    tblCustomer.FindNearest( [ebFindValue.Text] );   
end;

Save and Run

|  |  |
| --- | --- |
| · | Select Save All from the File menu. |

|  |  |
| --- | --- |
| · | Select Run from the Run menu, or press the [F9] key to build and run your application. |

Congratulations!

Congratulations, you have completed your first Advantage Delphi application!