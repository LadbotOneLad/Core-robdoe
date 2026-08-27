import hashlib

def hash_node(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def compute_merkle_root(blocks: list) -> str:
    if not blocks:
        return hash_node("")
    layer = [hash_node(b) for b in blocks]
    while len(layer) > 1:
        next_layer = []
        for i in range(0, len(layer), 2):
            left = layer[i]
            right = layer[i+1] if i + 1 < len(layer) else left
            combined = left + right
            next_layer.append(hash_node(combined))
        layer = next_layer
    return layer[0]

if __name__ == "__main__":
    lattice_blocks = [
        "Node: 0xf091867EC603A6628eD83D274E8335539D82e9cc8",
        "Directive: Law of Shaped Force Active",
        "Namespace: robdoe.com",
        "Hub Status: Blackhawk Active"
    ]
    root_hash = compute_merkle_root(lattice_blocks)
    print(f"[*] Theta Root Hash (Tree of Life): {root_hash}")
