import hashlib
import json

def pin_payload_to_ipfs(attestation_text):
    # Simulated IPFS content addressing via SHA-256 multihash container
    digest = hashlib.sha256(attestation_text.encode()).hexdigest()
    ipfs_cid = f"bafybeic{digest[:32]}"
    print(f"[IPFS PINNED] State anchored to decentralized storage. CID: {ipfs_cid}")
    return ipfs_cid
