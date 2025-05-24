[Resource](https://www.youtube.com/watch?v=fkWxiesfrgk)

## Delta Lake
* optimized storage layer
* open-aource software thatextends Parquet data files with a file-based transaction log for ACID transactions and scalable metadata handling

1. File Storage
    * our table
    * delta log

2. Meta Store
top-level container of objects, storing information such as metadata about tables.views or access credentials  

    * Hive metastore  
    * Unity Catalog  
    * other - Microsoft fabric catalog/aws glue data catalog  


### Databricks Commands
``` sql
> SHOW DATABASES
> USE <db name> - to switch to that database
> SHOW TABLES
> SELECT current_database();
> CREATE DATABASE <db name> / CREATE SCHEMA <db name>  
> DROP DATABASE <db name>
> CREATE OR REPLACE TABLE <DB NAME>.<table name>(x int)
> SELECT * FROM <DB NAME>.<table>
> DROP SCHEMA <db name> - 'does not work if schema is not empty'
> DROP SCHEMA <db name> cascade
```
#### Create Table, Insert, Update
``` sql
DROP TABLE IF EXISTS <TABLE>;
CREATE TABLE <TABLE> (ID INT, name, STRING)

-- INSERT
INSERT INTO <TABLE> VALUES
(1, 'A'),
(2, 'B')

INSERT OVERWRITE <TABLE> VALUES
(1, 'P') -- THIS OVERWRITES EVERYTHING
```
``` sql
> DESC <TABLE> / DESCRIBE <TABLE>
> DESCRIBE FORMATTED <TABLE>
> DESCRIBE EXTENDED <TABLE>
> DESC DETAIL <TABLE>
> %fs ls <path>
> DESC HISTORY <TABLE>
```
> delta lake is single source of truth 