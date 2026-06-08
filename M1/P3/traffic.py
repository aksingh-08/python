ALLOWED_STATES = {"Green", "Yellow", "Red"}

def is_valid_transition(current, next_state):
    transitions = {
        "Green": "Yellow", 
        "Yellow": "Red",
        "Red": "Green"
    }
    return transitions.get(current) == next_state
    # if current == "Green" and next_state == "Yellow":
    #     return True
    # if current == "Yellow" and next_state == "Red":
    #     return True
    # if current  == "Red" and next_state == "Green":
    #     return True
    # return False

def validate_sequence(sequence):
    for state in sequence:
        if state not in ALLOWED_STATES:
            return False
            
    for i in range(len(sequence) - 1):
        if not is_valid_transition(sequence[i], sequence[i + 1]):
            return False
    return True

sequence = ["Green", "Yellow", "Red", "Green"]
print(validate_sequence(sequence))