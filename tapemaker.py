import webbrowser
import base64
print('What would you like to do?')
print('1. Generate tape from file')
print('2. Generate tape from pasted text')
choices = ['1', '2']
choice = '0'
choice = input('Please type 1 or 2 and press Enter ')
if choice == "1":
    print('coming soon')
elif choice == '2':
    data = input('enter data for tape')

tapeData = data
binaryData = ''.join(format(ord(i), 'b') for i in tapeData)
print(binaryData)

tapePrintHTML = '<!doctype html> \
<html lang=en>\
<head>\
<meta charset=UTF-8>\
<style>body,html{width:11in;height:8.5in}.white,white{background-color:#fff!important;width:2cm;height:2cm;display:inline-block;outline-style:solid;-webkit-print-color-adjust:exact}.gray,gray{background-color:gray!important;width:2cm;height:2cm;display:inline-block;outline-style:solid;-webkit-print-color-adjust:exact}.black,black{background-color:#000!important;width:2cm;height:2cm;display:inline-block;outline-style:solid;-webkit-print-color-adjust:exact}</style>\
<title>Tape to print</title>\
</head>\
<body onload="window.print()">'

binaryDataHTML = ""
for x in binaryData:
    binaryDataHTML = binaryDataHTML + str('<gray></gray>')
    print(x)
    if (x == "1"):
        binaryDataHTML = binaryDataHTML + str('<white></white>')
    else:
        binaryDataHTML = binaryDataHTML + str('<black></black>')
binaryDataHTML = binaryDataHTML + str('<gray></gray>')

tapePrintHTML = tapePrintHTML + binaryDataHTML

tapePrintHTML = tapePrintHTML + '</body></html>'
print(tapePrintHTML)

base64HTML = base64.b64encode(tapePrintHTML.encode("utf-8"))
print(base64HTML)
base64URL = b"data:text/html;base64," + base64HTML
print(base64URL)
webbrowser.open(str(base64URL))
