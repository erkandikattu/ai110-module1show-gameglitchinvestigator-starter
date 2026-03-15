# Pytest tests for game logic functions in logic_utils.py

# Added imports for new_game fix test using Copilot Agent mode
import ast
from pathlib import Path

# Updated imports for testing logic_utils functions using Copilot Agent mode
from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50) #Updated to use check_guess from logic_utils.py using Copilot Agent mode
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50) #Updated to use check_guess from logic_utils.py using Copilot Agent mode
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50) #Updated to use check_guess from logic_utils.py using Copilot Agent mode
    assert result == "Too Low"

# Test that the range for "Hard" difficulty is greater than "Normal" difficulty using get_range_for_difficulty from logic_utils.py
# Test generated using Copilot Agent mode
def test_difficulty_ranges_hard_is_greater_than_normal():
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")

    assert (easy_low, easy_high) == (1, 20)
    assert (normal_low, normal_high) == (1, 50)
    assert (hard_low, hard_high) == (1, 100)
    assert hard_high > normal_high

# Test that starting a new game resets the "status" in session state to "playing" in app.py
# Test generated using Copilot Agent mode
def test_new_game_resets_playing_state_in_app_source():
    app_path = Path(__file__).resolve().parents[1] / "app.py"
    source = app_path.read_text(encoding="utf-8")
    tree = ast.parse(source)

    new_game_if = None
    for node in ast.walk(tree):
        if isinstance(node, ast.If) and isinstance(node.test, ast.Name) and node.test.id == "new_game":
            new_game_if = node
            break

    assert new_game_if is not None, "Expected an if new_game block in app.py"

    assigned_keys = {}
    for stmt in new_game_if.body:
        if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1:
            target = stmt.targets[0]

            if (
                isinstance(target, ast.Attribute)
                and isinstance(target.value, ast.Attribute)
                and isinstance(target.value.value, ast.Name)
                and target.value.value.id == "st"
                and target.value.attr == "session_state"
            ):
                assigned_keys[target.attr] = stmt.value

    assert "status" in assigned_keys, "New game must reset status"
    assert isinstance(assigned_keys["status"], ast.Constant)
    assert assigned_keys["status"].value == "playing"

    for key in ["attempts", "score", "history", "secret"]:
        assert key in assigned_keys, f"New game should reset '{key}'"

    secret_value = assigned_keys["secret"]
    assert isinstance(secret_value, ast.Call)
    assert isinstance(secret_value.func, ast.Attribute)
    assert isinstance(secret_value.func.value, ast.Name)
    assert secret_value.func.value.id == "random"
    assert secret_value.func.attr == "randint"
    assert len(secret_value.args) == 2
    assert isinstance(secret_value.args[0], ast.Name)
    assert isinstance(secret_value.args[1], ast.Name)
    assert secret_value.args[0].id == "low"
    assert secret_value.args[1].id == "high"
