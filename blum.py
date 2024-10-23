from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
from pynput.mouse import Button, Controller

mouse = Controller()
time.sleep(0.5)

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

def print_welcome(language):
    if language == '1':
        print("""

███████╗███████╗███╗   ██╗
╚══███╔╝██╔════╝████╗  ██║
  ███╔╝ █████╗  ██╔██╗ ██║
 ███╔╝  ██╔══╝  ██║╚██╗██║
███████╗███████╗██║ ╚████║
╚══════╝╚══════╝╚═╝  ╚═══╝

    [!] | ZEn | TELEGRAM @airdropgxhunter                 
    [!] | ZEn | Welcome to the auto-clicker for Blum.
    [!] | ZEn | To select the Telegram Desktop window, enter 1.
    """)
    elif language == '2':
        print("""

███████╗███████╗███╗   ██╗
╚══███╔╝██╔════╝████╗  ██║
  ███╔╝ █████╗  ██╔██╗ ██║
 ███╔╝  ██╔══╝  ██║╚██╗██║
███████╗███████╗██║ ╚████║
╚══════╝╚══════╝╚═╝  ╚═══╝

    [!] | ZEn | Telegram @airdropgxhunter          
    [!] | ZEn | Selamat datang di klik otomatis untuk Blum.
    [!] | ZEn | Untuk memilih halaman windows Telegram Dekstop, klik 1.
    """)

def print_pause_message(language, paused):
    if language == '1':
        if paused:
            print('[-] | Pause activated, press "q" to continue.')
        else:
            print('[+] | Resuming work.')
    elif language == '2':
        if paused:
            print('[-] | Jeda diaktifkan, tekan "q" untuk melanjutkan')
        else:
            print('[+] | Sedang berjalan.')

def print_not_found_message(language, window_name):
    if language == '1':
        print(f"[-] | Window - {window_name} not found!")
    elif language == '2':
        print(f"[-] | Halaman - {window_name} tidak ditemukan!")

def print_found_message(language, window_name):
    if language == '1':
        print(f"[+] | Window found - {window_name}\n[+] | Press 'q' to pause.")
    elif language == '2':
        print(f"[+] | Halaman ditemukan - {window_name}\n[+] | Tekan 'q' untuk menjeda proses.")

def print_stop_message(language):
    if language == '1':
        print('[!] | Program stopped.')
    elif language == '2':
        print('[!] | Program dihentikkan.')

print("Select language / Pilih Bahasa: (1: English, 2: Indonesia)")
language = input().strip()

if language not in ['1', '2']:
    language = '1'  # Default to English if invalid input

print_welcome(language)

window_name = input('\nEnter 1 to select the window / Tekan 1 untuk memilih halaman window: ')

if window_name == '1':
    window_name = "TelegramDesktop"

check = gw.getWindowsWithTitle(window_name)
if not check:
    print_not_found_message(language, window_name)
else:
    print_found_message(language, window_name)

telegram_window = check[0]
paused = False

# Color ranges for green bacteria and bombs
green_bacteria_range = ((102, 200, 0), (220, 255, 125))  # Specify the range for green bacteria more accurately
bomb_range = ((50, 50, 50), (200, 200, 200))  # Approximate range for bombs

while True:
    if keyboard.is_pressed('q'):
        paused = not paused
        print_pause_message(language, paused)
        time.sleep(0.2)

    if paused:
        continue

    window_rect = (
        telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
    )

    if telegram_window != []:
        try:
            telegram_window.activate()
        except:
            telegram_window.minimize()
            telegram_window.restore()

    scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

    width, height = scrn.size
    pixel_found = False
    if pixel_found == True:
        break

    for x in range(0, width, 20):
        for y in range(0, height, 20):
            r, g, b = scrn.getpixel((x, y))

            # Check for green bacteria
            if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                screen_x = window_rect[0] + x
                screen_y = window_rect[1] + y

                # Additional check to avoid clicking on bombs
                # Check a small area around the pixel to ensure it's not a bomb
                is_bomb = False
                try:
                    for bx in range(-5, 6):
                        for by in range(-5, 6):
                            br, bg, bb = scrn.getpixel((x + bx, y + by))
                            if bomb_range[0][0] <= br <= bomb_range[1][0] and bomb_range[0][1] <= bg <= bomb_range[1][1] and bomb_range[0][2] <= bb <= bomb_range[1][2]:
                                is_bomb = True
                                break
                        if is_bomb:
                            break
                except:
                    continue

                if not is_bomb:
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)
                    pixel_found = True
                    break

print_stop_message(language)
