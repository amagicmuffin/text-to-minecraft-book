import pyautogui
from time import sleep

# set up file
file = open("bookWritingTextDocument.txt", "r")

fileText = file.read()

file.close()

# buffer time
sleep(2)
print('doing things')

# loop through text file
count = 0
page = ""

for letter in fileText:
    page += letter
    count += 1
    
    # when page full, copypaste page and reset page
    if count % 264 == 0:
        print('page is: ' + page + '\n')
        pyautogui.typewrite(page)
        # TODO: using pagedown would be better. why tf does it not work
        # pyautogui.press("pagedown")
        pyautogui.click()
        page = ""

print('last page is: ' + page)
pyautogui.typewrite(page)    

sleep(2)




print('program done')

#266 chars per book

