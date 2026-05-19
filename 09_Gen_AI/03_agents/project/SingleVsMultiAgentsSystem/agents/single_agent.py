from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

SINGLE_AGENT_SYSTEM = """You are a helpful AI.
Task: Provide a well-reasoned recommendation to the user question.
Rules:
- Make your best effort without browsing the web.
- Be structured: Summary, Pros, Cons, Recommendation, Risks, Confidence (0-100).
"""
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
def single_agent_answer(question: str) -> str:
    msgs = [
        SystemMessage(content=SINGLE_AGENT_SYSTEM),
        HumanMessage(content=question),
    ]
    return llm.invoke(msgs).content