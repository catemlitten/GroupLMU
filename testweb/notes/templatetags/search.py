from .formatting import *

def search(fileContents, fileNames, term, maxOutputLen):
    # file contents is a list of strings, each of which is the entire body of a note/file.
    # file names is a list of strings as well,
    # only containing the name of the file which corresponds by index to the file contents list.
    # term is just the search term
    # max output length limits how long a string of output can be (for a clean output).
    output = []
    # final output
    for i in range(len(fileNames)):
        # iterate through each file
        currFile = [fileNames]
        # start building a result for the current file, starting with this file's name
        lines = fileContents.split('\n')
        print(str(lines))
        if lines:
            for j in range(len(lines)):
                print("Debugging... " + str(lines))
                found = []
                # list to compile all locations where it was found on the line
                words = charsToSpaces(lines[j]).split(' ')
                w = 0
                for k in range(len(words)):
                    if words[k].lower() == term.lower():
                        found.append(w)
                    # if the word is found, append the index of the word
                    w += len(words[k]) + 1
                for k in range(len(found)):
                    # for each location where the word was found, format the output
                    line = formatLine(lines[j], maxOutputLen, found[k], term, j)
                    currFile.append(line)
                    # append the formatted output to the current file's result
            if len(currFile) > 1:
                # if a word has been found in this file
                output.append(currFile)
            # add this file's results to the final output
        return output


### View sample input in 'dummy_test.py'

### Format of search hits:
#	[STRING of text surrounding the term, the line number, index of first letter of term in STRING,
#   index of last letter of term in STRING]
#		first and last letter indexes to help with highlighting the word

### SAMPLE OUTPUT: search for 'when', with a max output length of 60
"""

[
	["Cousin Tribulation's Story",
		["... ear's breakfast which I had when I was a little girl. What d ...", 1, 32, 35],
		["... our things and help me, and when we come back, we'll get som ...", 14, 32, 35],
		["... e didn't get any of it; and when we came away, leaving them  ...", 21, 32, 35],
		["Testing the search for when, let's see", 22, 23, 26]
	],
	["The Story of An Hour",
		['... een in the newspaper office when intelligence of the railroa ...', 2, 32, 35],
		["... ment, in her sister's arms. When the storm of grief had spen ...", 3, 32, 35],
		['... r, quite motionless, except when a sob came up into her thro ...', 7, 32, 35],
		['... nder hands would have been. When she abandoned herself a lit ...', 10, 32, 35],
		['... w that she would weep again when she saw the kind, tender ha ...', 11, 32, 35],
		['When the doctors came they said she had died of heart diseas ...', 20, 0, 3]
	]
]

"""
