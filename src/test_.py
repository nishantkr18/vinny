from src.bot_state import BotState
from src.bot import Bot
from langchain.schema import HumanMessage, SystemMessage, FunctionMessage, AIMessage
from src.bot_state import AgentMemory
import dotenv, os
dotenv.load_dotenv()

def test_conv_save():
    state = BotState()
    state.conv_hist['demo_agent'] = AgentMemory()
    
    state.conv_hist['demo_agent'].append(SystemMessage(content='Hello'))
    state.conv_hist['demo_agent'].append(HumanMessage(content='Hi'))

    state.conv_hist['demo_agent2'] = AgentMemory()
    state.conv_hist['demo_agent2'].append(AIMessage(content='test2'))

    state.save_to_file('conv_test.json')

def test_conv_load():
    state = BotState()
    state.load_from_file('conv_test.json')
    assert len(state.conv_hist) == 2
    assert len(state.conv_hist['demo_agent']) == 2
    assert len(state.conv_hist['demo_agent2']) == 1
    assert state.conv_hist['demo_agent'][0].content == 'Hello'
    assert state.conv_hist['demo_agent'][1].content == 'Hi'
    assert state.conv_hist['demo_agent2'][0].content == 'test2'


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

def test_initial_conv():
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    file_path = 'convs/conv_hist_test.json'
    if os.path.exists(file_path):
        os.remove(file_path)
    print("File deleted successfully.")
    state = BotState(username='test')
    bot = Bot(state=state)

    bot.ask("Hello")
    
