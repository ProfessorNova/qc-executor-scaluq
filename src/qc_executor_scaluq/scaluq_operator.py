"""Scaluq native operator wrapper.

Wraps a generic :class:`qc_executor.quantum_operator.QuantumOperator` for
Scaluq's expectation-value/sampling routines. Like the circuit wrapper, this
class intentionally does not subclass
:class:`qc_executor.base.operator_base.QuantumOperatorBase`.

The generic operator carries a Qiskit ``SparsePauliOp`` as its intermediate
representation, reachable via ``operator.qiskit_operator``.
"""

from __future__ import annotations

from qc_executor.quantum_operator import QuantumOperator


class ScaluqOperator:
    """Backend-native operator for Scaluq."""

    @classmethod
    def from_quantum_operator(cls, operator: QuantumOperator) -> "ScaluqOperator":
        """Create a Scaluq native operator from a generic ``QuantumOperator``."""
        return cls(operator)

    def __init__(self, operator: QuantumOperator) -> None:
        self._source_operator = operator
        self._num_qubits = operator.num_qubits

    @property
    def num_qubits(self) -> int:
        """Return the number of qubits the operator acts on."""
        return self._num_qubits
