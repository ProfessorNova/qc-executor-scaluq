"""Scaluq native circuit wrapper.

Wraps a generic :class:`qc_executor.quantum_circuit.QuantumCircuit` and exposes
it in a form Scaluq can execute.
"""

from __future__ import annotations

from typing import Any, FrozenSet

from qc_executor.base.gate_set import GATE_DEFS, OpCode
from qc_executor.quantum_circuit import QuantumCircuitBase


class ScaluqCircuit(QuantumCircuitBase):
    """Backend-native circuit for Scaluq."""

    def __init__(self, circuit: QuantumCircuitBase) -> None:
        self._source_circuit = circuit
        self._num_qubits = circuit.num_qubits
        return self._build_native()

    # ------------------------------------------------------------------
    # Backend hooks
    # ------------------------------------------------------------------

    @classmethod
    def supported_opcodes(cls) -> FrozenSet[OpCode]:
        """Return the opcodes this circuit type can represent natively.

        The default accepts the whole gate set.  Backends narrow this so that
        :meth:`from_quantum_circuit` lowers anything else into supported gates.
        """
        return frozenset(GATE_DEFS)

    def _build_native(self) -> Any:
        """Compile the IR into this backend's native circuit representation.

        Returns:
            The native object.  The generic circuit has none.
        """
        return self.from_quantum_circuit(self._source_circuit)

    @classmethod
    def from_quantum_circuit(cls, circuit: QuantumCircuitBase) -> "ScaluqCircuit":
        """Create a Scaluq native circuit from a generic ``QuantumCircuitBase``."""
        return cls(circuit)

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def num_qubits(self) -> int:
        """Return the number of qubits in the circuit."""
        return self._num_qubits
