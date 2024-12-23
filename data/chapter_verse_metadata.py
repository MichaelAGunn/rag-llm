'''
This script is for developing the chapter & verse reference for
split chunks of the documents. The function that I am developing
is get_citation().
'''
import pandas as pd
from uuid import uuid4
import json
import os


with open('en_kjv.json', 'r') as json_f:
	kjv_dict = json.load(json_f)
haggai_dict = {}
haggai_dict['Haggai'] = kjv_dict['Haggai'] # Testing on a small book with 2 chapters

kjv_df = pd.read_csv('en_kjv.csv')
book_metadata = pd.read_csv(os.path.join('metadata', 'books.csv'))

# This is the function that I am developing here.
def get_citation(text, df):
	'''
	Returns a dictionary with chapter and verse numbers included in the text.
	Only includes citations for complete verses, i.e. exclusive of edges.
	'''
	citation = {} # Key is chapter number; value is list of verse numbers
	for index, row in df.iterrows():
		if row['text'] in text.page_content:
			if row['chapter'] in citation.keys():
				citation[row['chapter']].append(row['verse'])
			else:
				citation[row['chapter']] = [row['verse']]
	return citation


# What follows this line is straight out of the MVP1 notebook (see notebooks dir).
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

local_llm = 'llama3'
token_size=500
dimensions=300

def document_verses(doc_dict):
    documents = []
    count = 0 # Count batches for sanity's sake.
    for doc_index, doc in enumerate(doc_dict):
        count += 1
        doc = Document(
            page_content=doc_dict[doc],
            metadata={
                'title': doc,
                'author': book_metadata.loc[book_metadata['book'] == doc]['author'].values[0],
                'book_index': doc_index
            },
            id=count
        )
        documents.append(doc)
    uuids = [str(uuid4()) for _ in range(len(documents))]
    return documents, uuids

kjv_docs, kjv_ids = document_verses(haggai_dict) #(kjv_dict)
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=token_size, chunk_overlap=100
)
split_docs = text_splitter.split_documents(kjv_docs)
print("Documents split.")

# Adding citation data here!
for split_doc in split_docs:
	#print("KJV_DF TITLE: {} | METADATA TITLE: {}".format(haggai_dict, split_doc.metadata['title']))
	abbreviation = book_metadata.loc[book_metadata['book'] == split_doc.metadata['title']]['abbreviation'].values[0]
	split_doc.metadata['citation'] = get_citation(split_doc, kjv_df[kjv_df['book']==abbreviation])
	#split_doc.metadata['citation'] = get_citation(split_doc, kjv_df[kjv_df['book']==split_doc.metadata['title']])
	#split_doc.metadata['citation'] = get_citation(split_doc, kjv_df[kjv_df['book']==book_metadata.loc[book_metadata['title'] == split_doc.metadata['title']]['abbreviation'].values[0]])
print(split_docs[1].page_content)
print(split_docs[1].metadata)

# book_metadata.loc[book_metadata['abbreviation'] == book]['author'].values[0]
# split_doc.metadata['citation'] = get_citation(split_doc, kjv_df[kjv_df['book']==book_metadata.loc[book_metadata['title'] == split_doc.metadata['title']]['abbreviation'].values[0]])