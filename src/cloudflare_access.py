# https://github.com/cloudflare/cloudflare-python
# https://developers.cloudflare.com/api/resources/dns/

import os
from cloudflare import Cloudflare
from dotenv import load_dotenv

load_dotenv()
print(os.environ.get("CLOUDFLARE_API_TOKEN"))

client = Cloudflare(
     api_token=os.environ.get("CLOUDFLARE_API_TOKEN"),  # This is the default and can be omitted
)

all_accounts = []
# Automatically fetches more pages as needed.
for account in client.accounts.list():
    # Do something with account here
    all_accounts.append(account)
print(all_accounts)