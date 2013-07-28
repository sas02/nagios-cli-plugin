#!/usr/bin/env python

import plivo

#dummy account id for Api Testing
auth_id = "MAMGZKNTNHY2M3ZJFKYZ"
auth_token = "MjVhNjBmODUwNWU5ZDc1MjdhN2M1YTcyMjU4ZWNl"

p = plivo.RestAPI(auth_id, auth_token)

# Get account
response = p.get_account()

print response[0]



# Modify Account
params = {
        'name': 'santoshsas',
        'city': 'Bangalore',
        'address':'Bangalore-22'
        }
response = p.modify_account(params)

print response[0]

 
