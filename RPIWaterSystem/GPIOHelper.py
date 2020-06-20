import IOHelper

if not IOHelper.IsInRaspberry():
    # Running on Windows
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
    def OpenValve():
        toaster.show_toast("RPIWaterSystem - GPIO", "Openning Valve")

    def CloseValve():
        toaster.show_toast("RPIWaterSystem - GPIO", "Closing Valve")
else:
    # Running on RaspberryPi
    from gpiozero import LED

    VALVE_GPIO = 17 # TODO
    valve = LED(VALVE_GPIO)

    def OpenValve():
        valve.on()

    def CloseValve():
        valve.off()