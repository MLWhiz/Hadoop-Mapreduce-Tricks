import sys

current_key = None
key = None
count = 0

for line in sys.stdin:
    line = line.strip()
    rec = line.split('\t')
    key = rec[0]    
    value = int(rec[1])
    
    if current_key == key:
        count += value
    else:
        if current_key:
            print "%s:%s" %(key,str(count))     
        current_key = key
        count = value

if current_key == key:
    print "%s:%s" %(key,str(count)) 