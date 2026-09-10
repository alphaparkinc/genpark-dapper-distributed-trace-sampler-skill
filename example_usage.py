from client import DapperSampler

def main():
    print("=== Testing Dapper Trace Sampler ===")
    dapper = DapperSampler(sample_rate=0.01)
    s1, r1 = dapper.should_sample("12345678", is_error=True)
    print("Error sampling decision:", s1, r1)
    assert s1 and r1 == "TAIL_RULE_ANOMALY"

    s2, r2 = dapper.should_sample("12345678", latency_ms=1500.0)
    print("High latency sampling decision:", s2, r2)
    assert s2 and r2 == "TAIL_RULE_ANOMALY"
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
