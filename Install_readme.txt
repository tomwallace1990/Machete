### Machete ###

#Installing Machete
Click on 'Machete.exe' on the GitHub page. Nothing will show up, but then click 'Download' to the right hand side. It may take up to 20 seconds for the save window to appear (dependent on internet speed). Save the file to anywhere on your computer. Once it has downloaded Chrome may say the software is uncommon and maybe dangerous - click the up arrow on the right and click 'keep'. Double click on 'Machete.exe' where you downloaded it. Windows could now do one of three things; 1. It could say that the app is unrecognised in which case click 'More info' and then 'Run anyway'. 2. It could say you need an app from the Windows store to run the program, just click cancel. 3. It could just work! Once Windows lets the program run a black window will appear, which you can ignore, and after a few seconds the main window should appear.

#Using Machete
1. Click on 'Browse' and navigate to the text you want to process. .docx is the default, if you want to load .txt then selected it the drop-down menu on the right side of the browse window. Machete works best if you only include the body text of documents and exclude headings.

2. Click on the second 'Browse' and select the output folder you want to save the two output files to. Leaving this as '.' will save them to the folder Machete.exe is currently in.

3. Set the minimum sentence size (default: 4). This will remove any sentences shorter than this value which can be useful for excluding headings, titles or errors.

4. Click 'Generate'. Machete will then produce 'Machete_results.csv' and 'Machete_statistics.txt' in the folder you specified. The .csv file contains every sentence in the document ordered from longest to shortest. You can now Ctrl+F in the original document and easily find the longest sentences to edit. The .txt file contains some basic statistics for the document such as average sentence length. If you want to generate your own statistics simply copy the 'Length' column (which is a vector of the length of every sentence in the document) from the .csv file into your statistics software of choice.

#Robustness
Because Machete is so small, it is not designed to give any errors to the user if it has a problem; it will simply close. This means if you enter an invalid path or document it will just close; reload it and enter something less stupid.

#Encoding
Machete uses Microsoft 1252 encoding which should work with all normal files produced on Windows. If you enter text with a different encoding special characters may not display correctly. If you have a file with different encoding, copy it into a word document and save it as a normal .docx and it should convert the encoding.

#.docx vs .txt
The same text may result in slightly different output depending on if .docx or .txt is used. This issue stems from the way .txt handles new lines. docx is slightly more accurate and the differences are minor.

#Licence
This software is open source and is provided for free, but is offered with no warranty or support.

#Version
1.3.
Tested under Windows 10 and Windows 7.
Written in Python 3.6.4.

#Contact
Dr Tom Wallace
@tomwallace1990
tomwallacedata@gmail.com
