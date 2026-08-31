# Evidence Covenant

Evidence Covenant is a standalone GenLayer primitive for reusable semantic decision receipts. A caller fixes a question, explicit requirements, a closed outcome vocabulary and trusted HTTPS origins. A resolver can later supply records only from that frozen policy. Validators independently fetch the records and must agree on the bounded outcome, exact citation indexes and SHA-256 content digests.

It is useful for insurance gates, compliance checks, procurement decisions, release policies and any workflow that needs an auditable semantic decision without allowing an LLM to invent the decision space or substitute evidence.

## Security invariants

- Outcomes and origins are distinct, bounded and immutable after creation.
- At least two distinct evidence records are required.
- Every URL must match an owner-authorized HTTPS origin.
- Evidence is explicitly treated as untrusted data.
- Consensus binds outcome, citations and exact fetched content digests.
- No funds move and no downstream action is chosen; integrators consume the receipt deterministically.

## Verify

```bash
genvm-lint check contracts/contract.py
python -m pytest -q
```

## StudioNet

- Contract: `0x70D44F88c9a20C267f7bF3FbFb0Ff6820F046D80`
- Deployment: `0x23b54a1e5baf7b5edc477ccce2830ee8135d58802f59c159372c2cc5c2aeb129`
- Create proof: `0x06cb492c4d610e4bfaec5ad6effc6e1bb80f54c280fb38bba5fbb75acdbaf2d2`
- Resolve proof: `0xe213bb8f5e896d5d31309c625758e17567a1b99f97318dcded2562a6d237caae`
