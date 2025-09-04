Task 5: Implement Your Procedure Logic




Advantage Database Server 12  

Task 5: Implement Your Procedure Logic

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Task 5: Implement Your Procedure Logic  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Task 5: Implement Your Procedure Logic Advantage Concepts master\_Task\_5\_implement\_your\_procedure\_logic Advantage Concepts > Advantage Functionality > Advantage Extended Procedures > TDataSet Descendant Tutorial > Task 5:  Implement Your Procedure Logic / Dear Support Staff, |  |
| Task 5: Implement Your Procedure Logic  Advantage Concepts |  |  |  |  |

In order to keep this example simple, we are just going to make our AEP add a new record to the orders table and return. A real-world AEP would likely perform actions such as updating the accounts receivable table, modifying the inventory, and updating the sales representatives quota numbers.

Add Procedure Logic:

|  |  |
| --- | --- |
| 1. | Cut/paste the following helper function into the body of your AEP, directly above MyProcedure: |

{\* Helper function for returning output parameters. \*}

procedure ReturnParameter( tblOutput : TAdsTable; strVar : string; vValue : variant );

begin

with tblOutput do

begin

open;

 

{\* If we've already set up a parameter to return then we'll already have a

\* row in this table, so don't add one. \*}

if eof then

insert

else

edit;

 

FieldByName( strVar ).Value := vValue;

post;

close;

end;

end;

|  |  |
| --- | --- |
| 2. |  |

function MyProcedure( ulConnectionID: UNSIGNED32;

hConnection: ADSHANDLE;

pulNumRowsAffected: PUNSIGNED32 ): UNSIGNED32;

{$IFDEF WIN32}stdcall;{$ENDIF}{$IFDEF LINUX}cdecl;{$ENDIF} // Do not change prototype

var

strManufacturer : string;

strProduct : string;

iQuantity : integer;

iNewOrderNum : integer;

ItemPrice : currency;

DM1 : TDM1;

begin

 

Result := AE\_SUCCESS;

 

{\* Get this connection's data module from the session manager. \*}

DM1 := TDM1( AEPSessionMgr.GetDM( ulConnectionID ) );

 

try

with DM1 do

begin

 

{\* MyProcedure is called with the following input parameters:

\* manufacturer

\* product id

\* quantity

\*}

tblInput.open;

strManufacturer := tblInput.FieldByName( 'mfr' ).Value;

strProduct := tblInput.FieldByName( 'product' ).Value;

iQuantity := tblInput.FieldByName( 'quantity' ).Value;

tblInput.close;

 

{\* Now we have our input parameters, so let's get to work. \*}

tblProducts.Locate( 'mfr\_id;product\_id', VarArrayOf( [strManufacturer, strProduct] ) , [] );

 

{\* Save the item price. \*}

ItemPrice := tblProducts.FieldByName( 'price' ).Value;

{\* Reduce the number on hand. \*}

tblProducts.Edit;

tblProducts.FieldByName( 'qty\_on\_hand' ).Value := tblProducts.FieldByName( 'qty\_on\_hand' ).Value - iQuantity;

tblProducts.Post;

 

{\* Add a new record to the orders table.

\* NOTE : This is no where near multi-user safe (not checking for a

\* lock failure). For the purpose of this example we will just use

\* an order number one larger than the last order. \*}

with tblOrders do

begin

Last;

Edit; {\* this will lock the record. \*}

iNewOrderNum := FieldByName( 'order\_num' ).AsInteger + 1;

Append;

FieldByName( 'order\_num' ).Value := iNewOrderNum;

FieldByName( 'order\_date' ).Value := Date;

FieldByName( 'mfr' ).Value := strManufacturer;

FieldByName( 'product' ).Value := strProduct;

FieldByName( 'qty' ).Value := iQuantity;

FieldByName( 'amount' ).Value := iQuantity \* ItemPrice;

Post;

end;

 

{\* MyProcedure returns the following output parameters:

\* order number

\* total price

\*}

ReturnParameter( tblOutput, 'order\_num', iNewOrderNum );

ReturnParameter( tblOutput, 'total\_price', iQuantity \* ItemPrice );

 

end; {\* with DM1 \*}

 

except

on E : EADSDatabaseError do

{\* ADS-specific error, use ACE error code \*}

DM1.DataConn.Execute( 'INSERT INTO \_\_error VALUES ( ' + IntToStr( E.ACEErrorCode ) + ', ' + QuotedStr( E.Message ) + ' )' );

on E : Exception do

{\* other error \*}

DM1.DataConn.Execute( 'INSERT INTO \_\_error VALUES ( 1, ' + QuotedStr( E.Message ) + ' )' );

end;

 

end;

|  |  |
| --- | --- |
| 3. | If using Delphi 6 or greater, add "Variants" to the uses clause. |

Build Your Procedure:

|  |  |
| --- | --- |
| 1. | Select Build from the Project menu. |

|  |  |
| --- | --- |
| 2. | You should now have a file called MyFirstAEP.aep in your working directory. |