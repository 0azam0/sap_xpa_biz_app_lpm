# Data Assets

This folder is meant to contain CSV version of the various data assets used in the SAP XPA Biz App LPM project which will be provided later.
As of now, all of the relevant datasets reside in a connected SAP Datasphere instance and are consumed during model development and prediction generation phases. SAP Datasphere acquires the relevatn datasets from an SAP Cloud ERP system.

## Data Sources

Data is acquired and stored in the connected SAP Datasphere from various SAP Cloud ERP tables which are as lsited in the following

- __KNA1__ table is part of the general view of customer master data in SAP S/4HANA.
- __VBRK__ table is part of the Billing and Invoicing sub-module in the Sales and Distribution (SD) module of SAP S/4 HANA. The SD module also includes other sub-modules, such as: Sales Order Management, Delivery Management, Customer Management, and Sales Analytics
- __BSEG__ table in SAP S/4 HANA is part of the S/4 FICO data model. It stores accounting header and line item entries, and is still relevant for some operational finance processes
- __BSAD__ table is part of the Accounting module in SAP. It is a secondary index for customers with cleared items
- __FEBEP__ table is part of the Electronic Bank Statement (EBS) module in SAP S/4 HANA

## Data Acquisition

Required data sets can be acquired from SAP Cloud ERP via either [SAP HANA Connector](https://help.sap.com/docs/SAP_DATASPHERE/be5967d099974c69b77f4549425ca4c0/e6b63f176d3640609adcf06297fb37e9.html?q=connector) or [SAP ABAP Connector](https://help.sap.com/docs/SAP_DATASPHERE/be5967d099974c69b77f4549425ca4c0/a75c1aacf951449ba3b740c7e46da3a9.html?q=connector) depending upon the on-premesis or cloud version.

The data assets lsited above are essential for the functionality of the SAP XPA Biz App LPM project. Data from various listed tables is combined via an SQL query to generate training as well as scoring data sets.

## Suggested Training and Scoring Data Views

Following is a suggested layout of the SAP Datasphere dataview which can be leverage to train and deploy a desired predictive model to predict payment late days. If the model is developed and deployed using the suggested dataview layout, then the same dataview layout is to be used for a datview containing the data for prediction generation.

| COLUMN             | TYPE             |
|--------------------|------------------|
| INVOICE_NUMBER | INTEGER64 |
| ORDER_DATE | DATE|
| CUSTOMER_NUMBER|INTEGER64 |
| CUSTOMER_NAME | NAVARCHAR(5000) |
| MATERIAL_NUMBER | DOUBLE |
| MATERIAL_NAME | NAVARCHAR(5000) |
| NET_VALUE_OF_ITEM | DOUBLE |
| SHIP_DATE| DATE |
| ACTUAL_INVOICED_QUANTITY_CASES | DOUBLE |
| ITEM_CREDIT_PRICE_ROUNDED | DOUBLE |
| ITEM_CREDIT_PRICE | DOUBLE |
| STATUS_MANUAL_PRICE_CHANGE | NAVARCHAR(5000) |
| INVOICE_DUE_DATE | DATE |
| ACTUAL_PAID_DATE | DATE |
| EXPECTED_AMOUNT | DOUBLE |
| BASELINE_DT_FOR_DUE_DATE_CALC | DATE |
| PAYMENT_TERM | NAVARCHAR(5000) |
| CASH_DISCOUNT_DAYS | DOUBLE |
| NET_PAYMENT_TERMS_PERIOD | DOUBLE |
| CASH_DISCOUNT_PERCENTAGE | DOUBLE |
| AMT_ELIGIBLE_FOR_CASH_DISCOUNT | DOUBLE |
| CASH_DISCOUNT_AMOUNT | DOUBLE |
| INVOICE_DUE_DATE_YEAR_MONTH | DATE |
| DAYS_LATE | DOUBLE |
| ORDER_TO_PAID_DAYS | DOUBLE |
| INVOICE_TO_PAID_DAYS | DOUBLE |
| DAYS_TO_SHIP | DOUBLE |
|
