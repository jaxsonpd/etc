# C Flavoured Languages Style Guide
This guide intends to standardise the way I write C flavoured languages to ensure that I don't freak-out and lose my mind halfway through a project. This guide is very subjective and may contain information that is incorrect or not nessasary.

# Credits
This guide is losely based on the google and Univercity of Cantubury style guides with suplimentry material taken from a multitued of sources from stack overflow threads to in person conversations.

# Table of Contents
- [Example](#Example)
- [General File Formating](#General-File-Formating)
    - [Indentation and Line Length](#Indentation-and-Line-Length)
- [Comments](#Comments)
    - [File Comments](#File-Comments)
    - [Function Comments](#Function-Comments)
    - [Variable and Constants Comments](#Variable-and-Constants-Comments)
- [Naming](#Naming)
- [Functions](#Functions)
- [Variables and structs](#Variables-and-structs)
- [Constants, Enums and Macros](#Constants,-Enums-and-Macros)
- [Includes](#Includes)
- [Header Files](#Header-Files)
  
# Example
The easiest way to start off is with an example below is an example of a c header and source file with the styles implemented correctly. These files along with templates can be found in the same folder as this guide.

```c
/**
 * @Brief An example header file
 *
 */
```

```c
/**
 *
 *
 */
```

# General File Formating
This section details the general formating of files.

- New lines are used to indicate seperation between blocks of code, all top level functions and classes will have two new lines after their definitions.

- All files end with one blank new line.

- Mathmatical and assignments expresions will always have a space between numbers/values and operators
- Brackets will be used even when optional unless it reduces readability (in some mathmatical expressions for example).
```c
int y = 4 + (5 * 6);   // Good

int x = 4 + 5 * 6;     // Bad 

int z = (4 + (5 * 6)); // Unessasary
```

- Function, loop, and class definition braces will occur after one space from the command (not on a new line).
- Normal Brackets will occur after one space the name of the function or keyword.

```c
int function (void) {
    // Code
}
```

- Use a single space after a comma in a function call etc.

## Indentation and Line Length
Indetation is always using **spaces** with an indent of 4 spaces per level.

Lines will not exceed 80 columns unless it is; part of a link, a string literal were new line characters can affect it, or by developer discretion. This limit is to improve writing of code in a split window configuration.

# Comments
Comments are vitaly important and should be used anywhere that code may become hard to understand. All files should conform to the doxgen commenting standard even if doxgen is not intended to be run on the code. This is done to improve standardisation and I like the way it looks.

Not all comments in files need to be doxgen comments only text that is directly relevant to variables, functions etc. should be in the doxgen style. General comments regarding code should be done using the `//` style of comment ether inline or the line before depending on what makes more sense for readability. If a block of text is needed the `/* */` can be used but this should be avoided to reduce confusion around what is doxgen viewed and what is not.

## Doxgen Summary
Doxgen is a documentation software that creates a manual just from your source code (Assuming that you comment the code correctly). Doxgen looks at the comments in your code to pull this information, it knows what comments to pull using spesific commenting styles these are described below. Doxgen uses special commands that tell it what type of information is being presented e.g. a parameter or a description. While doxgen does allow the use of the \ character to prefix commands the @ should be used to improve searching and differenacal. Three comment styles for doxgen information should be used these can be seen below.

Doxgen Refences:

- [Usage Example](https://fnch.users.sourceforge.net/doxygen_c.html)
- [Doxgen Manual](https://doxygen.nl/manual/docblocks.html)

A line above comment:
```c
//// This is a variable
int x = 1;
```

An inline comment:
```c
int x = 1; ///< This is a variable
```

A block comment. Notice the space before the asterix on a new line this is not nessasary but should be used for readability (The only part required is the `/**`).
```c
/**
 * @brief this is a function 
 *
 * @param input an input
 */
```

## File Comments
All files should start with a title block which provides information about the contents aswell as author etc. This title block should unsurprisingly follow the doxgen format and be located on the first line of the file. An example title block can be seen below:

```c
/**
 * @file led.c                                                // The name of the file so doxgen looks at it
 * @author Jack Duignan (JackpDuignan@gmail.com)              // Authors names and email if they have contributied to the file (seperated by "and")
 * @date 9/02/2025                                            // The date the file was created on
 * @brief An led driver module to improve abstraction         // A brief description
 *
 * This module is used to drive leds from the 5V outputs      // A longer description with markdown etc.
 * @see https://en.wikipedia.org/wiki/Light-emitting_diode    // Helpful information or other files etc. to look at
 */
```

## Function Comments
All functions including class methods should be commented using the doxgen standard. An example can be seen below:

```c
/**
 * @brief Change the led state and get its previous state
 *
 * This funcion uses digitalWrite() to chnage an leds state    // Optional
 * @param led the led to change the state of                   // Don't include if this is void
 * @param state the state to set the led to
 *
 * @return the previous state of the led                       // Don't include if this is void
 *
 * @see digitalWrite                                           // All below this is optional
 * @note this only works if an led is connected to the pin
 * @warning there must be a current limiting resistor in series with the led
 */
bool ledSet(int led, bool state) {
    // Code
}
```
Often not all of the parts of this example are needed especially the lower sections it is up to the developer to decied what is nessasary. At a bare minium a function should have an `@brief`. Functions should be commented in their header file if possible (obviously not if its a static function etc.).

## Variable and Constants Comments
All global, class, and static function variables should contain doxgen comments describing their use. All other variables (eg. local function variables) do not need doxgen and may not even need c style comments if they are named correctly and used for only one purpose.

All constants both macros and `const` should be commented with doxgen notation as they are important for documentation.

# Naming

| Type | Naming Convetion |
| ----- | ---------------- |
| Files | `PFX_PascalCase` | 
| Structs | `PFX_PascalCase` |
| Types | `camelCase_t` |

| Variable | Naming Convetion |
| -------- | ---------------- |
| Pointers | `p_camelCase` |
| Global Variables | `g_camelCase` |
| Const Variables | `c_camelCase` |
| Return Variables | `r_camelCase` |
| Local Variables | `camelCase` |
| Defines | `ALL_CAPS` |
| Enums | `camelCase_e` |
| Enum Members | `ALL_CAPS` |

| Function | Naming Convetion |
| -------- | ---------------- |
| Exposed Functions | `PFX_camelCase` |
| Local Functions & Macros | `camelCase` |

Where the PFX is a three letter abreviation for the module

# Functions
All functions should be commented as described in the previous sections. Were possible functions should be definied before their use without the use of pre declerations. Functions should contain first the decliration of their local variables then the return variable if applicable can be precided by 'r_' then the code. Functions should aim to contain less than 10 lines of actual code (not including variable assignment etc.), but this is not a hard rule.  

# Variables and structs
Global variables and structs should be declared after includes and constants/macros with structs before variables. Structs should often be declared using typedef in the following form:

```c
typedef struct {
    structMember;
} structName;
```
# Constants, Enums and Macros
Global constants, enums and macros should be declared after the includes in a file, with macros before constants. Local constants (Do not use macros as local constants as they are not) should be defined at the top of the function before the local variables. When selecting between using a gloabl macro, a global constant and a local constant the following should be considered:

1. Is it functioning as a configuration option (use a macro)
2. Is it functioning as a no configurable value in an equation (use a constant)
3. Is this value only ever used in this function (use a local constant)
4. Is this value part of a group of other values that have easy numerical values (Use an enum)

# Includes
Includes should occur directly after the file comment block and have the following structure (with new lines in between each block):

1. C standard header files
2. C++ standard header files
3. Custom made utility header files
4. Custom made header files that provide functionality
5. The header file for the file itself (if it is a source file)

An example of custom utitility files would be special string processing functions etc.

# Header Files
Header files should share the same name as the source file. The header file should contain all function description comments for the module. 








