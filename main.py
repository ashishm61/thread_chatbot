import os
from dotenv import load_dotenv
from crewai import Crew
from agents import sales_agent, hr_agent, finance_agent, marketing_agent
from tasks import analysis_task
from tools import document_content

load_dotenv()   

DOCUMENT_TYPES = ["sales", "hr", "finance", "marketing"]

AGENT_MAP = {
    "sales": sales_agent,
    "hr": hr_agent,
    "finance": finance_agent,
    "marketing": marketing_agent
}

def analyze_document(question):
    for doc_type in DOCUMENT_TYPES:
        content = document_content(doc_type)
        if not content:
            continue    
            
        agent = AGENT_MAP[doc_type]()
            
        result = Crew(
            agents=[agent],
            tasks=[analysis_task(question, agent, content, doc_type)],
            verbose=False
        ).kickoff()
        
        if "INFO_NOT_FOUND" not in str(result):
            return result
    
    return "No relevant information found in any documents."

def main():
    while True:
        user_input = input("\nHi I am Thread. Ask me anything (or 'exit'): ")
        if user_input.lower() == 'exit':
            break
            
        result = analyze_document(user_input)
        print(f"\nAnswer: {result}\n")

main()
