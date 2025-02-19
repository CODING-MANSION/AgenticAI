from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
load_dotenv()

Web_Search_Agent= Agent(
    name='Web_Search_Agent',
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)


Finance_Agent= Agent(
    name="Finance_Agent",
    model=Groq( id = "llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True, company_info=True, analyst_recommendations=True,
                      company_news=True,technical_indicators=True,historical_prices=True)
    ],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)


multi_agent= Agent(
    team=[Web_Search_Agent, Finance_Agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Search web for the information", "use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# multi_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA",stream=True)