"""
A simple Merkle Tree application.

Author:
Arnaud SENE, arnaud.sene@pm.me
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from Crypto.Hash import keccak


@dataclass
class MerkleTree:
    """
    Class to build a Merkle Tree.

    It allows
        - to create a merkle tree from a list of data
        - to create a proof structure (automatically)
        - to verify a data in merkle tree
        - to get informations as (size, depth, etc.)
    """

    _merkle_tree: list[str] = field(default_factory=list)
    _leaves: List[str] = field(default_factory=list)
    _depth: int = 1
    _proofs: Dict[str, Tuple[str, str]] = field(default_factory=dict)

    def count_leaves(self) -> int:
        """Count the number of leaves in the merkle tree.

        Returns:
            int: The number of leaves.
        """
        return len(self._leaves)

    def get_leaves(self) -> List[str]:
        """Get the leaves in the merkle tree.

        Returns:
            list[str]: A list of leaves.
        """
        return self._leaves

    def get_merkle_tree(self):
        """Get the merkle tree structure.

        Returns:
            list[str]: A merkle tree structure.
        """
        return self._merkle_tree

    def get_depth(self) -> int:
        """Get the depth of the merkle tree.

        Returns:
            int: The depth of the merkle tree.
        """
        return self._depth

    def get_size(self) -> int:
        """Get the size of the merkle tree.

        This is the number of node/leaf not empties in the merkle tree.

        Returns:
            int: The number of elements in the merkle tree.
        """
        return len(self.get_merkle_tree())

    def get_root_tree(self) -> str:
        """Get the root of the Merkle tree.

        Returns:
            str: The merkle tree root.
        """
        try:
            return self.get_merkle_tree()[-1]
        except IndexError:
            raise IndexError("No merkle tree found!")

    def build_merkle_tree(self, values: list[str]) -> None:
        """Build a merkle tree.

        Args:
            values (list[str]): The values required to build the merkle tree.

        Returns:
            None

        Raises:
            ValueError: No ``values`` provided.
        """
        self._build_merkle_tree(values)

    def _build_merkle_tree(self, values: list[str], offset: int = 0) -> None:
        """Build a merkle tree.

        Args:
            values (list[str]): The values required to build the merkle tree.
            offset (int): The offset value (offset)

        Returns:
            None

        Raises:
            ValueError: No ``values`` provided.
        """
        if not values:
            raise ValueError("No value provided!")

        # Init merkle tree with leaves
        if len(self.get_merkle_tree()) == 0:
            self._merkle_tree = values.copy()
            self._leaves = values.copy()

        # Copy of values (leaves)
        values_copy = values.copy()
        new_values: list[str] = []
        _offset = offset
        offset = len(self.get_merkle_tree())

        # Count depth of merkle
        if len(values_copy) >= 2:
            self._depth += 1

        for i in range(0, len(values_copy), 2):
            pair = values_copy[i:i + 2]

            if len(pair) == 2:
                hash = self._hash_pair(pair[0], pair[1])

                # Create proofs
                self._proofs[pair[0]] = (pair[1], hash)
                self._proofs[pair[1]] = (pair[0], hash)

                # Add hash to merkle tree
                self._merkle_tree.append(hash)
                _offset += 2

            else:
                hash = pair[0]

            new_values.append(hash)

        if len(new_values) > 1:
            self._build_merkle_tree(new_values, offset)

    def get_merkle_proof(self, leaf: str):
        """Get the merkle tree proof structure.

        Args:
            leaf (str): The leaf's proof to provide

        Returns:
            list[str]: The merkle tree proof structure
        """
        return self._get_merkle_proof(leaf)

    def _get_merkle_proof(self, leaf: str, values: Optional[List[str]] = None):
        """Get the merkle tree proof structure.

        Args:
            leaf (str): The leaf's proof to provide
            values (list[str]): The proof values

        Returns:
            list[str]: The merkle tree proof structure
        """
        if values is None:
            values = []

        hash = None
        if self._proofs.get(leaf) is not None:
            value, hash = self._proofs[leaf]
            values.append(value)

        if hash:
            self._get_merkle_proof(hash, values)

        return values

    def verify(self, proof: list[str], root_tree: str, leaf: str) -> bool:
        """Check that a value is part of the merkle tree.

        Args:
            proofs (list[str]): The proofs values.
            root_tree (str): The merkle tree root.
            leaf (str): The value to check.

        Returns:
            True if the value is part of the merkle tree.
        """
        return self._verify(proof, leaf) == root_tree

    def _verify(self, proof: list[str], leaf: str):
        """Build a merkle tree root based on values provided.

        Args:
            proofs (list[str]): The proofs values.
            leaf (str): The value to check.

        Returns:
            The merkle tree root.
        """
        computed_hash = leaf
        for i in proof:
            computed_hash = self._hash_pair(computed_hash, i)

        return computed_hash

    # -----------------------------------------------
    # Static methods
    # -----------------------------------------------

    @staticmethod
    def _hash_value(value: str) -> str:
        """
        Hash a string using sha3 algorithm.

        Args:
            value (str): A string to hash.

        Returns:
            str: The value hashed
        """
        return keccak.new(digest_bits=256, data=value.encode()).hexdigest()

    @staticmethod
    def _hash_pair(a: str, b: str) -> str:
        """
        Concatenate and hash a pair of values using sha3 algorithm.

        Args:
            a (str): The first value to hash
            b (str): The second value to hash

        Returns:
            str: The values concatenated and hashed.
        """
        if all([not isinstance(a, str), not isinstance(b, str)]):
            raise TypeError("a and b not string")

        if a < b:
            return keccak.new(
                digest_bits=256, data=(a.encode() + b.encode())
            ).hexdigest()
        return keccak.new(
            digest_bits=256, data=(b.encode() + a.encode())
        ).hexdigest()
