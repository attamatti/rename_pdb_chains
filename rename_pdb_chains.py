#!/usr/bin/env python

import sys

try:
    pdbfile = sys.argv[1]
    chain_names = {}
    for x in sys.argv[2:]:
        chain_names[x.split(',')[0]] = x.split(',')[1]
except:
    sys.exit('USAGE: rename_pdb_chain.py <pdbfile> <old 1>,<new 1> <old 2>,<new 2> ...<old n>,<new n>')

pdbdata = open(pdbfile,'r').readlines()

output = open('{0}_rechained.pdb'.format(pdbfile.split('.')[0]),'w')
for line in pdbdata:
        if line[0:4] =='ATOM':
            chain = line[21]
            print(line.replace('\n',''))
            try:
                newline = '{0}{1}{2}'.format(line[0:21],chain_names[chain],line[22:])
                print(newline)
                output.write(newline)
            except:
                output.write(line)