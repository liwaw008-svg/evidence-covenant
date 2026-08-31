import json,re,time
from pathlib import Path
from genlayer_py import create_client,create_account
from genlayer_py.chains import studionet
R=Path(__file__).parents[1];env=(R.parents[3]/'accounts.env').read_text();key=re.search(r'^ACCOUNT_4_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',env,re.M).group(1);c=create_client(chain=studionet,account=create_account(account_private_key=key));a=json.loads((R/'deployment.json').read_text())['contract'];i='EC-'+str(int(time.time()));urls=['https://raw.githubusercontent.com/liwaw008-svg/docksure/bff03a0/evidence/demo-carrier-record.json','https://github.com/liwaw008-svg/docksure/raw/bff03a0/evidence/demo-carrier-record.json']
def send(fn,args):
 h=c.write_contract(address=a,function_name=fn,args=args);print(fn,h,flush=True);c.wait_for_transaction_receipt(transaction_hash=h,status='ACCEPTED',retries=120,interval=10000);return h
created=send('create_covenant',[i,'Do the two independently fetched JSON records contain exactly the same shipment identity, lane, delivery timestamps, status and seal condition?',['Shipment identifiers are identical','Lane and timestamps are identical','Status and seal values are identical'],['MATCH','NO_MATCH'],'MATCH',urls]);resolved=send('resolve',[i,urls]);state=c.read_contract(address=a,function_name='get_covenant',args=[i]);print(json.dumps({'create':created,'resolve':resolved,'state':state},indent=2));assert state['status']=='RESOLVED' and state['outcome']=='MATCH' and len(state['digests'])==2
