CrisisComm is a natural language processing model for post-disaster aid acquisition. Please make sure you have referred to the requirements.txt file on this respository to download the respective components. Download the data folder too as it has all the context for the LLM to operate on.
Make sure to host ollama as a server by using the command "ollama serve" in the terminal. Then, make sure to run mistral on ollama using "ollama pull mistral" in the terminal. These are important steps before you run a query through app.py

**UPDATE** Please make sure to create a virtual environment in your IDE before you try to use the LLM, otherwise the langchain imports will not work.
