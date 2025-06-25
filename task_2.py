# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 310,
    "AMZN": 125
}

# Dictionary to store user portfolio
portfolio = {}

# Input: number of stocks
num_stocks = int(input("📈 How many different stocks do you want to enter? "))

for _ in range(num_stocks):
    stock = input("\nEnter stock symbol (e.g., AAPL): ").upper()
    if stock not in stock_prices:
        print("❌ This stock is not available in our database.")
        continue
    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = quantity

# Calculate total investment
total_value = 0
print("\n💼 Your Stock Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"- {stock}: {quantity} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Optional: Save to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    filename = "portfolio_summary.txt"
    with open(filename, "w") as file:
        file.write("Your Stock Portfolio:\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"- {stock}: {quantity} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print(f"✅ Portfolio saved to {filename}")
