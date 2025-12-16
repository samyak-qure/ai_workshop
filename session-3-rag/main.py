import sys
import os

# Add the parent directory to sys.path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import call_llm

def retrieve(query: str):
    knowledge_base = {
        "What is rag?": "RAG is a technique that allows you to use a large language model to answer questions about a specific topic.",
        "What is tokenization?": "Tokenization is the process of breaking down a text into smaller units called tokens.",
    }
    return knowledge_base.get(query, "No relevant documents found")

def augment(retrieved_documents: str, query: str):
    user_prompt = f"<context> augmented prompt: {retrieved_documents}</context> based on the above context, answer the following query: {query}"
    return user_prompt

def generate(user_prompt: str):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful RAG assistant. If you have no relevant documents, just say 'No relevant documents found' irrespective of the query."
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]
    return call_llm(messages)

def main():
    query = "What is rag"
    # 1. Retrieve the documents
    retrieved_documents = retrieve(query)
    # 2. Augment the prompt
    augmented_prompt = augment(retrieved_documents, query)
    # 3. Generate the response
    response = generate(augmented_prompt)
    print(response)

if __name__ == "__main__":
    main()