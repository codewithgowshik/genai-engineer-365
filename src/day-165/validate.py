import json

file_path = "train.jsonl"

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

required_fields = {"instruction", "input", "output"}

for line_number, line in enumerate(lines, start=1):
    try:
        record = json.loads(line)

        if not required_fields.issubset(record.keys()):
            raise ValueError("Missing required fields")

        print(f"Line {line_number}: Valid")

    except (json.JSONDecodeError, ValueError) as error:
        print(f"Line {line_number}: Invalid - {error}")

print(f"\nTotal examples: {len(lines)}")