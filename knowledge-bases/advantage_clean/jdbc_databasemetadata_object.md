---
title: Jdbc Databasemetadata Object
slug: jdbc_databasemetadata_object
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: jdbc_databasemetadata_object.htm
source: Advantage CHM
tags:
  - jdbc
checksum: 7641e3ba2e7a3932049cc2d8af559783f80c47e4
---

# Jdbc Databasemetadata Object

DatabaseMetaData Object

DatabaseMetaData Object

Advantage JDBC Driver

| DatabaseMetaData Object  Advantage JDBC Driver |  |  |  |  |

| Methods | Version Introduced | Supported | Comments |
| boolean allProceduresAreCallable () | 1.0 | Yes |  |
| boolean allTablesAreSelectable () | 1.0 | Yes |  |
| boolean dataDefinitionCausesTransactionCommit () | 1.0 | Yes |  |
| boolean dataDefinitionIgnoredInTransactions () | 1.0 | Yes |  |
| boolean deletesAreDetected (int) | 2.0 Core | Yes |  |
| boolean doesMaxRowSizeIncludeBlobs () | 1.0 | Yes |  |
| ResultSet getBestRowIdentifier (String, String, String, int, boolean) | 1.0 | Yes |  |
| String getCatalogSeparator () | 1.0 | Yes |  |
| String getCatalogTerm () | 1.0 | Yes |  |
| ResultSet getCatalogs () | 1.0 | Yes |  |
| ResultSet getColumnPrivileges (String, String, String, String) | 1.0 | Yes |  |
| ResultSet getColumns (String, String, String, String) | 1.0 | Yes |  |
| Connection getConnection () | 2.0 Core | Yes |  |
| ResultSet getCrossReference (String, String, String, String, String, String) | 1.0 | Yes |  |
| String getDatabaseProductName () | 1.0 | Yes |  |
| String getDatabaseProductVersion () | 1.0 | Yes |  |
| int getDefaultTransactionIsolation () | 1.0 | Yes |  |
| int getDriverMajorVersion () | 1.0 | Yes |  |
| int getDriverMinorVersion () | 1.0 | Yes |  |
| String getDriverName () | 1.0 | Yes |  |
| String getDriverVersion () | 1.0 | Yes |  |
| ResultSet getExportedKeys (String, String, String) | 1.0 | Yes |  |
| String getExtraNameCharacters () | 1.0 | Yes |  |
| String getIdentifierQuoteString () | 1.0 | Yes |  |
| ResultSet getImportedKeys (String, String, String) | 1.0 | Yes |  |
| ResultSet getIndexInfo (String, String, String, boolean, boolean) | 1.0 | Yes |  |
| int getMaxBinaryLiteralLength () | 1.0 | Yes |  |
| int getMaxCatalogNameLength () | 1.0 | Yes |  |
| int getMaxCharLiteralLength () | 1.0 | Yes |  |
| int getMaxColumnNameLength () | 1.0 | Yes |  |
| int getMaxColumnsInGroupBy () | 1.0 | Yes |  |
| int getMaxColumnsInIndex () | 1.0 | Yes |  |
| int getMaxColumnsInOrderBy () | 1.0 | Yes |  |
| int getMaxColumnsInSelect () | 1.0 | Yes |  |
| int getMaxColumnsInTable () | 1.0 | Yes |  |
| int getMaxConnections () | 1.0 | Yes |  |
| int getMaxCursorNameLength () | 1.0 | Yes |  |
| int getMaxIndexLength () | 1.0 | Yes |  |
| int getMaxProcedureNameLength () | 1.0 | Yes |  |
| int getMaxRowSize () | 1.0 | Yes |  |
| int getMaxSchemaNameLength () | 1.0 | Yes |  |
| int getMaxStatementLength () | 1.0 | Yes |  |
| int getMaxStatements () | 1.0 | Yes |  |
| int getMaxTableNameLength () | 1.0 | Yes |  |
| int getMaxTablesInSelect () | 1.0 | Yes |  |
| int getMaxUserNameLength () | 1.0 | Yes |  |
| String getNumericFunctions () | 1.0 | Yes |  |
| ResultSet getPrimaryKeys (String, String, String) | 1.0 | Yes |  |
| ResultSet getProcedureColumns (String, String, String, String) | 1.0 | Yes |  |
| String getProcedureTerm () | 1.0 | Yes |  |
| ResultSet getProcedures (String, String, String) | 1.0 | Yes |  |
| String getSQLKeywords () | 1.0 | Yes |  |
| String getSchemaTerm () | 1.0 | Yes |  |
| ResultSet getSchemas () | 1.0 | Yes |  |
| String getSearchStringEscape () | 1.0 | Yes |  |
| String getStringFunctions () | 1.0 | Yes |  |
| String getSystemFunctions () | 1.0 | Yes |  |
| ResultSet getTablePrivileges (String, String, String) | 1.0 | Yes |  |
| ResultSet getTableTypes () | 1.0 | Yes |  |
| ResultSet getTables (String, String, String, String []) | 1.0 | Yes |  |
| String getTimeDateFunctions () | 1.0 | Yes |  |
| ResultSet getTypeInfo () | 1.0 | Yes |  |
| ResultSet getUDTs (String, String, String, int []) | 2.0 Core | Yes | Always returns empty ResultSet. |
| String getURL () | 1.0 | Yes |  |
| String getUserName () | 1.0 | Yes |  |
| ResultSet getVersionColumns (String, String, String) | 1.0 | Yes |  |
| boolean insertsAreDetected (int) | 2.0 Core | Yes |  |
| boolean isCatalogAtStart () | 1.0 | Yes |  |
| boolean isReadOnly () | 1.0 | Yes |  |
| boolean nullPlusNonNullIsNull () | 1.0 | Yes |  |
| boolean nullsAreSortedAtEnd () | 1.0 | Yes |  |
| boolean nullsAreSortedAtStart () | 1.0 | Yes |  |
| boolean nullsAreSortedHigh () | 1.0 | Yes |  |
| boolean nullsAreSortedLow () | 1.0 | Yes |  |
| boolean othersDeletesAreVisible (int) | 2.0 Core | Yes |  |
| boolean othersInsertsAreVisible (int) | 2.0 Core | Yes |  |
| boolean othersUpdatesAreVisible (int) | 2.0 Core | Yes |  |
| boolean ownDeletesAreVisible (int) | 2.0 Core | Yes |  |
| boolean ownInsertsAreVisible (int) | 2.0 Core | Yes |  |
| boolean ownUpdatesAreVisible (int) | 2.0 Core | Yes |  |
| boolean storesLowerCaseIdentifiers () | 1.0 | Yes |  |
| boolean storesLowerCaseQuotedIdentifiers () | 1.0 | Yes |  |
| boolean storesMixedCaseIdentifiers () | 1.0 | Yes |  |
| boolean storesMixedCaseQuotedIdentifiers () | 1.0 | Yes |  |
| boolean storesUpperCaseIdentifiers () | 1.0 | Yes |  |
| boolean storesUpperCaseQuotedIdentifiers () | 1.0 | Yes |  |
| boolean supportsANSI92EntryLevelSQL () | 1.0 | Yes |  |
| boolean supportsANSI92FullSQL () | 1.0 | Yes |  |
| boolean supportsANSI92IntermediateSQL () | 1.0 | Yes |  |
| boolean supportsAlterTableWithAddColumn () | 1.0 | Yes |  |
| boolean supportsAlterTableWithDropColumn () | 1.0 | Yes |  |
| boolean supportsBatchUpdates () | 2.0 Core | Yes |  |
| boolean supportsCatalogsInDataManipulation () | 1.0 | Yes |  |
| boolean supportsCatalogsInIndexDefinitions () | 1.0 | Yes |  |
| boolean supportsCatalogsInPrivilegeDefinitions () | 1.0 | Yes |  |
| boolean supportsCatalogsInProcedureCalls () | 1.0 | Yes |  |
| boolean supportsCatalogsInTableDefinitions () | 1.0 | Yes |  |
| boolean supportsColumnAliasing () | 1.0 | Yes |  |
| boolean supportsConvert () | 1.0 | Yes |  |
| boolean supportsConvert (int, int) | 1.0 | Yes |  |
| boolean supportsCoreSQLGrammar () | 1.0 | Yes |  |
| boolean supportsCorrelatedSubqueries () | 1.0 | Yes |  |
| boolean supportsDataDefinitionAndDataManipulationTransactions () | 1.0 | Yes |  |
| boolean supportsDataManipulationTransactionsOnly () | 1.0 | Yes |  |
| boolean supportsDifferentTableCorrelationNames () | 1.0 | Yes |  |
| boolean supportsExpressionsInOrderBy () | 1.0 | Yes |  |
| boolean supportsExtendedSQLGrammar () | 1.0 | Yes |  |
| boolean supportsFullOuterJoins () | 1.0 | Yes |  |
| boolean supportsGroupBy () | 1.0 | Yes |  |
| boolean supportsGroupByBeyondSelect () | 1.0 | Yes |  |
| boolean supportsGroupByUnrelated () | 1.0 | Yes |  |
| boolean supportsIntegrityEnhancementFacility () | 1.0 | Yes |  |
| boolean supportsLikeEscapeClause () | 1.0 | Yes |  |
| boolean supportsLimitedOuterJoins () | 1.0 | Yes |  |
| boolean supportsMinimumSQLGrammar () | 1.0 | Yes |  |
| boolean supportsMixedCaseIdentifiers () | 1.0 | Yes |  |
| boolean supportsMixedCaseQuotedIdentifiers () | 1.0 | Yes |  |
| boolean supportsMultipleResultSets () | 1.0 | Yes |  |
| boolean supportsMultipleTransactions () | 1.0 | Yes |  |
| boolean supportsNonNullableColumns () | 1.0 | Yes |  |
| boolean supportsOpenCursorsAcrossCommit () | 1.0 | Yes |  |
| boolean supportsOpenCursorsAcrossRollback () | 1.0 | Yes |  |
| boolean supportsOpenStatementsAcrossCommit () | 1.0 | Yes |  |
| boolean supportsOpenStatementsAcrossRollback () | 1.0 | Yes |  |
| boolean supportsOrderByUnrelated () | 1.0 | Yes |  |
| boolean supportsOuterJoins () | 1.0 | Yes |  |
| boolean supportsPositionedDelete () | 1.0 | Yes |  |
| boolean supportsPositionedUpdate () | 1.0 | Yes |  |
| boolean supportsResultSetConcurrency (int, int) | 2.0 Core | Yes |  |
| boolean supportsResultSetType (int) | 2.0 Core | Yes |  |
| boolean supportsSchemasInDataManipulation () | 1.0 | Yes |  |
| boolean supportsSchemasInIndexDefinitions () | 1.0 | Yes |  |
| boolean supportsSchemasInPrivilegeDefinitions () | 1.0 | Yes |  |
| boolean supportsSchemasInProcedureCalls () | 1.0 | Yes |  |
| boolean supportsSchemasInTableDefinitions () | 1.0 | Yes |  |
| boolean supportsSelectForUpdate () | 1.0 | Yes |  |
| boolean supportsStoredProcedures () | 1.0 | Yes |  |
| boolean supportsSubqueriesInComparisons () | 1.0 | Yes |  |
| boolean supportsSubqueriesInExists () | 1.0 | Yes |  |
| boolean supportsSubqueriesInIns () | 1.0 | Yes |  |
| boolean supportsSubqueriesInQuantifieds () | 1.0 | Yes |  |
| boolean supportsTableCorrelationNames () | 1.0 | Yes |  |
| boolean supportsTransactionIsolationLevel (int) | 1.0 | Yes |  |
| boolean supportsTransactions () | 1.0 | Yes |  |
| boolean supportsUnion () | 1.0 | Yes |  |
| boolean supportsUnionAll () | 1.0 | Yes |  |
| boolean updatesAreDetected (int) | 2.0 Core | Yes |  |
| boolean usesLocalFilePerTable () | 1.0 | Yes |  |
| boolean usesLocalFiles () | 1.0 | Yes |  |
