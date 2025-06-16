from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

import asyncio

from dotenv import load_dotenv

load_dotenv()


async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args": ["mathserver.py"], # this is the absolute path of the mcp server
                "transport":"stdio"
            },
            "weather" : {
                "url": "http://127.0.0.1:8000/mcp",
                "transport":"streamable_http"
            }
        }
    )
    import os

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()

    model = ChatGroq(model="qwen-qwq-32b")
    agent = create_react_agent(
        model=model,
        tools=tools
    )

    math_response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role" : "user",
                    "content": "What is (3 + 5) * 12 ?"
                }
            ]
        }
    )

    print(f'math response: \n {math_response["messages"][-1].content}')

    weather_response = await agent.ainvoke(
        {
            "messages":[
                {
                    "role" : "user",
                    "content" : "what is the weather in New Jersey?"
                }
            ]
        }
    )

    print(f'weather response: \n {weather_response["messages"][-1].content}')

asyncio.run(main())