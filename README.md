
# 0x00. AirBnB clone - The console

 >Foundations - Higher-level programming ― AirBnB clone

 ![Console Help Preview](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

## AirBnB Clone Console

Welcome to the AirBnB Clone Console! This is the first step towards building the AirBnB clone project, a full web application that mimics some functionalities of the popular accommodation rental platform, Airbnb.

## Overview

The AirBnB Clone Console is a Python-based command-line interface (CLI) that allows you to manage AirBnB objects, such as users, states, cities, places, and more. With this console, you can perform various operations on these objects, including creating, retrieving, updating, and deleting them.

And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the following actions can be performed:

- Creating new objects (ex: a new User or a new Place)
- Retrieving an object from a file, a database etc…
- Performing operations on objects (count, compute stats, etc…)
- Updating attributes of an object
- Destroying an object

### Command List

## Create Command

> Create Command to create a new instance of <Model_name>
Example:

```markdown
(hbnb) create <Model_name>
```

## Update Command

>Update Command to Updates an instance based on the `Model_name` and `id` by adding or updating attribute.
Example:

```markdown
(hbnb) update <Model_name> <id> <attribute name> <value>
```

## Destroy Command

>Destroy Command to deletes an instance and save changes based on the `Model_name` and  `id`

Example:

```markdown
(hbnb) destroy <Model_name> <id>
```

## Show Command

>Show Command to prints the string representation of an instance based on the `Model_name` and `id`

Example:

```markdown
(hbnb) show <Model_name> <id>       
```

## All Command
>
>All Command to Prints all string representation of all
instances based or not on the <Model_name>.
Example:

```markdown
(hbnb) all                
    to print all models
```

```markdown
(hbnb) all <Model_name>                
    to print all <Model_name> 
```

## Quit Command
>
> Quit command to exit the program
Example:

```markdown
(hbnb) quit
```

**Proudly written by:**

- **[Meriem Ben Ayad](https://github.com/meriembenayad)**
- **[Thami Baladi](https://github.com/ThamiBa)**

> Copyright © 2023. All rights reserved.
