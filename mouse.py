from pynput.mouse import Controller

mouse = Controller()

# Scroll up by 2 units
mouse.scroll(0, 2)

# Scroll down by 2 units
mouse.scroll(0, -2)

# Scroll right by 2 units
mouse.scroll(2, 0)

# Scroll left by 2 units
mouse.scroll(-2, 0)