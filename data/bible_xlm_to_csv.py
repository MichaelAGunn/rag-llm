from xml.etree import ElementTree as ET
import pandas as pd
import os

def bible_xml2csv(lang, trans, out_path=''):
	'''
	Converts XML file of the Bible into a CSV file.
	Designed to work with: https://github.com/gratis-bible/bible
	'''
	bible_path = os.environ.get('BIBLES')
	out_file = lang + '_' + trans + '.csv'
	data = []
	file_path = os.path.join(bible_path, lang, trans + '.xml')
	tree = ET.parse(file_path)
	root = tree.getroot()
	for child in root.iter():
		if child.tag.endswith('verse'):
			code, text = child.attrib['osisID'], child.text
			book, chapter, verse = code.split('.')
			data.append([lang, trans, book, chapter, verse, text])
	df = pd.DataFrame(data=data, columns=['language', 'translation', 'book', 'chapter', 'verse', 'text'])
	df.to_csv(os.path.join(out_path, out_file), encoding='utf-8')

def bible_interlin2csv():
	'''
	Converts csv file of interlinear Bible to preferred format.
	Designed to work with: https://github.com/ivandustin/bible
	'''
	bible_path = os.environ.get('BIBLE_INTERLINEAR')
	out_file = 'interlinear.csv'
	file_path = os.path.join(bible_path, 'data')
	data = []
	for root, dirs, files in os.walk(file_path):
		for file in files:
			file_path = os.path.join(root, file)
			df = pd.read_csv(file_path)
			break
			# TO DO: get this part working!

if __name__ == '__main__':
	#bible_xml2csv('en', 'kjv')
	bible_interlin2csv()
