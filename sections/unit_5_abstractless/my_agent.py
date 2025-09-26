import ollama
import json
import httpx
import sqlite3
import os
from datetime import datetime

class OllamaAgent:
    def __init__(self, model_name: str = "deepseek-r1:1.5b", host: str = "http://localhost:11434"):
        self.model_name = model_name
        self.client = ollama.Ollama(model = model_name, host = host)
        self.conversation_history = []

        self.tools = {
            {
                "type": "function",
                "function": {
                    "name": "fetch_trending_papers_info",
                    "description": "Fetches the latest trending research papers cards with their info from huggingface.co/papers/trending from specific date",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "date": {
                                "type": "string",
                                "description": """The date the user wants to get trending papers from in YYYY-MM-DD format
                                                if no data is provided, don't pass any date parameter""",
                            }
                        }
                    }
                }
            }
        }

        self.papers = []

    def fetch_trending_papers_info(self, date: str = None):
        """
        Funcao responsavel por pegar as informacoes basicas dos papers
        """
        if date:
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            url = f"https://huggingface.co/papers/date/{date}"
        else:
            url = "https://huggingface.co/papers/trending"

        with httpx.Client() as client:
            response = client.get(url)
            response.raise_for_status()
            papers = response.json()
        self.papers.extend(papers)
        return self.papers

    def chat(self, user_message: str) -> str:
        """
        Funcao de chat principal
        """

        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        try:
            response = self.client.chat(
                model = self.model_name,
                messages = self.conversation_history,
                tools = self.tools
            )

            message = response['message']

            if message.get('tool_calls'):
                for tool_call in message['tool_calls']:
                    function_name = tool_call['function']['name']
                    function_args = tool_call['function']['arguments']

                    print(f"Chamando ferramenta: {function_name} com argumentos: {function_args}")

                    tool_result = self.execute_tool(function_name, function_args)

                    self.conversation_history.append({
                        "role": "assistant",
                        "content": "",
                        "tool_calls": [tool_call]
                    })

                    self.conversation_history.append({
                        "role": "tool",
                        "content": json.dumps(self.execute_tool(tool_result))
                
                final_response = self.client.chat(
                    model = self.model_name,
                    messages = self.conversation_history
                )

                final_message = final_response["message"]["content"]
                self.conversation_history.append({
                    "role": "assistant",
                    "content": final_message
                })

                return final_message
            else:
                assistant_message = message['content']
                self.conversation_history.append({
                    "role": "assistant",
                    "content": assistant_message
                })

                return assistant_message
        
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            print(f"❌ {error_msg}")
            return error_msg