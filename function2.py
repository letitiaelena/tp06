def on_button_pressed_b():
    global humidite
    humidite = randint(0, 100)
    if "humidite" <= "60":
        basic.show_string("Watering the plant")
        led.enable(True)
    else:
        if "humidite" >= "70":
            basic.show_string("Stopped watering the plant")
        led.enable(False)
input.on_button_pressed(Button.B, on_button_pressed_b)