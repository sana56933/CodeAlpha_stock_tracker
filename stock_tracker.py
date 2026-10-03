stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please choose from the available stocks.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print("Stock price:", stock_prices[stock])
    print("Investment for", stock, ":", investment)

print("\n===== Portfolio Summary =====")
print("Total investment value: $", total_investment)

save = input("Do you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-----------------------\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("Portfolio saved to portfolio.txt")
else:
    print("Portfolio was not saved.")

print("Thank you for using the Stock Portfolio Tracker!")