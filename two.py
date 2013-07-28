#!/usr/bin/env python
import os,sys
# one.py : Api testing for Account validation 
return_response_code=os.popen("\\./one.py").readlines()


# checks whether the list is empty or not , returns boolean value
def check_elemnt():
    if return_response_code:
        return True
    else:
        return False 
# Takes response code and Flags the rigth system code 
def code_checker(code):
    
    if code == 200:
        print "OK  request has been executed"
        if not check_elemnt():
             sys.exit(0)

    elif code == 201:
        print "OK  resource created "
        if not check_elemnt():
            sys.exit(0)

    elif code == 202:
        print "OK  resource changed "
        if not check_elemnt():
            sys.exit(0)

    elif code == 204:
        print "BAD  resource deleted "
        if not check_elemnt():
            sys.exit(1)

    elif code == 400:
        print "BAD a parameter is missing or is invalid "
        if not check_elemnt():
            sys.exit(1)

    elif code == 401:
        print "BAD  authentication failed"
        if not check_elemnt():
            sys.exit(2)

    elif code == 404:
        print "BAD  Resource Cannot be found "
        if not check_elemnt():
            sys.exit(2)

    elif code == 405:
        print "BAD  http method not allowed "
        if not check_elemnt():
            sys.exit(2)

    elif code == 500:
        print "BAD  Server Error"
        if not check_elemnt():
            sys.exit(2)

    else :
        print "Unkown Have A look ! "
        sys.exit(3)

#driving Code
def main():
    while return_response_code:
        code = return_response_code.pop(0).strip('\n')
        code = int(code)
        code_checker(code)


if __name__ == '__main__':
    main()




