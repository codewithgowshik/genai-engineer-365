from llm import llm

def main():
    question = input("Ask anything: ")
    print(llm(question))


# Run main() only when this file is executed directly.
# If another file imports this file, main() will NOT run automatically.
if __name__ == "__main__":
    main()
