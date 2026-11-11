"""Scaluq native circuit wrapper.

Wraps a generic :class:`qc_executor.quantum_circuit.QuantumCircuit` and exposes
it in a form Scaluq can execute. Like most in-tree backends, this class is
standalone (it does not subclass
:class:`qc_executor.base.circuit_base.QuantumCircuitBase`) and only implements
the methods the executor needs.

The generic circuit carries a Qiskit circuit as its intermediate
representation, reachable via ``circuit.qiskit_circuit``.
"""

from __future__ import annotations

from qc_executor.quantum_circuit import QuantumCircuit


class ScaluqCircuit:
    """Backend-native circuit for Scaluq."""

    @classmethod
    def from_quantum_circuit(cls, circuit: QuantumCircuit) -> "ScaluqCircuit":
        """Create a Scaluq native circuit from a generic ``QuantumCircuit``."""
        return cls(circuit)

    def __init__(self, circuit: QuantumCircuit) -> None:
        self._source_circuit = circuit
        self._num_qubits = circuit.num_qubits

    @property
    def num_qubits(self) -> int:
        """Return the number of qubits in the circuit."""
        return self._num_qubits
