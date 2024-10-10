import sys

if len(sys.argv) != 3:
    print("USAGE: welcome.py characters replacements")
    exit()
    
strToTransform = sys.argv[1]
replacePattern = sys.argv[2]

if len(strToTransform) != len(replacePattern):
    print("ERROR: Arguments must be the same length.")
    exit()
    
translationDict = {}
for i in range(len(strToTransform)):
    translationDict[strToTransform[i]] = replacePattern[i]

for line in sys.stdin:
    output = ''
    for char in line:
        if char in translationDict:
            output += translationDict[char]
        else:
            output += char
    print(output, end='')

