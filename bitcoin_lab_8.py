"""Write a test for your Bitcoin program (from the API topic) that converts a number of Bitcoin to their value in US Dollars.
Structure your program so you don't need to mock user input. 
Structure your program so it's possible to isolate and then mock the API call. 
Mock the API call by providing a mock JSON response. Assert that your program calculates the correct value in dollars."""
import requests
from pprint import pprint#not needed in this new version

url = 'https://claraj.github.io/mock-bitcoin/currentprice.json'#set as global variable.

print()

def main():
    data = bitcoin_api_call()#api_call to get the json data
    # pprint(data)#for testing
    print(data)
    bitcoins = get_user_bitcoin_amount()#ask user for their # of bitcoins. Avoiding mocking user input directly, by mocking this funtion?
    bitcoin_value = usd_exchange_rate(data)#send the json data, and parse out the exchange rate
    conversion_calculation = bitcoins_usd_conversion(bitcoins, bitcoin_value)#calculate dollars using input and exchange rate
    print_user_info(bitcoin_value, conversion_calculation)#display the exchange rate and their assets to the user

def bitcoin_api_call():
    reponse = requests.get(url).json()#I think this needs the .json() here?
    return reponse

def get_user_bitcoin_amount():#inputting number of bitcoins
    while True:#while True loop to force user to input an answer, also, I think it stops the return of None?
        try:
            how_much_bitcoin = float(input('How many bitcoins do you have? '))#convertng input into float because bitcoins don;t have to be owned in whole
            if how_much_bitcoin >= 0:#ensure user cannot enter negative numbers
                return how_much_bitcoin
            else:
                print('Must be a greater than zero.')
        except:
            print('Must be numeric.')#strings cannot be converted to floats, so this will print
    
def usd_exchange_rate(data):
    exchange_rate = data['bpi']['USD']['rate_float']#pull out the float rate from the json
    return exchange_rate

def bitcoins_usd_conversion(bitcoins, bitcoin_value):
    calculation = bitcoins * bitcoin_value
    return calculation

def print_user_info(exchange_rate, usd_conversion_calculation):
    print()
    print(f'The current exchange rate is ${exchange_rate} for every 1 bitcoin.')
    print(f'You have ${usd_conversion_calculation} in bitcoins.')

if __name__ == '__main__':
    main()#needed to run