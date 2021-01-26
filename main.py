reader = open('builtdiff.txt', 'r')
output = open('trashtalk.cfg', 'w')

BIND_KEY = 'p'

try:
    length = len(open('builtdiff.txt').readlines())
    output.write('alias "builtdiff" "builtdiff1"\n')
    counter = 1
    for line in reader.readlines():
        output.write('alias "builtdiff' + str(counter) + '" "say ' + line.strip('\n') + '; alias builtdiff builtdiff')
        if counter == length:
            output.write('1"\n')

        else:
            output.write(str(counter) + '"\n')

        counter += 1
    
    output.write('bind "' + BIND_KEY + '" "builtdiff"\n\n')

finally:
    reader.close()

reader = open('trashtalk.txt', 'r')

BIND_KEY = 'o'

try:
    length = len(open('trashtalk.txt').readlines())
    output.write('alias "trashtalk" "trashtalk1"\n')
    counter = 1
    for line in reader.readlines():
        output.write('alias "trashtalk' + str(counter) + '" "say ' + line.strip('\n') + '; alias trashtalk trashtalk')
        if counter == length:
            output.write('1"\n')

        else:
            output.write(str(counter) + '"\n')

        counter += 1
    
    output.write('bind "' + BIND_KEY + '" "trashtalk"\n\n')

finally:
    reader.close()
    output.close()