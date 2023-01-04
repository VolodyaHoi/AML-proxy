#//////////////////////////////////////#
#/             AML proxy              /#
#/      Author: VolodyaHoi (At0m)     /#
#/	   Team: Atomic Threat Team       /#
#//////////////////////////////////////#

# P.S: Code is rather crutch, but i think it will not cause any
# special problems woth understanding x)

from colorama import Fore, Back, Style
import os
import requests
from bs4 import BeautifulSoup
import time

link = "https://free-proxy-list.net/" # free proxies source link

def main(): # main
    gd = get_data(get_html(link))

def get_html(link): # request
    response = requests.get(link)
    return response.text

def get_data(html): # get proxies

    startCommand = "empty" # values for menu and errors
    saveProxiesInTextFile = "empty"
    countOfNeedyProxy = 0
    outputProxies = "empty"
    restartApp = "empty"
    lil_bool = False
    big_bool = False

    os.system('cls' if os.name == 'nt' else 'clear') # intro
    print(Fore.GREEN + '''╭━━━┳━╮╭━┳╮			  
┃╭━╮┃┃╰╯┃┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
┃┃╱┃┃╭╮╭╮┃┃╱╱╭━━┳━┳━━┳╮╭┳╮╱╭╮
┃╰━╯┃┃┃┃┃┃┃╱╭┫╭╮┃╭┫╭╮┣╋╋┫┃╱┃┃
┃╭━╮┃┃┃┃┃┃╰━╯┃╰╯┃┃┃╰╯┣╋╋┫╰━╯┃
╰╯╱╰┻╯╰╯╰┻━━━┫╭━┻╯╰━━┻╯╰┻━╮╭╯
╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╭━╯┃ 
╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯╱╱╱╱╱╱╱╱╱╰━━╯
╱╱ ''' + Fore.YELLOW + "Dev:" + Fore.MAGENTA + " VolodyaHoi (At0m) " + Fore.GREEN + "╱╱╱")
    print("╱" + Fore.YELLOW + " Team:" + Fore.MAGENTA + " Atomic Threat " + Fore.GREEN + "╱╱╱╱╱╱" + Style.RESET_ALL)
    print("")

    while startCommand != "start": # start procces
        startCommand = input(Fore.CYAN + "[" + Fore.GREEN + "!" + Fore.CYAN + "]" + Style.RESET_ALL + " For start program enter <start> >>> ")

    print(Fore.CYAN + "[" + Fore.YELLOW + "+" + Fore.CYAN + "]" + Style.RESET_ALL + " Custom settings...\n") # set configuration

    while saveProxiesInTextFile != "Y" and saveProxiesInTextFile != "N": # save in text file proxy
        saveProxiesInTextFile = input(Fore.CYAN + "[" + Fore.GREEN + "!" + Fore.CYAN + "]" + Style.RESET_ALL + " You want save valid proxies in proxies.txt? Y/N >>> ")

    while big_bool != True: # input proxy`s count (fix if input string or wrong numbers)
        try:
            countOfNeedyProxy = int(input(Fore.CYAN + "[" + Fore.GREEN + "!" + Fore.CYAN + "]" + Style.RESET_ALL + " Enter count of needy proxies(1-300) >>> "))
            if countOfNeedyProxy >= 1 and countOfNeedyProxy <= 300:
                big_bool = True
            else:
                big_bool = False
        except:
            while lil_bool != True:
                try:
                    countOfNeedyProxy = int(input(Fore.CYAN + "[" + Fore.GREEN + "!" + Fore.CYAN + "]" + Style.RESET_ALL + " Enter count of needy proxies(1-300) >>> "))
                    if countOfNeedyProxy < 1 and countOfNeedyProxy > 300:
                        countOfNeedyProxy = int(input(Fore.CYAN + "[" + Fore.GREEN + "!" + Fore.CYAN + "]" + Style.RESET_ALL + " Enter count of needy proxies(1-300) >>> "))
                        lil_bool = False
                    else:
                        lil_bool = True
                except:
                    lil_bool = False

    # update status
    print(Fore.CYAN + "[" + Fore.YELLOW + "+" + Fore.CYAN + "]" + Style.RESET_ALL + " Getting proxies from free-proxy-list.net...\n")

    # starting main app`s function x)

    # values for get proxies
    ip = []
    host = []
    count = 0
    ip_i = 0
    host_i = 0
    global proxies
    proxies = []
    soup = BeautifulSoup(html,'lxml')
    trs = soup.find('div', class_=('table-responsive fpl-list')).find('table').find_all('tr')
    valid_proxies = []
    countOfValidProxy = 0
    countOfUnvalidProxy = 0
    valid = False

    # starting parsing 
    
    for tr in trs:
        position = tr.find_all('td')
        for i in position:
            positions = i.text.replace('\n','')
            if count == 0:
                ip.append(positions) 
                ip_i += 1
            elif count == 1:
                host.append(positions)
                host_i += 1
            else:
                count = 0
                break;     

            count += 1   
            
    countOfAllProxy = ip_i # max proxies from link

    for k in range(0, countOfAllProxy): # add all proxies in array
        proxies.append(ip[k] + ":" + host[k])

    # update status
    print(Fore.CYAN + "[" + Fore.YELLOW + "+" + Fore.CYAN + "]" + Style.RESET_ALL + " Checking proxies on valid...\n")

    # check proxies on valid
    for u in range(0, countOfNeedyProxy):
        session = requests.Session()
        proxy = proxies[u]
        session.proxies = {"http": proxy, "https": proxy}

        try: # valid proxy 
            sg = session.get("http://icanhazip.com", timeout=1.5)
            valid = True
        except Exception as e: # unvalid proxies
            countOfUnvalidProxy += 1
            valid = False
            continue
        
        if valid == True: # add valid proxy in array
            valid_proxies.append(str(proxy))
            countOfValidProxy += 1

    if saveProxiesInTextFile == "Y": # write valid proxies in text file (proxies.txt)
        print(Fore.CYAN + "[" + Fore.YELLOW + "+" + Fore.CYAN + "]" + Style.RESET_ALL + " Saving valid proxies in proxies.txt...\n")
        textFile = open("proxies.txt", "w")
        for v in range(0, countOfValidProxy):
            textFile.write(str(valid_proxies[v] + "\n"))
        textFile.close()

    # results
    print(Fore.CYAN + "[" + Fore.YELLOW + "+" + Fore.CYAN + "]" + Style.RESET_ALL + " Find: " + str(countOfValidProxy) + " Valid proxies | " + str(countOfUnvalidProxy) + " Unvalid proxies\n")

    # output valid proxies in app
    while outputProxies != "see":
        outputProxies = input(Fore.CYAN + "[" + Fore.GREEN + "!" + Fore.CYAN + "]" + Style.RESET_ALL + " For output valid proxies enter <see> >>> ")

    # example
    print(Fore.CYAN + "[" + Fore.YELLOW + "output" + Fore.CYAN + "]" + Style.RESET_ALL + " valid proxies: [n] ip:host\n")

    # output
    for l in range(0, countOfValidProxy):
        print(Fore.CYAN + "[" + Fore.MAGENTA + str(l + 1) + Fore.CYAN + "] " + Style.RESET_ALL + valid_proxies[l])

    # finish program
    while restartApp != "res":
        restartApp = input(Fore.CYAN + "[" + Fore.GREEN + "!" + Fore.CYAN + "]" + Style.RESET_ALL + " For restart programm enter <res> >>> ")

    #restart
    print(Fore.RED + "[!]" + Style.RESET_ALL + " Restart (3 seconds..) " + Fore.RED +"[!]")
    time.sleep(3)
    main()

if __name__=='__main__': # starting
    main()

