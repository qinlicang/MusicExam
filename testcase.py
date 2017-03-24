import string,re


if __name__ == '__main__':
    r = r'^paper(\d{1,4})[/]?'
    if re.match(r,"paper27"):
        print('done')
        
    if re.match(r,"paper27/"):
        print('done')    

    if re.match(r,"paper271"):
        print('done') 
           
    print('defeat')