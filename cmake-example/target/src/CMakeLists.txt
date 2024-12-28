add_executable(exampleExecutable main.c)

# target_compile_options(exampleExecutable PRIVATE -Os -DF_CPU=16000000UL -mmcu=atmega328p -Wall -Wstrict-prototypes -Wextra)
# target_link_libraries(exampleExecutable PRIVATE avr-extends)

# add_program_target(exampleExecutable PROGRAM_TARGET program)