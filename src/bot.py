from typing import List, Any
from src.bot_state import BotState
from langchain.chat_models.openai import _convert_message_to_dict, _convert_dict_to_message
from src.agents.main_agent import MainAgent
import logging
from langchain.schema import HumanMessage, SystemMessage, FunctionMessage, AIMessage
from langchain.callbacks import get_openai_callback

logging.basicConfig(level=logging.INFO,
                    format='::::::%(levelname)s:::::: %(message)s')

class Bot:
    def __init__(self, state: BotState = None):
        if state is None:
            self.state = BotState()
        else:
            self.state = state
        self.agents = [
            MainAgent(self.state),
        ]
        self.state.agent_names = [agent.name for agent in self.agents]

    def _ask(self, user_input: str):
        # Clear the products list to return
        self.state.products_list = []

        # Continue running a loop until the agent returns an answer.
        self.state.last_human_input = user_input
        while True:
            response = self.agents[self.state.current_agent_index].ask()
            self.state.save_to_file()
            if response is not None:
                return response
    
    # Wrapper for checking the cost of the request.
    def ask(self, user_input: str):
        with get_openai_callback() as cb:
            response = self._ask(user_input)
            logging.info(f'Total cost: {cb.total_cost}')
            logging.info(f'Total tokens: {cb.total_tokens}')
            logging.info(f'Total requests: {cb.successful_requests}')
        return response
