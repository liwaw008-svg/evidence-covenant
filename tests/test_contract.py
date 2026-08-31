from pathlib import Path
import ast
S=(Path(__file__).parents[1]/'contracts/contract.py').read_text()
def test_parse_and_surface():ast.parse(S);assert all(('def '+x) in S for x in ('create_covenant','resolve','get_covenant','list_covenants'))
def test_origin_and_digest_binding():assert 'unauthorized source' in S and 'hashlib.sha256' in S and "m['digests']==t.get('digests')" in S
def test_bounded_consensus():assert "o not in allowed" in S and "m['outcome']==t.get('outcome')" in S and "m['citations']==t.get('citations')" in S
def test_no_forbidden_equivalence():assert 'eq_principle' not in S and 'prompt_non_comparative' not in S
def test_identical_content_outcome_is_explicit_and_deterministic():assert 'identical_content_outcome:str' in S and "exact not in os" in S and 'all(x==digests[0]' in S
