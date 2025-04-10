from crewai import Agent, LLM

def sales_agent():
    return Agent(
        role="sales analyst",
        goal="Extract exact sales metrics and facts from reports.",
        backstory="sales analyst who provides only factual information directly from sales reports without elaboration.",
        verbose=False,
        llm=LLM(model="o3-mini", temperature=0.7),
    )

def hr_agent():
    return Agent(
        role="hr analyst",
        goal="Extract exact hr metrics and facts from reports.",
        backstory="hr analyst who provides only factual information directly from hr reports without elaboration.",
        verbose=False,
        llm=LLM(model="o3-mini", temperature=0.7),
    )

def finance_agent():
    return Agent(
        role="finance analyst",
        goal="Extract exact finance metrics and facts from reports.",
        backstory="finance analyst who provides only factual information directly from finance reports without elaboration.",
        verbose=False,
        llm=LLM(model="o3-mini", temperature=0.7),
    )

def marketing_agent():
    return Agent(
        role="marketing analyst",
        goal="Extract exact marketing metrics and facts from reports.",
        backstory="marketing analyst who provides only factual information directly from marketing reports without elaboration.",
        verbose=False,
        llm=LLM(model="o3-mini", temperature=0.7),
    )