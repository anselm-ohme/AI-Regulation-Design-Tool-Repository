import openai
import pandas as pd

# Load the CSV file
csv_file = "AI Policy Repository outlined by OECD as of May 2025.csv"
data = pd.read_csv(csv_file)

# Set up OpenAI API key
openai.api_key = "your_openai_api_key_here"

def search_policy(question):
    """
    Searches the CSV file for relevant information based on the question.
    """
    # Combine all rows into a single text block for context
    context = "\n".join(data.apply(lambda row: " | ".join(row.astype(str)), axis=1))
    
    # Use OpenAI's API to answer the question
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"The following is a repository of AI policies:\n\n{context}\n\nQuestion: {question}\nAnswer:",
        max_tokens=200,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to the AI Regulation Q&A Tool!")
    print("Ask any question about AI regulations based on the OECD repository.")
    print("Type 'exit' to quit.")
    
    while True:
        question = input("\nYour question: ")
        if question.lower() == "exit":
            print("Goodbye!")
            break
        
        try:
            answer = search_policy(question)
            print(f"\nAnswer: {answer}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
