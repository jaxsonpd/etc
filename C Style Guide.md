# C Flavoured Languages Style Guide
This guide intends to standardise the way I write C flavoured languages to ensure that I don't freakout and lose my mind halfway through a project. This guide is very subjective and may contain information that is incorrect or not nessasary.

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

- New lines are used to indicate seperation between blocks of code all top level functions and classes will have two new lines after their definitions.

- All files end with one blank new line.

- Mathmatical and assignments expresions will always have a space between numbers/values and operators
- Brackets will be used even when optional unless it reduces readability (in some mathmatical expressions for example).
```c
int y = 4 + (5 * 6); // Good

int x = 4 + 5 * 6; // Bad 

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

Lines will not exceed 80 columns unless it is part of a link, is a string literal were new line characters can affect it or by developer discretion. This limit is to improve writing of code in a split window configuration.

# Comments
Comments are vitaly important and should be used anywhere that code may become hard to understand. All files should conform to the doxgen commenting standard even if doxgen is not intended to be run on the code. This is done to improve standardisation and I like the way it looks.

Not all comments in files need to be doxgen comments only text that is directly relevant to variables, functions etc. should be in the doxgen style. General comments regarding code should be done using the `//` style of comment ether inline or the line before depending on what makes more sense for readability. If a block of text is needed the `/* */` can be used but this should be avoided to reduce confusion around what is doxgen viewed and what is not.

## Doxgen Summary
Doxgen is a documentation software that creates a manaul just from your source code (Assuming that you comment the code correctly). Doxgen looks at the comments in your code to pull this information. While doxgen does allow the use of the \ character to prefix commands the @ should be used to improve searching and differenacal. Three comment styles for information should be used these can be seen below.

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
All files should start with a title block which provides information about the contents aswell as author etc. This title block should unsupprisingly follow the doxgen format and be located on the first line of the file. An example title block can be seen below:

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
Often not all of the parts of this example are needed especially the lower sections it is up to the developer to decied what is nessasary. At a bare minium a function should have an `@brief`.

## Variable and Constants Comments
All global, class, and static function variables should contain doxgen comments describing their use. All other variables (eg. local function variables) do not need doxgen and may not even need c style comments if they are named correctly and used for only one purpose.

All constants both macros and `const` should be commented with doxgen notation as they are important for documentation.

# Functions

# Variables and structs

# Constants

# Includes

# Header Files







