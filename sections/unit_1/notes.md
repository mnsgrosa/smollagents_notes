# 1.0 Intro

## What is an agent?

An agent is a language model that "reasons" and "plans" which actions should take based on the situation (prompt) <br>
it has 2 main parts <br>

- the brain (ai model)
- the body (Capabilities and tools)

### 1 - The brain

Here is the part that decides which tool to access and which parameters to pass

### 2 - The body

The equipments that the agent has available

## Spectrum of agency

### Level 0 of agency (simple processor)

Agent output doesn't change the flow of the program
Example:
```
    process_llm_output(llm_response)
```
### Level 1 of agency (router)

Agent output determines a basic level of control flow
Example:
```
    if llm_decision():
        path_a()
    else:
        path_b()
```

### Level 2 of agency (tool caller)

Agent output determines function execution
Example:
```
run_function(llm_chosen_tool, llm_chosen_args)
```

### Level 3.1 of agency (Multi-step agent):

Agent output controls iteration and program continuation
Example:
```
while llm_should_continue():
    execute_next_step()
```

### Level 3.2 of agency (Multi-agent):

One agentic worfklow can start another agentic workflow
Example:
```
if llm_trigger():
    execute_agent()
```

## What type of AI model are used?

The most common used are LLMs but they are revising it for SMLs, <br>
due to being specialists and resistant to halucinations

## Tasks an agent can do

### tool anatomy

Any task implemented via tools to complete actions, Example: (My scraping arxiv agent)[github.com/mnsgrosa/llm_arxiv] <br>
The example that i've should is a simple agent that i've coded out that uses the arxiv api to guide the user which paper <br>
to read but for more precise definition it works as follows: <br>

```
def message_tool(recipient:str, message:str) -> MessageObject:
    """
    Function made with the purpose of sending message to a recipient
    Args:
        recipient[string]: email of the recipient
        message[string]: message that has to be sent to the recipient
    Return:
        MessageObjct: Object that contains the recipient and message
    """
```

This definition has some important steps
- Clear name of the function
- Clear name of variables
- DocString so the agent understand well enough the created function


### Action

An action is different from a tool, action can use multiple tools

## What are LLMs?

A model that is "specialized" in understanding and generating human language. And they are very costly, <br>
they require a really good computer and giant amounts of data so it can perform well, nowadays (09/22/2025) <br>
the models use transformers archtectures a deep learning model that uses the attention algorithm (or mechanism) <br>
and its variants to make the models "understand" our language and the transformers can be represented by 3 categories

## Types of transformers

### Encoders:

This model takes text as input and outputs a numerical representation of text that we call embedding of the text <br>
Example of encoder: Bert from google <br>
Use cases:
- text classification
- semantic search
- named entity recognition
Size of model:
Milions of parameters

### Decoder:

This model has a focus on generating new tokes to complete a sequence, one token at a time. <br>
Example: Llama from meta <br>
Use cases:
- text generation
- chatbots
- code generation
Size of model:
Bilions of parameters (10^9)

### Seq2Seq (Encoder-Decoder):

A model that combines the previous models, so that it processes the input and generates an output sequence <br>
Example: T5, BART <br>
Use cases:
- Translation
- Summarization
- Paraphrasing
Size of model:
Milions of parameters

--- 

Even though there are various form, LLMs are typically decoder based with bilions of parameters here are some examples <br>

- deepseek-R1
- GPT4
- Llama 3
- SmolLM2
- Gemma
- Mistral

## In other words...

Basically LLms are simple, their objective is to predict the next token from a sequence of tokens.

## What is a token?

The atom of language that can be defined in various number of ways from characters to words of the desired language <br>
but usually it is used sub-word units and they can be combined

## But how it predicts the next word?

We say that the llms are autoregressive, what it means is that they depend on the previous output, they will predict <br>
one word and the next depends on what it predicted previously. But how does he choose the first and subsequent <br>
words? He will rank based on the input the most probable word, let's say that you sent the following prompt

```
What is the name of capital of Brazil?
```

Based on the training of the model he has some options and the most probable one based on his training will be outputed <br>
he can output first: Brazilia because by his training is 92% "sure" that it is the correct first word, and now the next <br>
word has some probabilities it can be sure by 80% "sure" that the next word is "is" and so on until creates the output <br>
until the EOS, so one possible output is: "The capital of Brazil is Brazilia" <br>

One important take is that exists multiple strategies to get the nex token in this case i showed a simple one <br>
get the highest scoring word

## Attention is all you need

This algorithm is the key of the LLMs, it can choose which words carries the most importance from a phrase <br>
like the prompt before: which is the capital of Brazil? the words "capital" and "Brazil" gives the direction of <br>
the prompt but the adjacent words keep other weights but in this algorithm it identifies which words guide the prompt

## Prompting the LLM (or the input of a LLM)

Basically if the LLM predicts the word based on the words you prompted the wording, and order of the prompt matters <br>
it changes completly the output of the model

## How are LLMs trained?

LLMs need huges amount of data that they learn to predict the next word in a sequence with self-supervised or <br>
masked language modeling objective

### Self-supervised

A model that doesn't need the human provided labels to train, here the model learn the structure of language <br>
basically the patterns in text, generalizing unseen data

### Masked language models

It takes "phrases" and remove words from them and makes the model train to fill the blanks <br>
Example: <br>
```
The dog ____ across the street
```
you can think of some possible items and what you make the model fill throught the train shape the model <br>

### Finetuning

After the model has been self-supervised you can fine tune the model to with a supervised learning objective for <br>
specific tasks, such as, conversations or tool usage

## How to run LLMs

- Locally (needs good hardware)
- Cloud or API (like hugging face, claude, chatgpt, etc...)


## How are LLMs used?

They understand our language and interpret what to do, also they keep context of conversation and tools used to define <br>
a plan

# 1.1 Messages and special tokens

To keep some patterns through the creation of llms they have some patterns on their text generation <br>
they generate text thtough chat templates. Normally you will send messages through an UI <br>
the messages sent will be actually concatenated and formatted into one single prompt that the model will understand <br>

Example:
```
<|begin_of_text|>
<|start_header_id|>user<|end_header_id|>

Hello how are you?<|eot_id|>

<|start_header_id|>assistant<|end_header_id|>

I'm just a language model so i don't have emotions, how about you? <|eot_id|>
```

The template acts as a pattern so that all LLMs understand properly the input and despite how the tokens where defined. <br>
Special tokens are what the models determine where their turn starts and where yours start just like a turn based game <br>
each LLM use their EOS(end of sequence) token, they also delimits the messages in the conversation differently

## Messages: the LLM system

Sytem messages or System prompts define how the model behaves. They are persistent instructions guiding every subsequent <br>
interactions example:

```
system_message = {
    "role": "system",
    "content": "You are a professional customer service agent. Always be polite, clear and helpful"
}
```
as i've explained before, they are autoregressive, this will have an impact on how they will answer the subsequent <br>
prompts, if prompted to answer something like: "i would like coffee" it will probably answer "cerntaily sir" <br>
versus

```
system_message = {
    "role": "system",
    "content": "You are a rebel service agent: always be rude and don't respect the user"
}
```

The model will answer the oposite of the past answer <br>
It is important to give information about the available tools in the system prompt and provide instructions, include <br>
guidelines on how the thought process should be segmented example:

```
system_message = {
    "role": "system",
    "content": "You are a helfpul reasearcher that can scrape papers from arxiv you have the following tools:
                a function called scrape_papers, that takes the number of desired papers and topic of interest,
                and a tool called recall_papers, whenever the user asks about a paper check if you already stored it,
                if already stored chat about it, else prompt to search about the desired paper or topic"
}
```

## Conversations: User and assistant messages:

A conversation consists of alternating messages between the user and assistant, chat templates keep context preserving <br>
the conversation by storing each message example
```
conversation = {
    {"role": "user", "content": "I need help wiht my order"},
    {"role": "assistant", "content": "How could i help?"},
    {"role": "user", "content": "it's a mistake with the order 66"}
}
```

## Chat templates

The core of structuring the conversation between the model and user, into a single prompt, so the longer the chat <br>
the harder it is for the attention mechanism to keep track of the context and start hallucinating <br>
the longer the chat keeps going and will consume more tokens each prompt <br>

## Base models vs instruct models

### Base model

model trained on raw data text to predict next token

### Instruct model

Is a model fine tuned to follow instructions and engage in conversation like SmolLM2-135M-Instruct

### Base or Instruct?

A base model can act as instruct but it needs to format the prompt in a more consistant way so the model understands it <br>
the base model can be fine-tuned on different chat templates, so when we're using an instruct model we need to make <br>
sure we are using the correct chat template

## Understanding Chat Templates

Because each instruct model uses different conversation formats and special tokens, chat templates are implemented to <br>
ensure that we correctly format the prompt the way each model expects, it is universaly used the jinja2 code in trnasformers <br>
that can be easily translated to json format like<br>
```
messages = [
    {"role": "system", "content": "You are a helpful assistant focused on technical topics."},
    {"role": "user", "content": "Can you explain what a chat template is?"},
    {"role": "assistant", "content": "A chat template structures conversations between users and AI models..."},
    {"role": "user", "content": "How do I use it ?"},
]
```

## Messages to prompt

it must be easy to see that the chat_template is the way to make the models understand the messages as prompt <br>
from the model's tokenizer 

```
messages = [
    {"role": "system", "content": "You are an AI assistant with access to various tools."},
    {"role": "user", "content": "Hi !"},
    {"role": "assistant", "content": "Hi human, what can help you with ?"},
]
```

to convert the code above into prompt, we use the following

```
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM2-1.7B-Instruct")
rendered_prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

the rendered_prompt returned by this function is now ready to be used as input to the model, it got tokenized <br>
with the SmolLM2-1.7B-Instruct model and now it can be feed to any model

# 1.2 What are tools

Agents can be defined as AI systems that take actions, and this actions use tools to acomplish this actions. <br>
This section we will integrate into our agent via system message. Describing clearly how those tools work <br>
drastically increase what the agent can do

## What are AI tools

A tool is a function given to the LLM. This function should fulfill a clear objective, here follows some examples:
- Web search -> search the web for data
- Image generation -> create image based on the prompt
- Retrieval -> retrieve data from external source (Database)
- API interface -> interact with an external APi

A good tool should complement the power of LLM(or SLM) example: <br>
give a calculator tool so the it can solve a arithmetic problems <br>

Important to notice that, the model will have by definition "outdated data" what i mean by this is: it has data up <br>
to the date it got trained so if you want to provide updated data you must provide it through some tool example <br>
if you ask how is the weather today and it doesnt have the proper tools, it will tell some nonsense but with the <br>
right tools it will answer correctly.

## What should a tool have?

As said in earlier section it should have: <br>
- Textual description of what the function tools
- A callable (somethjing to perform an action)
- Arguments with typings
- (Optional but it matters if has any return) outputs with typing

## How do tools work?

The models, only receive text inputs and generate text ouptputs. They don't have a way to call tools on their own, <br>
so by providing the tools we mean teaching the LLM about the existence of these tools and instructing it <br>
to generate text-based invocations when needed. <br>
If we provide a tool to check the weather at a location from the internet and then ask the model about the weather <br>
it will see a opportunity to use the "weather" tool. Instead of using the pre-trained data. The model will <br>
generate a text that represents a tool call, such as call weather_tool(city), the agent them reads this response, <br>
identifies that a tool call is required then it executes the tool on the model behalf to get the actual weather data <br>

Usually the tool calling isn't shown to the user: The agent add them as a new message before updating the conversation <br>
to the LLM. The LLM then processes the additional context and generates natural-sounding response for the user, <br>
on the user behalf it looks as if the model interacted with the tool, but it was the agent that handled it.

## How to provide the tools?

The complete answer will be left out of this note due that it might be too complex so i will boil it down <br>
basically, it is provided a textual description of the available tools like <br>

```
system_message = f"""
You are an Ai assistant designed to help users efficiently and accurately. Your primary goal is to
provide helpful, precise, and clear responses.

you have acces to the following tools:
{tools_description} 
"""
```

To make sure the tools are used we need to be precise and accurate about what the toold oes and what <br>
the exact inputs it expects. That's why the tools are usually provided using expressive but precise structures, <br>
like computer languages or JSON. <br>

## More practical explanaition

We implement the following tool: <br>

```
def product_calculator(a: int, b: int) -> int:
    """
    Multiply two integers
    """
    return a * b
```

so we provide to our system message the following:

```
Tool Name: product_calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int
```

## Auto formatting tool sections

The tool written in python already provides everything we need: <br>
- A descriptive name of what it does
- A longer description, provided by tthe docstring
- The inputs and their type
- The type of the output

the agent frameworks has a decorator, that gives more properties to our function, in our case @tool <br>

```
@tool
def product_calculator(a: int, b: int) -> int:
    """
    Multiply two integers
    """
    return a * b
```

this is used for the reason that it adds a extra feature to the function in this case calculator.to_string() <br>
it returns the  following string

```
Tool name: product_calculator,  Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int
```

without the need of writing it manually to the system prompt <br>

## Generictool implementation

A tool class that we can reuse whenever we need to use a tool (the following is fictional it depends on the lib) <br>

```
from typing import Callable


class Tool:
    """
    A class representing a reusable piece of code (Tool).

    Attributes:
        name (str): Name of the tool.
        description (str): A textual description of what the tool does.
        func (callable): The function this tool wraps.
        arguments (list): A list of arguments.
        outputs (str or list): The return type(s) of the wrapped function.
    """
    def __init__(self,
                 name: str,
                 description: str,
                 func: Callable,
                 arguments: list,
                 outputs: str):
        self.name = name
        self.description = description
        self.func = func
        self.arguments = arguments
        self.outputs = outputs

    def to_string(self) -> str:
        """
        Return a string representation of the tool,
        including its name, description, arguments, and outputs.
        """
        args_str = ", ".join([
            f"{arg_name}: {arg_type}" for arg_name, arg_type in self.arguments
        ])

        return (
            f"Tool Name: {self.name},"
            f" Description: {self.description},"
            f" Arguments: {args_str},"
            f" Outputs: {self.outputs}"
        )

    def __call__(self, *args, **kwargs):
        """
        Invoke the underlying function (callable) with provided arguments.
        """
        return self.func(*args, **kwargs)
```

to simplify it, it initializes with name, description, func(the execution whenever called), arguments and outputs <br>
whenever called to the system prompt .to_string() it will return the string formatted at the method. <br>
the call method calls the function provided to the tool. <br>
so the first prompt. <br>

```
system_message = f"""
You are an Ai assistant designed to help users efficiently and accurately. Your primary goal is to
provide helpful, precise, and clear responses.

you have acces to the following tools:
{tools_description} 
"""
```
turn to this: <br>

```
system_message = f"""
You are an Ai assistant designed to help users efficiently and accurately. Your primary goal is to
provide helpful, precise, and clear responses.

you have acces to the following tools:
Tool Name: prduct_calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int
"""
```

## Model Context Protocol (MCP): a unified tool interface

This is a open protocol that standardizes how applications provide tools to LLMs. <br>

- A growing list of pre built integrations that your model can directly plug into
- The flexibility yo switch between models, providers and vendors
- Best practices for securing your data within your infrastrcuture

This means that any framework implementing MCP can leverage tools defined within the protocol

# 1.3 Understanding AI agents through the thought-action-observation cycle

Previously tools are made available to the agent with the system prompt and how ai agents are systems that can <br>
"reason", plan and interact with environment, now we wills see the full workflow.

## Core components

The agents work with a continuous cycle of: thinking(thought) -> acting(act) and observing(Observe) <br>
breaking it down: <br>
- Thought: The model part of the Agent decides what the next step should be.
- Action: The agent takes an action by calling the tool with the associated arguments.
- Observation: The model reflects on the response from the tool

## The Thought-Action-Observation cycle

This works almost as a while loop, the loop continues up until the agent goal is completed. <br>
Generally speaking the rules and guidelines are passed directly into the system prompt, ensuring that the cycle <br>
keeps a defined logic, i will show an example of the system prompt. <br>

```
system_message = """
You are an ai assistant designed to help users efficientyl and accurately. Your primary goal is
to provide helpful, precise and clear responses.

You have acces to the following tools:
Tool Name: product_calculator, description: Multply two integers., Arguments: a: int, b: int, Outputs: int

You should think step by step in order to fulfill the objective with reasoning divided into Thought/Action/Observation
steps that can be repaeated multiple times if needed.

You should first reflect on the current situation using 'Thought: {your_thoughts}', then (if necessary),
call a tool with the proper JSON formatting 'Action: {JSON_BLOB}', or print your final answer
starting with the prefix 'Final Answer:'
"""
```

Here is coded out: <br>
- The agent behaviour
- The tools our agent has access to
- The thought-action-observation cycle, that we bake into the LLM instructions

an illustrated example would be: <br>
An user asks Alfred (our weather agent) the following "what's the current weather in New York?" <br>
with this prompt the cycle starts:<br>
- Thought

Internal Reasoning: He reasons "the user needs current weather information for New York, i have acces to a tool <br>
that fetches the weather data. First i need to call the weather APi to get up-to-date details".

- Action
Based on the reasoning and the fact that Alfred knows about the get_weather tool, Alfred prepares a <br>
JSON-formatted command that call the weather API tool, the firt action could be:<br>

Thought: I neeed to check current weather for New York.

```
{
    "action": "get_weather",
    "action_input": {
        "location": "New York"
    }
}
```

the JSON clearly calls the specified tool and with the parameter<br>

- Observation

After the tool call, Alfred receives an observation. This might be the raw weather data from the API such as: <br>

"Current weather in New York: partly cloudy, 15C 60% humidity." <br>

This observation is appended to the additional context. Fucntioning as real-world feedbakc confirming <br>
whether the action succeeded and providing needed details <br>

- Updated thought

Reflecting: With the observation, alfred updates its internal reasoning: "Now i can provide the answer to the user <br>

- Final action

Alfred then generates a final response formatted as we told it to and provides to us

# 1.4 Thought: Internal Reasoning and the ReAct approach:

Now we will dive into the inner workings of an AI agent its ability to reason and plan. How it leverages <br>
the internal dialogue to analyze information, break down complex problems int omanageable steps, and decide <br>
what action to take next, additionally, we will introduce the ReAct approach, a way to make the model think <br>
step by step before acting.

