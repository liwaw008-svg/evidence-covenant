import hashlib
from conftest import CONTRACT

RULES=['https://records.example/shipments/','https://archive.example/receipts/']

def covenant(direct_deploy):
    c=direct_deploy(CONTRACT)
    c.create_covenant('EC-1','Do the independent records agree on the complete shipment result?',
        ['Match shipment identity','Match final status'],['MATCH','NO_MATCH'],'MATCH',RULES)
    return c

def test_hostname_prefix_bypass_is_rejected(direct_vm,direct_deploy):
    c=covenant(direct_deploy)
    with direct_vm.expect_revert('distinct authorized HTTPS slot'):
        c.resolve('EC-1',['https://records.example.evil.test/shipments/1','https://archive.example/receipts/1'])

def test_two_records_cannot_reuse_one_authorized_slot(direct_vm,direct_deploy):
    c=covenant(direct_deploy)
    with direct_vm.expect_revert('distinct authorized HTTPS slot'):
        c.resolve('EC-1',['https://records.example/shipments/1','https://records.example/shipments/2'])

def test_digest_covers_bytes_beyond_prompt_limit(direct_vm,direct_deploy):
    c=covenant(direct_deploy);prefix='A'*2400
    first=(prefix+'LEFT').encode();second=(prefix+'RIGHT').encode()
    direct_vm.mock_web(r'records\.example',{'status':200,'body':first.decode()})
    direct_vm.mock_web(r'archive\.example',{'status':200,'body':second.decode()})
    direct_vm.mock_llm(r'.*Evidence Covenant.*','{"outcome":"NO_MATCH","rationale":"Trailing bytes differ."}')
    direct_vm.mock_llm(r'.*Evidence Covenant.*','{"outcome":"NO_MATCH","rationale":"Trailing bytes differ."}')
    result=c._judge(c.covenants['EC-1'],['https://records.example/shipments/1','https://archive.example/receipts/1'])
    assert result['digests']==[hashlib.sha256(first).hexdigest(),hashlib.sha256(second).hexdigest()]
    assert result['digests'][0]!=result['digests'][1]
