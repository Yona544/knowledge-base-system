---
title: Ade Task 5 Add Search Functionality
slug: ade_task_5_add_search_functionality
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_task_5_add_search_functionality.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 4b51dd16ed4d56f0a63584b5a1c286db3da01fc3
---

# Ade Task 5 Add Search Functionality

Task 5: Add Search Functionality

Task 5: Add Search Functionality

Advantage TDataSet Descendant

| Task 5: Add Search Functionality  Advantage TDataSet Descendant |  |  |  |  |

In this task you will add search functionality to your application using the Locate function.

Add Search GroupBox

- Choose the Standard tab on the Delphi Component Palette.

- Select a GroupBox component and place it on Form1.

Object Inspector:

Name - grpbxSearch

Caption - Search

Figure 6 - Browser with the New Search GroupBox

Add Search Edit Boxes and Labels

- Choose the Standard tab on the Delphi Component Palette.

- Select a Label component and place it in the Search groupbox.

Object Inspector:

Caption - Field

- Select an Edit component and place it in the Search groupbox next to the Field label.

Object Inspector:

Name - ebSearchField

Text - " (empty string)

- Select a Label component and place it in the Search groupbox.

Object Inspector:

Caption - Value

- Select an Edit component and place it in the Search groupbox next to the Value label.

Object Inspector:

Name - ebSearchValue

Text - " (empty string)

Add Search Button and Code

- Choose the Standard tab on the Delphi Component Palette.

- Select a Button component and place it in the Search groupbox.

Object Inspector:

Name - btnSearch

Caption - Search

- Double-click the Search button and add the following code to the OnClick event handler:

procedure TForm1.btnSearchClick(Sender: TObject);  
begin  
  tblCustomer.Locate( ebSearchField.text,Variant(ebSearchValue.text), [loPartialKey] );   
end;

 

Note For more information on the Locate method, reference your Delphi documentation.

Save and Run

- Select Save All from the File menu.

- Select Run from the Run menu, or press the [F9] key to build and run your application.
