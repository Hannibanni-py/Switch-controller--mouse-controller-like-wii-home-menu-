from pyjoycon import GyroTrackingJoyCon, get_R_id
import time
import pyautogui


def opposite(number):
  return -1 * number

def move_smooth(z, y, t):
    for i in range(t):
        pyautogui.moveRel(z/int(t), y/int(t))

clicked_l = False
clicked_r  = False
allow_move = True
joycon_id = get_R_id()
joycon = GyroTrackingJoyCon(*joycon_id)
while True:

    if joycon.get_button_x():
       pyautogui.moveTo(960, 540)
    y_pos = opposite(joycon.get_gyro_y())
    y_move = int(y_pos/5)
    z_pos = joycon.get_gyro_z()
    z_move = int(z_pos/5)
    if allow_move == True:
        move_smooth(z_move, y_move,  1)

    if joycon.get_button_a():
        allow_move=False
    if joycon.get_button_b():
        allow_move=True

    if not clicked_l:         
        if joycon.get_button_zr():
            pyautogui.mouseDown(button='right')
            clicked_l = True
    if not clicked_r:
        if joycon.get_button_r():
            pyautogui.mouseDown(button='left')
            clicked_r = True

    if clicked_l:
        if not joycon.get_button_zr():
            pyautogui.mouseUp(button="right")
            clicked_l  = False
    if clicked_r:
        if not joycon.get_button_r():
            pyautogui.mouseUp(button="left")
            clicked_r  = False

    stick_r = joycon.get_stick_right_vertical()
    stick_r=stick_r/500
    if stick_r > 4:
        pyautogui.scroll(stick_r)
    if stick_r <  2:
        pyautogui.scroll(opposite(stick_r) * 4.8)
    time.sleep(0.01)