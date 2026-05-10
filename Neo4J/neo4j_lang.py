# import os
from typing import Annotated, TypedDict

# from langchain_neo4j import Neo4jGraph
from langchain_neo4j.checkpoint import Neo4jSaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages

# 1. Setup Neo4j Connection
DB_URI = "bolt://localhost:7687"
DB_USER = "neo4j"
DB_PASS = "bloodyroots"


# 2. Define State
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    tenant_id: str


# 3. Define a simple ReAct Node
def call_model(state: AgentState):
    # This ensures a NEW message is added to the state
    return {"messages": [("assistant", "I am session 2 and I am now active!")]}


# 4. Build the Graph with Persistence
builder = StateGraph(AgentState)
builder.add_node("agent", call_model)
builder.add_edge(START, "agent")
builder.add_edge("agent", END)

# Use Neo4j as the Checkpointer (Memory)
with Neo4jSaver.from_conn_string(uri=DB_URI, user=DB_USER, password=DB_PASS) as checkpointer:
    # Run once to setup indexes for persistence
    checkpointer.setup()

    app = builder.compile(checkpointer=checkpointer)

    # 5. Test the Execution
    config = {"configurable": {"thread_id": 'session-2'}}
    input_data = {
        "messages": [("user", "Who is the CEO of Acme Corp?")],
        "tenant_id": "tenant-001"
    }

    print("--- Starting Agent ---")
    for event in app.stream(input_data, config):
        for value in event.values():
            print("Assistant:", value["messages"][-1])
