SQL Operators




Advantage Database Server 12  

SQL Operators

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SQL Operators  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - SQL Operators Advantage SQL Engine master\_Sql\_operators Advantage SQL > Supported SQL Grammar > SQL Operators / Dear Support Staff, |  |
| SQL Operators  Advantage SQL Engine |  |  |  |  |

The Advantage SQL Engine supports the following operators. They are listed in order of precedence from highest precedence to lowest. Note that the operator precedence can be modified with the use of parentheses.

|  |  |
| --- | --- |
| Description | Operators |
| Sign (unary plus/minus) | +, -, ~ |
| Multiplication | \*, / |
| Modulo | % |
| Addition | +, - |
| Bitwise | &, |, ^, >>, << |
| Comparison | >, >=, <, <=, =, <>, [NOT] LIKE, [NOT] IN, [NOT] BETWEEN, IS [NOT] NULL |
| Logical NOT | NOT |
| Logical AND | AND |
| Logical OR | OR |

The following rules describe which operand types can be used with which operators:

|  |  |
| --- | --- |
| · | Numeric values are valid operands for Sign, Multiplication, modulo, and Addition. |

|  |  |
| --- | --- |
| · | Numeric, date, time and timestamp values are valid operands for Comparison operators except for [NOT] LIKE. |

|  |  |
| --- | --- |
| · | String values are valid operands for the + Addition operator (concatenation) and all Comparison operators. |

|  |  |
| --- | --- |
| · | Logical values are valid operands for Comparison operators = (equals), <> (not equals) and IS [NOT] NULL. |

|  |  |
| --- | --- |
| · | Date values are valid operands for Addition operators when one side is a numeric value. For example, date + numeric, date - numeric, and numeric + date are all valid. |

|  |  |
| --- | --- |
| · | Valid operands for the logical operators NOT, AND, and OR are any valid comparison expression. |

|  |  |
| --- | --- |
| · | Fixed length Binary values (RAW fields) are valid operands for all Compare operators except the [NOT] LIKE and [NOT] BETWEEN operators. |

|  |  |
| --- | --- |
| · | Variable length binary values (BLOB fields) are valid operands for the IS [NOT] NULL operator. |

|  |  |
| --- | --- |
| · | The & (AND), | (OR), and ^ (XOR) bitwise operators require one operand to be a numeric type without decimals. The other operand can be binary or numeric without decimals. |

|  |  |
| --- | --- |
| · | The ~ (NOT) bitwise operator requires the operand to be numeric without decimals. Binary types are not allowed. |

|  |  |
| --- | --- |
| · | The >> (SHIFT RIGHT) and << (SHIFT LEFT) bitwise operators require both operands to be numeric types without decimals. Binary types are not allowed. |

Bitwise Operators

There are six supported bitwise operators: & (AND), | (OR), ^ (XOR), ~ (NOT), >> (SHIFT RIGHT), << (SHIFT LEFT). Each operator requires the operands to be numeric or binary types (some exceptions apply). In all cases, the operands will be converted to an integer to perform the operation. The result of the operation will always be an integer type with the size dependent on the size of the operands (BIT, SHORT, INTEGER or LONG INTEGER). For example, two SHORT operands will return a SHORT value, whereas a SHORT and an INTEGER operand will produce an INTEGER value. Numeric value is converted to the smallest possible integer type that can properly store the numeric value. More precisely, numeric values with precision of less than 5 are converted SHORT (16 bit) integer. Numeric values with precision between 5 and 9 are converted to INTEGER (32 bit). Numeric values with precision between 10 and 18 are converted to LONG INTEGER (64 bit). Numeric values with precision greater than 18 will produce an overflow error at runtime when it is an operand of a bitwise operation. Operands with decimal portions such as double or numeric with a non-zero scale are not allowed. The CAST and CONVERT scalars can be helpful in adjusting the operand types to ensure the result type is the desired type.

Bitwise AND, OR, XOR Operators

The bitwise AND, OR, and XOR operators accept two numeric or one numeric and one binary operand. When one operand of type binary, the number of bits involved in the operation will be the same number of bits for the integer type of the other operand.

Bitwise NOT Operator

The bitwise NOT operator performs a bitwise negation of the given value. The bitwise NOT operator can only be used on numeric operands. Binary operands are not allowed.

Bitwise SHIFT RIGHT and SHIFT LEFT Operators

The bitwise SHIFT RIGHT and SHIFT LEFT operators perform a binary shift on the given value. The left operand is the value to shift and the right operand is the number of bits to shift. The bitwise SHIFT operators can only be used on numeric operands. Binary operands are not allowed.