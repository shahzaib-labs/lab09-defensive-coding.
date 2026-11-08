
def process_transaction():
    print("Secure Financial Gateway")
    
    # Accept user input
    expression = input("Enter transaction amount: ")

    # Vulnerability: eval() executes arbitrary Python expressions
    try:
        amount = eval(expression)
        print("Transaction Amount:", amount)

    except Exception:
        print("Transaction processing failed.")


if __name__ == "__main__":
    process_transaction()
