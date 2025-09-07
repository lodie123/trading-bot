import time
import requests

class Trader:
    def __init__(self, strategy, logger):
        self.strategy = strategy
        self.logger = logger
        self.coins = 0
        self.usd = 1000
        self.price_history = []

    def get_price(self):
        try:
            url = "https://api.dexscreener.com/latest/dex/tokens/ethereum"
            response = requests.get(url)
            data = response.json()
            return float(data["pairs"][0]["priceUsd"])
        except Exception:
            return None

    def run(self):
        while True:
            price = self.get_price()
            if price:
                self.price_history.append(price)
                decision = self.strategy(self.price_history)

                if decision == "BUY" and self.usd > 0:
                    self.coins = self.usd / price
                    self.logger.log("BUY", price, self.coins)
                    self.usd = 0

                elif decision == "SELL" and self.coins > 0:
                    self.usd = self.coins * price
                    self.logger.log("SELL", price, self.coins)
                    self.coins = 0

            time.sleep(10)  # elke 10 sec updaten
