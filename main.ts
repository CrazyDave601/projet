input.onPinPressed(TouchPin.P0, function () {
    basic.showString("ok enough weirdness")
})
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Asleep)
    basic.pause(1000)
    basic.showString("bruh")
})
input.onPinPressed(TouchPin.P2, function () {
    basic.showString("" + (5 + 9 * (20 % 3)))
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("MORE HIDDEN STUF")
})
input.onButtonPressed(Button.B, function () {
    basic.showString("WOW U FOUND HIDDEN THING ")
})
input.onPinPressed(TouchPin.P1, function () {
    basic.showString("erm what")
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("i'm crazy")
})
basic.showLeds(`
    # # . # .
    # . # # #
    . # # # .
    # # # . #
    . # . # #
    `)
basic.pause(1000)
basic.showString("DON'T press A")
