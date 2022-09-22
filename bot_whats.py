from doctest import testfile
from multiprocessing.spawn import old_main_modules
from sre_constants import OP_LOCALE_IGNORE
import pyautogui as spam
import time

limite_msg = input("numero de repetições:")
msg = input("Mensagem:")

i = 0

time.sleep(2)

while i < int(limite_msg):
    spam.typewrite(msg)
    spam.press("Enter")

i += 1
