### Machete ###
#This program reads in a docx or txt file, splits the text into sentences and outputs a CSV with a descending list of sentences by length.
#Dr Tom Wallace
#08/03/2019

################################# Import packages #################################
import docx
import csv
import PySimpleGUI as sg
import statistics
################################# Main program #################################

#GUI
layout = [[sg.Text('Please select your document and output folder...')],    
	[sg.Text('Select document:', size=(13, 1)), sg.InputText(), sg.FileBrowse(file_types=(('Docx files', '*.docx'),('Text files','*.txt')))],      
	[sg.Text('Output folder:', size=(13, 1)), sg.InputText('.'), sg.FolderBrowse()],
	[sg.Text('Minimum sentence size: ', size=(18, 1)), sg.InputText('4', size=(4,1))],      
	[sg.Submit(button_text='Generate', size=(10, 1)), sg.Cancel(size=(10, 1))],
	[sg.Text('T. Wallace, v1.0.', size=(60, 1), justification='right')]]    

window = sg.Window('Machete').Layout(layout)  

event, values = window.Read()  
window.Close()

source_filename = values[0]
output_path = values[1]
sentence_size = values[2]

#Program
try:
	if event=='Generate' and source_filename!='':
		docpath = source_filename

		def getDocx(filename):
				doc = docx.Document(filename)
				fullText = []
				for para in doc.paragraphs:
					fullText.append(para.text)
				return (fullText)

		def getTxt(filename):
			txtfile=open(filename,'r')
			fulltext = txtfile.read()
			txtfile.close()
			fulltext_list = fulltext.split('\n')
			return(fulltext_list)

		if source_filename.endswith('.docx'):
			text = getDocx(docpath)
		elif source_filename.endswith('.txt'):
			text = getTxt(docpath)
		else:
			print('Error. Incorrect document type')

		splitlist=[]
		for string in text:
			string = string.replace('!', '.')
			string = string.replace('?', '.')
			splitstring = string.split('. ')
			splitlist.append(splitstring)

		flat_list = [item for sublist in splitlist for item in sublist]
		flat_list = [x for x in flat_list if x]
		flat_list = [x for x in flat_list if len(x.strip()) > 0]

		lengthlist=[]
		for sentence in flat_list:
			lenght=len(sentence.split())
			lengthlist.append(lenght)

		sentence_size = int(sentence_size)

		export_data = [(a, b) for a, b in zip(lengthlist, flat_list) if a >=sentence_size]
		export_data = sorted(export_data, key=lambda x: x[0], reverse=True)
	 
		lengthlist = [a for a in lengthlist if a >= sentence_size]
		total = sum(lengthlist)
		count = len(lengthlist)
		ave = total/count
		med = statistics.median(lengthlist)
		sd = statistics.stdev(lengthlist)
		var = statistics.variance(lengthlist)

		count_str = 'Sentences processed: ' + str(count) + '\n'
		ave_str = 'Mean sentence length: ' + str(ave) + '\n'
		med_str = 'Median sentence length: ' + str(med) + '\n'
		sd_str = 'Standard deviation: ' + str(sd) + '\n'
		sentence_size_str = 'Minimum sentence size: ' + str(sentence_size) + '\n'

		statspath = output_path + '/Machete_statistics.txt'

		with open(statspath, 'w') as f:
			f.write('Statistics')
			f.write('\n\n')
			f.write(count_str)
			f.write(sentence_size_str)
			f.write(ave_str)
			f.write(med_str)
			f.write(sd_str)
			f.write('\n')
			f.write('---\n')
			f.write('Machete version 1.0. Written by Tom Wallace - tomwallace1990@gmail.com')
		f.close()
		
		output = output_path + '/Machete_results.csv'
		with open(output, 'w', encoding='1252', errors='replace', newline='') as myfile:
			wr = csv.writer(myfile)
			wr.writerow(('Length', 'Sentence'))
			wr.writerows(export_data)
		myfile.close()

	else:
		pass
except:
	pass