User Defined Functions and Packages




Advantage Database Server 12  

     User Defined Functions and Packages

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| User Defined Functions and Packages  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      User Defined Functions and Packages Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_User\_Defined\_Functions\_and\_Packages Advantage Developer's Guide > Part II - Advantage SQL > Chapter 13 - SQL Scripting Language > User Defined Functions and Packages / Dear Support Staff, |  |
| User Defined Functions and Packages  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

When you create a user defined function, you have the option of associating it with a package. A package is nothing more than a container for user defined functions.

The primary benefit of a package is that it defines a namespace for the user defined functions it contains. While all of the user defined functions in a given namespace must have different names, two or more user defined functions in different name spaces can have the same name.

For example, imagine that you have two packages in your data dictionary, one called CustomUtils and another called Math. Each of these packages can include a user defined function named GetType. When calling the GetType function, you identify which of these two functions you want by identifying the associated namespace using dot notation. For example, the following call to GetType invokes the GetType function from the CustomUtils package:

CustomUtils.GetType('CUSTOMER')

The use of packages is optional. If you do not have many user defined functions and dont find a need for packages, you can create your user defined functions without placing them in packages. In those cases, you omit the namespace when you call your functions. For example, if the GetType function is not in a package, you can invoke it using the following call:

GetType('CUSTOMER')

The function you will create in the following sections is rather simple. This function, named RandomRange, returns a random integer between a low and high value that you define. You define the low and high limit of the range by passing two integers in your call to RandomRange.

This function is interesting for two reasons. First, it extends the Advantage Query Engine with a function that it does not currently support.

The second interesting thing about this function is that, although the actual calculation to produce an integer at random for a range is not very complex, if you need this calculation in many different areas of your client application and you don't use a user defined function, you run the risk of having one or more of the instances of this calculation performed incorrectly. So, even though the function code is not elaborate, using a user defined function ensures that once the calculation is correct, it will be performed correctly every time the function is called. This benefit increases in direct proportion to the complexity of the code contained in your function and the number of places from which it is called.

The following sections walk you through the process of creating a package, creating a user defined function in that package, and calling the function.