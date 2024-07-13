# C Flavoured Languages Style Guide

This guide intends to standardise the way I write C flavoured languages to ensure that I don't freak-out and lose my mind halfway through a project. This guide is very subjective and may contain information that is incorrect or not nessasary.

## Credits

This guide is loosely based on the google and University of Canterbury style guides with suplimentry material taken from a multitude of sources from stack overflow threads to in person conversations.

## Table of Contents
- [Example](#Example)
- [File Formatting](#File-Formatting)
    - [Indentation and Line Length](#Indentation-and-Line-Length)
    - [File Structure](#File-Structure)
- [Comments](#Comments)
    - [File Comments](#File-Comments)
    - [Function Comments](#Function-Comments)
    - [Variable and Constants Comments](#Variable-and-Constants-Comments)
- [Naming](#Naming)
- [Functions](#Functions)
- [Variables and Structs](#Variables-and-Structs)
- [Constants, Enums and Macros](#Constants-Enums-and-Macros)
- [Includes](#Includes)
- [Header Files](#Header-Files)
  
## Example

The easiest way to start off is with an example these can be found in the same folder as the guide. The two files are `example.c/.h`.

## File Formatting

This section details the general formatting of files.

- New lines are used to indicate separation between blocks of code, all top level functions and classes will have two new lines after their definitions.

- All files end with one blank new line.

- Mathematical and assignments expressions will always have a space between numbers/values and operators

- Brackets will be used even when optional unless it reduces readability (in some mathematical expressions for example).
```c
int y = 4 + (5 * 6);   // Good

int x = 4 + 5 * 6;     // Bad 

int z = (4 + (5 * 6)); // Nessasary
```

- Function, loop, and class definition braces will occur after one space from the command (not on a new line).

- Normal Brackets will occur after one space the name of the function or keyword.

```c
int function (void) {
    // Code
}
```

- Use a single space after a comma in a function call etc.

### Indentation and Line Length

Indentation is always using **spaces** with an indent of 4 spaces per level.

Lines will not exceed 80 columns unless it is; part of a link, a string literal were new line characters can affect it, or by developer discretion. This limit is to improve writing of code in a split window configuration.

### File Structure

All Files should follow the same structure:

1. File Comment
2. Includes
3. Defines and macros
4. Struts and typedefs
5. Global variables
6. Function Definitions

## Comments

Comments are vitally important and should be used anywhere that code may become hard to understand. All files should conform to the doxygen commenting standard even if doxygen is not intended to be run on the code. This is done to improve standardisation and I like the way it looks.

Not all comments in files need to be doxygen comments only text that is directly relevant to variables, functions etc. should be in the doxygen style. General comments regarding code should be done using the `//` style of comment, ether inline or the line before depending on what makes more sense for readability. If a block of text is needed the `/* */` can be used but this should be avoided to reduce confusion around what is doxygen viewed and what is not.

### Doxygen Summary

Doxygen is a documentation software that creates a manual just from your source code (Assuming that you comment the code correctly). Doxygen looks at the comments in your code to pull this information, it knows what comments to pull using specific commenting styles these are described below. Doxygen uses special commands that tell it what type of information is being presented e.g. a parameter or a description. While doxygen does allow the use of the \ character to prefix commands the @ should be used to improve searching and differential. Three comment styles for doxygen information should be used these can be seen below.

Doxygen References:

- [Usage Example](https://fnch.users.sourceforge.net/doxygen_c.html)
- [Doxgen Manual](https://doxygen.nl/manual/docblocks.html)

A line above comment:

```c
/// @brief This is a variable
int x = 1;
```

An inline comment:

```c
int x = 1; ///< @brief This is a variable
```

A block comment. Notice the space before the asterisk on a new line this is not nessasary but should be used for readability (The only part required is the `/**`).

```c
/**
 * @brief this is a function 
 *
 * @param input an input
 */
```

### File Comments

All files should start with a title block which provides information about the contents as well as author etc. This title block should unsurprisingly follow the doxygen format and be located on the first line of the file. An example title block can be seen below:

```c
/**
 * @file led.c                                                // The name of the file so doxygen looks at it
 * @author Jack Duignan (JackpDuignan@gmail.com)              // Authors names and email if they have contributed to the file (separated by "and")
 * @date 9/02/2025                                            // The date the file was created on
 * @brief An led driver module to improve abstraction         // A brief description
 *
 * This module is used to drive leds from the 5V outputs      // A longer description with markdown etc.
 * @see https://en.wikipedia.org/wiki/Light-emitting_diode    // Helpful information or other files etc. to look at
 */
```

### Function Comments

All functions including class methods should be commented using the doxygen standard. An example can be seen below:

```c
/**
 * @brief Change the led state and get its previous state
 *
 * This function uses digitalWrite() to change an leds state    // Optional
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

Often not all of the parts of this example are needed especially the lower sections it is up to the developer to decided what is nessasary. At a bare minimum a function should have an `@brief`. Functions should be commented in their header file if possible (obviously not if its a static function etc.).

### Variable and Constants Comments

All global, class, and static function variables should contain doxygen comments describing their use. All other variables (eg. local function variables) do not need doxygen and may not even need c style comments if they are named correctly and used for only one purpose.

All global constants both macros and `const` should be commented with doxygen notation as they are important for documentation.

## Naming

| Type | Naming Convention |
| ----- | ---------------- |
| Files | `snake_case` | 
| Structs | `PascalCase` |
| Types | `snake_case_t` |

Some of the below variable naming types can be not used in cases where it creates
overly complex code or names.

| Variable | Naming Convention |
| -------- | ---------------- |
| Pointers | `p_snake_case` |
| Global Variables | `g_snake_case` |
| Const Variables | `c_snake_case` |
| Return Variables | `r_snake_case` |
| String pointers | `s_snake_case` |
| Local Variables | `snake_case` |
| Defines | `ALL_CAPS` |
| Enums | `snake_case_e` |
| Enum Members | `ALL_CAPS` |

ALl exposed functions should be prefixed by an identifier from the module eg. `led_`, `serial_` or `pwm_`. 

| Function | Naming Convention |
| -------- | ---------------- |
| Exposed Functions | `snake_case` |
| Local Functions & Macros | `snake_case` |
| Macros | `ALL_CAPS` |

## Functions

All functions should be commented as described in the previous sections. Were possible functions should be defined before their use without the use of pre declarations. Functions should contain first the declaration of their local variables then the return variable if applicable can be preceded by 'r_' then the code. Functions should aim to contain less than 10 lines of actual code (not including variable assignment etc.), but this is not a hard rule.  

## Variables and Structs

Global variables and structs should be declared after includes and constants/macros with structs before variables. Structs should often be declared using typedef in the following form:

```c
typedef struct StructName{
    structMember;
} struct_type_t;
```

## Constants, Enums and Macros

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

An example of custom utility files would be special string processing functions etc.

# Header Files

Header files should share the same name as the source file. The header file should contain all function description comments for the module. 