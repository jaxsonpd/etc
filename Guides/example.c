/**
 * @file example.c                                            
 * @author Jack Duignan (JackpDuignan@gmail.com)              
 * @date 9/02/2025                                            
 * @brief An led driver module to improve abstraction         
 *
 * This module is used to drive leds from the 5V outputs      
 * @see https://en.wikipedia.org/wiki/Light-emitting_diode    
 */

#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>

#include "PIO" // made up I/O driver

#include "example.h"

led_t* LED_init (uint16_t pin, bool startState) {
    PIO_init(pin, INPUT);

    PIO_write(pin, startState);

    led_t* rp_led = (led_t *)malloc(sizeof(led_t));

    rp_led->pin = pin;
    rp_led->state = startState;  

    return rp_led;
}


bool LED_toggle (led_t* led) {
    PIO_write(led->pin, !led->state);

    led->state = !led->state;

    return led->state;
}


