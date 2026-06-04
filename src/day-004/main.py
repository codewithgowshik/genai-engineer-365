from dotenv import load_dotenv # this helps to find any .env file
import os # this helps to finnd the path from the operating system

load_dotenv()#used to read the values from the env (opening the notebook and read it )

name = os.getenv("MY_Name") #  used to get the perticular value 

print(name)
