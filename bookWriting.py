# imports
import pyautogui
from time import sleep

# notFiveWideCharacters variable
from specialCharacters import *

# set up file
file = open("bookWritingTextDocument.txt", "r")

fileText = file.read()

file.close()

# buffer time
sleep(2)
print("doing things")

# loop through text file
colPixelsCount = 0
rowCount = 0
page = ""

for letter in fileText:
    if letter in notFiveWideCharacters:
        colPixelsCount += notFiveWideCharacters[letter]
    else:
        colPixelsCount += 5
    # add one pixel to end of each letter
    colPixelsCount += 1

    # is the math right? nobody knows
    if colPixelsCount > (56 * 2):  # 57 i's can fit on a page. *2 because of math
        rowCount += 1
        colPixelsCount = 0

    page += letter

    # when page full, copypaste page and reset page
    if rowCount == 12:
        print("page is: " + page + "\n")
        pyautogui.typewrite(page)
        pyautogui.click()

        rowCount = 0
        page = ""


print("last page is: " + page)
pyautogui.typewrite(page)

sleep(2)


print("program done")

# 57 i's fit on a column
# 14 rows fit on a page
