# Refectored get_range_for_difficulty logic into logic_utils.py using Copilot Agent mode
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100

# Refectored parse_guess logic into logic_utils.py using Copilot Agent mode
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except (TypeError, ValueError):
        return False, None, "That is not a number."

    return True, value, None

# Refectored check_guess logic into logic_utils.py using Copilot Agent mode
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    try:
        guess_value = int(guess)
        secret_value = int(secret)
    except (TypeError, ValueError):
        guess_value = str(guess)
        secret_value = str(secret)

    if guess_value == secret_value:
        return "Win", "🎉 Correct!"

    if guess_value > secret_value:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"

# Refectored update_score logic into logic_utils.py using Copilot Agent mode
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
