---
title: Arc Number Of Tps Visibility List Elements Info
slug: arc_number_of_tps_visibility_list_elements_info
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_number_of_tps_visibility_list_elements_info.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 09141d5d819cae72d54003acf52eeaa6c55521b5
---

# Arc Number Of Tps Visibility List Elements Info

Number of TPS Visibility List Elements Info

Number of TPS Visibility List Elements Info

| Number of TPS Visibility List Elements Info |  |  |  |  |

While changes are being made to the database, the Advantage TPS hides those updates from other users until the data is committed. The uncommitted data is visible only to the application performing the transaction. Other applications view the data as it was before the transaction began. If the transaction is rolled back, the uncommitted data is never seen by any users other than the one who was performing the transaction. If the transaction is committed, the updated data becomes visible to all users at one time. The TPS Visibility List Elements are used to provide this "data hiding" during a transaction. The TPS Visibility List is specific to changes made to database files and their associated index files.
