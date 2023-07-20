from src.bot_state import BotState
from langchain.schema import HumanMessage, SystemMessage, FunctionMessage, AIMessage


def test_conv_save():
    state = BotState()
    state.conv_hist = {
        'demo_agent': [SystemMessage(content='Hello'),
                       HumanMessage(content='Hi')],
        "demo_agent2": [
            AIMessage(content='Hello'),
            SystemMessage(content='How are you?')]
    }
    state.save_to_file('conv_test.json')

def test_conv_load():
    state = BotState()
    state.load_from_file('conv_test.json')
    assert state.conv_hist == {
        'demo_agent': [SystemMessage(content='Hello'),
                       HumanMessage(content='Hi')],
        "demo_agent2": [
            AIMessage(content='Hello'),
            SystemMessage(content='How are you?')]
    }

def test_proper_type_save_json():
    state = BotState()
    state.load_from_file('conv_test.json')
    