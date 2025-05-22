## Spark Architecture

Spark is unified computing engine for parallel data processing on computer cluster  

#### Steps (High Level)
* So there is a application where we have written our python/sql code
* Goes to driver and creates spark session
* driver distributes the tasks to executor
* between driver and executor there is cluster manager that decides which task should be given to which executor
* each executor has slots within them, slots are number of CPU core and meaning that many tasks are performed parallely
* after compltion of individual tasks, executors shares data with each other (data shuffling) if required
* then the data is been sent back to driver or stored in some location

#### 2 operation you can do with Spark

1. Transformation
    * business logic that we want to apply to our data
    * it takes one or more RDD/DataFrame/DataSet and transform it to new
    * transformation can be either narrow or wide. Wide transformation requires shuffling data between partitions
    * Narrow: Filter, Select, Create new column, Cast
    * wide: group by, sort, join

2. Actions
    * Demand for results
    * collect, count, save, take, show
    * Actions are the operations that kick off the computation 

#### Laziness of Spark

> Read => GroupBy => Wide T. => Filter => Show  
that would be smart to filter the data first, so spark engine does that and try to move filter as early as posible in sequence  
> Read => Filter => GroupBy => Wide T. => Show  

> Catalyst Optimizer - handles logical and physical query plan
> Tungsten - provides low-level optimizations and code generation techniques to improve overall performance
> AQE dynamically adjusts query execution based on runtime conditions

#### Data Shuffling
* Shuffling is a process of redistributing data across partitions, and typically involves data exchange between executor nodes
* wide transformation requires shuffling

#### Optimization
* use parquet or delta, instead of csv
* avoid expensive operations like sort
* minimize volume of data
* Cache/persist dataframes
* Repartition/coalesce
* avoid UDFs
* partition and/or index data
* Bucketing
* Optimize cluster
* ...  

[www.youtube.com/embed/iXVIPQEGZ9Y?si=2y8XGn0EpWUTBLlz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>](https://youtu.be/iXVIPQEGZ9Y?si=bqT_99cmX3PA0IRo)