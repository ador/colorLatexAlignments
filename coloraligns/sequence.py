class Sequence(object):
    name = ""
    seq = [""]
    def __init__(self, name, seq):
        self.name = name
        self.seq = self.check(seq)

    def wrap(self, seq, l):
        # remove newline chars and break the string into l long pieces
        pass

    def get_name(self):
        return self.name

    def get_seq(self):
        return self.seq

    def get_seq_str(self):
        ret = ""
        for line in self.seq:
            ret = ret + line
        return str(ret)
