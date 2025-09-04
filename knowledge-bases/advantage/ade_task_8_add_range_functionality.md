Task 8: Add Range Functionality




Advantage Database Server 12  

Task 8: Add Range Functionality

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Task 8: Add Range Functionality  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Task 8: Add Range Functionality Advantage TDataSet Descendant ade\_Task\_8\_add\_range\_functionality Advantage TDataSet Descendant > Developing and Distributing Applications > Developing a Sample Advantage-Enabled Delphi Application > Task 8: Add Range Functionality / Dear Support Staff, |  |
| Task 8: Add Range Functionality  Advantage TDataSet Descendant |  |  |  |  |

In this task you will add the ability to set a range on your table using the active index. For more information on ranges, see [Index Scopes (Ranges)](master_index_scopes_ranges.htm) or reference your Delphi documentation.

Add Range GroupBox

|  |  |
| --- | --- |
| · | Choose the Standard tab on the Delphi Component Palette. |

|  |  |
| --- | --- |
| · | Select a GroupBox component and place it on Form1. |

Object Inspector:

Name - grpbxRange

Caption - Range

Figure 10 - Browser with the New Range GroupBox

Add RangeTop and RangeBottom Edit Boxes

|  |  |
| --- | --- |
| · | Choose the Standard tab on the Delphi Component Palette. |

|  |  |
| --- | --- |
| · | Select a Label component and place it in the Range groupbox. |

Object Inspector:

Caption - Top

|  |  |
| --- | --- |
| · | Select an Edit component and place it in the Range groupbox next to the Top label from the previous step. |

Object Inspector:

Name - ebRangeTop

Text - " (empty string)

|  |  |
| --- | --- |
| · | Select a Label component and place it in the Range groupbox. |

Object Inspector:

Caption - Bottom

|  |  |
| --- | --- |
| · | Select an Edit component and place it in the Range groupbox next to the Bottom label from the previous step. |

Object Inspector:

Name - ebRangeBottom

Text - " (empty string)

|  |  |
| --- | --- |
| · | Select a Button component and place it in the Range groupbox. |

Object Inspector:

Name - btnSetRange

Caption - Set

|  |  |
| --- | --- |
| · | Double-click the Set button and add the following code to the OnClick event handler: |

procedure TForm1.btnSetRangeClick(Sender: TObject);  
var  
  def: TIndexDef;   
begin  
  {\* make sure there is an active index \*}   
  with cbActiveIndex do   
  begin   
    if Items[ItemIndex] = 'Natural Order' then   
    begin   
      Application.MessageBox( 'No Active Index', 'Error', 0 );   
      exit;   
    end;   
  end;   
   
  if btnSetRange.Caption = 'Set' then   
  begin   
    {\* set the range \*}   
    with tblCustomer do   
    begin   
      try   
        SetRangeStart;   
        def := IndexDefs.   
        Find(cbActiveIndex.Items[cbActiveIndex.ItemIndex]);   
        FieldByName(def.fields).asstring := ebRangeTop.Text;   
        SetRangeEnd;   
        FieldByName(def.fields).asstring := ebRangeBottom.Text;   
        ApplyRange;   
      except   
        on E: Exception do   
        begin   
          Application.MessageBox( PChar(E.message), 'Error', 0 );   
          exit;   
        end;   
      end;

   
      btnSetRange.Caption := 'Clear';   
    end;   
  end {\* if setting range\*}   
  else   
  begin   
    {\* clear the range \*}   
    tblCustomer.CancelRange;   
    btnSetRange.Caption := 'Set';   
  end;   
end;

 

Note For more information about SetRangeStart, SetRangeEnd, and ApplyRange reference your Delphi documentation.

Save and Run

|  |  |
| --- | --- |
| · | Select Save All from the File menu. |

|  |  |
| --- | --- |
| · | Select Run from the Run menu, or press [F9] to build and run your application. |