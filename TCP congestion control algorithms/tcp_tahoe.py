class TCPTahoe:
    def __init__(self):
        self.cwnd = 1
        self.ssthresh = 16

    def ack(self):
        # slow start(exponential growth )
        if self.cwnd < self.ssthresh:
            self.cwnd *= 2
        else:
            self.cwnd += 1

    def packet_loss(self):
        # congestion avoidance
        self.ssthresh = max(self.cwnd // 2, 1)
        self.cwnd = 1
