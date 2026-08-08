from src.prompts.extraction_prompt import build_extraction_prompt

def test_extraction_prompt_contains_document():

    document = "this is sustainability report"

    prompt = build_extraction_prompt(document)

    assert document in prompt 