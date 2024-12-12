# rag-llm
End-to-end large language model with retrievement augmentation, for free use.

## Project Plan
### Data Collection
The RAG components come from Bible repositories:
- Many public domain translations of Bibles: https://github.com/gratis-bible/bible
- Interlinear Bibles: https://github.com/ivandustin/bible
### Notebooks
The exploratory plan is presented in a jupyter notebook format for easy presentation.
- Cookie Cutter
- Start Learning
- DS MLE
- DS MLE saved to .csv
### Deployment
This model is first deployed to a local LLM. This requires LLM studio to be running with a viable endpoint, or an equivalent API.
### Marketing & UX
This project is meant to be viewable and consumable by anyone without the need for a commercial LLM subscription.
To Do:
- README refinement
- GitHub optimaization
- inline visualizations
## Installation Instructions
- Install Ollama from this website: https://ollama.com/download/windows
- Open Command Prompt and type `olamma pull llama3` to install the Llama3 model (or install minstral).
- confirm that Ollama is running by checking localhost:11434, which should say, "Ollama is running".
To Do:
- vector database
- fine tuning
- RAG setup
### Running Langchain through local Olamma model
Run the following code after running `pip install langchain-community` in your virtual environment:
`from langchain_community.llms import Ollama`
`llm = Ollama(model="llama3")`
`llm.invoke("Write a haiku.")`
I like to test it by writing a haiku because I know the output will be quick.
If this code works, then you have correctly setup Ollama on your local machine.
## Analyzing the Text Corpus
This project is meant to provide easy reference to Bible content and compare translations and languages.
## Loading the Corpus to Database
An LLM only understands language as a vector of integers representing word-tokens. Therefore, the human-readable text corpus must be translated into vectors. For user convenience, these vectors are stored in a vector database as a flat file.
## Querying the LLM
It's finally time to enjoy the fruits of your labour! Your LLM is able to retrieve information from your text corpus.
