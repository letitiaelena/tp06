humidite = 0

def on_button_pressed_a():
    basic.show_number(input.temperature())
    led.enable(True)
    if input.temperature() >= 10 and input.temperature() <= 18:
        basic.show_string("Watering the plant")
input.on_button_pressed(Button.A, on_button_pressed_a)
