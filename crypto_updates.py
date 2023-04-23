import requests
import datetime
import fear_and_greed

# Define the cryptocurrency symbols for which you want to get price updates
crypto_symbols = {"bitcoin":None, "ethereum":None, "solana":None}

results = []

def get_price_updates():

    # Loop through the cryptocurrency symbols and fetch price updates for each symbol
    for symbol in crypto_symbols:
        # Construct the API URL with the symbol, start date, and end date
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd&include_24hr_change=true"
        
        # Send GET request to CoinGecko API
        response = requests.get(url)

        
        # Check if the request was successful
        if response.status_code == 200:
            # Extract the price data from the response
            price_data = response.json()

            coin = list(price_data.keys())[0]
            price = price_data[coin]['usd']
            change = price_data[coin]['usd_24h_change']
            
            update = f"{coin} current price is {price} usd which is a {change} percent change from yesterday"

            results.append(update)
            # Loop through the price data and print the daily prices
            
        else:
            print(f"Failed to get price updates for {symbol}. Error: {response.status_code}")

    

    return results

def fear_greed():
    index = {
        'fear': """
        when the index is at extreme levels of fear,
        it may signal that the market is oversold and that prices may rebound, 
        presenting a potential buying opportunity.
        Also When the market sentiment is in extreme fear, it may lead some traders to panic and sell their positions
        """,
        'greed': """
        when the index is at extreme levels of greed, 
        it may signal that the market is overbought and that prices may decline, 
        presenting a potential selling opportunity.
        extreme greed may lead to irrational exuberance and overly optimistic trading decisions
        """
    }
    res = fear_and_greed.get()
    value = res.value
    desc = res.description
    advice = index[desc]

    situation = f"The current fear and index value is {value} making the market sentiment being {desc}. The best course of action is {advice}"

    return situation


fear_greed()