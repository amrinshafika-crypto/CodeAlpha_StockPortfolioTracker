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
        file.write("Stock Portfolio Result\n")
        file.write("----------------------\n")

        for stock, details in portfolio.items():
            file.write(
                f"{stock}: {details['quantity']} shares x "
                f"${details['price']} = ${details['value']}\n"
            )

        file.write(f"\nTotal Investment Value: ${total_value}\n")


def save_as_csv(portfolio, total_value):
    with open("portfolio_result.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Investment Value"])

        for stock, details in portfolio.items():
            writer.writerow(
                [stock, details["quantity"], details["price"], details["value"]]
            )

        writer.writerow([])
        writer.writerow(["Total Investment Value", "", "", total_value])


def main():
    portfolio = {}
    total_value = 0

    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))
    stock_count = int(input("How many different stocks do you want to add? "))

    for _ in range(stock_count):
        stock_name = input("Enter stock symbol: ").upper()

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

    print("\nStock Portfolio Summary")
    print("-----------------------")

    for stock, details in portfolio.items():
        print(
            f"{stock}: {details['quantity']} shares x "
            f"${details['price']} = ${details['value']}"
        )

    print(f"\nTotal Investment Value: ${total_value}")

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