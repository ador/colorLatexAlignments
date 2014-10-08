import os
from sequence import Sequence


class FastaNotFound(Exception): 
    def __init__(self, path):
        Exception.__init__(self, 'Fasta file not found: %s ' % header)

class DuplicateSeqNameException(Exception):
    def __init__(self, header):
        Exception.__init__(self, 'Duplicated fasta header: %s ' % header)


class FastaReader(object):

    # returns False if its a new seqence name, True if not new
    def check_seen_seqname(self, seq_list, seqname):
        for seq in seq_list:
            if seq.name == seqname:
                return True
        return False

    def read_seqs(self, path):
        results = []
        with open(path, 'r') as infile:
            inlines = infile.readlines()
            header = ''
            seq_items = []
            first = True
            for line in inlines:
                if line[0] == ';':
                    continue # comment
                elif line[0] == '>':
                    if not first:
                        seq = "".join(seq_items)
                        results.append(Sequence(header, seq))
                        seq_items = []
                    header = line[1:-1].strip() # eat '>' and '\n' ans extra whitespace
                    first = False
                else:
                    seq_items.append(line.strip().upper())
            if len(seq_items) > 0:
                seq = "".join(seq_items)
                if not self.check_seen_seqname(results, header):
                    results.append(Sequence(header, seq))
                else:
                    infile.close()
                    raise DuplicateSeqNameException(header)
            infile.close()
        return results

