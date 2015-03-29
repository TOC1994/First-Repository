# -*- coding: iso-8859-1 -*-
infile = 'GDS5047_full.soft'

fh = open(infile)

line= fh.readline()
while line[:19] != 'dataset_table_begin':
    line=fh.readline()

header= fh.readline().strip()

colnames={}

index=0
for title in header.split('\t'):
    colnames[title]=index
    print '%s\t%s'%(title,index)
    index=index+1

genefile=open('genes.txt', 'w')
expressionfile=open('expression.txt', 'w')
probefile=open('probes.txt', 'w')

genefields=['Gene ID', 'Gene symbol', 'Gene title']
samples=header.split('\t')[2:int(colnames['Gene title'])]
probefields=['ID_REF', 'Gene ID']

def buildrow(row, fields):
        '''Creates a tab separated list of values according to the values listed in fields
        row: a list of values 
        fields: a list of columns. Only the values in row corresponding to the columns in fields are output.
        returns: a tab separated string of values that is terminated by a newline'''
    newrow=[]
    for f in fields:
        newrow.append(row[int(colnames[f])])
    return "\t".join(newrow)+"\n"

def build_expression(row, samples):
        '''Builds tab separated rows for expression data. For each of the samples listed
        it generates a line with the probe id, sample id and expression value.
        row: a list of values
        samples: a list of column headings corresponding to the samples
        '''
    exprrows=[]
    for s in samples:
        newrow=[s,]
        newrow.append(row[int(colnames['ID_REF'])])
        newrow.append(row[int(colnames[s])])
        exprrows.append("\t".join(newrow))
    return "\n".join(exprrows)+"\n"

rows=0
forline in fh.readlines():
    try:
        if line[0]=='!':
            continue
        row=line.strip().split('\t')
        genefile.write(buildrow(row, genefields))
        probefile.write(buildrow(row,probefields))
        expressionfile.write(build_expression(row, samples))
        rows=rows+1
    except:
        pass
genefile.close()
probefile.close()
expressionfile.close()

print '%s rows processed'%rows