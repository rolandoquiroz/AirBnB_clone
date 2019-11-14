## Holberton School: 0x00. AirBnB clone - The console

![holbie](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20191114%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20191114T141415Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b3ab4587e3c7d1a579ae4f1ff292a05d43f5461ca9423a6e5acce7b18c268134)

## Description
This repository contains  is a  first phase full-stack clone of the web application AirBnB. This version includes a command interpreter that parses and evaluates input from the command line appropriately with Unit test suite included.

## Repository Contents

| Module| Description |
| :-:   | :-: |
| AUTHORS | Contributors list to this project |
| console.py | The main console file |
| amenity.py | The amenity subclass|
|base_model.py|The base model superclass|
|city.py|The city subclass|
|place.py|The place subclass|
|review.py|The review subclass|
|state.py | The state subclass|
|user.py | The user subclass|
|file_storage.py| The file storage class |
|test_console.py | The unittest module for console |
|test_amenity.py| The unittest module for amenity|
|test_base_model.py| The unittest module for base model |
|test_city.py| The unittest module for city |
|test_place.py| The unittest module for place |
|test_review.py| The unittest module for review |
|test_state.py| The unittest module for state |
|test_user.py| The unittest module for user |
|test_file_storage.py| The unittest module for file storage |

## Getting Started

## Installation

```js
git clone https://github.com/amartinezre05/AirBnB_clone.git
```

## Short usage guide

There are two ways to run the console: running like an executable file or calling python3 to run the console.py file:

* Run directly ./console.py

* Calling python python3 console.py

Next, you should see a command prompt. This tells us the console are ready to run operations.

```bash
$ ./console.py
(hbnb)
```
## Basic commands

### quit

Usage: quit

Exits the console

### help
Usage: help <topic>

Without parameters, shows a list of commands or operations who has a little description.

```sh
$ ./console.py 
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
```
With topic, shows the description about the given topic
```sh
(hbnb) help all

        all - Prints all string representation of all instances
        based or not on the class name
```
## Other Commands Samples
```sh
(hbnb) create City
(hbnb) show <class> <id>
(hbnb) destroy <class> <id>
(hbnb) all <class>
(hbnb) all
(hbnb) update <class> <id> <attribute_name> "<attribute value>"

```

## Authors
Albéniz Martínez Restrepo 
email: 913@holbertonschool.com
Rolando Quiroz 
email: 906@holbertonschool.com

## License
[MIT](https://choosealicense.com/licenses/mit/)