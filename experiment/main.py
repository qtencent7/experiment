"""
要求：

这个agent框架应该以一种api的形式给到别人去调用，

各部分分模块去写，方便后续的维护和扩展。



"""

from abc import ABC, abstractmethod
class LLMModel(ABC):
    def __init__(self, ):
        pass

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

class Agent:
    def __init__(self, model: LLMModel, memory: ChatMemory, system_prompt: str, tools: list[BaseTool], ):
        self.model = model
        self.memory = memory
        self.system_prompt = system_prompt
        self.tools = tools

    def step(self, step: int, auto: bool = False):
        pass

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





