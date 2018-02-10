import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

choice = input ('\n\Hi! Choose the practice you want, enter it\'s number and press Enter\n\
\n\
1 - \"Gentle Morning Practice\"\n\
\n\
2 - \"Yoga To Start Your Day!\"\n\
\n\
3 - \"Energizing Morning Sequence\"\n\
\n\
4 - \"Yoga For Lower Back Pain\"\n\
\n\
5 - \"5-Minute Morning Yoga\"\n\
\n\
6 - \"Yoga To Get The Juices Flowing!\"\n\
\n\
7 - \"Bedtime Yoga Sequence!\"\n\
\n\
8 - \"Yoga Rinse\"\n\
')

def chrome(x):
    #open Chrome
    driver = webdriver.Chrome()
    #go to the chosen URL
    driver.get(x)
    #find the player element by ID
    element = driver.find_element_by_id("player")
    #use ActionChains to press F11(full screen) and then click the player to start playing
    actions = ActionChains(driver)
    actions.send_keys(Keys.F11)
    actions.click(element)
    #initiate actions
    actions.perform()
    #sleep, because otherwise the function breaks and closes the browser
    time.sleep(2000)

if choice =="1":
    chrome('https://www.youtube.com/embed/Is8tMCpv4F8')

elif choice =="2":
    chrome('https://youtube.com/embed/Is8tMCpv4F8')

elif choice =="3":
    chrome('https://www.youtube.com/embed/K-Ina_WW4Yc')

elif choice =="4":
    chrome('https://youtube.com/embed/XeXz8fIZDCE?t=54')

elif choice =="5":
    chrome('https://www.youtube.com/embed/4C-gxOE0j7s')

elif choice =="6":
    chrome('https://www.youtube.com/embed/JOilkvadChg')

elif choice =="7":
    chrome('https://www.youtube.com/embed/XOTGz-1vizY')

elif choice == "8":
    chrome('https://www.youtube.com/embed/3NtNAQodk8E?t=34s')

    # FURTHER PLAN:

    #fix video links
    #Chrome is being controlled by an automated software - remove this notification
    #is it possible to fastforward the player to where I need videos to start?
    #is time.sleep() really the best option to continue running the browser?
    #close tab/window after video finishes. is it possible to use isodate or pafy to find the exact video time??
    #write some tests