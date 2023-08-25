import favlinks 

site = int(input('choose your site by it\'s number \n 1- google  2- facebook  3- youtube\n '))

dec = {
    1:'www.google.com',
    2:'www.facebook.com',
    3:'www.youtube.com'
}

favlinks.firefox(dec[site])