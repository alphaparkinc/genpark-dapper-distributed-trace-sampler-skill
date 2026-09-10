class DapperSampler:
    """
    Dapper Adaptive Distributed Trace Sampler.
    Guarantees retention of anomaly and error traces while sampling standard traffic.
    """
    def __init__(self, sample_rate=0.1):
        self.sample_rate = sample_rate

    def should_sample(self, trace_id, is_error=False, latency_ms=0.0):
        if is_error or latency_ms > 1000.0:
            return True, "TAIL_RULE_ANOMALY"

        val = int(trace_id[:8], 16) % 10000
        sampled = (val < self.sample_rate * 10000)
        return sampled, "PROBABILISTIC_HEAD"
