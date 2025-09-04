---
title: Ade Data Conversion Using Advantage Data Architect
slug: ade_data_conversion_using_advantage_data_architect
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_data_conversion_using_advantage_data_architect.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 8d626c0a953d0c69d4c993322fae629b2b5cdf85
---

# Ade Data Conversion Using Advantage Data Architect

Data Conversion Using Advantage Data Architect

Data Conversion Using Advantage Data Architect

Advantage TDataSet Descendant

| Data Conversion Using Advantage Data Architect  Advantage TDataSet Descendant |  |  |  |  |

The first step in any conversion is to move existing data to the Advantage data format. It is possible to write your own Delphi/C++Builder application for this purpose, but you will most likely find it easier to use the [Advantage Data Architect](ade_advantage_data_architect.md).

| 1. | Create a new data directory to store your Advantage files. |

| 2. | Select Connection, Create New Connection from the main menu. |

| 3. | In the ConnectionPath property, enter the path you created in step 1. |

| 4. | In the DatabaseName property enter a name for this new connection. |

| 5. | Click the OK button. |

| 6. | From the Tools menu, choose Import Data. |

| 7. | Select the type of data you will be importing. |

| 8. | In the source file name edit box, enter the path to your data in the Import Filename text box, or click the browse button to search. |

| 9. | Select the desired Import Table Type |

| 10. | Enter the destination alias for the new connection you created above. This is where all of your new Advantage tables will be created. |

| 11. | Click the Finish button to begin the data conversion. |

Note You will encounter a Paradox Import Note when converting Paradox tables that have primary indexes defined. By default, the PRIMARY index is not the default index with an Advantage application. The PRIMARY index can be set as the default index in the Advantage Data Dictionary or otherwise, the PRIMARY indexes will need to be explicitly activated in your application. Click OK to continue.

| 13. | When the conversion is finished, click Close. |

 

Note See [Data Types](ade_data_types.md) for more information if converting from Paradox tables.
