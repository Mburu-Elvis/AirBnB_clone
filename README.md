# AirBnB_clone
---

## Introduction

The AirBnB Clone Console project aims to provide a command-line interface (CLI) for managing various entities within a simulated AirBnB environment. Users can interact with the console to create, view, update, and delete instances of different classes such as BaseModel, City, User, Place, Review, State, Amenity.

## Installation

To use the AirBnB Clone Console, follow these steps:

- Clone or download the project repository from GitHub.
- Ensure that you have Python 3 installed on your system.
- Install any required dependencies specified in the requirements.txt file.
- Run the `console.py` file using Python to start the console application.
```bash
python3 console.py
```
  
### Usage:

Once the console is running, users can interact with it using various commands. Here are the available commands and their usage:

**create:**

Usage: `create <class>`  
Description: Creates a new instance of the specified class (BaseModel, City, User, etc.) and generates a unique identifier for it. The instance is then saved to the data storage.  

**show:**

Usage: `show <class> <id>`  
Description: Displays the string representation of the instance specified by its class name and unique identifier (id).  

**destroy:**

Usage: `destroy <class> <id>`  
Description: Deletes the instance specified by its class name and unique identifier (id) from the data storage.  

**all:**

Usage: `all [<class>]`  
Description: If no class is specified, displays the string representations of all instances stored in the data storage. If a class is specified, displays the string representations of instances of that class only.  

**update:**

Usage: `update <class> <id> <attribute_name> "<attribute_value>"`  
Description: Updates the specified attribute of the instance identified by its class name and unique identifier (id) with the new value provided.  

**quit/EOF:**

Usage: `quit` or `Ctrl+D`  
Description: Quits the AirBnB Clone Console.  

**Additional Features:**

- The console automatically saves changes to the data storage after each operation.  
- Error handling is implemented to handle invalid inputs and edge cases.  

**Contributing:**

Contributions to the AirBnB Clone Console project are welcome! If you'd like to contribute, please follow the guidelines outlined in the project's repository.  

**Credits:**

The AirBnB Clone Console project was developed by Elvis Mburu and Sandra Mabonga. Special thanks to the contributors and the AirBnB team for inspiration.  

**Contact:**
For any inquiries or feedback regarding the AirBnB Clone Console project, please contact [email](mburuelvis21@gmail.com).  
