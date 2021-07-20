from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import stdiomask
from colorama import Fore, Back, Style, Cursor
from colorama import  init

print("""█───█─▄▀▀─█───▄▀▀─▄▀▀▄─█▄─▄█─▄▀▀
█───█─█───█───█───█──█─█▀▄▀█─█──
█───█─█▀▀─█───█───█──█─█─▀─█─█▀▀
█▄█▄█─█───█───█───█──█─█───█─█──
─▀─▀───▀▀──▀▀──▀▀──▀▀──▀───▀──▀▀""")

init(autoreset=True)

def read_creds():
    user = passw = ""
    with open("creds.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw

gmail_username ,gmail_password =  read_creds()

print()

print(Style.BRIGHT + "-"*30)
print(Fore.RED + Style.BRIGHT + "a) 8aonline2021-22")
print(Fore.BLUE + Style.BRIGHT + "b) 8bonline2021-22")
print(Fore.CYAN + Style.BRIGHT + "c) 8conline2021-22")
print(Fore.GREEN + Style.BRIGHT + "d) 8donline2021-22")
print(Fore.YELLOW + Style.BRIGHT + "e) 8eonline2021-22")
print(Style.BRIGHT + "-"*30)


print(Back.RED + Style.BRIGHT + 'If ClassCode is Not in The Above list Then press "Enter"')
DefaultClasses = str(input("Enter Class No.(eg: type in 'a' to join class 8 A): "))
Classcode = str(input("If you have a classcode that is not in the above list pls Enter it here: "))
options = ""

if DefaultClasses == "a" or DefaultClasses == "A":
    options = "8aonline2021-22"
    print(options)

elif DefaultClasses == "b" or DefaultClasses == "B":
    options = "8bonline2021-22"
    print(options)

elif DefaultClasses == "c" or DefaultClasses == "C":
    options = "8conline2021-22"
    print(options)

elif DefaultClasses == "d" or DefaultClasses == "D":
    options = "8donline2021-22"
    print(options)

elif DefaultClasses == "e" or DefaultClasses == "E":
    options = "8eonline2021-22"
    print(options)



#Loads chrome with default settings
opt=Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})

#Gives path to chrome webdriver and loads classroom webpage
driver=webdriver.Chrome(chrome_options=opt, executable_path='chromedriver.exe')
driver.get('https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&_ga=2.202657617.1548804968.1626754708-1234738350.1626754708&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

driver.find_element_by_id("identifierId").send_keys(gmail_username)
driver.find_element_by_id("identifierNext").click()
time.sleep(5)
driver.find_element_by_name("password").send_keys(gmail_password)
driver.find_element_by_id("passwordNext").click()

time.sleep(10)

driver.find_element_by_xpath('//*[@id="i3"]').send_keys(options or Classcode)

driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div/div[2]/button/span').click()


time.sleep(5)

#Turns off mic and camera and joins the meet
camera=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div')
camera.click()
mic=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div')

mic.click()

join=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span')
join.click()