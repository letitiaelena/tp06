def on_logo_pressed():
    if led.brightness() > 120:
        if input.is_gesture(Gesture.SHAKE):
            led.enable(True)
    else:
        if led.brightness() <= 120:
            basic.show_string("Stopped watering the plant")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)