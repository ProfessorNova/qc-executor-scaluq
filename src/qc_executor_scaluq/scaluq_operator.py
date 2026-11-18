"""Scaluq native operator wrapper.

Wraps a generic :class:`qc_executor.quantum_operator.QuantumOperator` for
Scaluq's expectation-value/sampling routines.
"""

from __future__ import annotations

from typing import Any

from qc_executor.quantum_operator import QuantumOperatorBase


class ScaluqOperator(QuantumOperatorBase):
    """Backend-native operator for Scaluq."""

    def __init__(self, operator: QuantumOperatorBase) -> None:
        self._source_operator = operator
        self._num_qubits = operator.num_qubits
        return self._build_native()

    # ------------------------------------------------------------------
    # Backend hooks
    # ------------------------------------------------------------------

    def _build_native(self) -> Any:
        """Compile the representation into this backend's native operator."""
        return self.from_quantum_operator(self._source_operator)

    @classmethod
    def from_quantum_operator(cls, operator: QuantumOperatorBase) -> "ScaluqOperator":
        """Create a Scaluq native operator from a generic ``QuantumOperator``."""
        return cls(operator)

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def num_qubits(self) -> int:
        """Return the number of qubits the operator acts on."""
        return self._num_qubits
