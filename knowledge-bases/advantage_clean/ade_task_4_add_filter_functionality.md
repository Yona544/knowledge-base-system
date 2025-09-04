---
title: Ade Task 4 Add Filter Functionality
slug: ade_task_4_add_filter_functionality
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_task_4_add_filter_functionality.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d55701687ac20d46aa17059d32eab6e257705e2b
---

# Ade Task 4 Add Filter Functionality

Task 4: Add Filter Functionality

Task 4: Add Filter Functionality

Advantage TDataSet Descendant

| Task 4: Add Filter Functionality  Advantage TDataSet Descendant |  |  |  |  |

In this task you will add the ability to set filters on the table using an expression provided by the user.

Add Filter GroupBox

- Choose the Standard tab on the Delphi Component Palette.

- Select a GroupBox component and place it on Form1.

Object Inspector:

Name - grpbxFilter

Caption - Filter

Figure 5 - Browser with the New Filter GroupBox

Add Filter Expression Edit Box

- Choose the Standard tab on the Delphi Component Palette.

- Select an Edit component and place it in the Filter groupbox.

Object Inspector:

Name - ebFilter

Text - " (empty string)

Add Filter Button and Code

- Choose the Standard tab on the Delphi Component Palette.

- Select a Button component and place it in the Filter groupbox.

Object Inspector:

Name - btnSetFilter

Caption - Set

- Double-click the Set button and add the following code to the OnClick event handler:

procedure TForm1.btnSetFilterClick(Sender: TObject);  
begin  
  if btnSetFilter.Caption = 'Set' then   
  begin   
    tblCustomer.Filter := ebFilter.Text;   
    try   
      tblCustomer.Filtered := TRUE;   
    except   
      on E: Exception do   
      begin   
        Application.MessageBox( Pchar(E.message), 'Filter Error', 0 );   
        exit;   
      end;   
    end;

   
    btnSetFilter.Caption := 'Clear';   
  end   
  else   
  begin   
    tblCustomer.Filtered := FALSE;   
    btnSetFilter.Caption := 'Set';   
  end;   
end;

Save and Run

- Select Save All from the File menu.

- Select Run from the Run menu, or press the [F9] key to build and run your application.
