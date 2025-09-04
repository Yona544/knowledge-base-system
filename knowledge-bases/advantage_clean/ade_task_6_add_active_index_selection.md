---
title: Ade Task 6 Add Active Index Selection
slug: ade_task_6_add_active_index_selection
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_task_6_add_active_index_selection.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 426fe2f8c1a365d32d6d25c008e504a205113f14
---

# Ade Task 6 Add Active Index Selection

Task 6: Add Active Index Selection

Task 6: Add Active Index Selection

Advantage TDataSet Descendant

| Task 6: Add Active Index Selection  Advantage TDataSet Descendant |  |  |  |  |

In this task you will add the ability to set the active index on the table. This will allow you to choose between the tables available indexes and view the table in its indexed order.

Add OrderBy GroupBox

- Choose the Standard tab on the Delphi Component Palette.

- Select a GroupBox component and place it on Form1.

Object Inspector:

Name - grpbxOrder

Caption - Order By:

- Select a ComboBox component and place it in the Order By: groupbox.

Object Inspector:

Name - cbActiveIndex

Style - csDropDownList

Figure 7 - Browser with the New OrderBy GroupBox

Add RefreshIndexList Procedure

The RefreshIndexList procedure is used to retrieve a list of indexes that belong to the table and place them in the cbActiveIndex combobox. In a later task you will add index creation capabilities to your application and include a call to RefreshIndexList to update the cbActiveIndex combobox with the names of any new indexes that may have been created.

- Add the "procedure RefreshIndexList" line to the end of the procedure declarations as highlighted below in the TForm1 class declaration in UNIT1.PAS:

procedure btnOpenCloseClick(Sender: TObject);   
procedure btnExitClick(Sender: TObject);   
procedure btnInsertEditClick(Sender: TObject);   
procedure btnSetFilterClick(Sender: TObject);   
procedure btnFindClick(Sender: TObject);   
procedure RefreshIndexList;   
private  
{ Private declarations }   
public  
{ Public declarations }   
end;

- Add the procedure TForm1.RefreshIndexList and its code to the implementation section as shown below in UNIT1.PAS:

var  
  Form1: TForm1;   
   
implementation  
   
uses Unit2;  
   
{$R \*.DFM}  
   
procedure TForm1.RefreshIndexList;  
begin  
  with cbActiveIndex do   
  begin   
    Items.Clear;   
    tblCustomer.GetIndexNames( Items );   
    Items.Add( 'Natural Order' );   
    ItemIndex := Items.Count - 1;   
  end;   
end;

- Select Forms from the View menu and double-click Form1.

- Double-click in a blank area inside Form1 to access the Form1 OnCreate event handler.

- Add the following code to the OnCreate event handler:

procedure TForm1.FormCreate(Sender: TObject);  
begin  
  RefreshIndexList;   
end;

Implement cbActiveIndex

- Select the cbActiveIndex combobox from Form1 and press [F11] to activate the Delphi Object Inspector.

- Select the Events tab in the Delphi Object Inspector.

- Double-click inside the OnChange edit box to access the OnChange event handler for cbActiveIndex.

- Add the following code to the OnChange event handler:

procedure TForm1.cbActiveIndexChange(Sender: TObject);  
begin  
  with cbActiveIndex do   
  begin   
    if Items[itemindex] = 'Natural Order' then   
      tblCustomer.IndexName := ''   
    else   
      tblCustomer.IndexName := Items[itemindex];   
  end;   
end;

Save and Run

- Select Save All from the File menu.

- Select Run from the Run menu, or press the [F9] key to build and run your application.
