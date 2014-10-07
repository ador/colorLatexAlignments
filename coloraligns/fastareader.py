import os
from sequence import Sequence


class FastaNotFound(Exception): 
    def __init__(self, path):
        Exception.__init__(self, 'Fasta file not found: %s ' % header)

class DuplicateSeqNameException(Exception):
    def __init__(self, header):
        Exception.__init__(self, 'Duplicated fasta header: %s ' % header)


class FastaReader(object):

    def read_seqs(self, path):
        if not os.path.exists(path):
            raise FastaNotFound(fasta_name)
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        return lines
        

    
            #if header in seen_headers:
            #            raise DuplicateSeqNameException(header)