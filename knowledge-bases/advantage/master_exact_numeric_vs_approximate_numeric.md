Exact Numeric vs Approximate Numeric




Advantage Database Server 12  

Exact Numeric vs Approximate Numeric

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Exact Numeric vs Approximate Numeric  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Exact Numeric vs Approximate Numeric Advantage SQL Engine master\_Exact\_numeric\_vs\_approximate\_numeric Advantage SQL > SQL Functionality > Exact Numeric vs Approximate Numeric / Dear Support Staff, |  |
| Exact Numeric vs Approximate Numeric  Advantage SQL Engine |  |  |  |  |

When an algebraic expression or aggregate function is used with numeric value as input, it is important to understand the difference between the exact numeric data and approximate numeric data. If all operand(s) of the expression are exact numeric values, the result will be exact numeric data. If any operand of the expression is approximate numeric, the result will be approximate numeric.

In Advantage SQL engine, the approximate numeric values are represented with IEEE Double. They can be derived from column data that have the column type SQL\_Double or Double. The numeric literals in the SQL statements are interpreted as approximate numeric values if they are written in scientific notation (e.g., 1e2 and 1e-2 will be interpreted as approximated numeric values). The numeric literals can also be interpreted as approximate numeric values if the precision of the numeric literals exceeds the maximum supported numeric precision, which is 30 in Advantage SQL engine. The approximate numeric can store a huge range of values 1.7E +/-308 but it has only about 15 digits of precision.

The exact numeric types are Integer (4-byte) and Numeric (i.e., Decimal, variable length). The exact numeric types are defined with precision (maximum number of decimal digits allowed in the value) and scale (maximum number of decimal digits allowed after the decimal point). If the result of the expression is to be in exact numeric, the precision and scale of the operands will have a direct influence on the result, as described later. The maximum precision for exact numeric type in the Advantage SQL engine is 30. It is clear that exact numeric can have many more digits of precision than the approximate numeric but it has a much smaller range.

The exact numeric types are derived from the following sources:

Integer

|  |  |
| --- | --- |
| 1. | 1. From column data that has the column type SQL\_INTEGER or Integer, SQL\_SMALLINT or ShortInt. The precision of the data will be 10 for integer and 5 for smallint. The scale will be 0. |

|  |  |
| --- | --- |
| 2. | 2. From numeric literals that do not have a decimal point and less than 9 digits. For example: 123456 and 1 are integers. The precision of the data will be the number of digits in the literal. |

Numeric

|  |  |
| --- | --- |
| 1. | 1. From column data that has the column type SQL\_NUMERIC or Numeric. The precision and scale of the data will be the same as defined by the column. |

|  |  |
| --- | --- |
| 2. | 2. From numeric literals that have a decimal point and precision less than or equal to maximum supported precision (30). It can also derive from numeric literals that do not have decimal point but the precision is too large to be stored in an integer. The precision and scale of the data are defined based on the actual value. For example, the numeric literal 1.234 will have precision of 4 and scale of 3. The numeric literal 1234567890 will be a numeric type with precision of 10 and scale of 0. |

Resultant Precision and Scale of Exact Numeric

For expression that takes only one input and all aggregate functions (MIN(), MAX(), and AVG()) except the SUM() aggregate function, the resultant type is the same as the input type. The SUM() aggregate function on a numeric (but not an integer) input will result in numeric type with precision that is 10 plus the precision of the source expression. The final precision cannot exceed the maximum allowed by the Advantage SQL engine.

If it is desirable to have the resultant type in a different type, the input data should be casted or converted into the appropriated types. For example, it is common to calculate the average of the data in an integer column and expect the result in fraction. AVG( int\_column ) will give the result in integer. To get the fractions, the expression should be AVG( Cast( int\_column AS SQL\_DOUBLE )).

For expressions that take two exact numeric values, Advantage SQL engine follows the guideline in the SQL standard:

"If the declared type of both operands of a dyadic arithmetic operator is exact numeric, then the declared type of the result is an implementation-defined exact numeric type, with precision and scale determined as follows:

|  |  |
| --- | --- |
| a. | a. Let S1 and S2 be the scale of the first and second operands respectively. |

|  |  |
| --- | --- |
| b. | b. The precision of the result of addition and subtraction is implementation-defined, and the scale is the maximum of S1 and S2. |

|  |  |
| --- | --- |
| c. | c. The precision of the result of multiplication is implementation-defined, and the scale is S1 + S2. |

|  |  |
| --- | --- |
| d. | d. The precision and scale of the result of division are implementation-defined." |

In Advantage SQL engine, if both operands are integer than the result is type integer. If either one of the operands is numeric, the result is type numeric.

For addition and subtraction, the precision of the result is (1 + scale + whole number digits). The "whole number digits" is the larger of the whole number portions of the two operands.

For multiplication, the precision of the result is (scale + sum of the whole number digits of both operands).

For addition, subtraction, and multiplication, if the calculated precision is larger than the maximum allowed precision, the precision is reduced to the maximum allowed precision. If the calculated scale is larger than the maximum allowed precision, the 2231 Numeric result out of range error will be returned during query preparation. (Refer to the Advantage Error Guide section of the help for error definitions.)

For division, there is no definitive method for determining the precision and scale of the result. Advantage will generally calculate the precision and scale of the result using the maximum and minimum possible values of the divisor. If the calculated precision is larger than the maximum allowed precision, the precision of the result will be set to the maximum allowed precision and the scale will be set to 20.

Because the precision of the numeric result is fixed at query preparation time and it cannot exceed the maximum allowed value, it is possible for the evaluated result of the expression to be outside the range of the predetermined precision and scale. For example, multiplication of two numeric values with precision of 20 and scale of 10 can result in a numeric value with precision of 40 and scale of 20. Since the maximum supported precision value is 30, it is possible for the result to exceed maximum supported precision. When such case is encountered, a 2232 Numeric overflow will be returned (Refer to the Advantage Error Guide section of the help for error definitions.). To remedy this error, it is generally necessary to cast the one of the operands of expression into the approximate numeric (i.e., Double).