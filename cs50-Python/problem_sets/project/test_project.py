from project import handle_states, get_state, case_two

def test_handle_states():
    assert handle_states("execute", [None,"w",1]) == "https://cs50.harvard.edu/x/2023/weeks/1"

def test_get_state():
    assert get_state([None]) == "menu"

def test_case_two():
    assert case_two("stat") == "stat"