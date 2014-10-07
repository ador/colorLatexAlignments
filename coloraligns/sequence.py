class Sequence(object):
    name = ""
    seq = ""

    def __init__(self, name, seq_lines):
        self.name = name
        for line in seq_lines:
            line2 = line.strip()
            self.seq = self.seq + line2

    def wrap_seq(self, l):
        ret = []
        cnt = 0
        todo_len = len(self.seq)
        while todo_len > l:
            ret.append(self.seq[cnt:cnt+l])
            todo_len = todo_len - l
            cnt = cnt + l
        ret.append(self.seq[cnt:])
        return ret

    def get_name(self):
        return self.name

    def get_seq(self):
        return self.seq

    def seq_without_gaps(self):
        return self.seq.replace("-","")

