"""
要求：

这个agent框架应该以一种api的形式给到别人去调用，

各部分分模块去写，方便后续的维护和扩展。



"""

from abc import ABC, abstractmethod
from typing import Optional
import openai

class LLMModel(ABC):
    def __init__(self):
        pass


class OpenAIModel(LLMModel):
    def __init__(self, model_name: str, api_key: str,  base_url: Optional[str] = None):
        super().__init__()
        self.model_name = model_name
        self.messages = []
        if base_url is None:
            openai.base_url = base_url
        openai.api_key = api_key

    def call(self, prompt: Optional[str] = None):
        if prompt is not None:
            self.messages.append({"role": "user", "content": prompt})
        response = openai.chat.completions.create(
            model=self.model_name,
            messages=self.messages,
            max_tokens=100
        )
        self.messages.append({"role": "assistant", "content": response.choices[0].message.content})
        return response.choices[0].message.content

    def set_system_prompt(self, system_prompt: str):
        if self.system_prompt is None:
            self.messages.append({"role": "system", "content": system_prompt})
        else:
            for message in self.messages:
                if message["role"] == "system":
                    self.messages.remove(message)
                    break  # 只删除第一条系统提示，然后退出循环
            self.messages.append({"role": "system", "content": system_prompt})
        self.system_prompt = system_prompt

    def set_task_prompt(self, task_prompt: str):
        self.task_prompt = task_prompt
        self.messages.append({"role": "user", "content": task_prompt})

"""
不同于llmmodel的messages，这个是持久化保存聊天历史到本地
"""
class ChatMemory(ABC):
    def __init__(self, ):
        pass
class BaseTool(ABC):
    def __init__(self, tool_name: str, description: str):
        self.tool = {
            "name": tool_name,
            "description": description,
            "function": self.body
        }
    
    @abstractmethod
    def body(self, args: dict):
        pass

    def call(self, **kwargs):
        return self.tool["function"](kwargs)

class ChatMessage(ABC):
    pass

class CriticAgent(ABC):
    pass

class Agent:
    def __init__(self, model: LLMModel, memory: ChatMemory, system_prompt: str, tools: list[BaseTool], ):
        self.model = model
        self.memory = memory
        self.system_prompt = system_prompt
        self.tools = tools

    def step(self) -> ChatMessage:
        self.model.call()

    def reset(self):
        pass

    def run(self):
        pass
        

    def call_tool(self, tool_name: str, args: dict):
        pass

    def final_result(self):
        pass

    def save(self, path: str):
        pass

    def load_memory(self, memory_id: str):
        pass

    def get_chat_hitory(self):
        pass





