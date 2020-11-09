def on_pin_pressed_p0():
    basic.show_string("ok enough weirdness")
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    basic.show_icon(IconNames.ASLEEP)
    basic.pause(1000)
    basic.show_string("bruh")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    basic.show_string("" + str((5 + 9 * (20 % 3))))
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    basic.show_string("MORE HIDDEN STUF")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("WOW U FOUND HIDDEN THING ")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    basic.show_string("erm what")
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_gesture_shake():
    basic.show_string("i'm crazy")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_leds("""
    # # . # .
    # . # # #
    . # # # .
    # # # . #
    . # . # #
    """)
basic.pause(1000)
basic.show_string("DON'T press A")

def on_forever():
    pass
basic.forever(on_forever)
