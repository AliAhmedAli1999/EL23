'''
I tried to make the script more generic by installing any extension 

I know there are some Bugs :D 
'''


from utilities import * 


appName = input("Enter the name of the extension you want to install in Vs code \n")

openVS()
search(appName)
install()






