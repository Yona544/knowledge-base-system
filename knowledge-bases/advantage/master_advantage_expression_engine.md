Advantage Expression Engine




Advantage Database Server 12  

Advantage Expression Engine

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Expression Engine  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Advantage Expression Engine Advantage Concepts master\_Advantage\_expression\_engine Advantage Concepts > Advantage Functionality > Advantage Expression Engine / Dear Support Staff, |  |
| Advantage Expression Engine  Advantage Concepts |  |  |  |  |

The Advantage Expression Engine, which resides in the Advantage server, is used to evaluate expressions within filters or index statements. Successful expression evaluation allows Advantage to build indexes and filter records on the Advantage server. This provides faster results by avoiding the need to send raw data to the client for evaluation.

The Expression Engine can parse and evaluate operators, fields (columns), literal values, and many functions within the expression. A number of scalar functions are supported for navigational use (e.g., in filters and index expressions). The following general types of functions are supported:

[Math Functions](master_math_functions.htm)

[String Functions](master_string_functions.htm)

[Date/Time Functions](master_date_time_functions.htm)

[Miscellaneous Functions](master_miscellaneous_functions.htm)

Not all scalar functions are supported for both SQL usage and navigational usage. An overview of the support is discussed in [Indexes with Expressions](master_indexes_with_expressions.htm). In addition, each individual documentation page for the scalars indicates the environments in which it is supported.

Advantage ADT and Visual FoxPro (VFP) table types support true NULL values. If a true NULL value is supplied as part of the expression or as a parameter to an expression engine function listed below, the final result of the expression is typically NULL. Exceptions to this include the EMPTY and ISNULL functions, which always have a True or False result. The EMPTY and ISNULL functions are equivalent on ADT tables and return True when given a NULL value. With VFP tables, NULL and empty are not considered equivalent and the EMPTY and ISNULL functions return True/False appropriately.

The CDX and NTX DBF table types do not support true NULL values. Empty DBF fields are not considered as NULL in the expression engine. Instead, empty DBF fields are treated as its equivalent value. See [EMPTY()](master_empty.htm) for more information.

User-Defined Functions (UDFs) are not supported in the Advantage Expression Engine. If unsupported functions are used in your expressions, the Advantage Expression Engine will be unable to evaluate the expression.

Directly specifying memo, binary, and image field names in expressions is generally not supported by the Advantage Expression Engine. If memo, binary, or image fields are used directly or in most expression engine functions in your expressions, the Advantage Expression Engine will be unable to evaluate the expression. The [CONTAINS()](master_contains.htm) function is the only Expression Engine function that supports memo, binary, and image fields.

See also:

[Expression Engine Operators](master_expression_engine_operators.htm)

[Expression Engine Examples](master_expression_engine_examples.htm)

[Expression Engine Performance](master_expression_engine_performance.htm)