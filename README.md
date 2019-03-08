# Machete

Machete is a small program which helps chop down overly-long sentences in long documents. It takes in a .docx or .txt file containing prose (structured text) and outputs two results files. The main output is a .csv file containing a list of all the sentences in the input document ranked by length (decending). This allows the user to easily edit the longest sentences in the original document. The second output is a .txt file containing basic statistics such as average sentence length.

Please see 'Install_readme.txt' for more information on using Machete.

Written in Python 3.6.4.

####Change-log
1.0. - Initial version

1.1. - Changed splitter from simple '. ' to regex which significantly increases sentence detection accuracy.