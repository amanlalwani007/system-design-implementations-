class TCPReno:
    def __init__(self):
        self.cwnd = 1
        self.ssthresh = 16

    def ack(self):
        if self.cwnd < self.ssthresh:
            self.cwnd *= 2
        else:
            self.cwnd += 1

    def triple_duplicate_ack(self):
        self.ssthresh = max(self.cwnd // 2, 1)
        self.cwnd = self.ssthresh

    def timeout(self):
        self.ssthresh = max(self.cwnd // 2, 1)
        self.cwnd = 1
