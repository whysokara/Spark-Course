### Unity Catalog - Data Governance

#### Data Governance
1. Data Discovery - option to easily find data we are looking for
2. Access Control - control who can view and modify them
3. Data Lineage - to know from where data is coming and who is using
4. Auditing - who is using what with data
5. Cataloging - option to describe column
6. Quality

> Metastore - is the top-level container for catalog in Unity Catalog. Within a metastore, Unity catalog provides a 3-level namespace for organizing data: 
1. Catalogs, 
2. schemas (aka databases), and 
3. tables/views

##### Unity Catalog introduces three-level namespaces:
> catalog.schema.table
ex: main,sales.customer_data