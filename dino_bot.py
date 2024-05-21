import time
import keyboard
import pyautogui

# define positions for x and y. My resolution is 2560x1600
x_start = 270
x_end = 300
y = 990

while True:
    # panic button! if something goes wrong mash q button
    if keyboard.is_pressed('q'):
        break

    # loop where we are searching for obstacle in line from x_start to x_end to make sure we don't miss it
    for i in range(x_start, x_end):
        # take screenshot and sample colour from position x200 y200
        screen = pyautogui.screenshot()
        bg_color = screen.getpixel((200, 200))
        # for cactus; if something in line at y0 is different from colour sample we will jump
        if bg_color != screen.getpixel((x_end, y)):
            pyautogui.press('space')
            time.sleep(0.001)
            # because game increase speed every jump we increase x_end by 10 to overtake cactus
            x_end += 10
            if x_end >= 1600:
                x_end = 1600
            # because there is a chance to jump over obstacle during 'time theme' change we sample colours again
            screen = pyautogui.screenshot()
            bg_color = screen.getpixel((200, 200))

