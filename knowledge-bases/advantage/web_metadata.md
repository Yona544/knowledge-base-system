Advantage Web Platform Database Metadata




Advantage Database Server 12  

Database Metadata

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Database Metadata  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - Database Metadata Advantage Web Platform web\_metadata Advantage Web Development > Advantage Web Platform > Database Metadata / Dear Support Staff, |  |
| Database Metadata  Advantage Web Platform |  |  |  |  |

Metadata describing an exposed database is returned to the client by two URIs.  The root URI will return a simple list of all entities (tables & views).  The root URI with /$Metadata on the end will return a much more descriptive document with the details of all tables, fields, views, functions, & relationships.  All the metadata conforms to the odata.org Service Metadata Document specification. An OData client is expected to be able to understand this metadata to learn about the design of a database.

Here is an example of the root URI metadata document:

https://server:6282/adsweb/example\_db/v1

The response might be:

<?xml version="1.0" encoding="iso-8859-1" standalone="yes"?>

<service xml:base="http://pfunkwin7.ias.sybase.com:6272/adsweb/example\_db/v1" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:app="http://www.w3.org/2007/app" xmlns="http://www.w3.org/2007/app">

 <workspace>

   <atom:title>Default</atom:title>

   <collection href="Customers">

     <atom:title>Customers</atom:title>

   </collection>

   <collection href="Orders">

     <atom:title>Orders</atom:title>

   </collection>

   <collection href="Invoices">

     <atom:title>Invoices</atom:title>

   </collection>

   <collection href="View1">

     <atom:title>View1</atom:title>

   </collection>

 </workspace>

</service>

Here is an example of the more descriptive $Metadata document:

https://server:6282/adsweb/example\_db/v1/$Metadata

With a response of:

<?xml version="1.0" encoding="iso-8859-1" standalone="yes"?>

<edmx:Edmx Version="1.0" xmlns:edmx="http://schemas.microsoft.com/ado/2007/06/edmx">

 <edmx:DataServices xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" m:DataServiceVersion="2.0">

   <Schema Namespace="testdd.Model.Entities" xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://schemas.microsoft.com/ado/2007/05/edm">

     <EntityType Name="Customers">

       <Key>

         <PropertyRef Name="ID" />

       </Key>

       <Property Name="ID" Type="Edm.Int32" Nullable="false" />

       <Property Name="Name" Type="Edm.String" Unicode="false" FixedLength="true" MaxLength="20" />

       <Property Name="Location" Type="Edm.String" Unicode="false" FixedLength="true" MaxLength="20" />

     </EntityType>

     <EntityType Name="Orders">

       <Key>

         <PropertyRef Name="ID" />

       </Key>

       <Property Name="ID" Type="Edm.Int32" Nullable="false" />

       <Property Name="CustomerID" Type="Edm.Int32" />

       <Property Name="Part" Type="Edm.String" Unicode="false" FixedLength="true" MaxLength="20" />

       <Property Name="Quantity" Type="Edm.Int32" />

     </EntityType>

     <EntityType Name="Invoices">

       <Key>

         <PropertyRef Name="InvoiceID" />

       </Key>

       <Property Name="InvoiceID" Type="Edm.Int32" Nullable="false" />

       <Property Name="CustomerID" Type="Edm.Int32" />

       <Property Name="Amount" Type="Edm.Double" />

       <Property Name="OrderID" Type="Edm.Int32" />

     </EntityType>

     <EntityType Name="View1">

       <Key>

         <PropertyRef Name="EMPID" />

       </Key>

       <Property Name="DEPTNUM" Type="Edm.Int16" />

       <Property Name="LASTNAME" Type="Edm.String" Unicode="false" FixedLength="true" MaxLength="12" />

       <Property Name="FIRSTNAME" Type="Edm.String" Unicode="true" FixedLength="true" MaxLength="12" />

       <Property Name="DOH" Type="Edm.DateTime" Precision="0" />

       <Property Name="SALARIED" Type="Edm.Boolean" />

       <Property Name="EMPID" Type="Edm.Int32" Nullable="false" />

       <Property Name="PHONE" Type="Edm.String" Unicode="false" FixedLength="true" MaxLength="8" />

       <Property Name="DOB" Type="Edm.DateTime" Precision="0" />

       <Property Name="EXTENSION" Type="Edm.Int16" />

       <Property Name="SOC\_SEC\_NU" Type="Edm.String" Unicode="false" FixedLength="true" MaxLength="11" />

       <Property Name="MARRIED" Type="Edm.Boolean" />

       <Property Name="DIVISION" Type="Edm.String" Unicode="false" FixedLength="true" MaxLength="10" />

       <Property Name="BRANCH" Type="Edm.String" Unicode="false" FixedLength="true" MaxLength="16" />

     </EntityType>

     <EntityType Name="Result\_Proc2">

       <Key>

         <PropertyRef Name="o1" />

       </Key>

       <Property Name="o1" Type="Edm.Int32" Nullable="false" />

       <Property Name="o2" Type="Edm.DateTime" Precision="3" />

       <Property Name="o3" Type="Edm.Decimal" Precision="8" Scale="0" />

       <Property Name="o4" Type="Edm.String" FixedLength="false" Unicode="false" />

       <Property Name="o5" Type="Edm.String" FixedLength="false" Unicode="true" />

       <Property Name="o6" Type="Edm.String" FixedLength="false" MaxLength="10" Unicode="false" />

     </EntityType>

   </Schema>

   <Schema Namespace="testdd.Model" xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://schemas.microsoft.com/ado/2007/05/edm">

     <EntityContainer Name="testddData" m:IsDefaultEntityContainer="true">

       <EntitySet Name="Customers" EntityType="testdd.Model.Entities.Customers" />

       <EntitySet Name="Orders" EntityType="testdd.Model.Entities.Orders" />

       <EntitySet Name="Invoices" EntityType="testdd.Model.Entities.Invoices" />

       <EntitySet Name="View1" EntityType="testdd.Model.Entities.View1" />

       <EntitySet Name="Result\_Proc2" EntityType="testdd.Model.Entities.Result\_Proc2" />

       <FunctionImport Name="Proc1" ReturnType="Collection(Edm.Int32)">

         <Parameter Name="x" Type="Edm.Int32" Mode="In" />

         <Parameter Name="y" Type="Edm.Int32" Mode="In" />

       </FunctionImport>

       <FunctionImport Name="Proc2" EntitySet="Result\_Proc2" ReturnType="Collection(testdd.Model.Entities.Result\_Proc2)">

         <Parameter Name="i1" Type="Edm.Int16" Mode="In" />

         <Parameter Name="i2" Type="Edm.String" Mode="In" MaxLength="10" />

         <Parameter Name="i3" Type="Edm.DateTime" Mode="In" Precision="3" />

         <Parameter Name="i4" Type="Edm.DateTime" Mode="In" Precision="3" />

       </FunctionImport>

       <FunctionImport Name="proc3" ReturnType="Collection(Edm.String)">

       </FunctionImport>

       <FunctionImport Name="proc4" ReturnType="Collection(Edm.Decimal)">

       </FunctionImport>

     </EntityContainer>

   </Schema>

 </edmx:DataServices>

</edmx:Edmx>