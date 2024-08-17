CrisisComm is a natural language processing model for post-disaster aid acquisition. 

Prior to running the program, make sure Python, Virtual Studio Code (VSCode), and Ollama is downloaded onto your local machine. All of these can be downloaded by searching these on Google and clicking the first link that appears. After downloading these 3, follow the steps below to run our program:

1 - Download all files from the github repository to a local folder on your machine. For the purpose of this demonstration, suppose the folder is called "CrisisComm-LLM." Now open the "CrisisComm-LLM" folder in VSCode.

2 - Now, we must create and activate the virtual environment. Open a terminal in VSCode by cliking the "..." on the right side of the top left corner of the window, and by then clicking on "Terminal" and then "New Terminal". 
    2a - To create the virtual environment, type in "python -m venv .venv" for Windows or "python3 -m venv .venv" for Mac. A folder called ".venv" should pop up under the folder "__pycache__" in the VSCode file explorer if you successfully created the virtual environment.
    2b - To activate the virtual environment, type in "./.venv/Scripts/Activate" into the terminal. If you successfully activated it, then a green "(./venv)" should appear to the left of the file path that is shown in the terminal. 

3 - For our code to run successfully, we must install all the important python libraries. Run "pip install" (Windows) or "pip3 install" (Mac) on all the libraries listed in requirements.txt. For example, you would run "pip install pypdf langchain chromadb pytest boto3 streamlit langchain-community" in the VSCode terminal if you are on Windows (use pip3 instead of pip on Mac). Downloading will take some time, so be patient.

4 - Before running our code, we need to set up the LLM. This can be done by opening a terminal on your local machine, NOT in VSCode. So, this would be Powershell (on Windows) or Command Prompt (on Mac). Type in the following commands, which are the same across both Windows and Mac: 
    4a - "ollama pull llama3"
    4b - "ollama serve"
    4c - "ollama pull mxbai-embed-large"
    4d - "ollama pull mistral"
Now your server should be running. 

**NOTE** When inputting ollama serve, you may get an error stating a port in use. For example, it may look like the following: "Error: listen tcp 127.0.0.1:11434: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted." This is completely normal, and means your server is already running.

5 - The final step we must take to run the program is to click on "webapp.py." The python file should be open from doing this. Click on the play button in the top right corner of the VSCode Window, which should read "Run Python File" if you hover your cursor over it. Then, the VSCode terminal will show up, and you will get something similar to the following warning:

"Warning: to view this Streamlit app on a browser, run it with the following
command:

streamlit run c:/Users/name/OneDrive/Desktop/Projects/CrisisComm-LLM/webapp.py [ARGUMENTS]"

Copy the command that it shows you back into the terminal. So, in this context, you would copy and paste "streamlit run c:/Users/name/OneDrive/Desktop/Projects/CrisisComm-LLM/webapp.py" into the terminal and hit enter. This should open up a web app in your computer browser. Now, you can ask a question related to FEMA in the webapp! 

**NOTE** Responses may take upwards of 30 seconds to a minute to generate, as the LLM is using local resources (like your computer's operating system, cpu, etc.) rather than an online server.

Credits to the following YouTube Tutorials provided by IBM and pixiegami to provide a foundation for our project: (1) https://www.youtube.com/watch?v=XctooiH0moI and (2) https://youtu.be/2TJxpyO3ei4?si=wSAvS4ShQotpWoYO.

We plan to deploy this program to a web domain in the near future, so stay tuned.
