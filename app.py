'''
Based on the tutorial here: https://www.youtube.com/watch?v=tcqEUSNCn8I
Designed to use any set of markdown files as a data source for RAG.
'''
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
import os

DATA_PATH = os.environ.get('DATA_SOURCE')

def load_documents(path):
	loader = DirectoryLoader(path, glob='*.md')
	documents = loader.load()
	return documents

text_splitter = RecursiveCharacterTextSplitter(
	chunk_size = 1000,
	chunk_overlap = 500,
	length_function = len,
	add_start_index = True
)

documents = load_documents(DATA_PATH)
chunks = text_splitter.split_documents(documents)

print(chunks)