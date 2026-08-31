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
