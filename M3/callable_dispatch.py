# Strategy - Callable Dispatch
# The problem it solves: A long if/elif chain where each branch does the same kind of operation but differently,
# by the value of a single discriminating variable.
# 
# The mechanism: A dictionary maps discriminating values to callable functions (the "strategies").
# The evaluation machinery is a single dictionary lookup followed by a call.
# 
# Before: if/elif chain
# def processpayment(method, amount, currency):
#     if method == "stripe":
#         return stripe_api.charge(amount, currency)
#     elif method == "paypal":
#         return paypal_api.execute(amount, currency)
#     elif method == "bank_transfer":
#         return bank_api.initiate_transfer(amount, currency)
#     elif method == "crypto":
#         return crypto_api.send(amount, currency)
#     else:
#         raise ValueError(f"Unknown payment method: {method}")
# 
# After: Strategy pattern via callable dispatch
def stripe_strategy(amount, currency):
    return stripe_api.charge(amount, currency)

def paypal_strategy(amount, currency):
    return paypal_api.execute(amount, currency)

def bank_transfer_strategy(amount, currency):
    return bank_api.initiate_transfer(amount, currency)

def crypto_strategy(amount, currency):
    return crypto_api.send(amount, currency)


PAYMENT_STRATEGIES = {
    "stripe":        stripe_strategy,
    "paypal":        paypal_strategy,
    "bank_transfer": bank_transfer_strategy,
    "crypto":        crypto_strategy,
}

def process_payment(method, amount, currency):
    strategy = PAYMENT_STRATEGIES.get(method)
    if strategy is None:
        raise ValueError(f"Unknown payment method: {method}")
    return strategy(amount, currency)