import csv

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135,
}


def get_quantity(stock_name):
    while True:
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity < 0:
                print("Quantity cannot be negative. Try again.")
                continue
            return quantity
        except ValueError:
            print("Please enter a valid whole number.")


def save_as_txt(portfolio, total_value):

    with open("portfolio_result.txt", "w") as file:

        file.write("\n******** STOCK PORTFOLIO REPORT ********\n\n")
        file.write("=" * 45 + "\n")

        for stock, details in portfolio.items():

            file.write(
                f"{stock}: {details['quantity']} shares x "
                f"${details['price']} = ${details['value']}\n"
            )

        file.write("=" * 45 + "\n")
        file.write(f"Total Investment Value: ${total_value}\n")
        file.write("=" * 45 + "\n")

def save_as_csv(portfolio, total_value): 
    
    with open("portfolio_result.csv", "w", newline="") as file: 
        
        writer = csv.writer(file) 
        writer.writerow(["Stock", "Quantity", "Price", "Investment Value"]) 
        
        for stock, details in portfolio.items(): writer.writerow( [stock, details["quantity"], details["price"], details["value"]] ) 
        
        writer.writerow([]) 
        writer.writerow(["Total Investment Value", "", "", total_value])


def main():
    portfolio = {}
    total_value = 0

    print("\nAvailable stocks:\n", ",\n ".join(STOCK_PRICES.keys()))
    stock_count = int(input("\nHow many different stocks do you want to add? "))

    for _ in range(stock_count):
        stock_name = input("\nEnter stock symbol: ").upper()

        if stock_name not in STOCK_PRICES:
            print(f"{stock_name} is not available in the price list.")
            continue

        quantity = get_quantity(stock_name)
        price = STOCK_PRICES[stock_name]
        investment_value = quantity * price

        portfolio[stock_name] = {
            "quantity": quantity,
            "price": price,
            "value": investment_value,
        }

        total_value += investment_value

    print("\n******** STOCK PORTFOLIO REPORT ********\n")
    print("="*45)
    print("\n")

    for stock, details in portfolio.items():
        print(
            f"{stock}: {details['quantity']} shares x "
            f"${details['price']} = ${details['value']}"
        )

    print("\n")
    print("=" * 45)
    print(f"Total Investment Value: ${total_value}")
    print("=" * 45)

    save_choice = input("\nSave result? Enter txt, csv, or no: ").lower()

    if save_choice == "txt":
        save_as_txt(portfolio, total_value)
        print("Result saved to portfolio_result.txt")
    elif save_choice == "csv":
        save_as_csv(portfolio, total_value)
        print("Result saved to portfolio_result.csv")
    else:
        print("Result not saved.")


if __name__ == "__main__":
    main()





















    