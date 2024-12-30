# Data Assets

This folder is meant to contain CSV version of the various data assets used in the SAP XPA Biz App LPM project which will be provided later.
As of now, all of the relevant datasets reside in a connected SAP Datasphere instance and are consumed during model development and prediction generation phases. SAP Datasphere acquires the relevatn datasets from an SAP Cloud ERP system.

## Data Sources

Data is acquired and stored in the connected SAP Datasphere from various SAP Cloud ERP tables which are as lsited in the following

- __KNA1__ table is part of the general view of customer master data in SAP S/4HANA.
- __VBRK__ table is part of the Billing and Invoicing sub-module in the Sales and Distribution (SD) module of SAP S/4 HANA. The SD module also includes other sub-modules, such as: Sales Order Management, Delivery Management, Customer Management, and Sales Analytics
-  __BSEG__ table in SAP S/4 HANA is part of the S/4 FICO data model. It stores accounting header and line item entries, and is still relevant for some operational finance processes
- __BSAD__ table is part of the Accounting module in SAP. It is a secondary index for customers with cleared items
- __FEBEP__ table is part of the Electronic Bank Statement (EBS) module in SAP S/4 HANA

The data assets lsited above are essential for the functionality of the SAP XPA Biz App LPM project. Data from various listed tables is combined via an SQL query to generate training as well as scoring data sets.