'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and
compute the average of those values and produce an output as shown below. Do
not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

a = 0
t = 0
total = 0
for line in fh:
    x = line.find("X-DSPAM-Confidence:")
    if x is 0:
        t = float(line[x+19 :].strip())
        
        a = a + 1
        total = total + t
print("Average spam confidence:", total /a)
