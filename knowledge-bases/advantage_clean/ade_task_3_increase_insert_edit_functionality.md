---
title: Ade Task 3 Increase Insert Edit Functionality
slug: ade_task_3_increase_insert_edit_functionality
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_task_3_increase_insert_edit_functionality.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 958e5c0e64c94caa32409b4e42ad18176f5789ca
---

# Ade Task 3 Increase Insert Edit Functionality

Task 3: Increase Insert/Edit Functionality

Task 3: Increase Insert/Edit Functionality

Advantage TDataSet Descendant

| Task 3: Increase Insert/Edit Functionality  Advantage TDataSet Descendant |  |  |  |  |

In this task you will add a separate form to support single record edits and/or insertions. This task will introduce you to the concept of linking data-aware controls to individual fields in your table.

Create Insert/Edit Form (Form2)

- Select New Form from the File menu.

Object Inspector:

Caption - Insert/Edit

- Select Use Unit from the File menu and double-click Unit1. This step allows Form2 to access objects and methods that belong to Form1. This link must be established to access the table component on Form1.

Add Data-Aware Controls

- Choose the Standard tab on the Delphi Component Palette.

- Select a GroupBox component and place it on Form2.

Object Inspector:

Name - grpbxCustInfo

Caption - Customer Information

Figure 3 - Single Record Entry Screen

- For each column in the table that is displayed do the following (Note: the columns in the CUSTOMER.ADT file are CustNo, Company, Addr1, Addr2, City, State, Zip, Country, Phone, Fax, TaxRate, Contact, and LastInvoiceDate):

- Choose the Standard tab on the Delphi Component Palette.

- Select a Label component and place it in the Customer Info groupbox.

Object Inspector:

Caption -<name of field> (e.g., Contact, Phone, etc.)

- Align the labels from top to bottom by column position.

- Choose the Data Controls tab on the Delphi Component Palette.

- Select a DBEdit component and place it in the Customer Info groupbox next to the label created in the previous step.

Object Inspector:

Name - eb<name of field> (e.g., ebContact)

DataSource - Form1.dsCustomer

DataField - <name of field> (e.g., Contact, Phone, etc.)

- Align the edit boxes next to the corresponding label.

- Choose the Data Controls tab from the Delphi Component Palette.

- Select a DBNavigator component and place it on Form2.

Object Inspector:

DataSource - Form1.dsCustomer

Add Insert, Edit, Post, and Close Buttons

- Choose the Standard tab on the Delphi Component Palette.

- Select 4 Button components and place them on Form2.

Object Inspector:

Name - btnInsert, btnEdit, btnPost, btnClose

Caption - Insert, Edit, Post, Close

Default - True (for the Close button only)

- Double-click the Insert button and add the following code to the OnClick event handler:

procedure TForm2.btnInsertClick(Sender: TObject);  
begin  
  Form1.tblCustomer.Insert;   
end;

 

- Double-click the Edit button and add the following code to the OnClick event handler:

procedure TForm2.btnEditClick(Sender: TObject);  
begin  
  Form1.tblCustomer.Edit;   
end;

 

- Double-click the Post button and add the following code to the OnClick event handler:

procedure TForm2.btnPostClick(Sender: TObject);  
begin  
  Form1.tblCustomer.Post;   
end;

- Double-click the Close button and add the following code to the OnClick event handler:

procedure TForm2.btnCloseClick(Sender: TObject);  
begin  
  Close;  
end;

 

Note The functionality added with the Insert, Edit and Post buttons already exists in the DBNavigator control (see your Delphi DBNavigator documentation for details). These buttons were included to demonstrate an alternate way of controlling record manipulation.

Modify Form1 to Display Form2

- Select Forms from the View menu and double-click Form1.

- Choose the Standard tab on the Delphi Component Palette.

- Select a Button component and place it below the Open/Close button in the Table groupbox on Form1.

Object Inspector:

Name - btnInsertEdit

Caption - Insert/Edit

- Double-click the Insert/Edit button and add the following code to the OnClick event handler:

procedure TForm1.btnInsertEditClick(Sender: TObject);  
begin  
  Form2.ShowModal;   
end;

 

- Select Use Unit from the File menu and double-click Unit2. This step allows Form1 to access objects and methods that belong to Form2. This link must be established in order for Form1 to display Form2.

Figure 4 - Browser with the Insert/Edit Button in Place

 

Save and Run

- Select Save All from the File menu.

- Select Run from the Run menu, or press the [F9] key to build and run your application.
