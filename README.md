# Merke Tree in python

This code aims to build a Merkle tree from a list of values.
All data are hashed using the cryptographic hash algorithm SHA-3 (Secure Hash Algorithm 3).

![workflow](https://github.com/ArnaudSene/python-merkle-tree/actions/workflows/01-test.yml/badge.svg)

---


> It is recommended to hash the values provided to the MerkleTree class.

## Features
- build a merkle tree
- create a merkle proof
- verify a value with a merkle proof
- get the merkle tree root
- get the merkle tree `size`
- get the merkle tree `depth`
- get/count the `leaves`

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
