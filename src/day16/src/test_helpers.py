from helper import clean_prompt

def test_clean_prompt():
    assert clean_prompt("  hello  ") == "hello"
