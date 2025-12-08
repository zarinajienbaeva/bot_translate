import os
import dotenv

dotenv.load_dotenv()

token = os.getenv("TOKEN")
my_id=int(os.getenv("MY_ID"))