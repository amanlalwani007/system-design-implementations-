# Linux commonly uses Cubic. Instead of linear growth after Slow Start, it uses a cubic function of time since the last congestion event.
class TCPCubic:
    def __init__(self):
        self.cwnd = 1
        self.K = 3

    def ack(self, t):
        # Simplified cubic growth
        self.cwnd = max(1, (t - self.K) ** 3 + 20)

    def packet_loss(self):
        self.cwnd *= 0.7  # Multiplicative decrease

    def status(self):
        print(f"cwnd={self.cwnd:.2f}")
