"""
Given a list of dictionaries of events, both positive and negative,
return a minimal list of dictionaries of the actual changes that occurred.

That is to say some events will cancel out, and we only want the final results.
Events can cancel out if they match in both the product and location.

Events are of the form:
    events = [
        {"location": 1, "product": 1, "quantity": +1},
        {"location": 1, "product": 1, "quantity": -1},
        {"location": 1, "product": 1, "quantity": +1},
        {"location": 1, "product": 2, "quantity": +1},
    ]

The result should be in the same format as the input,
but with the minimal number of events needed to describe the changes:
    result = [
        {"location": 1, "product": 1, "quantity": +1},
        {"location": 1, "product": 2, "quantity": +1},
    ]
"""

def simplify(events):
    # TODO: Implement
    return []

# TODO: Test cases
