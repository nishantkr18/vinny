from src.bot import Bot
from src.bot_state import BotState
import dotenv, os
dotenv.load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# Delete convs/conv_hist_test.json to reset the conversation history
file_path = 'convs/conv_hist_test.json'
if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully.")

def init():
    state = BotState(username='test')
    bot = Bot(state=state)
    for conv in state.get_conv_hist():
        print(conv)
init()
while True:
    state = BotState(username='test')
    bot = Bot(state=state)
    user_input = input('User Input:')
    print(bot.ask(user_input))