---
title: Master Task 3 Implement Your Trigger
slug: master_task_3_implement_your_trigger
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_task_3_implement_your_trigger.htm
source: Advantage CHM
tags:
  - master
checksum: 7f6a62eb47753d98d0e537b4a59279f2fa05fdc9
---

# Master Task 3 Implement Your Trigger

Task 3: Implement Your Trigger

Task 3: Implement Your Trigger

Advantage Concepts

| Task 3: Implement Your Trigger  Advantage Concepts |  |  |  |  |

For this tutorial you will implement an AFTER INSERT trigger on the "orders" table. After a new order is placed in the table, the trigger code will verify there is enough product on hand to fill the order. To keep the example simple, we will not deal with the concept of backorders. In a real-world situation, the trigger could either automatically order more product, or return an error (which when using the Advantage Database Server, would automatically roll back the original insertion into the orders table).

Once the trigger has verified there is enough inventory to place the order, it will update the "products" table with a new QTY\_ON\_HAND value.

Take the appropriate steps below depending on your development environment:

Borland Delphi/Kylix

| 1. | Add the following local variables to MyFunction |

oQuery : TAdsQuery;

strMfr : String;

strProduct : String;

iQuantityOrdered : Integer;

| 1. | Add the following code to the body of MyFunction (right below the "YOUR TRIGGER CODE GOES HERE" comment) |

oQuery := TAdsQuery.Create( nil );

oQuery.DatabaseName := 'conn';

// See how many items were ordered.

oQuery.SQL.Text := 'SELECT mfr, product, qty FROM \_\_new';

oQuery.Open;

strMfr := oQuery.Fields[0].AsString;

strMfr := UpperCase( strMfr );

strProduct := oQuery.Fields[1].AsString;

strProduct := UpperCase( strProduct );

iQuantityOrdered := oQuery.Fields[2].AsInteger;

 

// See how many items are in stock.

oQuery.SQL.Text := 'SELECT qty\_on\_hand FROM products WHERE mfr\_id = ' +

QuotedStr( strMfr ) + ' AND product\_id = ' +

QuotedStr( strProduct );

oQuery.Open;

 

// If more items are required, return an error

if ( iQuantityOrdered > oQuery.Fields[0].AsInteger ) then

begin

SetError( oConn, 1, 'Insufficient inventory to place order.' );

exit;

end;

 

// Otherwise update the quantity on hand

oConn.Execute( 'UPDATE products SET qty\_on\_hand = ' +

IntToStr( oQuery.Fields[0].AsInteger - iQuantityOrdered ) +

' WHERE mfr\_id = ' +

QuotedStr( strMfr ) + ' AND product\_id = ' +

QuotedStr( strProduct ) );

| 2. | Save and build the project. |

Microsoft Visual Studio .NET (C# users)

| 1. | Add the following local variables to MyFunction |

IDataReader oReader;

String strMfr;

String strProduct;

Int32 iQuantityOrdered;

Int32 iOnHand;

| 3. | Add the following code to the body of MyFunction (right below the "YOUR TRIGGER CODE GOES HERE" comment) |

// See how many items were ordered.

oCommand.CommandText = "SELECT mfr, product, qty FROM \_\_new";

oReader = oCommand.ExecuteReader();

oReader.Read();

strMfr = oReader.GetString( 0 );

strMfr = strMfr.ToUpper();

strProduct = oReader.GetString( 1 );

strProduct = strProduct.ToUpper();

iQuantityOrdered = oReader.GetInt32( 2 );

oReader.Close();

// See how many items are in stock.

oCommand.CommandText = "SELECT qty\_on\_hand FROM products WHERE mfr\_id = '" +

strMfr + "' AND product\_id = '" +

strProduct + "'";

oReader = oCommand.ExecuteReader();

oReader.Read();

iOnHand = oReader.GetInt32( 0 );

oReader.Close();

// If more items are required, automatically place row in BACKORDERS table

if ( iQuantityOrdered > iOnHand )

{

oCommand.CommandText = "INSERT INTO \_\_error( message ) " +

"VALUES( 'Insufficient inventory to place order.' )";

oCommand.ExecuteNonQuery();

return 0;

}

// Otherwise update the quantity on hand

oCommand.CommandText = "UPDATE products SET qty\_on\_hand = " +

( iOnHand - iQuantityOrdered ).ToString() +

" WHERE mfr\_id = '" + strMfr +

"' AND product\_id = '" + strProduct + "'";

oCommand.ExecuteNonQuery();

| 4. | Save and build the project. |

Microsoft Visual Studio .NET (VB users)

| 1. | Add the following local variables to MyFunction |

Dim oReader As IDataReader

Dim strMfr As String

Dim strProduct As String

Dim iQuantityOrdered As Int32

Dim iOnHand As Int32

| 5. | Add the following code to the body of MyFunction (right below the "YOUR TRIGGER CODE GOES HERE" comment) |

' See how many items were ordered.

oCommand.CommandText = "SELECT mfr, product, qty FROM \_\_new"

oReader = oCommand.ExecuteReader()

oReader.Read()

strMfr = oReader.GetString(0)

strMfr = strMfr.ToUpper()

strProduct = oReader.GetString(1)

strProduct = strProduct.ToUpper()

iQuantityOrdered = oReader.GetInt32(2)

oReader.Close()

' See how many items are in stock.

oCommand.CommandText = "SELECT qty\_on\_hand FROM products WHERE mfr\_id = '" + \_

strMfr + "' AND product\_id = '" + \_

strProduct + "'"

oReader = oCommand.ExecuteReader()

oReader.Read()

iOnHand = oReader.GetInt32(0)

oReader.Close()

' If more items are required, automatically place row in BACKORDERS table

If (iQuantityOrdered > iOnHand) Then

oCommand.CommandText = "INSERT INTO \_\_error( message ) " + \_

"VALUES( 'Insufficient inventory to place order.' )"

oCommand.ExecuteNonQuery()

Return 0

End If

 

' Otherwise update the quantity on hand

oCommand.CommandText = "UPDATE products SET qty\_on\_hand = " + \_

(iOnHand - iQuantityOrdered).ToString() + \_

" WHERE mfr\_id = '" + strMfr + \_

"' AND product\_id = '" + strProduct + "'"

oCommand.ExecuteNonQuery()

| 6. | Save and build the project. |
