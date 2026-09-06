# Evidence Covenant

Evidence Covenant is a standalone GenLayer primitive for reusable semantic decision receipts. A caller fixes a question, explicit requirements, a closed outcome vocabulary and trusted HTTPS origins. A resolver can later supply records only from that frozen policy. Validators independently fetch the records and must agree on the bounded outcome, exact citation indexes and SHA-256 content digests.

It is useful for insurance gates, compliance checks, procurement decisions, release policies and any workflow that needs an auditable semantic decision without allowing an LLM to invent the decision space or substitute evidence.

## Security invariants

- Outcomes and origins are distinct, bounded and immutable after creation.
- At least two distinct evidence records are required.
- Every URL must match an owner-authorized HTTPS origin.
- Evidence is explicitly treated as untrusted data.
- Consensus binds outcome, citations and SHA-256 digests of the complete fetched response bytes. Only a separately bounded representation is sent to the model.
- Authorized source policies use parsed HTTPS origins and normalized path boundaries. Lookalike hostnames and reuse of one authorized slot are rejected.
- No funds move and no downstream action is chosen; integrators consume the receipt deterministically.

## Verify

```bash
genvm-lint check contracts/contract.py
python -m pytest -q
```

## StudioNet

- Contract: `0x3F9eB93e0158f4AEE23A8a497aD09d282C1271f9`
- Deploy tx: `0xc9c2a91289652af89268f2ef09e2c9f00281f40262d2700de30327b9b1603c66`
- Reviewed source: `2b2455b41b6c97779c256a27700722f5beace153`
- Create proof: `0xaeab824fc57fb77706485f5a08a6fbbe1823327e3bce4e34cf97a3dc71f0b316`
- Resolve proof: `0x8d23cdb477f051bce79449e5ab980099ba0a234ac47a09ddbbc7f685c8361d1b`
- Final receipt: `EC-1788710947`, `RESOLVED`, outcome `MATCH`

The complete lifecycle and exact response digests are recorded in `evidence/network-run.json`. Direct regression tests prove that hostname-prefix bypasses and same-slot evidence are rejected, and that responses with identical first 2,400 characters but different trailing bytes produce different digests.
