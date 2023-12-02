from challenge2 import is_valid_game, get_required_cubes

def test_is_valid_game():
    game = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert is_valid_game(game) == True

def test_is_valid_game_too_many_red():
    game = "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    assert is_valid_game(game) == False

def test_is_valid_game_too_many_blue():
    game = "1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    assert is_valid_game(game) == False


def test_get_data():
    game_string = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert get_required_cubes(game_string) == {
        'red':4,
        'green':2,
        'blue':6,
    }