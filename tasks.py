from crewai import Task

def analysis_task(question, agent, document_content, doc_type):
    return Task(
        description=(
            f"Analyze this {doc_type} report and answer: {question}\n\n"
            f"{doc_type} report: {document_content}\n\n"
            "IMPORTANT: Provide ONLY the exact information found in the document. "
            "Do not elaborate, analyze, or add any information not explicitly stated in the document. "
            "If the information is not in the document, respond with exactly 'INFO_NOT_FOUND'."
        ),
        expected_output="Brief factual answer using only information explicitly stated in the document.",
        agent=agent,
    )


# def sales_analysis_task(question, sales_agent, document_content):
#     return analysis_task(question, sales_agent, document_content, "sales")

# def hr_analysis_task(question, hr_agent, document_content):
#     return analysis_task(question, hr_agent, document_content, "hr")

# def finance_analysis_task(question, finance_agent, document_content):
#     return analysis_task(question, finance_agent, document_content, "finance")

# def marketing_analysis_task(question, marketing_agent, document_content):
#     return analysis_task(question, marketing_agent, document_content, "marketing")