import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill
from agentexecutor import CurrencyAgentExecutor

def main():
    skill = AgentSkill(
        id="currency_conversion",
        name="Currency Converter",
        description="Convert currencies from one to another.",
        tags=["currency", "conversion", "exchange"],
        examples=["Convert 100 USD to EUR", "What is the exchange rate from GBP to JPY?"],
    )

    agent_card = AgentCard(
        name="Currency Converter Agent",
        description="A specialized agent for currency conversion",
        url="http://localhost:9999/",
        defaultInputModes=["text"],
        defaultOutputModes=["text"],
        skills=[skill],
        version="1.0.0",
        capabilities=AgentCapabilities(),
    )

    request_handler = DefaultRequestHandler(
        agent_executor=CurrencyAgentExecutor(),
        task_store=InMemoryTaskStore(),
    )

    server = A2AStarletteApplication(
        http_handler=request_handler,
        agent_card=agent_card,
    )

    uvicorn.run(server.build(), host="0.0.0.0", port=9999)


if __name__ == "__main__":
    main()