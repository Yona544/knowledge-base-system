---
title: Dotnet Create Sample Database
slug: dotnet_create_sample_database
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_create_sample_database.htm
source: Advantage CHM
tags:
  - dotnet
checksum: ff1aedd5e9401eace95539db24d03447da38f3b8
---

# Dotnet Create Sample Database

Create Sample Database

Create Sample Database

Advantage .NET Data Provider

| Create Sample Database  Advantage .NET Data Provider |  |  |  |  |

The following database is used by the quickstart guide in the rest of the tasks.  You can create the example database using the [Advantage Data Architect](master_advantage_data_architect.md).

| 1. | Select File | Create New Data Dictionary |

| 2. | For the Name enter EFDemo |

| 3. | For the Path enter c:\example\ |

| 4. | Click OK |

| 5. | Select Tools | SQL Utility |

| 6. | Select File | New SQL Script |

| 7. | Paste the following SQL Script into the query window and select SQL | Execute Query |

See Also

[Entity Framework Quick Start Overview](dotnet_entity_quick_start_overview.md)

[Create the Entity Data Model](dotnet_create_an_entity_model.md)

[Display Records using LINQ](dotnet_display_records_using_linq.md)

 

CREATE TABLE Contacts (

    ID Integer,

    Surname Char( 20 ),

    GivenName Char( 20 ),

    Title Char( 34 ),

    Street Char( 30 ),

    City Char( 20 ),

    State Char( 16 ),

    Country Char( 16 ),

    PostalCode Char( 10 ),

    Phone Char( 13 ),

    Fax Char( 13 ),

    CustomerID Integer) IN DATABASE;

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'Contacts',

  'Contacts.adi',

  'ID',

  'ID',

  '',

  2051,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'Contacts',

  'Contacts.adi',

  'CUSTOMERID',

  'CustomerID',

  '',

  2,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_ModifyTableProperty( 'Contacts',

  'Table\_Primary\_Key',

  'ID', 'APPEND\_FAIL', 'Contactsfail');

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Contacts',

    'ID', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Contactsfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Contacts',

    'Surname', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Contactsfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Contacts',

    'GivenName', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Contactsfail' );

 

CREATE TABLE Customers (

    ID INTEGER,

    Surname Char( 20 ),

    GivenName Char( 20 ),

    Street Char( 30 ),

    City Char( 20 ),

    State Char( 16 ),

    Country Char( 16 ),

    PostalCode Char( 10 ),

    Phone Char( 13 ),

    CompanyName Char( 32 )) IN DATABASE;

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'Customers',

  'Customers.adi',

  'ID',

  'ID',

  '',

  2051,

  512,

  '' );

 

EXECUTE PROCEDURE sp\_ModifyTableProperty( 'Customers',

  'Table\_Primary\_Key',

  'ID', 'APPEND\_FAIL', 'Customersfail');

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Customers',

    'ID', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Customersfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Customers',

    'Surname', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Customersfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Customers',

    'GivenName', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Customersfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Customers',

    'Street', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Customersfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Customers',

    'Phone', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Customersfail' );

 

CREATE TABLE Departments (

    DepartmentID Integer,

    DepartmentName Char( 40 ),

    DepartmentHeadID Integer) IN DATABASE;

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'Departments',

  'Departments.adi',

  'DEPARTMENTID',

  'DepartmentID',

  '',

  2051,

  512,

  '' );

 

EXECUTE PROCEDURE sp\_ModifyTableProperty( 'Departments',

  'Table\_Primary\_Key',

  'DEPARTMENTID', 'APPEND\_FAIL', 'Departmentsfail');

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Departments',

    'DepartmentID', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Departmentsfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Departments',

    'DepartmentName', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Departmentsfail' );

 

CREATE TABLE Employees (

    EmployeeID Integer,

    ManagerID Integer,

    Surname Char( 20 ),

    GivenName Char( 20 ),

    DepartmentID Integer,

    Street Char( 30 ),

    City Char( 20 ),

    State Char( 16 ),

    Country Char( 16 ),

    PostalCode Char( 10 ),

    Phone Char( 13 ),

    Status Char( 2 ),

    SocialSecurityNumber Char( 11 ),

    Salary Money,

    StartDate Date,

    TerminationDate Date,

    BirthDate Date,

    BenefitHealthInsurance Logical,

    BenefitLifeInsurance Logical,

    BenefitDayCare Logical,

    Sex Char( 2 )) IN DATABASE;

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'Employees',

  'Employees.adi',

  'EMPLOYEEID',

  'EmployeeID',

  '',

  2051,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'Employees',

  'Employees.adi',

  'DEPARTMENTID',

  'DepartmentID',

  '',

  2,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_ModifyTableProperty( 'Employees',

  'Table\_Primary\_Key',

  'EMPLOYEEID', 'APPEND\_FAIL', 'Employeesfail');

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Employees',

    'EmployeeID', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Employeesfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Employees',

    'Surname', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Employeesfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Employees',

    'GivenName', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Employeesfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Employees',

    'DepartmentID', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Employeesfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Employees',

    'Street', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Employeesfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Employees',

    'City', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Employeesfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Employees',

    'StartDate', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Employeesfail' );

 

CREATE TABLE FinancialCodes (

    Code Char( 2 ),

    Type Char( 10 ),

    Description Char( 50 )) IN DATABASE;

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'FinancialCodes',

  'FinancialCodes.adi',

  'CODE',

  'Code',

  '',

  2051,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_ModifyTableProperty( 'FinancialCodes',

  'Table\_Primary\_Key',

  'CODE', 'APPEND\_FAIL', 'FinancialCodesfail');

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'FinancialCodes',

    'Code', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'FinancialCodesfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'FinancialCodes',

    'Type', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'FinancialCodesfail' );

 

CREATE TABLE FinancialData (

    Year Char( 4 ),

    Quarter Char( 2 ),

    Code Char( 2 ),

    Amount Integer) IN DATABASE;

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'FinancialData',

  'FinancialData.adi',

  'FINANCIALDATAKEY',

  'Year;Quarter;Code',

  '',

  2051,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'FinancialData',

  'FinancialData.adi',

  'CODE',

  'Code',

  '',

  2,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_ModifyTableProperty( 'FinancialData',

  'Table\_Primary\_Key',

  'FINANCIALDATAKEY', 'APPEND\_FAIL', 'FinancialDatafail');

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'FinancialData',

    'Year', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'FinancialDatafail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'FinancialData',

    'Quarter', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'FinancialDatafail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'FinancialData',

    'Code', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'FinancialDatafail' );

 

CREATE TABLE MarketingInformation (

    ID Integer,

    ProductID Integer,

    Description Memo) IN DATABASE;

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'MarketingInformation',

  'MarketingInformation.adi',

  'ID',

  'ID',

  '',

  2051,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'MarketingInformation',

  'MarketingInformation.adi',

  'PRODUCTID',

  'ProductID',

  '',

  2,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_ModifyTableProperty( 'MarketingInformation',

  'Table\_Primary\_Key',

  'ID', 'APPEND\_FAIL', 'MarketingInformationfail');

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'MarketingInformation',

    'ID', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'MarketingInformationfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'MarketingInformation',

    'ProductID', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'MarketingInformationfail' );

 

CREATE TABLE Products (

    ID Integer,

    Name Char( 15 ),

    Description Char( 30 ),

    Size Char( 18 ),

    Color Char( 6 ),

    Quantity Integer,

    UnitPrice Money,

    Photo Blob) IN DATABASE;

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'Products',

  'Products.adi',

  'ID',

  'ID',

  '',

  2051,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_ModifyTableProperty( 'Products',

  'Table\_Primary\_Key',

  'ID', 'APPEND\_FAIL', 'Productsfail');

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Products',

    'ID', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Productsfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Products',

    'Name', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Productsfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Products',

    'Description', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Productsfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Products',

    'Size', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Productsfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Products',

    'Color', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Productsfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Products',

    'Quantity', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Productsfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'Products',

    'UnitPrice', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'Productsfail' );

 

CREATE TABLE SalesOrderItems (

    ID INTEGER,

    LineID Short,

    ProductID Integer,

    Quantity Integer,

    ShipDate Date) IN DATABASE;

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'SalesOrderItems',

  'SalesOrderItems.adi',

  'SALESORDERITEMSKEY',

  'ID;LineID',

  '',

  2051,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'SalesOrderItems',

  'SalesOrderItems.adi',

  'ID',

  'ID',

  '',

  2,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_ModifyTableProperty( 'SalesOrderItems',

  'Table\_Primary\_Key',

  'SALESORDERITEMSKEY', 'APPEND\_FAIL', 'SalesOrderItemsfail');

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'SalesOrderItems',

    'ID', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'SalesOrderItemsfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'SalesOrderItems',

    'LineID', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'SalesOrderItemsfail' );

 

CREATE TABLE SalesOrders (

    ID INTEGER,

    CustomerID Integer,

    OrderDate Date,

    FinancialCode Char( 2 ),

    Region Char( 7 ),

    SalesRepresentative Integer) IN DATABASE;

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'SalesOrders',

  'SalesOrders.adi',

  'ID',

  'ID',

  '',

  2051,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'SalesOrders',

  'SalesOrders.adi',

  'CUSTOMERID',

  'CustomerID',

  '',

  2,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'SalesOrders',

  'SalesOrders.adi',

  'SALESREPRESENTATIVE',

  'SalesRepresentative',

  '',

  2,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_CreateIndex90(

  'SalesOrders',

  'SalesOrders.adi',

  'FINANCIALCODE',

  'FinancialCode',

  '',

  2,

  512,

  '' );

 

 

EXECUTE PROCEDURE sp\_ModifyTableProperty( 'SalesOrders',

  'Table\_Primary\_Key',

  'ID', 'APPEND\_FAIL', 'SalesOrdersfail');

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'SalesOrders',

    'ID', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'SalesOrdersfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'SalesOrders',

    'CustomerID', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'SalesOrdersfail' );

 

EXECUTE PROCEDURE sp\_ModifyFieldProperty ( 'SalesOrders',

    'SalesRepresentative', 'Field\_Can\_Be\_Null',

    'False', 'APPEND\_FAIL', 'SalesOrdersfail' );

 

 

INSERT INTO "Contacts" VALUES( 1, 'Hildebrand', 'Jane', 'ma', '280 Washington St.', 'Kanata', 'CA', 'USA', '94608', '5105551309', '5105554209', 119 );

INSERT INTO "Contacts" VALUES( 2, 'Simmon', 'Larry', 'sa', '343 Granville St.', 'Kitchener', 'TX', 'USA', '77079', '7135558960', '7135559265', 332 );

INSERT INTO "Contacts" VALUES( 3, 'Critch', 'Susan', 'pd', '457 Center St.', 'Yale', 'WY', 'USA', '01923', '5085554829', '5085553025', 220 );

INSERT INTO "Contacts" VALUES( 4, 'Lambert', 'Terry', 'ad', '20434 Page St.', 'Phillipsburg', 'CO', 'USA', '94608', '6175552246', '6175553692', 174 );

INSERT INTO "Contacts" VALUES( 5, 'Sullivan', 'Dorothy', 'cs', '541 Minuteman Dr.', 'Uxbridge', 'ME', 'USA', '01742', '5085553925', '5085559931', NULL );

INSERT INTO "Contacts" VALUES( 6, 'Paull', 'Rose', 'fi', '718 Bay St.', 'Huntsville', 'AZ', 'USA', '01945', '6175556392', '6175551495', 221 );

INSERT INTO "Contacts" VALUES( 7, 'Glassmann', 'Beth', 'pd', '144 Oak St.', 'Newcastle', 'IL', 'USA', '02173', '6175550273', '6175559933', 158 );

INSERT INTO "Contacts" VALUES( 8, 'Powell', 'Gene', 'tr', '52 West Main St.', 'Newcastle', 'IL', 'USA', '02173', '6175553528', '6175559563', 188 );

INSERT INTO "Contacts" VALUES( 9, 'Fish', 'Jeffrey', 'ma', '168 Red Acre Rd.', 'Newcastle', 'IL', 'USA', '02173', '6175553528', '6175559563', 158 );

INSERT INTO "Contacts" VALUES( 10, 'Clarke', 'Molly', 'sa', '557 Pine Grove Rd.', 'Newcastle', 'IL', 'USA', '02173', '6175554325', '6175557638', 188 );

INSERT INTO "Contacts" VALUES( 11, 'Kelley', 'William', 'do', '163 Rainbow Rd.', 'Hamilton', 'MI', 'USA', '01803', '6175558474', '6175552594', 204 );

INSERT INTO "Contacts" VALUES( 12, 'Lyman', 'Thomas', 'cs', '642 Story Rd.', 'Kanata', 'CA', 'USA', '94608', '5105555378', '5105553372', 126 );

INSERT INTO "Contacts" VALUES( 13, 'Davidson', 'Joann', 'ma', '6 Story Rd.', 'Kanata', 'CA', 'USA', '94608', '5105557363', '5105559278', 126 );

INSERT INTO "Contacts" VALUES( 14, 'Pettengill', 'Mark', 'sa', '126 Briarwood Ter.', 'Kanata', 'CA', 'USA', '94608', '5105553533', '5105551146', 168 );

INSERT INTO "Contacts" VALUES( 15, 'Moore', 'Dawn', 'sa', 'One Park Drive', 'Oakville', 'GA', 'USA', '30339', '4045554834', '4045558291', 195 );

INSERT INTO "Contacts" VALUES( 16, 'Lencki', 'John', 'cs', '20 Brook Road', 'Hamilton', 'MI', 'USA', '01803', '6175555348', '6175554619', 204 );

INSERT INTO "Contacts" VALUES( 17, 'Kaplan', 'Burt', 'sa', '491 Keaton Lane', 'London', 'CO', 'USA', '02174', '6175553887', '6175552398', 139 );

INSERT INTO "Contacts" VALUES( 18, 'Hayne', 'William', 'cs', '883 Cornfield Ave.', 'Waterloo', 'AZ', 'USA', '01720', '5085557780', '5085554422', NULL );

INSERT INTO "Contacts" VALUES( 19, 'Chin', 'David', 'pd', '162 Waverly Rd.', 'Hamilton', 'MI', 'USA', '01803', '6175553378', '6175554453', 204 );

INSERT INTO "Contacts" VALUES( 20, 'White', 'Pauline', 'sa', '5756 Prince St.', 'Kitchener', 'TX', 'USA', '77079', '7135553345', '7135559222', 332 );

INSERT INTO "Contacts" VALUES( 21, 'Cobb', 'Paul', 'cs', '81 Greenville St.', 'Oakville', 'GA', 'USA', '30339', '4045552239', '4045558111', 195 );

INSERT INTO "Contacts" VALUES( 22, 'Goggin', 'Kevin', 'cs', '808 East Main St.', 'Kitchener', 'TX', 'USA', '77079', '7135553340', '7135559211', 444 );

INSERT INTO "Contacts" VALUES( 23, 'Cohen', 'Paul', 'cs', '10 Park Street', 'Hamilton', 'MI', 'USA', '01803', '6175558883', '6175554499', NULL );

INSERT INTO "Contacts" VALUES( 24, 'Quinn', 'Peter', 'sa', '8817 Shaw Rd.', 'Cornwall', 'NY', 'USA', '02192', '6175552222', '6175559337', 116 );

INSERT INTO "Contacts" VALUES( 25, 'Brier', 'Michael', 'ad', '97 Blackstone St.', 'London', 'CO', 'USA', '02174', '6175552398', '6175553337', 128 );

INSERT INTO "Contacts" VALUES( 26, 'Mulley', 'Joan', 'pd', '10 Westborn Ter.', 'Hamilton', 'MI', 'USA', '01803', '6175553998', '6175552299', 190 );

INSERT INTO "Contacts" VALUES( 27, 'Evans', 'Carrie', 'sa', '189 Washington St.', 'Oakville', 'GA', 'USA', '30339', '4045551169', '4045558244', 195 );

INSERT INTO "Contacts" VALUES( 28, 'Philley', 'Mary', 'sa', '592 Franklin Pl.', 'Kitchener', 'TX', 'USA', '77079', '7135553338', '7135559066', 444 );

INSERT INTO "Contacts" VALUES( 29, 'Sinibaldi', 'Joseph', 'do', '117 Center St.', 'London', 'CO', 'USA', '02174', '6175556699', '6175554231', 139 );

INSERT INTO "Contacts" VALUES( 30, 'DeMarco', 'Michael', 'pd', '231 Clare Ave.', 'Elora', 'OR', 'USA', '01730', '6175554400', '6175557876', 551 );

INSERT INTO "Contacts" VALUES( 31, 'Miller', 'Henry', 'tr', '932 Porter St.', 'Hamilton', 'MI', 'USA', '01803', '6175553356', '6175551332', 190 );

INSERT INTO "Contacts" VALUES( 32, 'Reeves', 'Scott', 'cs', '10 Linden St.', 'Hespeler', 'NJ', 'USA', '08830', '6035550988', '6035555556', 101 );

INSERT INTO "Contacts" VALUES( 33, 'Page', 'Lynn', 'sa', '53 Central Ave.', 'Cornwall', 'NY', 'USA', '02192', '6175558890', '6175554544', 111 );

INSERT INTO "Contacts" VALUES( 34, 'Crowley', 'Charles', 'hr', '19 Edson St.', 'Hamilton', 'MI', 'USA', '01803', '6175551344', '6175559877', 159 );

INSERT INTO "Contacts" VALUES( 35, 'Burrill', 'Dana', 'pd', '942 Beacon St.', 'Cornwall', 'NY', 'USA', '02192', '6175557956', '6175552398', 111 );

INSERT INTO "Contacts" VALUES( 36, 'Caruso', 'William', 'fi', '199 Edison St.', 'Elora', 'OR', 'USA', '01730', '6175552144', '6175551656', NULL );

INSERT INTO "Contacts" VALUES( 37, 'Purcell', 'Beth', 'sa', '1348 Cherry Hill St.', 'London', 'CO', 'USA', '02174', '6175552349', '6175551765', 174 );

INSERT INTO "Contacts" VALUES( 38, 'Weaver', 'Joe', 'ma', '818 Main St.', 'Kitchener', 'TX', 'USA', '77079', '7135551956', '7135554455', NULL );

INSERT INTO "Contacts" VALUES( 39, 'Dewey', 'Michael', 'fi', '105 Pleasant St.', 'Cornwall', 'NY', 'USA', '02192', '6175559877', '6175552322', 116 );

INSERT INTO "Contacts" VALUES( 40, 'Jordan', 'Susan', 'pd', '915 Gordon St.', 'Hamilton', 'MI', 'USA', '01803', '6175551123', '6175551999', 159 );

INSERT INTO "Contacts" VALUES( 41, 'Romeo', 'John', 'ad', '2350 Long Way', 'Sheffield', 'CA', 'USA', '90806', '3105554533', '3105551233', 133 );

INSERT INTO "Contacts" VALUES( 42, 'Haddad', 'Paul', 'pd', '89 Pleasant St.', 'Fort Frances', 'IL', 'USA', '60173', '7065558337', '7045555644', 661 );

INSERT INTO "Contacts" VALUES( 43, 'Schott', 'Amy', 'hr', '919 Remington St.', 'Kitchener', 'TX', 'USA', '77079', '7135558912', '7135554565', 444 );

INSERT INTO "Contacts" VALUES( 44, 'Short', 'Russell', 'cs', '412 Newton St.', 'Cornwall', 'NY', 'USA', '02192', '6175550993', '6175551170', NULL );

INSERT INTO "Contacts" VALUES( 45, 'Galvin', 'Liz', 'ma', '3165 Lexington St.', 'London', 'CO', 'USA', '02174', '6175559312', '6175559870', 128 );

INSERT INTO "Contacts" VALUES( 46, 'Crossland', 'Ellen', 'pd', '527 Rush Rd.', 'Hamilton', 'MI', 'USA', '01803', '6175550004', '6175558005', 159 );

INSERT INTO "Contacts" VALUES( 47, 'Bertrand', 'Coleman', 'do', '978 Dunster Pl.', 'Fort Frances', 'IL', 'USA', '60173', '7065552886', '7045554532', 661 );

INSERT INTO "Contacts" VALUES( 48, 'Rayner', 'Doug', 'ot', '341 Chapin St.', 'Kitchener', 'TX', 'USA', '77079', '7135558444', '7135559934', NULL );

INSERT INTO "Contacts" VALUES( 49, 'Lull', 'John', 'sa', '932 Lawn Rd.', 'Elora', 'OR', 'USA', '01730', '6175551745', '6175551233', 551 );

INSERT INTO "Contacts" VALUES( 50, 'Shishov', 'Irina', 'ma', '57 Park Drive', 'Oakville', 'GA', 'USA', '30339', '4045551233', '4045556837', 197 );

INSERT INTO "Contacts" VALUES( 51, 'Trayers', 'Ken', 'sa', '134 Heather Drive', 'London', 'CO', 'USA', '02174', '6175552384', '6175554127', 128 );

INSERT INTO "Contacts" VALUES( 52, 'Long', 'Peter', 'tr', '778 Grayson Rd.', 'Hamilton', 'MI', 'USA', '01803', '6175554519', '6175554339', 159 );

INSERT INTO "Contacts" VALUES( 53, 'Tippet', 'Debbie', 'cs', '185 Aberdeen Rd.', 'Fort Frances', 'IL', 'USA', '60173', '7065558227', '7045558474', 661 );

INSERT INTO "Contacts" VALUES( 54, 'Hodson', 'Jack', 'cs', '969 Lincoln St.', 'Waterloo', 'AZ', 'USA', '01720', '5085552998', '5085550022', NULL );

INSERT INTO "Contacts" VALUES( 55, 'Kosko', 'Kim', 'pd', '3234 Pleasant St.', 'Kitchener', 'TX', 'USA', '77079', '7135554657', '7135552738', 444 );

INSERT INTO "Contacts" VALUES( 56, 'McEvoy', 'Jim', 'sa', '323 Hawthorne Rd.', 'Fort Frances', 'IL', 'USA', '60173', '7065558532', '7045550123', 207 );

INSERT INTO "Contacts" VALUES( 57, 'Goodall', 'Sandra', 'sa', '756 Summer St.', 'Hamilton', 'MI', 'USA', '01803', '6175553647', '6175550059', NULL );

INSERT INTO "Contacts" VALUES( 58, 'Elkins', 'John', 'tr', '89 Goddard Highway', 'Hespeler', 'NJ', 'USA', '08830', '6035551200', '6035550078', 147 );

INSERT INTO "Contacts" VALUES( 59, 'Masalsky', 'Kurt', 'cs', '129 Garden St.', 'Oakville', 'GA', 'USA', '30339', '4045555111', '4045558347', 197 );

INSERT INTO "Contacts" VALUES( 60, 'Collins', 'MaryBeth', 'cs', '93 Lincoln Street', 'Hamilton', 'MI', 'USA', '01803', '6175551199', '6175559586', 661 );

 

 

INSERT INTO "Customers" VALUES( 101, 'Devlin', 'Michaels', '114 Pioneer Avenue', 'Kingston', 'NJ', 'USA', '07070', '2015558966', 'The Power Group' );

INSERT INTO "Customers" VALUES( 102, 'Reiser', 'Beth', '33 Whippany Road', 'Rockwood', 'NY', 'USA', '10154', '2125558725', 'AMF Corp.' );

INSERT INTO "Customers" VALUES( 103, 'Niedringhaus', 'Erin', '190 Windsor Street', 'Tara', 'PA', 'USA', '19301', '2155556513', 'Darling Associates' );

INSERT INTO "Customers" VALUES( 104, 'Mason', 'Meghan', '5520 Dundas Street East', 'Cheslea', 'TN', 'USA', '37919', '6155555463', 'P.S.C.' );

INSERT INTO "Customers" VALUES( 105, 'McCarthy', 'Laura', '110 Highway 36', 'Clinton', 'IN', 'USA', '46032', '3175558437', 'Amo & Sons' );

INSERT INTO "Customers" VALUES( 106, 'Phillips', 'Paul', '200 Cherry Creek N. Dr.', 'Brandon', 'CT', 'USA', '64579', '2035553464', 'Ralston Inc.' );

INSERT INTO "Customers" VALUES( 107, 'Colburn', 'Kelly', '1131 Vallco Parkway', 'Chandler', 'NC', 'USA', '27695-7209', '9195555152', 'The Home Club' );

INSERT INTO "Customers" VALUES( 108, 'Goforth', 'Matthew', '101 Wayzata Blvd.', 'Harriston', 'TN', 'USA', '37421', '6155558926', 'Raleigh Co.' );

INSERT INTO "Customers" VALUES( 109, 'Gagliardo', 'Jessie', '201 Park Avenue', 'Preston', 'PQ', 'Canada', 'K1A 0H3', '8195559539', 'Newton Ent.' );

INSERT INTO "Customers" VALUES( 110, 'Agliori', 'Michael', '135 North Glebe Road', 'Oshawa', 'OH', 'USA', '43216', '6145552496', 'The Pep Squad' );

INSERT INTO "Customers" VALUES( 111, 'Ricci', 'Dylan', '1470 Prosperity Avenue', 'Hastings', 'NY', 'USA', '13202', '3155554486', 'Dynamics Inc.' );

INSERT INTO "Customers" VALUES( 112, 'McDonough', 'Shawn', '1575 S Main Street', 'Orillia', 'MN', 'USA', '55428', '6125555603', 'McManus Inc.' );

INSERT INTO "Customers" VALUES( 113, 'Kaiser', 'Samuel', '44 Bristol Street', 'Lake of the Woods', 'MN', 'USA', '55041', '6125553409', 'Lakes Inc.' );

INSERT INTO "Customers" VALUES( 114, 'Chopp', 'Shane', '95 Summer Street', 'Newmarket', 'MN', 'USA', '55104', '6125556453', 'Howard Co.' );

INSERT INTO "Customers" VALUES( 115, 'Phillips', 'Shannon', '2055 Cory Road', 'Newmarket', 'MN', 'USA', '55114', '6125556425', 'Sterling & Co.' );

INSERT INTO "Customers" VALUES( 116, 'Gugliuzza', 'Brian', '391 Wyman Street', 'Stayner', 'NY', 'USA', '10543', '9145553817', 'Sampson & Sons' );

INSERT INTO "Customers" VALUES( 117, 'Morgan', 'Meredith', '9191 Galveston Drive', 'Unionville', 'OH', 'USA', '43081', '6145558989', 'Square Sports' );

INSERT INTO "Customers" VALUES( 118, 'Sanford', 'Kristina', '22 96th Street', 'Chandler', 'NC', 'USA', '27695-7209', '9195555152', 'Raleigh Active Wear' );

INSERT INTO "Customers" VALUES( 119, 'Smith', 'Tomm', '37 Post Oak Blvd.', 'Owen Sound', 'CA', 'USA', '92677', '7145554996', 'Ocean Sports' );

INSERT INTO "Customers" VALUES( 120, 'Steinberg', 'Gertrude', '14 Amon Carter Blvd.', 'Hockley Valley', 'NY', 'USA', '10523', '9145553476', 'Carney Co.' );

INSERT INTO "Customers" VALUES( 121, 'Elkins', 'Pete', '233 Lawerence Street', 'Clinton', 'IN', 'USA', '46032', '3175558437', 'Carmel Industries' );

INSERT INTO "Customers" VALUES( 122, 'Dente', 'Al', '2 N.E. 38th Place', 'Conestogo', 'VA', 'USA', '22102', '7035557491', 'Virgina Power' );

INSERT INTO "Customers" VALUES( 123, 'Lin', 'Amanda', '255 North Pine Grove', 'Pembroke', 'MB', 'Canada', 'R3C 3V6', '2045555559', 'North Land Trading' );

INSERT INTO "Customers" VALUES( 124, 'Farmer', 'Fanny', '240 Barnard Lane', 'Waterford', 'MA', 'USA', '01887', '6175559386', 'The Ristuccia Center' );

INSERT INTO "Customers" VALUES( 125, 'Smelledge', 'Sidney', '3125 Merritt Drive', 'Keswick', 'MO', 'USA', '63101', '3145553426', 'Bush Pro Shop' );

INSERT INTO "Customers" VALUES( 126, 'Ovar', 'Sam', '23 Lindenwood Drive', 'King City', 'CA', 'USA', '94105', '4155555972', 'Golden Gate Active Wear' );

INSERT INTO "Customers" VALUES( 127, 'Lamm', 'Mary', '110 McKinney', 'Dundas', 'FL', 'USA', '34243', '8135557566', 'The Palms' );

INSERT INTO "Customers" VALUES( 128, 'Mums', 'Hardy', '911 5th Avenue S.W.', 'Charlottetown', 'CO', 'USA', '02106', '6175554340', 'BoSox Club' );

INSERT INTO "Customers" VALUES( 129, 'Fahrvergnugen', 'Karl', '113 Armagh Street', 'Stroud', 'MD', 'USA', '21202', '3015553322', 'Camden Sports Apparel' );

INSERT INTO "Customers" VALUES( 130, 'Monella', 'Sal', '92 Eastlake Avenue', 'St. Jacobs', 'WI', 'USA', '53141', '4145556799', 'Wyse Corp.' );

INSERT INTO "Customers" VALUES( 131, 'Sinnot', 'Daljit', '5145 Presidents Landing', 'Kenora', 'NY', 'USA', '11716', '5165559811', 'The Pro Shopp' );

INSERT INTO "Customers" VALUES( 132, 'King', 'Marilyn', '2167 South Ulster', 'Fort Erie', 'IN', 'USA', '46801', '2195554551', 'Bristol Co.' );

INSERT INTO "Customers" VALUES( 133, 'Bilhome', 'Moe', '18 W. Colfax Avenue', 'Sauble Beach', 'CA', 'USA', '91505', '8185558455', 'Bilhome Industries' );

INSERT INTO "Customers" VALUES( 134, 'O''Furniture', 'Paddy', '180 W. Las Colinas', 'Whitby', 'OH', 'USA', '44260', '2165556283', 'Gifts & Things' );

INSERT INTO "Customers" VALUES( 135, 'Clarke', 'Belinda', '24 Constitution Avenue', 'Rockwood', 'NY', 'USA', '10001', '2125555026', 'Hermanns' );

INSERT INTO "Customers" VALUES( 136, 'Wooten', 'Tommie', '132 Hing Wai Building', 'Forest Hill', 'MN', 'USA', '55447', '6125553373', 'Leisure Time' );

INSERT INTO "Customers" VALUES( 137, 'Morfek', 'Polly', '872 Hopyard Road', 'Hull', 'IN', 'USA', '46808', '2195554297', 'Sports Plus' );

INSERT INTO "Customers" VALUES( 138, 'Patoff', 'Regus', '222 James Way', 'Hamilton', 'ON', 'Canada', 'L7N 5L1', '9065554252', 'Sports Replay' );

INSERT INTO "Customers" VALUES( 139, 'Dimitros', 'Jai', '2366 Marineship Way', 'Charlottetown', 'CO', 'USA', '02201', '6175556354', 'Martins Landing' );

INSERT INTO "Customers" VALUES( 140, 'Thumb', 'Thomas', '2506 North Vine Street', 'Glasgow', 'UT', 'USA', '84180', '8015553550', 'Ski,Ski,Ski' );

INSERT INTO "Customers" VALUES( 141, 'Pyper', 'Peter', '4089 Beta Mall', 'Fort Erie', 'IN', 'USA', '46801', '2195554552', 'Mall Side Sports' );

INSERT INTO "Customers" VALUES( 142, 'Margolis', 'Alfredo', '40 Bloor Street East', 'Thunder Bay', 'MO', 'USA', '64114', '8165558543', 'Creative Customs Inc.' );

INSERT INTO "Customers" VALUES( 143, 'Piper', 'Peter', '310 Stevens Creek Blvd.', 'Pembroke', 'MB', 'Canada', 'R3C 3V6', '2045559414', 'Molly''''s' );

INSERT INTO "Customers" VALUES( 144, 'Wan', 'Fangmei', '3452 E. Hillsdale', 'Honey Harbor', 'MA', 'USA', '01775', '5085558979', 'Green Acre''s Custom Tee''''s' );

INSERT INTO "Customers" VALUES( 145, 'Doe', 'John', '346 Wellworth Ave', 'Ingersol', 'VA', 'USA', '22030', '7035552184', 'Doe, Rae, Mee' );

INSERT INTO "Customers" VALUES( 146, 'Yost', 'Alberto', '362 White Horse Road', 'Parry Sound', 'WA', 'USA', '99216', '5095559276', 'Custom Designs' );

INSERT INTO "Customers" VALUES( 147, 'Lela', 'Manoj', '572 Third Avenue North', 'Campbellford', 'NJ', 'USA', '07095', '9085556021', 'Norton Co.' );

INSERT INTO "Customers" VALUES( 148, 'Crooker', 'Beth', '450 College Road', 'Pembroke', 'MB', 'Canada', 'R3C 2P4', '2045555554', 'Cooper Inc.' );

INSERT INTO "Customers" VALUES( 149, 'Uhnfitte', 'Hans', '9723 West Wacker Dr', 'Pembroke', 'MB', 'Canada', 'R3C 2P4', '2045554744', 'The Ultimate' );

INSERT INTO "Customers" VALUES( 150, 'Mason', 'Carl', '3087 Powell Street', 'Windsor', 'ON', 'Canada', 'M3C 3N4', '4165555108', 'Power Play' );

INSERT INTO "Customers" VALUES( 151, 'Sinitskaya', 'Balwinder', '2893 Century Blvd', 'Drayton', 'KS', 'USA', '66210', '9135554519', 'Toto''s Active Wear' );

INSERT INTO "Customers" VALUES( 152, 'Jones', 'Frank', '8960 Inelt Business Ctr.', 'Barrie', 'NY', 'USA', '11746', '5165555952', 'Play it again Sports' );

INSERT INTO "Customers" VALUES( 153, 'Jones', 'Paul', '8751 Innovation Drive', 'Guelph', 'OH', 'USA', '45202', '5135557622', 'Three Rivers Pro Shop' );

INSERT INTO "Customers" VALUES( 154, 'Smythe', 'Marvin', '6329 North 27th Ave', 'New Hamburg', 'FL', 'USA', '33181', '3055559457', 'Marlin Mainia' );

INSERT INTO "Customers" VALUES( 155, 'Phipps', 'Milo', '8230 Osterbrogade', 'Wiarton', 'OH', 'USA', '44107', '2165552264', 'Things Remembered' );

INSERT INTO "Customers" VALUES( 156, 'DuCode', 'Sue', '3571 San Thomas Avenue', 'North Bay', 'MO', 'USA', '63131', '3145558227', 'Ozzie''s Haven' );

INSERT INTO "Customers" VALUES( 157, 'Watcom', 'William', '3259 Silver Lake Road', 'Elmira', 'IL', 'USA', '60645', '3125557433', 'The Cub''s Den' );

INSERT INTO "Customers" VALUES( 158, 'Cass', 'Jack', '26 West Court Street', 'Newcastle', 'IL', 'USA', '02173', '6175558610', 'Jordan''s Basement' );

INSERT INTO "Customers" VALUES( 159, 'Shaw', 'Rick', '15 West Loop South', 'Thamesford', 'MI', 'USA', '48324', '3135553638', 'ScrimShaw''''s' );

INSERT INTO "Customers" VALUES( 160, 'Nette', 'Clara', '9824 Wilshire Blvd', 'Laurelwood', 'NY', 'USA', '11050', '5165556250', 'Discount Department Store' );

INSERT INTO "Customers" VALUES( 161, 'Poole', 'Gene', '286 Vreeland Road', 'Port Colborne', 'DC', 'USA', '20581', '2025556537', 'State House Active Wear' );

INSERT INTO "Customers" VALUES( 162, 'Toste', 'Melba', '90 51st Ave North', 'Beechwood', 'OH', 'USA', '43065', '6145558983', 'The Real Deal' );

INSERT INTO "Customers" VALUES( 163, 'Peese', 'R.I.', '38 Buckingham', 'North York', 'ON', 'Canada', 'L4W 2S6', '4165556026', 'Mount Eastern Sports' );

INSERT INTO "Customers" VALUES( 164, 'Najarian', 'Aram', '257 Cambridge Center', 'Cambridge', 'CT', 'USA', '6811', '2035557907', 'Bloomfield''''s' );

INSERT INTO "Customers" VALUES( 165, 'Mournen', 'Tamara', '35 Choke Cherry Road', 'Hull', 'IN', 'USA', '46808', '2195554297', 'Moran''s Gift Shop' );

INSERT INTO "Customers" VALUES( 166, 'Naddem', 'Malcolm', '9813 Commerce Parkway', 'Long Point', 'GA', 'USA', '30518', '4045552529', 'Hospital Gift''''s' );

INSERT INTO "Customers" VALUES( 167, 'Cara', 'Nicklas', '5762 State Highway 249', 'Wiarton', 'OH', 'USA', '44107', '2165552264', 'The Road Side Inn' );

INSERT INTO "Customers" VALUES( 168, 'de Joie', 'Almen', '2150 Sweitzer Lane', 'Galt', 'CA', 'USA', '92649', '7145555475', 'Surf''s Up!' );

INSERT INTO "Customers" VALUES( 169, 'Terlemezian', 'Laura', '123 First Street', 'Bracebridge', 'NC', 'USA', '28105', '7045558411', 'CoMed' );

INSERT INTO "Customers" VALUES( 170, 'Neubauer', 'Manh', '236 Haddington Street', 'Easton', 'FL', 'USA', '32206', '9045553551', 'Jason''s Sporting Goods' );

INSERT INTO "Customers" VALUES( 171, 'Nahra', 'Vincent', '9873 Harwin Drive', 'Timmins', 'IL', 'USA', '60185-1120', '3125555551', 'Iron Mike''s Apparel' );

INSERT INTO "Customers" VALUES( 172, 'Perez', 'Grace', '230 Market Street', 'Collingwood', 'MA', 'USA', '20785', '3015557728', 'Avon Inc.' );

INSERT INTO "Customers" VALUES( 173, 'Pendelton', 'Grover', '861 Merritt Drive', 'Mississauga', 'MD', 'USA', '20871', '3015554284', 'Simply Tee''''s' );

INSERT INTO "Customers" VALUES( 174, 'Zoblotny', 'Anabai', '36920 N.E. Airport Way', 'Harvard', 'CO', 'USA', '80225', '3035552757', 'Hats Etc.' );

INSERT INTO "Customers" VALUES( 175, 'Perkins', 'Tawfik', '325 N.W. 7th Avenue', 'Halton Hills', 'BC', 'Canada', 'V8W 2B7', '6045553801', 'The Hat Company' );

INSERT INTO "Customers" VALUES( 176, 'Shumovich', 'Helen', '980 Park Plaza #1800', 'Stroud', 'MD', 'USA', '21209', '4105553322', 'The Bird''s Loft' );

INSERT INTO "Customers" VALUES( 177, 'Zubenko', 'Joseph', '960 Stonehollow Drive', 'Chandler', 'NC', 'USA', '27695', '9195555152', 'Avco Ent.' );

INSERT INTO "Customers" VALUES( 178, 'Naidu', 'Suresh', '351 Sycamore Drive', 'Ayr', 'CT', 'USA', '6320', '2035554440', 'Amy''s Silk Screening' );

INSERT INTO "Customers" VALUES( 179, 'Nguyen', 'Marsha', '21 Dunlaney Gate Circle', 'Goderich', 'FL', 'USA', '33027', '3055554336', 'Resco' );

INSERT INTO "Customers" VALUES( 180, 'Peros', 'Edith', '39 Market Street', 'Rockland', 'NY', 'USA', '14624', '7165554275', 'Breswick''s Department Store' );

INSERT INTO "Customers" VALUES( 181, 'Teeven', 'Emunah', '282 Wilshire Blvd.', 'Port Colborne', 'DC', 'USA', '20240', '2025552083', 'Hometown Tee''''s' );

INSERT INTO "Customers" VALUES( 182, 'Gardner', 'Leilani', '901 Campus Drive', 'McCord', 'CA', 'USA', '30102', '4045559283', 'Polly''s Custom Design' );

INSERT INTO "Customers" VALUES( 183, 'Nakagama', 'Marilyn', '109 Central Avenue', 'Killarney', 'FL', 'USA', '32792', '4075556776', 'Zoo Gift Shop' );

INSERT INTO "Customers" VALUES( 184, 'Serafina', 'Anoush', '3248 Greenway Place', 'Drayton', 'KS', 'USA', '66210', '9135554519', 'Westend Dealers' );

INSERT INTO "Customers" VALUES( 185, 'Belmont', 'Serop', '2158 Hadley Lane', 'Gimli', 'CT', 'USA', '6115', '2035555474', 'The Heartford' );

INSERT INTO "Customers" VALUES( 186, 'Tenorio', 'Thao', '9000 Midway Road', 'Thunder Bay', 'MO', 'USA', '64105', '8165558543', 'Wally''s World' );

INSERT INTO "Customers" VALUES( 187, 'Bensoul', 'Sebouh', '328 Van Ness Way', 'Ventura', 'IL', 'USA', '61614', '3095556915', 'Bensoul''s Boutique' );

INSERT INTO "Customers" VALUES( 188, 'Berenberg', 'Vartan', '259 110th Avenue N.E.', 'Dashwood', 'IL', 'USA', '60062', '7085552914', 'Diva''s Design' );

INSERT INTO "Customers" VALUES( 189, 'Berejiklian', 'Herbert', '36 Municiple Drive', 'Petersburg', 'KS', 'USA', '02142', '6175553547', 'Out of Town Sports' );

INSERT INTO "Customers" VALUES( 190, 'Arlington', 'Randy', '529 N Franklin Turnpike', 'Chatham', 'MI', 'USA', '48214', '3135555716', 'Jim Dandy''''s' );

INSERT INTO "Customers" VALUES( 191, 'Richards', 'Marta', '15920 Northridge Road', 'Winterbourne', 'FL', 'USA', '33172', '3055554711', 'Ocean Sports Wear' );

INSERT INTO "Customers" VALUES( 192, 'Beldov', 'Rosanna', '153 Northside Parkway', 'Leamington', 'IA', 'USA', '51102', '7125552741', 'Morrell Inc.' );

INSERT INTO "Customers" VALUES( 193, 'Neumann', 'Alfred', '1657 Northeast 99th Way', 'Thunder Bay', 'MO', 'USA', '64114', '8165558543', 'Big Sky Design' );

INSERT INTO "Customers" VALUES( 194, 'Chin', 'Jen-Chang', '3269 Oyster Point Blvd', 'Ingersol', 'VA', 'USA', '02203', '7035558037', 'Cinnamon Rainbow''''s' );

INSERT INTO "Customers" VALUES( 195, 'Jyh-Hwa', 'Li-Hui', '107 Potrero Avenue', 'Oakville', 'GA', 'USA', '30303', '4045556762', 'Peachtree Active Wear' );

INSERT INTO "Customers" VALUES( 196, 'Andrews', 'Ling Ling', '999 Roe Avenue', 'Orangeville', 'AB', 'Canada', 'T5N 1S5', '4035554884', 'The Igloo' );

INSERT INTO "Customers" VALUES( 197, 'Chermak', 'Maio', '203 Sycamore Road', 'Oakville', 'GA', 'USA', '30346', '4045558046', 'Southern Sports' );

INSERT INTO "Customers" VALUES( 198, 'Chen', 'Sheng', '9214 W. Six Mile Road', 'Pickering', 'CA', 'USA', '94583', '5105558666', 'Able Inc.' );

INSERT INTO "Customers" VALUES( 199, 'Mentary', 'Ella', '324 Embarcadero Center', 'Rockland', 'NY', 'USA', '14644', '7165554236', 'Nobel Co.' );

INSERT INTO "Customers" VALUES( 200, 'Chau', 'Helen', '1542 Yamato Road', 'Linwood', 'MD', 'USA', '20878', '3015553099', 'Stone''s Sporting Goods' );

INSERT INTO "Customers" VALUES( 201, 'Singh', 'Amit', '6530 Yonge Street', 'Drayton', 'KS', 'USA', '66210', '9135554519', 'Overland Army Navy' );

INSERT INTO "Customers" VALUES( 202, 'Murphy', 'Bubba', '4263 N. 44th Street', 'Welland', 'NY', 'USA', '10604', '9145556961', 'Dane''s World' );

INSERT INTO "Customers" VALUES( 203, 'Pepper', 'Salton', '201 Boylston Street', 'White Lake', 'WI', 'USA', '53705', '6085552673', 'Salt & Pepper''''s' );

INSERT INTO "Customers" VALUES( 204, 'Spaid', 'Robert', '222 Town Center', 'Victoriaville', 'MI', 'USA', '49202', '5175557883', 'Cognos Sports' );

INSERT INTO "Customers" VALUES( 205, 'Smythe', 'Elmo', '2459 Plaza Street', 'Mildmay', 'MA', 'USA', '01516', '5085554761', 'East Coast Traders' );

INSERT INTO "Customers" VALUES( 206, 'Jones', 'JohnPaul', '2999 Post Oak Blvd.', 'Dansbury', 'VA', 'USA', '22091', '7035556209', 'Chadwicks' );

INSERT INTO "Customers" VALUES( 207, 'Donchek', 'Wen-Chu', '1425 N. Mission', 'Peterborough', 'IL', 'USA', '60532', '7085555055', 'The Country Store' );

INSERT INTO "Customers" VALUES( 208, 'Suess', 'Derek', '397 King George Drive', 'Weyburn', 'NY', 'USA', '12208', '5185552623', 'Capital Center Sports' );

INSERT INTO "Customers" VALUES( 209, 'Boyle', 'Laura', '234 Pillsbury Road', 'Niagara Falls', 'CA', 'USA', '94022', '4155559678', 'Boyle''s Swap Meet' );

INSERT INTO "Customers" VALUES( 220, 'Clark', 'Lewis N.', '987 Expedition Hwy', 'Meaford', 'WY', 'USA', '85293', '3075556589', 'Trek Outfitters' );

INSERT INTO "Customers" VALUES( 221, 'Johnson', 'Jack', '65 Shoebox Lane', 'Armstrong', 'NM', 'USA', '40420', '5055554568', 'Turkey Creek Co.' );

INSERT INTO "Customers" VALUES( 222, 'Doe', 'Jane', '54 Disk Drive', 'Ajax', 'CA', 'USA', '94020', '4085558796', 'data Recovery Services' );

INSERT INTO "Customers" VALUES( 330, 'Major', 'Tom', '97 Rocket Pad', 'Exeter', 'FL', 'USA', '32200', '4075558574', 'Launch Facilities' );

INSERT INTO "Customers" VALUES( 331, 'Johansen', 'Dominic', '37 West Street', 'Wellesley', 'LA', 'USA', '33552', '5045558487', 'Mardi Gras Parties' );

INSERT INTO "Customers" VALUES( 332, 'Jue', 'Stanley', '37 Bronco Circle', 'Kitchener', 'TX', 'USA', '77057', '7135558857', 'Bay Town Bus Co.' );

INSERT INTO "Customers" VALUES( 333, 'Jones', 'Harry', '87 Software Rd', 'Ajax', 'CA', 'USA', '94020', '4085556689', 'Bits & Bytes' );

INSERT INTO "Customers" VALUES( 440, 'Curie', 'Marie', '573 Helping Hand Hwy', 'Lefroy', 'MA', 'USA', '02140', '6175558875', 'Wind & Rain' );

INSERT INTO "Customers" VALUES( 441, 'Bordon', 'Elizabeth', '21 Grinding Stone Rd', 'New Dundee', 'MA', 'USA', '01801', '5085558879', 'Blades & Things' );

INSERT INTO "Customers" VALUES( 444, 'Manager', 'Len', '90 Network Way', 'Fergus', 'TX', 'USA', '76552', '2145552685', 'Let''s get Connected' );

INSERT INTO "Customers" VALUES( 550, 'Antolini', 'Tony', '1539 Sliver Road', 'Woodstock', 'ND', 'USA', '60500', '7015553259', 'Flat Landers' );

INSERT INTO "Customers" VALUES( 551, 'Cruz', 'Tom', '248 Far Away Lane', 'Byron', 'OR', 'USA', '98524', '5035557462', 'Raceway Engines' );

INSERT INTO "Customers" VALUES( 552, 'O''Toole', 'Janice', '369 West Hill', 'Tweed', 'TN', 'USA', '37320', '6155553689', 'Greensleeves' );

INSERT INTO "Customers" VALUES( 553, 'Nickolas', 'Stevie', '22 Recordings Circle', 'Hanover', 'WA', 'USA', '96521', '5095551695', 'It''s a Hit!' );

INSERT INTO "Customers" VALUES( 555, 'Fernandez', 'Philipe', '24 Main Street', 'Arnprior', 'CA', 'USA', '90205', '2135554457', 'Quaker Fashions' );

INSERT INTO "Customers" VALUES( 661, 'Stutzman', 'Jennifer', '8 Back Pages Lane', 'Etobicoke', 'IL', 'USA', '60505', '7085556857', 'Stutzman Advertising' );

INSERT INTO "Customers" VALUES( 665, 'Thompson', 'William', '19 Washington Street', 'Bancroft', 'NY', 'USA', '11700', '5165552549', 'The Apple Farm' );

 

INSERT INTO "Departments" VALUES( 100, 'R & D', 501 );

INSERT INTO "Departments" VALUES( 200, 'Sales', 902 );

INSERT INTO "Departments" VALUES( 300, 'Finance', 1293 );

INSERT INTO "Departments" VALUES( 400, 'Marketing', 1576 );

INSERT INTO "Departments" VALUES( 500, 'Shipping', 703 );

 

 

INSERT INTO "FinancialCodes" VALUES( 'e1', 'expense', 'Fees' );

INSERT INTO "FinancialCodes" VALUES( 'e2', 'expense', 'Services' );

INSERT INTO "FinancialCodes" VALUES( 'e3', 'expense', 'Sales & Marketing' );

INSERT INTO "FinancialCodes" VALUES( 'e4', 'expense', 'R & D' );

INSERT INTO "FinancialCodes" VALUES( 'e5', 'expense', 'Administration' );

INSERT INTO "FinancialCodes" VALUES( 'r1', 'revenue', 'Fees' );

INSERT INTO "FinancialCodes" VALUES( 'r2', 'revenue', 'Services' );

 

 

INSERT INTO "FinancialData" VALUES( '1999', 'Q1', 'e1', 101 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q1', 'e2', 403 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q1', 'e3', 1437 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q1', 'e4', 623 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q1', 'e5', 381 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q1', 'r1', 1023 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q1', 'r2', 234 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q2', 'e1', 93 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q2', 'e2', 459 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q2', 'e3', 2033 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q2', 'e4', 784 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q2', 'e5', 402 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q2', 'r1', 2033 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q2', 'r2', 459 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q3', 'e1', 129 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q3', 'e2', 609 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q3', 'e3', 2184 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q3', 'e4', 856 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q3', 'e5', 412 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q3', 'r1', 2998 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q3', 'r2', 601 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q4', 'e1', 145 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q4', 'e2', 632 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q4', 'e3', 2145 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q4', 'e4', 1043 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q4', 'e5', 467 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q4', 'r1', 3014 );

INSERT INTO "FinancialData" VALUES( '1999', 'Q4', 'r2', 944 );

 

 

INSERT INTO "MarketingInformation" VALUES( 901, 300, '<html><head><meta http-equiv=Content-Type content="text/html; charset=windows-1252"><title>Tee Shirt</title></head><body lang=EN-US><p><span  style=''font-size:10.0pt;font-family:Arial''>We''ve improved the design of this perennial favorite. A sleek and technical shirt built for the trail, track, or sidewalk. UPF rating of 50+.</span></p></body></html>' );

INSERT INTO "MarketingInformation" VALUES( 902, 301, '<html><head><meta http-equiv=Content-Type content="text/html; charset=windows-1252"><title>Tee Shirt</title></head><body lang=EN-US><p><span  style=''font-size:10.0pt;font-family:Arial''>This simple, sleek, and lightweight technical shirt is designed for high-intensity workouts in hot and humid weather. The recycled polyester fabric is gentle on the earth and soft against your skin.</span></p></body></html>' );

INSERT INTO "MarketingInformation" VALUES( 903, 302, '<html><head><meta http-equiv=Content-Type content="text/html; charset=windows-1252"><title>Tee Shirt</title></head><body lang=EN-US><p><span  style=''font-size:10.0pt;font-family:Arial''>A sporty, casual shirt made of recycled water bottles. It will serve you equally well on trails or around town. The fabric has a wicking finish to pull perspiration away from your skin.</span></p></body></html>' );

INSERT INTO "MarketingInformation" VALUES( 904, 400, '<html><head><meta http-equiv=Content-Type content="text/html; charset=windows-1252"><title>Baseball Cap</title></head><body lang=EN-US><p><span  style=''font-size:10.0pt;font-family:Arial''>This fashionable hat is ideal for glacier travel, sea-kayaking, and hiking. With concealed draw cord for windy days.</span></p></body></html>' );

INSERT INTO "MarketingInformation" VALUES( 905, 401, '<html><head><meta http-equiv=Content-Type content="text/html; charset=windows-1252"><title>Baseball Cap</title></head><body lang=EN-US><p><span  style=''font-size:10.0pt;font-family:Arial''>A lightweight wool cap with mesh side vents for breathable comfort during aerobic activities. Moisture-absorbing headband liner.</span></p></body></html>' );

INSERT INTO "MarketingInformation" VALUES( 906, 500, '<html><head><meta http-equiv=Content-Type content="text/html; charset=windows-1252"><title>Visor</title></head><body lang=EN-US><p><span  style=''font-size:10.0pt;font-family:Arial''>Lightweight 100% organically grown cotton construction. Shields against sun and precipitation. Metallic ions in the fibers inhibit bacterial growth, and help neutralize odor.</span></p></body></html>' );

INSERT INTO "MarketingInformation" VALUES( 907, 501, '<html><head><meta http-equiv=Content-Type content="text/html; charset=windows-1252"><title>Visor</title></head><body lang=EN-US><p><span  style=''font-size:10.0pt;font-family:Arial''>A polycarbonate visor with an abrasion-resistant coating on the outside. Great for jogging in the spring, summer, and early fall. The elastic headband has plenty of stretch to give you a snug yet comfortable fit every time you wear it.</span></p></body></html>' );

INSERT INTO "MarketingInformation" VALUES( 908, 600, '<html><head><meta http-equiv=Content-Type content="text/html; charset=windows-1252"><title>Sweatshirt</title></head><body lang=EN-US><p><span  style=''font-size:10.0pt;font-family:Arial''>Lightweight 100% organically grown cotton hooded sweatshirt with taped neck seams. Comes pre-washed for softness and to lessen shrinkage.</span></p></body></html>' );

INSERT INTO "MarketingInformation" VALUES( 909, 601, '<html><head><meta http-equiv=Content-Type content="text/html; charset=windows-1252"><title>Sweatshirt</title></head><body lang=EN-US><p><span  style=''font-size:10.0pt;font-family:Arial''>Top-notch construction includes durable topstitched seams for strength with low-bulk, resilient rib-knit collar, cuffs and bottom. An 80% cotton/20% polyester blend makes it easy to keep them clean.</span></p></body></html>' );

INSERT INTO "MarketingInformation" VALUES( 910, 700, '<html><head><meta http-equiv=Content-Type content="text/html; charset=windows-1252"><title>Shorts</title></head><body lang=EN-US><p><span  style=''font-size:10.0pt;font-family:Arial''>These quick-drying cotton shorts provide all day comfort on or off the trails. Now with a more comfortable and stretchy fabric and an adjustable drawstring waist.</span></p></body></html>' );

 

 

Create Index IX\_PRODUCT\_COLOR on Products( COLOR );

Create Index IX\_PRODUCT\_DESCRIPTION on Products( DESCRIPTION );

Create Index IX\_PRODUCT\_NAME on Products( NAME );

Create Index IX\_PRODUCT\_SIZE on Products( SIZE );

 

INSERT INTO "Products" VALUES( 300, 'Tee Shirt', 'Tank Top', 'Small', 'White', 28, 9, NULL );

INSERT INTO "Products" VALUES( 301, 'Tee Shirt', 'V-neck', 'Medium', 'Orange', 54, 14, NULL );

INSERT INTO "Products" VALUES( 302, 'Tee Shirt', 'Crew Neck', 'One size fits all', 'Black', 75, 14, NULL );

INSERT INTO "Products" VALUES( 400, 'Baseball Cap', 'Cotton Cap', 'One size fits all', 'Black', 112, 9, NULL );

INSERT INTO "Products" VALUES( 401, 'Baseball Cap', 'Wool cap', 'One size fits all', 'White', 12, 10, NULL );

INSERT INTO "Products" VALUES( 500, 'Visor', 'Cloth Visor', 'One size fits all', 'White', 36, 7, NULL );

INSERT INTO "Products" VALUES( 501, 'Visor', 'Plastic Visor', 'One size fits all', 'Black', 28, 7, NULL );

INSERT INTO "Products" VALUES( 600, 'Sweatshirt', 'Hooded Sweatshirt', 'Large', 'Green', 39, 24, NULL );

INSERT INTO "Products" VALUES( 601, 'Sweatshirt', 'Zipped Sweatshirt', 'Large', 'Blue', 32, 24, NULL );

INSERT INTO "Products" VALUES( 700, 'Shorts', 'Cotton Shorts', 'Medium', 'Black', 80, 15, NULL );

 

 

INSERT INTO "SalesOrderItems" VALUES( 2001, 1, 300, 12, '2000-03-17' );

 

 

INSERT INTO "SalesOrders" VALUES( 2001, 101, '2000-03-16', 'r1', 'Eastern', 299 );

 

 

INSERT INTO Employees VALUES( 102,501,'Whitney','Fran',100,'9 East Washington Street','Cornwall','NY','USA','02192','6175553985','A','017349033',45700,'1984-08-28', NULL,'1958-06-05',1,1,0,'F' );

INSERT INTO Employees VALUES( 105,501,'Cobb','Matthew',100,'7 Pleasant Street','Grimsby','UT','USA','02154','6175553840','A','052345739',62000,'1985-01-01', NULL,'1960-12-04',1,1,0,'M' );

INSERT INTO Employees VALUES( 129,902,'Chin','Philip',200,'539 Pond Street','Oakville','GA','USA','30339','4045552341','A','024608923',38500,'1985-02-03', NULL,'1966-10-30',1,1,0,'M' );

INSERT INTO Employees VALUES( 148,1293,'Jordan','Julie',300,'1244 Great Plain Avenue','Woodbridge','AZ','USA','01890','6175557835','A','501704733',51432,'1985-04-05', NULL,'1951-12-13',1,1,0,'F' );

INSERT INTO Employees VALUES( 160,501,'Breault','Robert',100,'358 Cherry Street','Milton','PA','USA','02186','6175553099','A','025487623',57490,'1985-06-17', NULL,'1947-05-13',1,1,1,'M' );

INSERT INTO Employees VALUES( 184,1576,'Espinoza','Melissa',400,'1121 Apple Tree Way','Iroquois Falls','ME','USA','01775','5085552319','A','025481943',36490,'1985-10-18', NULL,'1939-12-14',1,1,0,'F' );

INSERT INTO Employees VALUES( 191,703,'Bertrand','Jeannette',500,'2090A Concord Street','Waterloo','AZ','USA','01720','5085558138','A','017348821',29800,'1985-11-19', NULL,'1964-12-21',1,1,1,'F' );

INSERT INTO Employees VALUES( 195,902,'Dill','Marc',200,'897 Hancock Street','Milton','PA','USA','02186','6175552144','A','079486634',54800,'1985-12-06', NULL,'1963-07-19',1,1,0,'M' );

INSERT INTO Employees VALUES( 207,1576,'Francis','Jane',400,'127 Hawthorne Drive','Scarborough','FL','USA','01742','5085559022','A','501708992',53870,'1986-02-03', NULL,'1954-09-12',1,1,0,'F' );

INSERT INTO Employees VALUES( 243,501,'Shishov','Natasha',100,'151 Milk Street','Grimsby','UT','USA','02154','6175552755','A','043216799',72995,'1986-06-07', NULL,'1949-04-22',1,1,0,'F' );

INSERT INTO Employees VALUES( 247,501,'Driscoll','Kurt',100,'1546 School Street','Grimsby','UT','USA','02154','6175551234','L','024601768',48023.69,'1986-07-01', NULL,'1955-03-05',1,1,1,'M' );

INSERT INTO Employees VALUES( 249,501,'Guevara','Rodrigo',100,'72 East Main Street','Fort Henry','NY','USA','01701','5085550029','A','084329990',42998,'1986-10-14', NULL,'1956-11-23',1,1,0,'M' );

INSERT INTO Employees VALUES( 266,501,'Gowda','Ram',100,'7 Page Street','Morrisburg','FL','USA','01760','5085558722','A','017346122',59840,'1986-11-30', NULL,'1947-10-18',0,1,0,'M' );

INSERT INTO Employees VALUES( 278,501,'Melkisetian','Terry',100,'871 Oxford Road','Sarnia','CO','USA','02172','6175555188','A','087602311',48500,'1986-12-06', NULL,'1966-05-17',1,1,1,'F' );

INSERT INTO Employees VALUES( 299,902,'Overbey','Rollin',200,'191 Companion Ct.','Kanata','CA','USA','94608','5105557255','A','025487133',39300,'1987-02-19', NULL,'1964-03-15',1,1,0,'M' );

INSERT INTO Employees VALUES( 316,501,'Pastor','Lynn',100,'1423 Cricklewood Drive','Hamilton','MI','USA','01803','6175552001','A','048667211',74500,'1987-04-26', NULL,'1962-07-14',1,1,1,'F' );

INSERT INTO Employees VALUES( 318,1576,'Crow','John',400,'14531 Main Street','Sarnia','CO','USA','02172','6175553332','A','079349168',41700.75,'1987-05-23', NULL,'1962-04-24',1,1,0,'M' );

INSERT INTO Employees VALUES( 390,1293,'Davidson','Jo Ann',300,'273 Mount Vernon Road','Cornwall','NY','USA','02192','6175553870','A','027341657',57090,'1987-06-02', NULL,'1957-02-17',0,1,1,'F' );

INSERT INTO Employees VALUES( 409,1576,'Weaver','Bruce',400,'190 Westmoreland Street','Newcastle','IL','USA','02173','6175554444','A','048781192',46550,'1987-06-10', NULL,'1946-04-05',1,1,0,'M' );

INSERT INTO Employees VALUES( 445,501,'Lull','Kim',100,'1997 Lincoln Street','Scarborough','FL','USA','01742','5085554444','A','017508821',87900,'1987-06-15', NULL,'1955-01-19',1,1,0,'M' );

INSERT INTO Employees VALUES( 453,501,'Rabkin','Andrew',100,'444 Birds Hill Way','Hamilton','MI','USA','01803','6175554444','A','029458129',64500,'1987-06-15', NULL,'1957-08-10',1,1,0,'M' );

INSERT INTO Employees VALUES( 467,902,'Klobucher','James',200,'1839 Corning Street','Kitchener','TX','USA','77079','7135558627','A','034281032',49500,'1987-07-10', NULL,'1952-11-09',1,1,0,'M' );

INSERT INTO Employees VALUES( 479,501,'Siperstein','Linda',100,'3481 Hillside Avenue','St. Clements','WY','USA','02164','6175556588','L','022415639',39875.5,'1987-07-23', NULL,'1967-09-21',1,1,0,'F' );

INSERT INTO Employees VALUES( 501,501,'Scott','David',100,'291 Riverdale Drive','Lethbridge','RI','USA','02178','6175553246','A','064983327',96300,'1987-08-04', NULL,'1947-03-01',1,1,1,'M' );

INSERT INTO Employees VALUES( 529,501,'Sullivan','Dorothy',100,'1294 Minuteman Drive','Newcastle','IL','USA','02173','6175553947','A','501324492',67890,'1988-02-03', NULL,'1950-04-19',1,1,0,'F' );

INSERT INTO Employees VALUES( 582,501,'Samuels','Peter',100,'504 Woodlawn Street','St. Clements','WY','USA','02164','6175558342','A','038218867',37400,'1988-03-23', NULL,'1968-02-28',1,1,0,'M' );

INSERT INTO Employees VALUES( 586,1293,'Coleman','James',300,'577 Heather Hill Drive','Waterloo','AZ','USA','01720','5085554735','L','031281245',42300,'1988-04-05', NULL,'1966-03-04',1,1,0,'M' );

INSERT INTO Employees VALUES( 591,1576,'Barletta','Irene',400,'937 Gleason Street','Elora','OR','USA','01730','6175558345','A','056872399',45450,'1988-07-18', NULL,'1957-01-30',1,1,1,'F' );

INSERT INTO Employees VALUES( 604,501,'Wang','Albert',100,'488 Edwin Street','Grimsby','UT','USA','02154','6175558741','A','023486621',68400,'1988-09-29', NULL,'1958-12-25',1,1,0,'M' );

INSERT INTO Employees VALUES( 641,902,'Powell','Thomas',200,'487 Kennedy Court','St. Clements','WY','USA','02162','6175551956','A','038726633',54600,'1988-10-14', NULL,'1951-10-31',1,1,0,'M' );

INSERT INTO Employees VALUES( 667,902,'Garcia','Mary',200,'9 Purvis Street','Kitchener','TX','USA','77079','7135553431','A','042706188',39800,'1988-11-22', NULL,'1963-01-23',0,1,1,'F' );

INSERT INTO Employees VALUES( 690,902,'Poitras','Kathleen',200,'501 The Fenway','Charlottetown','CO','USA','02118','6175553920','A','087236702',46200,'1988-11-28', NULL,'1965-09-29',0,1,0,'F' );

INSERT INTO Employees VALUES( 703,902,'Martinez','Jose',500,'475 Washington Street','Waterdown','AZ','USA','02090','6175557114','A','012896755',55500.8,'1988-12-01', NULL,'1953-07-22',1,1,0,'M' );

INSERT INTO Employees VALUES( 750,703,'Braun','Jane',500,'425 Wood Street','Petersburg','KS','USA','02140','6175557857','A','012459381',34300,'1989-01-03', NULL,'1939-08-09',1,1,0,'F' );

INSERT INTO Employees VALUES( 757,1293,'Higgins','Denis',300,'103 Massachusetts Avenue','Newcastle','IL','USA','02173','6175553985','A','067829311',43700,'1989-02-23', NULL,'1968-05-12',1,1,0,'F' );

INSERT INTO Employees VALUES( 839,501,'Marshall','Dean',100,'4468 Mount Pleasant Street','Lethbridge','RI','USA','02178','6175553707','A','034629123',42500,'1989-04-20', NULL,'1966-05-21',1,1,0,'M' );

INSERT INTO Employees VALUES( 856,902,'Singer','Samuel',200,'18 Orchard Road','Iroquois Falls','ME','USA','01775','5085553255','A','011349786',34892,'1989-06-01', NULL,'1959-04-07',1,1,0,'M' );

INSERT INTO Employees VALUES( 862,501,'Sheffield','John',100,'405 Belleview Drive','Kitchener','TX','USA','77079','7135553877','A','018458291',87900,'1989-06-15', NULL,'1955-09-25',1,1,1,'M' );

INSERT INTO Employees VALUES( 868,703,'Kuo','Felicia',500,'719 Oak Street','Petersburg','KS','USA','02140','6175552385','A','043592831',28200,'1989-07-12', NULL,'1968-07-24',1,1,0,'F' );

INSERT INTO Employees VALUES( 879,1293,'Coe','Kristen',300,'390 Rainbow Road','Trenton','WY','USA','02132','6175559192','A','027581035',36500,'1989-07-18', NULL,'1965-11-11',1,1,0,'F' );

INSERT INTO Employees VALUES( 888,1576,'Charlton','Doug',400,'578 Webster Street','Scarborough','FL','USA','01742','5085559246','A','036102935',28300,'1989-09-09', NULL,'1966-01-23',0,1,0,'M' );

INSERT INTO Employees VALUES( 902,1293,'Kelly','Moira',200,'127 Fountain Road','Wakefield','FL','USA','01930','5085553769','A','015923467',87500,'1989-10-01', NULL,'1950-08-16',1,1,0,'F' );

INSERT INTO Employees VALUES( 913,902,'Martel','Ken',200,'230 Lincoln Street','Cornwall','NY','USA','02192','6175558474','A','022783569',55700,'1989-10-16', NULL,'1943-04-23',0,1,0,'M' );

INSERT INTO Employees VALUES( 921,703,'Crowley','Charles',500,'4212 Beacon Street','Lethbridge','RI','USA','02178','6175559425','A','034568789',41700,'1989-10-22', NULL,'1960-09-11',1,1,0,'M' );

INSERT INTO Employees VALUES( 930,902,'Taylor','Ann',200,'251 Westminster Street','Oakville','GA','USA','30339','4045551515','A','062890293',46890,'1989-11-07', NULL,'1962-06-06',1,1,1,'F' );

INSERT INTO Employees VALUES( 949,902,'Savarino','Pamela',200,'1128 Beach Street','Sheffield','CA','USA','90806','3105551857','A','018762936',72300,'1989-11-07', NULL,'1955-07-28',1,1,0,'F' );

INSERT INTO Employees VALUES( 958,501,'Sisson','Thomas',100,'547 School Street','Kitchener','TX','USA','77079','7135558390','A','017283997',42100,'1990-01-15', NULL,'1969-10-02',1,1,0,'M' );

INSERT INTO Employees VALUES( 992,1576,'Butterfield','Joyce',400,'1191 Adams Street','Petersburg','KS','USA','02140','6175552232','A','023487085',34011,'1990-02-12', NULL,'1960-04-15',1,1,0,'F' );

INSERT INTO Employees VALUES( 1013,703,'Barker','Joseph',500,'589 West Drive','Elora','OR','USA','01730','6175558021','A','023470756',27290,'1990-03-12', NULL,'1969-02-14',0,1,0,'M' );

INSERT INTO Employees VALUES( 1021,902,'Sterling','Paul',200,'1125 Endicott Street','Scarborough','FL','USA','01742','5085550295','A','037846595',64900,'1990-04-29', NULL,'1950-02-27',1,1,1,'M' );

INSERT INTO Employees VALUES( 1039,902,'Chao','Shih Lin',200,'5 Holyoke Street','Newcastle','IL','USA','02173','6175555921','A','046973741',33890,'1990-05-13', NULL,'1969-12-12',0,1,1,'M' );

INSERT INTO Employees VALUES( 1062,1576,'Blaikie','Barbara',400,'665 Beaumont Terrace','Cornwall','NY','USA','02192','6175559345','A','019887257',54900,'1990-05-22', NULL,'1953-11-14',1,1,1,'F' );

INSERT INTO Employees VALUES( 1090,501,'Smith','Susan',100,'17 Johnson Street','Kitchener','TX','USA','77079','7135556613','A','013558813',51411,'1990-06-14', NULL,'1950-11-30',0,1,1,'F' );

INSERT INTO Employees VALUES( 1101,902,'Preston','Mark',200,'4971 Constitution Road','Charlottetown','CO','USA','02124','6175555862','A','027663454',37803,'1990-07-11', NULL,'1966-09-14',1,1,0,'M' );

INSERT INTO Employees VALUES( 1142,902,'Clark','Alison',200,'563 Carver Street','Kanata','CA','USA','94608','5105559437','A','055913622',45000,'1990-07-21', NULL,'1957-05-04',0,1,1,'F' );

INSERT INTO Employees VALUES( 1157,501,'Soo','Hing',100,'1921 Glenmeadow Street','Cornwall','NY','USA','02192','6175558748','A','023434587',39075,'1990-07-31', NULL,'1970-03-07',1,1,0,'M' );

INSERT INTO Employees VALUES( 1162,902,'Goggin','Kevin',200,'16 Wachusett Road','Stratford','UT','USA','02181','6175553785','A','075679377',37900,'1990-08-05', NULL,'1952-04-18',1,1,0,'M' );

INSERT INTO Employees VALUES( 1191,1576,'Bucceri','Matthew',400,'527 Taylor Place','Newcastle','IL','USA','02173','6175555336','A','023749270',45900,'1990-08-14', NULL,'1944-11-19',1,1,0,'M' );

INSERT INTO Employees VALUES( 1250,501,'Diaz','Emilio',100,'5112 Evergreen Street','Stratford','UT','USA','02181','6175553567','A','023476492',54900,'1990-08-19', NULL,'1936-01-02',1,1,0,'M' );

INSERT INTO Employees VALUES( 1293,1293,'Shea','Mary Anne',300,'297 Camden Road','Newcastle','IL','USA','02173','6175554616','A','019641485',138948,'1990-09-01', NULL,'1955-03-13',1,1,0,'F' );

INSERT INTO Employees VALUES( 1336,1293,'Bigelow','Janet',300,'83 Lunda Street','Grimsby','UT','USA','02154','6175551493','A','017326112',31200,'1992-02-25', NULL,'1950-07-21',1,1,1,'F' );

INSERT INTO Employees VALUES( 1390,1293,'Litton','Jennifer',300,'171 Downing Street','Scarborough','FL','USA','01742','5085553495','A','034786565',58930,'1992-04-06', NULL,'1948-04-05',0,1,0,'F' );

INSERT INTO Employees VALUES( 1446,902,'Yeung','Caroline',200,'252 Cypress Street','Oakville','GA','USA','30339','4045558347','A','038475825',32300,'1992-10-29', NULL,'1971-06-21',0,1,0,'F' );

INSERT INTO Employees VALUES( 1483,1293,'Letiecq','John',300,'951 Vista Drive','Hamilton','MI','USA','01803','6175551167','L','079372285',75400,'1993-03-01', NULL,'1939-04-27',1,1,0,'M' );

INSERT INTO Employees VALUES( 1507,1576,'Wetherby','Ruth',400,'38 Aberdeen Road','Cornwall','NY','USA','02192','6175555465','A','035673688',35745,'1993-04-12', NULL,'1959-07-19',1,1,0,'F' );

INSERT INTO Employees VALUES( 1570,703,'Rebeiro','Anthony',500,'93 Moody Street','Grimsby','UT','USA','02154','6175555737','A','034576347',34576,'1993-05-29', NULL,'1963-04-12',1,1,0,'M' );

INSERT INTO Employees VALUES( 1576,902,'Evans','Scott',400,'29-C Sunrise Circle','Scarborough','FL','USA','01742','5085550096','A','017429926',68940,'1993-07-01', NULL,'1960-11-15',1,1,0,'M' );

INSERT INTO Employees VALUES( 1596,902,'Pickett','Catherine',200,'457 Appleton Road','Elora','OR','USA','01730','6175553478','A','028375086',47653,'1993-08-12', NULL,'1959-11-18',1,1,1,'F' );

INSERT INTO Employees VALUES( 1607,1576,'Morris','Mark',400,'13 Example Way','Grimsby','UT','USA','02154','6175558344','A','501787474',61300,'1993-10-13', NULL,'1941-01-08',1,1,0,'M' );

INSERT INTO Employees VALUES( 1615,703,'Romero','Sheila',500,'197 Oakview Terrace','Elora','OR','USA','01730','6175558138','A','501175874',27500,'1993-11-19', NULL,'1972-09-12',1,1,1,'F' );

INSERT INTO Employees VALUES( 1643,1576,'Lambert','Elizabeth',400,'293 Union Street','Hamilton','MI','USA','01803','6175552357','A','023857807',29384,'1993-12-15', NULL,'1968-09-12',1,1,0,'F' );

INSERT INTO Employees VALUES( 1658,703,'Lynch','Michael',500,'716 Brookside Road','Grimsby','UT','USA','02154','6175558348','A','023850840',24903,'1994-02-27', NULL,'1973-01-18',1,1,0,'M' );

INSERT INTO Employees VALUES( 1684,1576,'Hildebrand','Janet',400,'7 Hilltop Street','Grimsby','UT','USA','02154','6175553845','A','038957036',45829,'1994-03-15', NULL,'1955-10-31',1,1,0,'F' );

INSERT INTO Employees VALUES( 1740,1576,'Nielsen','Robert',400,'558 Sargent Avenue','Elora','OR','USA','01730','6175558757','A','037534650',34889,'1994-06-24', NULL,'1965-06-19',1,1,0,'M' );

INSERT INTO Employees VALUES( 1751,1576,'Ahmed','Alex',400,'1141 Cushing Street','Cornwall','NY','USA','02192','6175558748','A','032547384',34992,'1994-07-12', NULL,'1963-12-12',1,1,0,'M' );

 

ALTER TABLE Customers ALTER COLUMN ID ID AutoInc;

 

ALTER TABLE SalesOrders ALTER COLUMN ID ID AutoInc;

 

EXECUTE PROCEDURE

sp\_CreateReferentialIntegrity (

    'ContanctsHasCustomer',

    'Customers',

    'Contacts',

    'CUSTOMERID',

    2,

    2,

    NULL/\* Enter Fail table path here. \*/,

    '',

    '');

 

EXECUTE PROCEDURE

sp\_CreateReferentialIntegrity (

    'SalesOrderHasEmployee',

    'Employees',

    'SalesOrders',

    'SALESREPRESENTATIVE',

    2,

    2,

    NULL/\* Enter Fail table path here. \*/,

    '',

    '');

 

EXECUTE PROCEDURE

sp\_CreateReferentialIntegrity (

    'OrderHasFinancialCode',

    'FinancialCodes',

    'SalesOrders',

    'FINANCIALCODE',

    2,

    2,

    NULL/\* Enter Fail table path here. \*/,

    '',

    '');

 

EXECUTE PROCEDURE

sp\_CreateReferentialIntegrity (

    'SalesOrderHasCustomer',

    'Customers',

    'SalesOrders',

    'CUSTOMERID',

    2,

    2,

    NULL/\* Enter Fail table path here. \*/,

    '',

    '');

 

EXECUTE PROCEDURE

sp\_CreateReferentialIntegrity (

    'ItemsHaveSalesOrder',

    'SalesOrders',

    'SalesOrderItems',

    'ID',

    2,

    2,

    NULL/\* Enter Fail table path here. \*/,

    '',

    '');

 

EXECUTE PROCEDURE

sp\_CreateReferentialIntegrity (

    'FinancialDataHasCode',

    'FinancialCodes',

    'FinancialData',

    'CODE',

    2,

    2,

    NULL/\* Enter Fail table path here. \*/,

    '',

    '');

 

EXECUTE PROCEDURE

sp\_CreateReferentialIntegrity (

    'EmployeeHasDepartment',

    'Departments',

    'Employees',

    'DEPARTMENTID',

    2,

    2,

    NULL/\* Enter Fail table path here. \*/,

    '',

    '');

 

EXECUTE PROCEDURE

sp\_CreateReferentialIntegrity (

    'MarketingInformationHasProduct',

    'Products',

    'MarketingInformation',

    'PRODUCTID',

    2,

    2,

    NULL/\* Enter Fail table path here. \*/,

    '',

    '');
