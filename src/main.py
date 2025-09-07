from trader import Trader
from strategies import simple_strategy
from logger import TradeLogger

def run_bot():
    logger = TradeLogger("trades.log")
    trader = Trader(strategy=simple_strategy, logger=logger)
    trader.run()

if __name__ == "__main__":
    run_bot()
