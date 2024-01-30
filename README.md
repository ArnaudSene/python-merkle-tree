# Merke Tree in python

[![GitHub Tag](https://img.shields.io/github/v/tag/ArnaudSene/python-merkle-tree)](https://github.com/ArnaudSene/python-merkle-tree/releases/tag/v0.1.0) [![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ArnaudSene/python-merkle-tree/01-test.yml?logo=githubactions&logoColor=white&label=%7C%20build)](https://github.com/ArnaudSene/python-merkle-tree/actions/workflows/01-test.yml) [![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgist.githubusercontent.com%2FArnaudSene%2Ffeb2ecb29f338262686c01a37361988a%2Fraw%2F4c8ef7edb32d9eb132cee83e5d987ad4411fa00a%2Fcovbadge.json&query=message&logo=pytest&logoColor=white&label=%7C%20Coverage&color=lemon)](https://github.com/ArnaudSene/python-merkle-tree/actions/workflows/01-test.yml) [![Static Badge](https://img.shields.io/badge/3.11-blue?logo=python&logoColor=white&label=%7C%20Python)](https://www.python.org/downloads/release/python-3110/) [![Static Badge](https://img.shields.io/badge/3.12-blue?logo=python&logoColor=white&label=%7C%20Python)](https://www.python.org/downloads/release/python-3120/)

---
This code aims to build a Merkle tree from a list of values.
All data are hashed using the cryptographic hash algorithm SHA-3 (Secure Hash Algorithm 3).

> It is recommended to hash the values provided to the MerkleTree class.

## Features
- Create a merkle tree
- Create a merkle proof
- Verify a value with a merkle proof
- Get the merkle tree root
- Get the merkle tree `size`
- Get the merkle tree `depth`
- Get/count the `leaves`

## Installation

### Clone the repository
```shell
git clone https://github.com/ArnaudSene/python-merkle-tree.git
cd python-merkle-tree
```

### Prepare environment
This code use `poetry` to manage dependencies

```shell
pipx install poetry==1.4.0
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
poetry install
```

## How to use it?

### Create a Merkle tree
```python
data = [
    '43a26051362b8040b289abe93334a5e3662751aa691185ae9e9a2e1e0c169350',  
    'f2ff61e5ca30a7708bfa760e5749e10dc81452d9006f8fb35db69d8f490ed637', 
    '487dced11563793b12e4357f218d5a521c730fff52fc03552442bfac917691c0', 
    '0e3c7b0c7fed34610a5da469ea9e44e2965a3f6ae0ae2d5d1ba5e9f5ac9d345b', 
    '1938b5f01496fa8768bc8d5a808d6cd1a3005742a9c7c12e4a17cf9f070ee2d8'
]

mt = MerkleTree()
mt.build_merkle_tree(data)
```

###  Get the merkle tree root
```python
mt.mt.get_root_tree()

'd84f7a7126b5b0ec9872893bb4c92741ee70c44d29043f2b0ff830116b9ee731'
```

### Get the merkle tree
```python
mt.get_merkle_tree()

[
    '43a26051362b8040b289abe93334a5e3662751aa691185ae9e9a2e1e0c169350', 
    'f2ff61e5ca30a7708bfa760e5749e10dc81452d9006f8fb35db69d8f490ed637', 
    '487dced11563793b12e4357f218d5a521c730fff52fc03552442bfac917691c0', 
    '0e3c7b0c7fed34610a5da469ea9e44e2965a3f6ae0ae2d5d1ba5e9f5ac9d345b', 
    '1938b5f01496fa8768bc8d5a808d6cd1a3005742a9c7c12e4a17cf9f070ee2d8', 
    'a1d17c81372869975854fe89a2f994a91caf5b337eeba198e40802ae047c373c', 
    'd5863df95241788aade3430587471066c6f23a6ed59aff3ee7559928acb518b1', 
    'd8f77eeaa7ae0f115390de80bb70082bbec539ab7b8e633ac149abd02ebc62a5', 
    'd84f7a7126b5b0ec9872893bb4c92741ee70c44d29043f2b0ff830116b9ee731'
]
```

### Get a merkle proof by providing a value (leaf)
```python
self.mt.get_merkle_proof('43a26051362b8040b289abe93334a5e3662751aa691185ae9e9a2e1e0c169350')

[
    'f2ff61e5ca30a7708bfa760e5749e10dc81452d9006f8fb35db69d8f490ed637', 
    'd5863df95241788aade3430587471066c6f23a6ed59aff3ee7559928acb518b1', 
    '1938b5f01496fa8768bc8d5a808d6cd1a3005742a9c7c12e4a17cf9f070ee2d8'
]
```

### Check if a value is in the Merkle tree
```python
leaf = '43a26051362b8040b289abe93334a5e3662751aa691185ae9e9a2e1e0c169350'
proofs = [
    'f2ff61e5ca30a7708bfa760e5749e10dc81452d9006f8fb35db69d8f490ed637', 
    'd5863df95241788aade3430587471066c6f23a6ed59aff3ee7559928acb518b1', 
    '1938b5f01496fa8768bc8d5a808d6cd1a3005742a9c7c12e4a17cf9f070ee2d8'
]

root_tree = 'd84f7a7126b5b0ec9872893bb4c92741ee70c44d29043f2b0ff830116b9ee731'

assert mt.verify(proofs, root_tree, leaf) == True
```

### Other Features
```python
# Count leaves
mt.count_leaves()
5

# Get leaves
mt.get_leaves()
[
    '43a26051362b8040b289abe93334a5e3662751aa691185ae9e9a2e1e0c169350',  
    'f2ff61e5ca30a7708bfa760e5749e10dc81452d9006f8fb35db69d8f490ed637', 
    '487dced11563793b12e4357f218d5a521c730fff52fc03552442bfac917691c0', 
    '0e3c7b0c7fed34610a5da469ea9e44e2965a3f6ae0ae2d5d1ba5e9f5ac9d345b', 
    '1938b5f01496fa8768bc8d5a808d6cd1a3005742a9c7c12e4a17cf9f070ee2d8'
]

# Get depth of the Merkle tree
mt.get_depth()
4

# Get size of the Merkle tree
mt.get_size()
9
```
