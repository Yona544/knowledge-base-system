---
title: Ade Task 7 Add Index Creation Capability
slug: ade_task_7_add_index_creation_capability
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_task_7_add_index_creation_capability.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: b47cd67f0705beec58fb03c1cdee1c9147ec633c
---

# Ade Task 7 Add Index Creation Capability

Task 7: Add Index Creation Capability

Task 7: Add Index Creation Capability

Advantage TDataSet Descendant

| Task 7: Add Index Creation Capability  Advantage TDataSet Descendant |  |  |  |  |

In this task you will add the ability to create new indexes to your application.

Create a New Form (Form3)

- Select New Form from the File menu.

Object Inspector:

Caption - Create Index

- Choose Use Unit from the File menu and double-click Unit1. This step allows Form3 to access objects and methods that belong to Form1. This link must be established to access the table component on Form1.

Add Indexname and Expression Edit Boxes

- Choose the Standard tab on the Delphi Component Palette.

- Select a Label component and place it on Form3.

Object Inspector:

Caption - Index Name

- Select an Edit component and place it next to the Index Name label.

Object Inspector:

Name - ebIndexName

Text - " (empty string)

- Select a Label component and place it on Form3 below the Index Name label.

Object Inspector:

Caption - Expression

- Select an Edit component and place it next to the Expression label.

Object Inspector:

Name - ebExpression

Text - " (empty string)

Figure 7 - Index Creation Form Layout

Add Options GroupBox

- Choose the Standard tab on the Delphi Component Palette.

- Select a GroupBox component and place it on Form3.

Object Inspector:

Name - grpbxOptions

Caption - Options

- Select a CheckBox component and place it in the Options groupbox.

Object Inspector:

Name - chkbxUnique

Caption - ixUnique

- Select a CheckBox component and place it in the Options groupbox.

Object Inspector:

Name - chkbxDescending

Caption - ixDescending

- Select a CheckBox component and place it in the Options groupbox.

Object Inspector:

Name - chkbxCaseInsensitive

Caption - ixCaseInsensitive

Add Create and Close Buttons

- Choose the Standard tab on the Delphi Component Palette.

- Select a Button component and place it on Form3.

Object Inspector:

Name - btnCreate

Caption - Create

- Double-click the Create button and add the following code to the OnClick event handler:

procedure TForm3.btnCreateClick(Sender: TObject);  
var  
  setOptions : TIndexOptions;   
begin  
  setOptions := [];   
  if chkbxUnique.Checked = TRUE then   
    setOptions := setOptions + [ixUnique];   
  if chkbxDescending.Checked = TRUE then   
    setOptions := setOptions + [ixDescending];   
  if chkbxCaseInsensitive.Checked = TRUE then  
    setOptions := setOptions + [ixCaseInsensitive];

   
  {\* close the table and open it for exclusive use \*}   
  with Form1.tblCustomer do   
  begin   
    Close;   
    Exclusive := TRUE;   
    Open;   
    AddIndex( ebIndexName.text, ebExpression.text, setOptions );   
    {\* re-open shared \*}   
    Close;   
    Exclusive := FALSE;   
    Open;   
  end;   
end;

- To use the setOptions variable of TIndexOptions type in the btnCreate OnCreate event you will need to add db.pas to the uses list in UNIT3.PAS:

uses  
Windows, Messages, SysUtils, Classes, Graphics, Controls, Forms, Dialogs, StdCtrls, DB;

 

- Select a Button component and place it on Form3.

Object Inspector:

Name - btnClose

Caption - Close

Default - TRUE

- Double-click the Close button and add the following code to the OnClick event handler:

procedure TForm3.btnCloseClick(Sender: TObject);  
begin  
  Form1.RefreshIndexList;   
  Close;   
end;

Modify Form1 to Display Form3

- Choose the Standard tab on the Delphi Component Palette.

- Select a Button component and place it in the Table groupbox in Form1.

Object Inspector:

Name - btnCreate

Caption - Create Index

- Double-click the Create Index button and add the following code to the OnClick event handler:

procedure TForm1.btnCreateClick(Sender: TObject);  
begin  
  Form3.ShowModal;   
end;

 

- Select Use Unit from the File menu and double-click Unit3. This step allows Form1 to access objects and methods that belong to Form3. This link must be established in order for Form1 to display Form3.

Figure 9 - Browser with the New "Create Index" Button

Save and Run

- Select Save All from the File menu.

- Select Run from the Run menu, or press the [F9] key to build and run your application.

Note If you get a 7008 error when trying to create an index, you have left the Active property on tblCustomer set to True. If this is the case then the instance of your program in the Delphi IDE has the table open shared, and when your application tries to get exclusive use of the table the open will fail, returning the 7008 error. To remedy this situation close your application, change the Active property on tblCustomer to False, and re-run your application.
