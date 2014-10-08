class Sequence(object):

    def __init__(self, name, seq_lines):
        self.name = name
        self.seq = ""
        for line in seq_lines:
            line = line.strip()
        self.seq = "".join(seq_lines)

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

    def seq_without_gaps(self):
        return self.seq.replace("-","")

