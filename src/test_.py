from src.bot_state import BotState
from langchain.schema import HumanMessage, SystemMessage, FunctionMessage, AIMessage
from src.bot_state import AgentMemory

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

def test_memory():
    conv_hist = AgentMemory(k=4)
    conv_hist.append(SystemMessage(content="system message"))
    assert len(conv_hist) == 1
    conv_hist.append(HumanMessage(content="test 1"))
    assert len(conv_hist) == 2
    conv_hist.append(HumanMessage(content="test 2"))
    assert len(conv_hist) == 3
    conv_hist.append(HumanMessage(content="test 3"))
    assert len(conv_hist) == 4
    conv_hist.append(HumanMessage(content="test 4"))
    assert len(conv_hist) == 4

    assert conv_hist[0].content == "system message"
    assert conv_hist[3].content == "test 4"
    assert conv_hist[2].content == "test 3"
    assert conv_hist[1].content == "test 2"