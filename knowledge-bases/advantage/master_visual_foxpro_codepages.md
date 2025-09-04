Visual FoxPro Codepages




Advantage Database Server 12  

Visual FoxPro Codepages

Advantage and Visual FoxPro

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Visual FoxPro Codepages  Advantage and Visual FoxPro |  |  | Feedback on: Advantage Database Server 12 - Visual FoxPro Codepages Advantage and Visual FoxPro master\_Visual\_FoxPro\_Codepages Visual FoxPro > Visual FoxPro Codepages / Dear Support Staff, |  |
| Visual FoxPro Codepages  Advantage and Visual FoxPro |  |  |  |  |

When Visual FoxPro creates a DBF table, it stores the current codepage number in the table header. When Advantage creates a new table, it will store the codepage number in the header only if you are using one of the [FoxPro-compatible collations](master_collation_support.htm). If a table does not have a codepage specified in the header, Visual FoxPro may prompt for the codepage to use when opening a table.

Although Advantage will store the codepage in the DBF header when using a FoxPro collation, it does not currently use the codepage to perform data conversions.