import requests

def main():

    print(requests.__version__)

    print(requests.get('http://google.com'))

    

main()