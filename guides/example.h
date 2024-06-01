/**
 * @file example.h                                                
 * @author Jack Duignan (JackpDuignan@gmail.com)              
 * @date 9/02/2025                                            
 * @brief An led driver module to improve abstraction         
 *
 * This module is used to drive leds from the 5V outputs      
 * @see https://en.wikipedia.org/wiki/Light-emitting_diode    
 */

#include <stdint.h>
#include <stdbool.h>


/// A struct to store the information about a spesific led 
typedef struct {
    uint16_t pin;
    bool state;
} led_t;

/**
 * @brief Initialise the led and create a new led struct
 * 
 * @param pin the pin the led is connected to
 * @param startState the starting state of the led
 * 
 * @return an led struct
 */
led_t* LED_init (uint16_t pin, bool startState);

/**
 * @brief Toggle the led's state
 * 
 * @param led the led struct to toggle
 * 
 * @return the new state of the led
*/
bool LED_toggle (led_t* led);



