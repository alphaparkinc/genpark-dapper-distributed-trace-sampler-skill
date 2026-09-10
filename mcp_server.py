import sys
import json
from client import DapperSampler

def main():
    sampler = DapperSampler()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "sample":
            decision, reason = sampler.should_sample(
                params.get("trace_id", "00000000"),
                params.get("is_error", False),
                params.get("latency_ms", 0.0)
            )
            res = {"sampled": decision, "reason": reason}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
