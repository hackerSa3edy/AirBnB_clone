
0x00. AirBnB clone - The console
=
<p align="center">
  <img src="https://github.com/Z-Sitawi/AirBnB_clone/blob/main/assets/hbnb_logo.png" alt="hbnb logo">
</p>
Description 🏷
==
Welcome to the AirBnB clone project!\
This team project is part of the "Alx" Software Engineering program.
It represents the first step towards building a full web application.

This first step consists of:\
a custom command-line interface for data management,
and the base classes for the storage of this data.

## Usage 💻

The console works both in interactive mode and non-interactive mode, much like a Unix shell.
It prints a prompt **(hbnb)** and waits for the user for input.

Command | Example
------- | -------
Run the console | ```./console.py```
Quit the console | ```(hbnb) quit```
Display the help for a command | ```(hbnb) help <command>```
Create an object (prints its id)| ```(hbnb) create <class>```
Show an object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Destroy an object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show all objects, or all instances of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` or ```(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```

### Interactive mode (example)

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Non-interactive mode (example)
All tests should also pass in non-interactive mode:

```bash 
$ echo "python3 -m unittest discover tests" | bash
```


```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Tests ✔
* [tests](./tests): Folder of test files. 
## Tasks

**0. README, AUTHORS**
  * [README.md](https://github.com/Z-Sitawi/AirBnB_clone/blob/main/README.md) 
  * [AUTHORS](https://github.com/Z-Sitawi/AirBnB_clone/blob/main/AUTHORS)

**1. Be pycodestyle compliant!**\
Write beautiful code that passes the pycodestyle checks.

**2. Unittests**\
All your files, classes, functions must be tested with unit tests

**3. BaseModel**
  * [models/base_model.py]()
  * [models/__init__.py]()

**4. Create BaseModel from dictionary**
  * [models/base_model.py]()
**5. Store first object**
  * [models/engine/file_storage.py]() 
  * [models/engine/__init__.py]()
  * [models/__init__.py]()
  * [models/base_model.py]()
**6. Console 0.0.1**
  * [console.py]()
**7. Console 0.1**
  * [console.py]()
**8. First User**
  * [models/user.py]()
  * [models/engine/file_storage.py]()
  * [console.py]()
**9. More classes!**
  * [models/state.py]()
  * [models/city.py]()
  * [models/amenity.py]()
  * [models/place.py]()
  * [models/review.py]()
**10. Console 1.0**
  * [console.py]()
  * [models/engine/file_storage.py]()
## Authors

- [Zakaria Aaichaou](https://github.com/Z-Sitawi)
- [Abdelrahman Mohamed](https://github.com/hackerSa3edy)


