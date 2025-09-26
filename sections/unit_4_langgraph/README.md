# Langgraph

## What is LangGraph?

A framework developed by langchain to manage the control flow of applications that integrate an LLM <br>

## Langchain != Langgraph?

Langchain is a standard interface to interact with models, the langchain classes might be used in langgraph <br>

## When and why should i learn langgraph?

Whenever you start to design a llm application you will face a trade off between control over the model <br>
or freedom so it gets more creative, and langgraph does exactly that, control, and smolagents give the other end. <br>
Langgraph gives the model a set of steps and flow, langgraph provides the flow to each action, if it is needed, <br>
a sequential agent langgraph is desired

## Key scenarios for langgraph

- Multistep reasoning processes that need explicit control on the flow 
- Applications requiring presistence of state between steps
- Systems that combine deterministic logic with ai capabilities
- Workflows that need human-in-the-loop intervations
- Complex agent archtectures with multiple components working together

## Main concepts

- Nodes -> Proecssing steps (calling an LLM, using a tool or make a decision)
- Edges -> Possible transitions between steps
- State -> User defined state that the model should go

## Building blocks 

An application starts from an entrypoint, and depending on the execution, the flow may go to one function <br>
or another until it reaches the end

### 1. State

Central concept in LangGraph. It represents all the information that flows through the application, it is user <br>
defined so it should be made really carefully with all data needed for decision-making. Basically what we need <br>
to keep track between each step

### 2. Nodes

Nodes are python functions, each node has the following properties:

- Take the state as input
- Performs some operation
- Return updates to the state

```
def node_1(state):
    print("---Node 1---")
    return {"graph_state": state['graph_state'] +" I am"}

def node_2(state):
    print("---Node 2---")
    return {"graph_state": state['graph_state'] +" happy!"}

def node_3(state):
    print("---Node 3---")
    return {"graph_state": state['graph_state'] +" sad!"}
```

Nodes can contain:

- LLM calls: Generate text or make decisions
- Tool calls: Interact with external systems
- Conditional Logic: Determine next steps
- Human intervation: Get input from user

### 3. Edges

Edges connect nodes and define the possible path through the graph:

```
import random
from typing import Literal

def decide_mood(state) -> Literal["node_2", "node_3"]:
    
    # Often, we will use state to decide on the next node to visit
    user_input = state['graph_state'] 
    
    # Here, let's just do a 50 / 50 split between nodes 2, 3
    if random.random() < 0.5:

        # 50% of the time, we return Node 2
        return "node_2"
    
    # 50% of the time, we return Node 3
    return "node_3"
```

edges have two types direct goes from a to b and conditional, choose the next based on current state <br>

### 4. StateGraph

Container with entire agent workflow

from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END

# Build graph
builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

# Logic
builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_mood)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

# Add
graph = builder.compile()