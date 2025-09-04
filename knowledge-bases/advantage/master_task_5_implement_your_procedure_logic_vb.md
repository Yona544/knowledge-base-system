Task 5: Implement Your Procedure Logic




Advantage Database Server 12  

Task 5: Implement Your Procedure Logic

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Task 5: Implement Your Procedure Logic  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Task 5: Implement Your Procedure Logic Advantage Concepts master\_Task\_5\_implement\_your\_procedure\_logic\_vb Advantage Concepts > Advantage Functionality > Advantage Extended Procedures > Visual Basic Tutorial > Task 5:  Implement Your Procedure Logic / Dear Support Staff, |  |
| Task 5: Implement Your Procedure Logic  Advantage Concepts |  |  |  |  |

In order to keep this example simple, we are just going to make our AEP add a new record to the orders table and return. A real-world AEP would likely perform actions such as updating the accounts receivable table, modifying the inventory, and updating the sales representatives quota numbers.

Add Procedure Logic:

|  |  |
| --- | --- |
| 1. | Cut/paste the following helper function into your class. |

 

Private Function QuotedStr(ByVal s As String) As String

Dim sChar As String

Dim pos As Integer

Dim opos As Integer

 

sChar = "'"

pos = InStr(1, s, sChar)

 

If (pos = 0) Then

QuotedStr = s

Exit Function

End If

 

Do While (pos > 0)

QuotedStr = QuotedStr & Mid(s, 1, pos) & sChar

s = Mid(s, pos + 1)

pos = InStr(1, s, sChar)

Loop

QuotedStr = QuotedStr & s

End Function

 

|  |  |
| --- | --- |
| 2. | Cut/paste the following code over your existing definition of MyProcedure. |

Public Function MyProcedure(ByVal ulConnectionID As Int32, \_

ByVal hConnection As Int32, \_

ByRef ulNumRowsAffected As Int32) As Int32 ' Do not change prototype

Dim oCommand As AdsCommand

Dim strConnStr As String

Dim oStateInfo As StateInfo

Dim strManufacturer As String

Dim strProduct As String

Dim iQuantity As Int32

Dim iQuantityOnHand As Int32

Dim iNewOrderNum As Int32

Dim ItemPrice As Double

Dim oReader As AdsDataReader

 

oCommand = nothing

oStateInfo = nothing

 

Try

 

' Get this clients state information before doing anything

SyncLock colClientInfo

oStateInfo = colClientInfo.Item(CStr(ulConnectionID))

End SyncLock

 

' MyProcedure is called with the following input parameters,

' which are automatically put in the table \_\_input:

' manufacturer

' product id

' quantity

oCommand = oStateInfo.DataConnection.CreateCommand

oCommand.CommandType = CommandType.TableDirect

oCommand.CommandText = "\_\_input"

oReader = oCommand.ExecuteReader

oReader.Read()

strManufacturer = oReader.GetString(0)

strProduct = oReader.GetString(1)

iQuantity = oReader.GetInt32(2)

oReader.Close()

 

' Now we have our input parameters, so let's get to work.

oCommand.CommandType = CommandType.Text

oCommand.CommandText = "SELECT \* FROM products WHERE mfr\_id = '" & \_

strManufacturer & "' AND product\_id = '" & strProduct & "'"

oReader = oCommand.ExecuteReader

 

' Save the item price.

oReader.Read()

ItemPrice = oReader.GetDouble(3)

' And the number on hand.

iQuantityOnHand = oReader.GetInt32(4)

oReader.Close()

 

' Reduce the number on hand.

oCommand.CommandText = "UPDATE products SET qty\_on\_hand = " & \_

          (iQuantityOnHand - iQuantity) & " WHERE mfr\_id = '" & strManufacturer & \_

          "' AND product\_id = '" & strProduct & "'"

oCommand.ExecuteNonQuery()

 

' Add a new record to the orders table.

' NOTE : This is no where near multi-user safe (not checking for a

' lock failure). For the purpose of this example we will just use

' an order number one larger than the last order.

oCommand.CommandText = "SELECT MAX(order\_num) FROM orders"

iNewOrderNum = oCommand.ExecuteScalar

iNewOrderNum = iNewOrderNum + 1

 

oCommand.CommandText = "INSERT INTO orders (order\_num, mfr, product, " & \_

     "qty, amount) VALUES ( " & iNewOrderNum & ", '" & strManufacturer & \_

     "', '" & strProduct & "', " & iQuantity & ", " & (iQuantity \* ItemPrice) & " )"

oCommand.ExecuteNonQuery()

 

' MyProcedure returns the following output parameters, which are returned

' in the \_\_output table:

' order number

' total price

oCommand.CommandText = "INSERT INTO \_\_output VALUES( " & iNewOrderNum & \_

     ", " & (iQuantity \* ItemPrice) & " )"

oCommand.ExecuteNonQuery()

 

Catch Ex As Exception

Dim oErrCommand As AdsCommand

 

' Handle any exceptions here. Errors can be returned by placing a

' row into the \_\_error table. Use a new command, in case currently

' using a reader on the other command.

If oStateInfo IsNot Nothing Then

 Using oErrCommand As IDbCommand = oStateInfo.DataConnection.CreateCommand

   oErrCommand.CommandText = "INSERT INTO \_\_error VALUES( 1, '" & Ex.Message & "' )"

   oErrCommand.ExecuteNonQuery()

 End Using

End If

 

Finally

If oCommand IsNot Nothing Then

 oCommand.Dispose()

End If

 

' Result is currently reserved and not used. Always return zero.

MyProcedure = 0

End Try

 

  Return 0

 

End Function