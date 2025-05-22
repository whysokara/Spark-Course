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