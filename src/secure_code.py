import os

def enforce_least_privilege():
    if hasattr(os, "geteuid") and os.geteuid() == 0:
        print("Error: Root execution is not permitted.")
        return False
    return True


def process_transaction():
    print("Secure Financial Gateway")

    if not enforce_least_privilege():
        return

    try:
        expression = input("Enter transaction amount: ")
        amount = float(expression)

        if not (0 < amount <= 1000000):
            raise ValueError

        print("Transaction Amount:", amount)

    except (ValueError, EOFError):
        print("Error: Invalid transaction request.")


if __name__ == "__main__":
    process_transaction()