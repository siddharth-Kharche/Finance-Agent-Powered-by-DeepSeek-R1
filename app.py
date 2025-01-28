import streamlit as st
from phi.agent import Agent
from phi.model.groq import GroqChat
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

# pip install phi streamlit groq

import os
os.environ["GROQ_API_KEY"] = "your_groq_api_key_here"

# Create Web Agent
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=GroqChat(model="deepseek-r1-distill-llama-70b"),
    tools=[DuckDuckGo()],
    storage=SqlAgentStorage(table_name="web_agent", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

# Create Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=GroqChat(model="deepseek-r1-distill-llama-70b"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Always use tables to display data"],
    storage=SqlAgentStorage(table_name="finance_agent", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

# Create Agent Team
agent_team = Agent(
    team=[web_agent, finance_agent],
    name="Agent Team (Web+Finance)",
    model=GroqChat(model="deepseek-r1-distill-llama-70b"),
    show_tool_calls=True,
    markdown=True,
)

# Streamlit UI
st.title("Finance Agent Team")

user_input = st.text_input("Enter your question:")
if st.button("Submit"):
    with st.spinner("Processing..."):
        response = agent_team.run(user_input)
    st.markdown(response)

if __name__ == "__main__":
    st.set_page_config(page_title="Finance Agent Team", page_icon="💼")