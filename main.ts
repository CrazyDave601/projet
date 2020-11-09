input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Asleep)
    basic.pause(1000)
    basic.showString("bruh")
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
basic.forever(function () {
	
})
