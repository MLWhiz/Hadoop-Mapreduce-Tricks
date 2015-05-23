import sys
dead_ids = set()

def read_cache():
    for line in open('ref'):
        id = line.strip()
        dead_ids.add(id)

read_cache()

for line in sys.stdin:
    rec = line.strip().split("|") # Split using Delimiter "|"
    id = rec[0]
    house = rec[2]
    if id not in dead_ids:
        print "%s\t%s" % (house,1)