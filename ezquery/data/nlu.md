
## lookup:table
table.txt

## lookup:column
column.txt

## lookup:domain
domain.txt



## lookup:sort
- last
- top
- all

## lookup:specific_high
- highest
- greatest
- most

## lookup:specific_low
- lowest
- least



## intent:insert_query
- Add [student](table) with [age](column) [15](value) years [marks](column) [50](value) [standard](column) 10 and [name](column) [Ed](value)
- insert into [student](table) table [age](column) [15](value) years [marks](column) [50](value) [standard](column) [10](value) and [name](column) [Ed](value)
- add a record to [student](table) table [name](column) [Eddie](value) [age](column) [15](value) years [marks](column) [50](value) [standard](column) as [10](value)
- New [student](table) [age](column) [15](value) years [marks](column) [100](value) [standard](column) [10](value) and [Name](column) [Monty](value)
- Add [Teacher](table) with [age](column) [40](value) years [subject](column) [Science](value) [standard](column) [12](value) and [name](column) [Rick](value)
- insert into [Teacher](table) with [age](column) [40](value) years [subject](column) [Science](value) [standard](column) as [10](value) and [name](column) [Rick](value)
- add a record to [Teacher](table) with [age](column) [40](value) years [subject](column) [Maths](value) [standard](column) [ten](value) and [name](column) [Rick](value)
- New [Teacher](table) with [age](column) [40](value) years [subject](column) [Science](value) [standard](column) as [10](value) and [name](column) [Rick](value)
- New [Teacher](name) with [age](column) [40](value) years [subject](column) [Science](value) and [name](column) [Rick](value) [standard](column) as [10](value)
- add a record to [student](table) table with [age](value) [15](value) years [marks](column) [50](value) [standard](column) as [10](value) and [name](column) [Eddie](value)
- add [student](table) [age](column) [10](value) years [name](column) [Saumitra](value) [standard](column) [12](value) [marks](column) [100](value)
- add a student having [name](value) [Bojack](value) [age](column) [12](value) years studying in [standard](column) [7](value) and [marks](column) [80](value)
- add a student having [name](column) [Bojack](value) [age](column) [12](value) [marks](column) [80](value) years studying in [standard](column) [7](value)
- add a [order](table) [id](column) [122](value) and [price](column) [100](value)
- add a [order](table) with [id](column) [12](value) and [price](column) [1222](value)
- add a [pencil](table) with [colour](column) [red](value) and [lead](column) [small](value)
- add [pencil](table) with [colour](column) [yellow](value) and [lead](column) [large](value)  
- add [pencil](table) with [colour](column) [blue](value) and [lead](column) [medium](value)
- add a [pencil](table) with [colour](column) [blue](value) and [lead](column) [small](value)  
- add to the [chocolate](table) with [colour](column) [black](value) and [flavour](column) [nuts](value) and [quanity](column) [20](value)
- add to the [chocolate](table) with [colour](column) [black](value) [flavour](column) [nuts](value) [quanity](column) [20](value)


## intent:select_query
- show me the [name](column),[age](column),[marks](column) of all the [students](table) having [marks](column) [greater](condition) than [10](value)
- show me the [marks](column),[name](column),[standard](column) of [all](sort) the [students](table) having [marks](column) [greater](condition) than [10](value)
- show me the [standard](column) of [all](sort) the [students](table) having [name](column) as [Edd](name)
- show me the [standard](column) of [all](sort) the [students](table) having [marks](column) [less](condition) than [equal](condition) to [10](value)
- show me the [standard](column) of [all](sort) the [students](table) having [marks](column) [equal](condition) to [10](value)
- show me the [name](column) of [top](sort) [10](sort_count) the [students](table) having [marks](column) [equal](condition) to [10](value)
- show me the [name](column) of [top](sort) [10](sort_count) the [students](table) having [marks](column) [equal](condition) to [10](value)
- display all the [students](table) with [age](column) [10](value) years
- display the [name](column) of [last](sort) [10](sort_count) the [students](table) having [marks](column) [greater](condition) [equal](condition) to [10](value)
- display everything of the [students](table) having [marks](column) [greater](condition) than or [equal](condition) to [10](value)
- select all the [students](table) with [age](column) [less](condition) than [10](value) years
- select all the [students](table) with [marks](column) [less](condition) than [5](value)
- select all the [students](table) with [age](column) [greater](condition) than or [equal](condition) to [12](value) years
- select all the [students](table) with [name](column) [Saumitra](value)
- select [name](column) ,[standard](column) ,[marks](column), [age](column) all the [students](table) with [marks](column) [less](condition) than [5](value)
- show me [all](sort) the [pencil](table) with [colour](column) [red](value)
- show me [top](sort) [ten](sort_count) [pencil](table) by [price](column)
- show me [price](column),[colour](column) of [pencils](table)
- show me [colour](column) of [pencils](table)
- display [pencil](table) with [lead](column) [small](value)
- show price of [order](table) with [id](column) [1231](value)
- show [all](sort) the [pencil](table) 
- show all [order](table)
- show all [order](table) with id [2112](value)   
- show [students](table) with [highest](specific_high) [marks](column)
- show [student](table) with [highest](specific_high) [marks](column)
- display [pencil](table) with [least](specific_low) [price](column)
- display [pencil](table) with [lowest](specific_low) [price](column)
- show the [pencil](table) with [lowest](specific_low) [price](column)
- select record from table [pencil](table) where [color](column) is [less](condition) than [10](value)
- select record from table [pencil](table) where [color](column) is [less](condition) than [50](value)
- select record from table [pencil](table) where [color](column) is [less](condition) than [Big](value)
- show record from table [pencils](table) where [lead](column) is [less](condition) than [10](value)
- show record from table [pencils](table) where [lead](column) is [less](condition) than [50](value)
- show record from table [pencils](table) where [lead](column) is [less](condition) than [Big](value)
- show record from table [pencils](table) where [lead](column) is [less](condition) than [Blue](value)
- show record from table [pencils](table) where [lead](column) is [less](condition) than [Red](value)
- show record from table [pencils](table) where [lead](column) is [less](condition) than [Small](value)
- show record from table [pencils](table) where [lead](column) is [more](condition) than [10](value)
- show record from table [pencils](table) where [lead](column) is [more](condition) than [50](value)
- show record from table [pencils](table) where [lead](column) is [more](condition) than [Big](value)
- show record from table [pencils](table) where [lead](column) is [more](condition) than [Blue](value)
- show record from table [pencils](table) where [lead](column) is [more](condition) than [Red](value)
- show record from table [pencils](table) where [lead](column) is [more](condition) than [Small](value)
- show record from table [pencils](table) where [price](column) is [less](condition) than [10](value)
- show record from table [pencils](table) where [price](column) is [less](condition) than [50](value)
- show record from table [pencils](table) where [price](column) is [less](condition) than [Big](value)
- show record from table [pencils](table) where [price](column) is [less](condition) than [Blue](value)
- show record from table [pencils](table) where [price](column) is [less](condition) than [Red](value)
- show record from table [pencils](table) where [price](column) is [less](condition) than [Small](value)
- show record from table [pencils](table) where [price](column) is [more](condition) than [10](value)
- show record from table [pencils](table) where [price](column) is [more](condition) than [50](value)
- show record from table [pencils](table) where [price](column) is [more](condition) than [Big](value)
- show record from table [pencils](table) where [price](column) is [more](condition) than [Blue](value)
- show record from table [pencils](table) where [price](column) is [more](condition) than [Red](value)
- show record from table [pencils](table) where [price](column) is [more](condition) than [Small](value)


## intent:create_table
- create table [order](table),having columns [id](column) [integer](domain) [date](column) [date](domain) [items](column) [integer](domain)
- new table [rooms](table) columns [number](column) [inttger](domain) [floor](column) [integer](domain) [incharge](column) [string](domain)
- new table [pencil](table) columns [colour](column) [string](domain) [lead](column) [string](domain)
- add new table [pen](table) columns [colour](column) [string](string) and [price](column) [string](domain)
- add new table [chocolate](table) [colour](column) [string](string) and [price](column) [string](domain)
- new table [teacher](table) columns [name](column) [string](domain) [subject](column) [string](domain) [age](column) [integer](domain)
- new table [manager](table) columns [name](column) [string](domain)


## intent:delete_query
- remove row from table [student](table) where [standard](column) is [equal](condition) than [100](numeric_value)
- remove row from table [student](table) where [standard](column) is [equal](condition) than [20](numeric_value)
- remove row from table [student](table) where [standard](column) is [equal](condition) than [30](numeric_value)
- remove row from table [student](table) where [standard](column) is [greater](condition) than [10](numeric_value)
- remove row from table [student](table) where [standard](column) is [greater](condition) than [100](numeric_value)
- remove row from table [student](table) where [standard](column) is [greater](condition) than [20](numeric_value)
- remove row from table [student](table) where [standard](column) is [greater](condition) than [30](numeric_value)
- remove row from table [student](table) where [standard](column) is [higher](condition) than [10](numeric_value)
- remove row from table [student](table) where [standard](column) is [higher](condition) than [100](numeric_value)
- remove row from table [student](table) where [standard](column) is [higher](condition) than [20](numeric_value)
- remove row from table [student](table) where [standard](column) is [higher](condition) than [30](numeric_value)
- remove row from table [student](table) where [standard](column) is [less](condition) than [10](numeric_value)
- remove row from table [student](table) where [standard](column) is [less](condition) than [100](numeric_value)
- remove row from table [student](table) where [standard](column) is [less](condition) than [20](numeric_value)
- remove row from table [student](table) where [standard](column) is [less](condition) than [30](numeric_value)
- remove row from table [student](table) where [standard](column) is [lesser](condition) than [10](numeric_value)
- remove row from table [student](table) where [standard](column) is [lesser](condition) than [100](numeric_value)
- remove row from table [student](table) where [standard](column) is [lesser](condition) than [20](numeric_value)
- remove row from table [student](table) where [standard](column) is [lesser](condition) than [30](numeric_value)
- remove row from table [student](table) where [standard](column) is [more](condition) than [10](numeric_value)
- remove row from table [student](table) where [standard](column) is [more](condition) than [100](numeric_value)
- remove row from table [student](table) where [standard](column) is [more](condition) than [20](numeric_value)
- remove row from table [student](table) where [standard](column) is [more](condition) than [30](numeric_value)
- remove row from table [students](table) where [id](column) is [equal](condition) than [10](numeric_value)
- remove row from table [students](table) where [id](column) is [equal](condition) than [100](numeric_value)
- remove row from table [students](table) where [id](column) is [equal](condition) than [20](numeric_value)
- remove row from table [students](table) where [id](column) is [equal](condition) than [30](numeric_value)
- remove row from table [students](table) where [id](column) is [greater](condition) than [10](numeric_value)
- remove row from table [students](table) where [id](column) is [greater](condition) than [100](numeric_value)
- remove row from table [students](table) where [id](column) is [greater](condition) than [20](numeric_value)
- remove row from table [students](table) where [id](column) is [greater](condition) than [30](numeric_value)
- remove row from table [students](table) where [id](column) is [higher](condition) than [10](numeric_value)
- remove row from table [students](table) where [id](column) is [higher](condition) than [100](numeric_value)
- remove row from table [students](table) where [id](column) is [higher](condition) than [20](numeric_value)
- remove row from table [students](table) where [id](column) is [higher](condition) than [30](numeric_value)
- remove row from table [students](table) where [id](column) is [less](condition) than [10](numeric_value)
- remove row from table [students](table) where [id](column) is [less](condition) than [100](numeric_value)
- remove row from table [students](table) where [id](column) is [less](condition) than [20](numeric_value)
- remove row from table [students](table) where [id](column) is [less](condition) than [30](numeric_value)
- remove row from table [students](table) where [id](column) is [lesser](condition) than [10](numeric_value)
- remove row from table [students](table) where [id](column) is [lesser](condition) than [100](numeric_value)
- remove row from table [students](table) where [id](column) is [lesser](condition) than [20](numeric_value)
- remove row from table [students](table) where [id](column) is [lesser](condition) than [30](numeric_value)
- remove row from table [students](table) where [id](column) is [more](condition) than [10](numeric_value)
- remove row from table [students](table) where [id](column) is [more](condition) than [100](numeric_value)
- remove row from table [students](table) where [id](column) is [more](condition) than [20](numeric_value)
- remove row from table [students](table) where [id](column) is [more](condition) than [30](numeric_value)
- remove row from table [students](table) where [marks](column) is [equal](condition) than [10](numeric_value)
- remove row from table [students](table) where [marks](column) is [equal](condition) than [100](numeric_value)
- remove row from table [students](table) where [marks](column) is [equal](condition) than [20](numeric_value)
- remove row from table [students](table) where [marks](column) is [equal](condition) than [30](numeric_value)
- remove row from table [students](table) where [marks](column) is [greater](condition) than [10](numeric_value)
- remove row from table [students](table) where [marks](column) is [greater](condition) than [100](numeric_value)
- remove row from table [students](table) where [marks](column) is [greater](condition) than [20](numeric_value)
- remove row from table [students](table) where [marks](column) is [greater](condition) than [30](numeric_value)
- remove row from table [students](table) where [marks](column) is [higher](condition) than [10](numeric_value)
- remove row from table [students](table) where [marks](column) is [higher](condition) than [100](numeric_value)
- remove row from table [students](table) where [marks](column) is [higher](condition) than [20](numeric_value)
- remove row from table [students](table) where [marks](column) is [higher](condition) than [30](numeric_value)
- remove row from table [students](table) where [marks](column) is [less](condition) than [10](numeric_value)
- remove row from table [students](table) where [marks](column) is [less](condition) than [100](numeric_value)
- remove row from table [students](table) where [marks](column) is [less](condition) than [20](numeric_value)
- remove row from table [students](table) where [marks](column) is [less](condition) than [30](numeric_value)
- remove data from table [students](table) where [marks](column) is [lesser](condition) than [10](numeric_value)
- remove data from table [students](table) where [marks](column) is [lesser](condition) than [100](numeric_value)
- remove data from table [students](table) where [marks](column) is [lesser](condition) than [20](numeric_value)
- remove data from table [students](table) where [marks](column) is [lesser](condition) than [30](numeric_value)
- remove data from table [students](table) where [marks](column) is [more](condition) than [10](numeric_value)
- remove data from table [students](table) where [marks](column) is [more](condition) than [100](numeric_value)
- remove data from table [students](table) where [marks](column) is [more](condition) than [20](numeric_value)
- remove data from table [students](table) where [marks](column) is [more](condition) than [30](numeric_value)
- remove data from table [students](table) where [standard](column) is [equal](condition) than [10](numeric_value)
- remove data from table [students](table) where [standard](column) is [equal](condition) than [100](numeric_value)
- remove data from table [students](table) where [standard](column) is [equal](condition) than [20](numeric_value)
- remove data from table [students](table) where [standard](column) is [equal](condition) than [30](numeric_value)
- remove data from table [students](table) where [standard](column) is [greater](condition) than [10](numeric_value)
- remove data from table [students](table) where [standard](column) is [greater](condition) than [100](numeric_value)
- remove data from table [students](table) where [standard](column) is [greater](condition) than [20](numeric_value)
- remove data from table [students](table) where [standard](column) is [greater](condition) than [30](numeric_value)

## intent:update_query
- change record in table [pencil](table) where [color](column) is [10](value) to [color](column) [10](value)
- change record in table [pencil](table) where [color](column) is [10](value) to [color](column) [50](value)
- change record in table [pencil](table) where [color](column) is [10](value) to [color](column) [Big](value)
- change record in table [pencil](table) where [color](column) is [10](value) to [color](column) [Blue](value)
- change record in table [pencil](table) where [color](column) is [10](value) to [color](column) [Red](value)
- change data in table [pencil](table) where [color](column) is [10](value) to [color](column) [Small](value)
- change data in table [pencil](table) where [color](column) is [10](value) to [id](column) [10](value)
- change data in table [pencil](table) where [color](column) is [10](value) to [id](column) [50](value)
- change record in table [pencil](table) where [color](column) is [10](value) to [id](column) [50](value) 
- change record in the [students](table) where [name](column) is [saumitra](value) to new [marks](column) [10](value) and [age](column) [12](value) years
- change record in the [students](table) table where [name](column) is [monil](value) to new [name](column) [manil](value) 
- change reecord in the [students](table) table where [name](column) is [morty](value) to new [name](column) [jack](value)
- change record in the [orders](table) table where [marks](column) is [20](value) to new [age](column) [20](value) years
- change records for [students](table) where [marks](column) is [20](value) to new [marks](column) [20](value)  