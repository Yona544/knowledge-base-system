---
title: Master Expression Engine Operators
slug: master_expression_engine_operators
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_expression_engine_operators.htm
source: Advantage CHM
tags:
  - master
checksum: a6b8e7a147b4ff1d7571ea5203e3c4dc57ccc990
---

# Master Expression Engine Operators

Expression Engine Operators

Expression Engine Operators

Advantage Concepts

| Expression Engine Operators  Advantage Concepts |  |  |  |  |

Operators used in expressions are standard in most dialects.

Alias Operators

In general, alias operators allow field evaluation for fields located in the table opened with the given alias name. Since the Advantage Expression Engine only supports evaluating fields in the current/selected table, if a field is aliased, that alias must be for the current/selected table. Table aliases are unlikely to be used with the Advantage TDataSet Descendant.

à, . Alias a field name. Examples: AliasNameàFieldName, or AliasName.FieldName

String Operators

+  Concatenates two strings. Trailing spaces in the strings are maintained.

- Joins two strings and removes trailing spaces from the string to the left of the operator and places them at the end of the string to the right of the operator.

Note If using ADI indexes (with the ADT table format) it is best to use the "Data Typeless Join Operator" instead of the + operator. When used with NULL data fields the + operator can produce unexpected results.

Data Typeless Join Operator

; Joins any two data types by concatenating the raw binary data. This operator is only valid for index key expressions in the ADI index file format. This operator allows any data to be concatenated regardless of data type.

Numeric Operators

+  Addition operator: The numeric value to the left of the operator is added to the numeric value to the right of the operator and the result is returned as a numeric value.

-  Subtraction operator. The numeric value to the right of the operator is subtracted from the numeric value to the left of the operator and the result is returned as a numeric value.

\*  Multiplication operator. The numeric value to the left of the operator is multiplied to the numeric value to the right of the operator and the result is returned as a numeric value.

/  Division operator. The numeric value to the left of the operator is divided by the numeric value to the right of the operator and the result is returned as a numeric value.

^, \*\* Exponentiation operators. The numeric value to the left of the operator is raised to the power of the numeric value to the right of the operator and the result is returned as a numeric value.

% Modulus operator. Returns a numeric value representing the remainder of the operand on the left divided by the operand on the right.

Date Operators

+  Addition operator: The numeric operand on one side of the operator is added as days to the date operand on the other side of the operator and the result is returned as a date value.

-  Subtraction operator. If both operands are date data type, the date operand on the right of the operator is subtracted from the date operator on the left of the operator and the result is returned as a numeric value representing the number of days between the two dates. If the left operand is date data type and the right operand numeric data type, the numeric operand is subtracted as days from date operand and a date value is returned. If the order of operands is reversed, an error occurs.

Relational Operators

=  Equal operator. Compares two values of the same data type and returns True if the operand on the left is equal to the operand on the right according to the following rules:

Char:  The comparison is based on the underlying ANSI or OEM code (depending upon which collation is being used). Assume two character strings, cLeft and cRight, where the expression to test is (cLeft = cRight).

When AdsSetExact, which can be set by calling the Advantage Client Engine directly, is False (the default):

| 1. | If cRight is an empty string, returns True. |

| 2. | If the length of cRight is greater than the length of cLeft, returns False. |

| 3. | Compare all characters in cRight with cLeft. If all characters in cRight equal cLeft, returns True; otherwise, returns False. |

When AdsSetExact, which can be set by calling the Advantage Client Engine directly, is True:

| 1. | After truncating all spaces, if the length of either string is greater than the other, returns False. |

| 2. | After truncating all spaces, compare all characters in cRight with cLeft. If any characters in cRight do not equal cLeft, returns False; otherwise, returns True. |

Note that if AdsSetExact is set to true, the equal operator will do an exact comparison for both length and content after trailing spaces have been truncated.

Examples:

AdsSetExact( TRUE )

"ABC" = "ABC "  // Result: TRUE

"ABC " = "ABC"  // Result: TRUE

"ABC" = "ABCDE"  // Result: FALSE

"ABCDE" = "ABC"  // Result: FALSE

"ABC" = ""  // Result: FALSE

"" = "ABC"  // Result: FALSE

AdsSetExact( FALSE )

"ABC" = "ABC "  // Result: FALSE

"ABC " = "ABC"  // Result: TRUE

"ABC" = "ABCDE"  // Result: FALSE

"ABCDE" = "ABC"  // Result: TRUE

"ABC" = ""  // Result: TRUE

"" = "ABC"  // Result: FALSE

 

Date:  Dates are compared according to the underlying date value.

Logical: True (.T.) is equal to true (.T.) and false (.F.) equal to false (.F.).

Numeric: Compared based on magnitude.

==  Exactly equal operator. Compares two values of the same data type for exact equality depending on the data type. Returns True if the operand on the left is equal to the operand on the right according to the following rules:

Char:  The comparison is based on the underlying ANSI or OEM code (depending upon which collation is being used). Unlike the relational equality operator (=) , true (.T.) is returned if the operand on the left and the operand on the right are exactly equal including trailing spaces; otherwise, the comparison returns false (.F.). The AdsSetExact setting has no effect on the exactly equal operator.

Examples:

"ABC" == "ABC"  // Result: TRUE

"BCD" == "ABC"  // Result: FALSE

"ABC" == "ABC "  // Result: FALSE

"ABC" == "AB"  // Result: FALSE

 

Date:  Dates are compared according to the underlying date value; behaves the same as the relational equality operator (=).

Logical: True (.T.) is exactly equal to true (.T.), and false (.F.) is exactly equal to false (.F.); behaves the same as the relational equality operator (=).

Numeric: Compared based on magnitude; behaves the same as the relational equality operator (=).

!=, <>, # Not equal operators. Compares two values of the same data type and returns True if the operand on the left is not equal to the operand on the right according to the following rules:

Char:  The comparison is based on the underlying ANSI or OEM code (depending upon which collation is being used) and is the inverse of the equal operator (=). Assume two character strings, cLeft and cRight, where the expression to test is (cLeft = cRight).

When AdsSetExact, which can be set by calling the Advantage Client Engine directly, is False (the default):

| 1. | If cRight is an empty string, returns False. |

| 2. | If the length of cRight is greater than the length of cLeft, returns True. |

| 3. | Compare all characters in cRight with cLeft. If any characters in cRight do not equal cLeft, returns True; otherwise, returns False. |

When AdsSetExact, which can be set by calling the Advantage Client Engine directly, is True:

| 1. | After truncating all spaces, if the length of either string is greater than the other, returns True. |

| 2. | After truncating all spaces, compare all characters in cRight with cLeft. If any characters in cRight do not equal cLeft, returns True; otherwise, returns False. |

Examples:

AdsSetExact( TRUE )

"ABC" != "ABC "  // Result: FALSE

"ABC " != "ABC"  // Result: FALSE

"ABC" != "ABCDE"  // Result: TRUE

"ABCDE" != "ABC"  // Result: TRUE

"ABC" != ""  // Result: TRUE

"" != "ABC"  // Result: TRUE

"" != ""  // Result: FALSE

AdsSetExact( FALSE )

"ABC" != "ABC "  // Result: TRUE

"ABC " != "ABC"  // Result: FALSE

"ABC" != "ABCDE"  // Result: TRUE

"ABCDE" != "ABC"  // Result: FALSE

"ABC" != ""  // Result: FALSE

"" != "ABC"  // Result: TRUE

"" != ""  // Result: FALSE

 

Date:  Dates are compared according to the underlying date value.

Logical:  True (.T.) is equal to true (.T.) and false (.F.) equal to false (.F.).

Numeric: Compared based on magnitude.

<  Less than operator. Compares two values of the same data type and returns True if the operand on the left is less than the operand on the right.

Char:  The comparison is based on the underlying ANSI or OEM code (depending upon which collation is being used). If the lengths of the strings are equal, a simple comparison is performed. If the lengths of the strings are not equal, the first X number of characters in the string are compared, where X is the length of the shorter string. If those first X characters are the same:

| 1. | If the string on the left is shorter, True is returned. |

| 2. | If the string on the right is shorter, False is returned. |

When AdsSetExact, which can be set by calling the Advantage Client Engine directly, is True trailing blanks are truncated for purposes of the comparison.

Examples:

AdsSetExact( TRUE )

"ABC" < "ABC "  // Result: FALSE

"ABC " < "ABC"  // Result: FALSE

"ABC" < "ABCDE"  // Result: TRUE

"ABCDE" < "ABC"  // Result: FALSE

"ABC" < ""  // Result: FALSE

"" < "ABC"  // Result: TRUE

AdsSetExact( FALSE )

"ABC" < "ABC "  // Result: TRUE

"ABC " < "ABC"  // Result: FALSE

"ABC" < "ABCDE"  // Result: TRUE

"ABCDE" < "ABC"  // Result: FALSE

"ABC" < ""  // Result: FALSE

"" < "ABC"  // Result: TRUE

 

Date:  Dates are compared according to the underlying date value.

Logical: False (.F.) is less than true (.T.).

Numeric: Compared based on magnitude.

>  Greater than operator. Compares two values of the same data type and returns True if the operand on the left is greater than the operand on the right.

Char:  The comparison is based on the underlying ANSI or OEM code (depending upon which collation is being used). If the lengths of the strings are equal, a simple comparison is performed. If the lengths of the strings are not equal, the first X number of characters in the string are compared, where X is the length of the shorter string. If those first X characters are the same:

| 1. | If the string on the left is shorter, False is returned. |

| 2. | If the string on the right is shorter and AdsSetExact is True, True is returned. |

| 3. | If the string on the right is shorter and AdsSetExact is False, False is returned. |

When AdsSetExact, which can be set by calling the Advantage Client Engine directly, is True trailing blanks are truncated for purposes of the comparison.

Examples:

AdsSetExact( TRUE )

"ABC" > "ABC "  // Result: FALSE

"ABC " > "ABC"  // Result: FALSE

"ABC" > "ABCDE"  // Result: FALSE

"ABCDE" > "ABC"  // Result: TRUE

"ABC" > ""  // Result: TRUE

"" > "ABC"  // Result: FALSE

AdsSetExact( FALSE )

"ABC" > "ABC "  // Result: FALSE

"ABC " > "ABC"  // Result: FALSE

"ABC" > "ABCDE"  // Result: FALSE

"ABCDE" > "ABC"  // Result: FALSE

"ABC" > ""  // Result: FALSE

"" > "ABC"  // Result: FALSE

 

Date:  Dates are compared according to the underlying date value.

Logical: True (.T.) is greater than false (.F.).

Numeric: Compared based on magnitude.

<=  Less than or equal to operator. Compares two values of the same data type and returns True if the operand on the left is less than or equal to the operand on the right.

Char:  The comparison is based on the underlying ANSI or OEM code (depending upon which collation is being used). If the lengths of the strings are equal, a simple comparison is performed. If the lengths of the strings are not equal, the first X number of characters in the string are compared, where X is the length of the shorter string. If those first X characters are the same:

| 1. | If the string on the left is shorter, True is returned. |

| 2. | If the string on the right is shorter, and AdsSetExact is True, False is returned. |

| 3. | If the string on the right is shorter, and AdsSetExact is False, True is returned. |

When AdsSetExact, which can be set by calling the Advantage Client Engine directly, is True trailing blanks are truncated for purposes of the comparison.

Examples:

AdsSetExact( TRUE )

"ABC" <= "ABC "  // Result: TRUE

"ABC " <= "ABC"  // Result: TRUE

"ABC" <= "ABCDE"  // Result: TRUE

"ABCDE" <= "ABC"  // Result: FALSE

"ABC" <= ""  // Result: FALSE

"" <= "ABC"  // Result: TRUE

AdsSetExact( FALSE )

"ABC" <= "ABC "  // Result: TRUE

"ABC " <= "ABC"  // Result: TRUE

"ABC" <= "ABCDE"  // Result: TRUE

"ABCDE" <= "ABC"  // Result: TRUE

"ABC" <= ""  // Result: TRUE

"" <= "ABC"  // Result: TRUE

 

Date:  Dates are compared according to the underlying date value.

Logical: False (.F.) is less than or equal to true (.T.).

Numeric: Compared based on magnitude.

>=  Greater than or equal to operator. Compares two values of the same data type and returns True if the operand on the left is greater than or equal to the operand on the right.

Char:  The comparison is based on the underlying ANSI or OEM code (depending upon which collation is being used). If the lengths of the strings are equal, a simple comparison is performed. If the lengths of the strings are not equal, the first X number of characters in the string are compared, where X is the length of the shorter string. If those first X characters are the same:

| 1. | If the string on the left is shorter, False is returned. |

| 2. | If the string on the right is shorter True is returned. |

When AdsSetExact, which can be set by calling the Advantage Client Engine directly, is True trailing blanks are truncated for purposes of the comparison.

Examples:

AdsSetExact( TRUE )

"ABC" >= "ABC "  // Result: TRUE

"ABC " >= "ABC"  // Result: TRUE

"ABC" >= "ABCDE"  // Result: FALSE

"ABCDE" >= "ABC"  // Result: TRUE

"ABC" >= ""  // Result: TRUE

"" >= "ABC"  // Result: FALSE

AdsSetExact( FALSE )

"ABC" >= "ABC "  // Result: FALSE

"ABC " >= "ABC"  // Result: TRUE

"ABC" >= "ABCDE"  // Result: FALSE

"ABCDE" >= "ABC"  // Result: TRUE

"ABC" >= ""  // Result: TRUE

"" >= "ABC"  // Result: FALSE

 

Date:  Dates are compared according to the underlying date value.

Logical: True (.T.) is greater than or equal to false (.F.).

Numeric: Compared based on magnitude.

$  String containment operator. A case-sensitive search is performed on the string to the right of the operator for the string to the left of the operator and returns True if found.

Examples:

"A" $ "BACK"  // Result: TRUE

"a" $ "BACK"  // Result: FALSE

 

Logical Operators

AND  Logically ANDs two operands. If both expressions are True, True is returned. If either expression is False, False is returned.

OR  Logically ORs two operands. If either expression is True, True is returned. If both expressions are False, False is returned.

NOT Unary logical operator that returns the logical inverse of the operand.

Evaluation Order

When more than one type of operator appears in an expression, the order of evaluation is as follows:

| 1. | alias operators |

| 2. | string and join operators |

| 3. | numeric and date operators |

| 4. | relational operators |

| 5. | logical operators |

Expressions containing more than one operator are evaluated from left to right. Parentheses are used to change the evaluation order. If parentheses are nested, the innermost set is evaluated first.

Numeric operators are evaluated according to generally accepted arithmetic principles:

| 1. | operators contained in parentheses |

| 2. | exponentiation |

| 3. | multiplication, division, and modulus |

| 4. | addition and subtraction |

Order of evaluation may by altered with parentheses:

3 + 4 \* 5 + 6 = 29

(3+4) \* 5 + 6 = 41

(3+4) \* (5+6) = 77

 

For clarity it is best to use parentheses rather than depend on the order of evaluation. The first two lines above would be better written as:

3 + (4\*5) + 6 = 29

((3+4) \*5) + 6 = 41

Logical operators are evaluated as NOT first, AND second, and OR last. Logical evaluation order may also be altered with parentheses. Again, to avoid confusion in multiple conditional expressions it is always best to use parentheses to clarify intent.
