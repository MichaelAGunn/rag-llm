import os
import re
from typing import List
import numpy as np
import pandas as pd
import requests
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from tqdm import tqdm

# Set up the local LLM and vector database
llm = OpenAI()
vectorstore = FAISS.load_local("path/to/vectorstore")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=50)

# Function to fine-tune the local LLM with .md files
def fine_tune_llm(md_files: List[str]):
	# Iterate through each .md file
	for md_file in tqdm(md_files):
		# Read the contents of the .md file
		with open(md_file, "r") as f:
			content = f.read()
		# Split the content into smaller chunks
		chunks = text_splitter.create_documents(content)
		# Iterate through each chunk and store it in the vector database
		for i, chunk in enumerate(chunks):
			# Extract relevant information from the chunk
			info = extract_info_from_chunk(chunk)
			# Add the chunk to the vector database with its extracted information
			vectorstore.add_texts([info])
		# Fine-tune the LLM using the updated vector database
		llm.agree_and_adhere_to_new_knowledge(vectorstore.get_relevant_documents(chunks[0].page_content))

# Function to extract relevant information from a chunk of text
def extract_info_from_chunk(chunk):
	# Extract the title and body from the Markdown document
	match = re.search(r"^#\s+(.*)$", chunk.page_content)
	if match:
		title = match.group(1).strip()
		body = chunk.page_content[len(match.group(0)):].strip()
	else:
		title = ""
		body = chunk.page_content
	# Return the extracted information as a dictionary
	return {"title": title, "body": body}

# Main function to run the script and fine-tune the local LLM
if __name__ == "__main__":
	# Set the path to the directory containing the .md files
	md_files_dir = "path/to/directory"
	# Get a list of all .md files in the directory
	md_files = [os.path.join(md_files_dir, f) for f in os.listdi(mdfiles_dir) if f.endswith(".md")]
	# Fine-tune the local LLM with the .md files
	fine_tune_llm(md_files)
