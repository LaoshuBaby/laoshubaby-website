# IaC deployment
# Because CDN is supported by Cloudflare, this place will follow its documents.
# https://developers.cloudflare.com/workers/platform/infrastructure-as-code/

DOMAIN="laoshubaby.moe"

pair=[
    ("towait.","CNAME","laoshubaby.moe/pages/towait"),
    ("environment.","CNAME","laoshubaby.moe/pages/environment"),
    ("vscode.","CNAME","laoshubaby.moe/pages/environment/vscode"),
    # ("vscode.","A","1.2.3.4"), # For situation that depoly on a VPS or Bare Metal machine.
    ("openhands.","CNAME","laoshubaby.moe/pages/environment/openhands"),
    # ("openhands.","A","1.2.3.4"), # For situation that depoly on a VPS or Bare Metal machine.
    ("git.","CNAME","laoshubaby.moe/pages/environment/openhands"),
    # Former Forgejo instance need to re-start on a new server
    # ("git.","A","1.2.3.4"), # For situation that depoly on a VPS or Bare Metal machine.
    ("osm.","CNAME","laoshubaby.moe/pages/osm"),
    # ("*.server.","A","11.22.33.44"), # For connect to a holding VPS device without remember its IP
]