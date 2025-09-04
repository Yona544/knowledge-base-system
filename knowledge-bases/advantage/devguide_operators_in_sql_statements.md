Operators in SQL Statements




Advantage Database Server 12  

     Operators in SQL Statements

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Operators in SQL Statements  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Operators in SQL Statements Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Operators\_in\_SQL\_Statements Advantage Developer's Guide > Part II - Advantage SQL > Chapter 11 - Introduction to Advantage SQL > Operators in SQL Statements / Dear Support Staff, |  |
| Operators in SQL Statements  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Operators are used to create or modify expressions. Unary operators, such as the integer (negation) and the Boolean NOT (negation), modify an operand. Binary operators, such as the string + (concatenation) and the Boolean = (equals), create a new expression by combining two operands.

The process of applying an operator to an expression is referred to as expression evaluation, and the result is also an expression of some type. For example, the following is an expression:

1 + 1

In this case, two expressions, each a numeric literal, are combined through addition. The result is a single numeric expression with the value of 2.

Expression evaluation normally proceeds from left to right. Consider the following expression using the addition operator (+), in which 1 and 1 are added together to make 2, and then 2 is added to 5 to make 7:

1 + 1 + 5

But not all operators have the same precedence. Operations involving operators of a higher precedence are executed first, followed by operators of lower precedence. When two operators have the same precedence, the operators are evaluated from left to right. For example, the multiplication operator (\*) has a higher precedence than the addition operator. Consider the following expression:

1 + 1 \* 5

The result of this expression is 6. The multiplication is executed first, resulting in a value of 5. Next, the addition operator adds 1 to 5, resulting in 6.

You can control precedence by using parentheses. Operations within parentheses are always performed as a unit. For example, the following expression evaluates to 10. First, 1 is added to 1 to get 2. Next, 2 is multiplied by 5 to produce 10.

(1 + 1) \* 5

The operators available in Advantage SQL are described in the following sections. These sections are divided by the type of expressions that the operators apply to. Within each section, the operators are further divided by operator type, ordered by operator type precedence. Operators with higher precedence are described before operators with lower precedence.

Boolean Operators

There are three Boolean operator types. These are logical comparison operators, the logical complement operator, and logical operators.

Logical Comparison Operators

Logical comparison operators are binary operators that employ two logical operands, and that result in a Boolean expression. The logical comparison operators are = (equals), <> (not equals), IS NULL, and IS NOT NULL. For both IS NULL and IS NOT NULL, the first operand must be a field name reference.

Logical Complement Operator

The logical complement operator is NOT. Use it to convert a Boolean True to False, and a Boolean False to True.

Logical Operators

There are two logical operatorsAND and ORand both require two Boolean operands. An AND operation results in a Boolean True if, and only if, both operands are True, and results in False otherwise. An OR operation evaluates to a Boolean True if at least one of the operands is a Boolean True, and evaluates to False only if both operands are False.

Numeric Operators

There are three categories of numeric operators. These are numeric sign change operators, numeric arithmetic operators, and numeric comparison operators.

Numeric Sign Change Operators

Numeric sign change operators are unary operators, and there are two: and +. In reality, only the sign change operator has utility. Precede a numeric operand with a - to change the sign of the numeric expression.

Numeric Arithmetic Operators

There are four numeric arithmetic operators: \* (multiplication), / (division), + (addition), (subtraction). Each of these operators requires two numeric operands, and result in a numeric expression. If at least one of the operands is a floating-point expression, the result will be a floating-point expression. Within this type, \* and / have higher precedence than + and .

Numeric Comparison Operators

The numeric comparison operators are > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to), = (equal to), IN, NOT IN, BETWEEN, NOT BETWEEN, IS NULL, and IS NOT NULL. Numeric comparison operators require two numeric operands and evaluate to a Boolean expression.

String Operators

There are two types of string operators: the string concatenation operator and string comparison operators.

String Concatenation Operator

The string concatenation operator (+) is used to combine two string operands, producing a string expression. The resulting string expression contains all characters in the first operand plus all characters in the second.

String Comparison Operators

The string comparison operators are > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to), = (equal to), LIKE, NOT LIKE, IN, NOT IN, BETWEEN, NOT BETWEEN, IS NULL, and IS NOT NULL. These are binary operators that evaluate to a Boolean expression. Using LIKE, IN, and BETWEEN is discussed in Chapter 12.

Date Operators

There are two types of date operators: date arithmetic operators and date comparison operators.

Date Arithmetic Operators

Date arithmetic operators are binary operators where one operand is a date expression and the other is an integer expression. Date arithmetic operators evaluate to a date expression. The date arithmetic operators are + (addition) and (subtraction). Use the + operator to calculate a date some specified number of days in the future, and the operator to calculate a date some specified number of days in the past.

Date Comparison Operators

Date comparison operators are binary operators that compare two date operands and evaluate to a Boolean expression. The valid date comparison operators are > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to), <> (not equal to), = (equal to), BETWEEN, NOT BETWEEN, IS NULL, and IS NOT NULL.

Time and Timestamp Operators

There is only one type of operator that applies to time and timestamp expressions. These are the time comparison operators.

Time Comparison Operators

Time comparison operators are binary operators that evaluate to a Boolean expression. The time operators are > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to), = (equal to), and <> (not equal to). The >, <, >=, <=, and <> operators require two time or timestamp operands.

Other Operators

Fixed-length and BLOB (binary large object) expressions can be used with comparison operators. Fixed-length binary expressions can employ the > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to), = (equal to), <> (not equal to), IN, NOT IN, IS NULL, and IS NOT NULL operators. These are binary operators that take two fixed-length binary operands and evaluate to a Boolean expression.

Variable-length binary (BLOB) fields support two comparison operators: IS NULL and IS NOT NULL. These unary operators take one BLOB field operand and evaluate to a Boolean expression.