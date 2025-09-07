class TradeLogger:
    def __init__(self, filename):
        self.filename = filename

    def log(self, action, price, amount):
        with open(self.filename, "a") as f:
            f.write(f"{action} {amount:.4f} coins @ ${price:.4f}\n")
        print(f"{action} {amount:.4f} coins @ ${price:.4f}")
