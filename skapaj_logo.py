import sys 
from termcolor import colored, cprint

s = [" #####     ", " #    #  ", "  #", "#  #  ", " ####"]
k = ["#  #", "  # #", "        #", "     # #", "      #  #"]
a = ["           #", "           # # ", "            #   #", "         #######", "       #       #"]
p = ["           ####", "         #  #", "         ####", "        #", "       #"]
a2 = ["        #", "       # # ", "      #   #", "        ####### ", "       #       #"]
j = ["            #", "          #", "          #", "     #  #", "      ###\n"]

zoznam1 = [s[0] + k[0] + a[0] + p[0] + a2[0] + j[0]]
zoznam2 = [s[1] + k[1] + a[1] + p[1] + a2[1] + j[1]]
zoznam3 = [s[2] + k[2] + a[2] + p[2] + a2[2] + j[2]]
zoznam4 = [s[3] + k[3] + a[3] + p[3] + a2[3] + j[3]]
zoznam5 = [s[4] + k[4] + a[4] + p[4] + a2[4] + j[4]]
str1 = ''.join(zoznam1)
str2 = ''.join(zoznam2)
str3 = ''.join(zoznam3)
str4 = ''.join(zoznam4)
str5 = ''.join(zoznam5)

def skapaj_text():
    print(colored(str1, 'red'))
    print(colored(str2, 'green'))
    print(colored(str3, 'blue'))
    print(colored(str4, 'green'))
    print(colored(str5, 'red'))
skapaj_text()