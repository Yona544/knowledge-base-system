Task 5: Add Search Functionality




Advantage Database Server 12  

Task 5: Add Search Functionality

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Task 5: Add Search Functionality  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Task 5: Add Search Functionality Advantage TDataSet Descendant ade\_Task\_5\_add\_search\_functionality Advantage TDataSet Descendant > Developing and Distributing Applications > Developing a Sample Advantage-Enabled Delphi Application > Task 5: Add Search Functionality / Dear Support Staff, |  |
| Task 5: Add Search Functionality  Advantage TDataSet Descendant |  |  |  |  |

In this task you will add search functionality to your application using the Locate function.

Add Search GroupBox

|  |  |
| --- | --- |
| · | Choose the Standard tab on the Delphi Component Palette. |

|  |  |
| --- | --- |
| · | Select a GroupBox component and place it on Form1. |

Object Inspector:

Name - grpbxSearch

Caption - Search

Figure 6 - Browser with the New Search GroupBox

Add Search Edit Boxes and Labels

|  |  |
| --- | --- |
| · | Choose the Standard tab on the Delphi Component Palette. |

|  |  |
| --- | --- |
| · | Select a Label component and place it in the Search groupbox. |

Object Inspector:

Caption - Field

|  |  |
| --- | --- |
| · | Select an Edit component and place it in the Search groupbox next to the Field label. |

Object Inspector:

Name - ebSearchField

Text - " (empty string)

|  |  |
| --- | --- |
| · | Select a Label component and place it in the Search groupbox. |

Object Inspector:

Caption - Value

|  |  |
| --- | --- |
| · | Select an Edit component and place it in the Search groupbox next to the Value label. |

Object Inspector:

Name - ebSearchValue

Text - " (empty string)

Add Search Button and Code

|  |  |
| --- | --- |
| · | Choose the Standard tab on the Delphi Component Palette. |

|  |  |
| --- | --- |
| · | Select a Button component and place it in the Search groupbox. |

Object Inspector:

Name - btnSearch

Caption - Search

|  |  |
| --- | --- |
| · | Double-click the Search button and add the following code to the OnClick event handler: |

procedure TForm1.btnSearchClick(Sender: TObject);  
begin  
  tblCustomer.Locate( ebSearchField.text,Variant(ebSearchValue.text), [loPartialKey] );   
end;

 

Note For more information on the Locate method, reference your Delphi documentation.

Save and Run

|  |  |
| --- | --- |
| · | Select Save All from the File menu. |

|  |  |
| --- | --- |
| · | Select Run from the Run menu, or press the [F9] key to build and run your application. |