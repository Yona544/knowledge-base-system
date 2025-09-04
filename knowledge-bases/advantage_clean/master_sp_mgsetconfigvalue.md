---
title: Master Sp Mgsetconfigvalue
slug: master_sp_mgsetconfigvalue
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mgsetconfigvalue.htm
source: Advantage CHM
tags:
  - master
checksum: a29d345f1d895c100981019c323466ade2821da8
---

# Master Sp Mgsetconfigvalue

sp\_mgSetConfigValue

sp\_mgSetConfigValue

Advantage SQL Engine

| sp\_mgSetConfigValue  Advantage SQL Engine |  |  |  |  |

Update a server configuration value.

Syntax

sp\_mgSetConfigValue (

 Setting, CiCharacter, 30,

 Value, CiCharacter, 256);

 

Parameters

| Setting (I) | The configuration Value to update. |
| Value (I) | The value to set in the configuration. |
| OldValue (O) | The value that was set prior to the calling this procedure. |
| Result (O) | An integer value indicating the result.  0 : Success.  The Change has been written and the server updated.  1 : The new value matches the existing value. No changes were made.  2 : The setting has been updated, but a restart is required to take effect.  3 : Modifying this setting via this stored procedure is not supported. |
| ResultText (O) | A result indicating if the change was successful, was successful but requires a restart, or is unsupported. |

Remarks

sp\_mgSetConfigValue is an administrative procedure that will update the Advantage configuration. The procedure may only be executed on an active [root dictionary](master_root_dictionary.md), and the user must be a member of the SERVER:Admin group. If a restart is required, the setting will be changed in the configuration and will take effect the next time the Advantage Service is restarted. The following table indicates which configuration settings can be modified through this procedure.

| Setting | Dynamic, Restart Required, Unsupported |
| [CONNECTIONS](master_number_of_connections_c_.md) | Restart Required to update displayed values |
| [WORKAREAS](master_number_of_work_areas_w_.md) | Restart Required to update displayed values |
| [TABLES / DBFS](master_number_of_tables_d_.md) | Restart Required to update displayed values |
| [INDEXES](master_number_of_index_files_i_.md) | Restart Required to update displayed values |
| [LOCKS](master_number_of_data_locks_l_.md) | Restart Required to update displayed values |
| [THREADS](master_number_of_worker_threads_t_.md) | Restart Required |
| [ERROR\_LOG\_MAX](master_error_log_file_size.md) | Dynamically Changed |
| [ERROR\_LOG\_TYPE](master_error_and_diagnostic_logs.md) | Unsupported |
| [ERROR\_ASSERT\_LOGS](master_error_and_assert_log_path.md) | Restart Required \* if an adsserver.ini exists, it will be copied to the new location |
| [PARTIAL\_CONNECTION\_TIMEOUT](master_partial_connection_timeout.md) | Unsupported |
| [TPS\_LOGS](master_transaction_log_files_path.md) | Restart Required |
| [LAN\_IP\_ADDRESS](master_lan_ip_address.md) | Unsupported |
| [INTERNET\_IP\_ADDRESS](master_internet_ip_address.md) | Unsupported |
| [RECEIVE\_IP\_PORT / IP\_PORT](master_ip_port.md) | Unsupported |
| [RECEIVE\_TLS\_PORT / TLS\_PORT](master_receive_tls_port.md) | Unsupported |
| [TLS\_CIPHERS](master_tls_ciphers.md) | Unsupported |
| [TLS\_KEY\_FILE](master_tls_key_file.md) | Unsupported |
| [TLS\_KEY\_PASSWORD](master_tls_key_password.md) | Unsupported |
| [FIPS](master_fips_config.md) | Unsupported |
| [COMPRESSION](master_compression_config_param.md) | Dynamically Changed |
| [FLUSH\_FREQUENCY](master_flush_frequency.md) | Unsupported |
| [CREATEMASK](master_createmask.md) | Unsupported |
| [LOWERCASE\_ALL\_PATHS](master_lowercase_all_paths.md) | Unsupported |
| [CLIENT\_TIMEOUT](master_client_timeout.md) | Dynamically Changed for new connections |
| [USE\_DYNAMIC\_CURSORS](master_use_dynamic_cursors.md) | Unsupported |
| [SUPRESS\_MESSAGE\_BOXES](master_suppress_message_boxes.md) | Dynamically Changed |
| [DISABLE\_FREE\_CONNECTIONS](master_disable_free_connections.md) | Dynamically Changed \*May only be set to TRUE, may not be set to FALSE |
| [INTERNET\_PORT](master_internet_port.md) | Unsupported |
| [INTERNET\_CLIENT\_TIMEOUT](master_internet_client_timeout.md) | Dynamically Changed for new connection |
| [PERMITTED\_REP\_ERRORS](master_permitted_rep_errors.md) | Restart Required |
| [MAX\_CACHE\_MEMORY](master_max_cache_memory.md) | Dynamically Changed |
| [TMP\_FILE\_POOL\_SIZE](master_tmp_file_pool_size.md) | Unsupported |
| MINIDUMPERROR | Dynamically Changed |
| MINIDUMPLINE | Dynamically Changed |
| MINIDUMPFILE | Dynamically Changed |
| EXTERNALMINIDUMPERROR | Dynamically Changed |
| [NONEXCLUSIVE\_PROPRIETARY\_LOCKING](master_non_exclusive_proprietary_locking.md) | Unsupported |
| [SE\_PASSWORDS](master_se_passwords.md) | Unsupported |
| [ROOT\_DICTIONARY](master_root_dictionary_config.md) | Unsupported |
| [SORT\_BUFFER](master_index_sort_buffer_size_z_.md) | Unsupported |
| [SQL\_SORT\_BUFFER](master_sql_sort_buffer_size.md) | Unsupported |
| [SQL\_STATEMENT\_LIMIT](master_sql_statement_limit.md) | Dynamically Changed |

Example

EXECUTE PROCEDURE sp\_mgSetConfigValue( 'CONNECTION', '100');

EXECUTE PROCEDURE sp\_mgSetConfigValue( 'ERROR\_ASSERT\_LOGS', 'c:\adslogs');

 

See Also

[Using SQL to Access Management Information](master_using_sql_to_access_management_information.md)
