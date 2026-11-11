"""Scaluq executor for the QC Executor framework.

Subclass of :class:`qc_executor.base.executor_base.ExecutorBase`.
"""

from __future__ import annotations

from typing import Any, List

import numpy as np
from qc_executor.base.circuit_base import QuantumCircuitBase
from qc_executor.base.executor_base import ExecutorBase
from qc_executor.base.operator_base import QuantumOperatorBase

from .scaluq_circuit import ScaluqCircuit
from .scaluq_operator import ScaluqOperator


class ScaluqExecutor(ExecutorBase):
    """Executor plugin for Scaluq.

    Args:
        backend (Any, optional): Backend-native device/simulator object or its
            string name. The framework convention is that this parameter is
            always called ``backend``; the factory forwards auto-detected
            objects and aliases through it.
        shots (int | None, optional): Number of shots for sampling.
        seed (int | None, optional): Random seed for reproducibility.
        log_file (str | None, optional): Path to the log file.
        log_level (str, optional): Logging level.
        caching (bool | None, optional): Whether to use in-memory caching.
        cache_dir (str, optional): Directory for caching.
        max_cache_size (int | None, optional): Maximum number of entries kept
            in each in-memory cache.
    """

    _native_circuit_class = ScaluqCircuit
    _native_operator_class = ScaluqOperator

    def __init__(
        self,
        backend: Any = None,
        shots: int | None = None,
        seed: int | None = None,
        log_file: str | None = None,
        log_level: str = "WARNING",
        caching: bool | None = None,
        cache_dir: str = "cache",
        max_cache_size: int | None = None,
    ):
        super().__init__(
            backend=backend,
            shots=shots,
            seed=seed,
            log_file=log_file,
            log_level=log_level,
            caching=caching,
            cache_dir=cache_dir,
            max_cache_size=max_cache_size,
        )

        # Dedicated caches for converted circuits/operators, mirroring the
        # in-tree backends.
        self._circuit_cache = self._make_cache()
        self._operator_cache = self._make_cache()

    @property
    def shots(self) -> int | None:
        """Return the number of shots."""
        return self._shots

    @shots.setter
    def shots(self, value: int | None) -> None:
        """Set the number of shots."""
        raise NotImplementedError

    @property
    def remote(self) -> bool:
        """Return True if execution accesses a remote backend."""
        return False

    @classmethod
    def get_accepted_backend_types(cls) -> List[type]:
        """Backend object types this executor accepts for auto-detection.

        Instances of these types passed to
        :meth:`qc_executor.factory.Executor.create` are routed to this executor.
        """
        return []

    @classmethod
    def get_accepted_backend_aliases(cls) -> List[str]:
        """String aliases the factory routes to this executor.

        Aliases are short names callers can pass instead of ``"scaluq"``.
        Each alias is forwarded to ``__init__`` as ``backend=<alias>``, and
        aliases must be unique across all registered backends.
        """
        return []

    def _expectation_value(
        self,
        circuit: QuantumCircuitBase | List[QuantumCircuitBase],
        observable: QuantumOperatorBase | List[QuantumOperatorBase],
        **parameters,
    ) -> float | np.ndarray:
        raise NotImplementedError

    def _expectation_value_derivatives(
        self,
        circuit: QuantumCircuitBase | List[QuantumCircuitBase],
        observable: QuantumOperatorBase | List[QuantumOperatorBase],
        *derivative,
        **parameters,
    ) -> float | np.ndarray | dict:
        raise NotImplementedError

    def _sample(
        self, circuit: QuantumCircuitBase | List[QuantumCircuitBase], **parameters
    ) -> dict | List[dict]:
        raise NotImplementedError

    def _statevector(
        self, circuit: QuantumCircuitBase | List[QuantumCircuitBase], **parameters
    ) -> np.ndarray:
        raise NotImplementedError

    def _transpile_circuit(self, circuit: QuantumCircuitBase) -> QuantumCircuitBase:
        raise NotImplementedError

    def _transpile_operator(
        self, operator: QuantumOperatorBase, **options: Any
    ) -> QuantumOperatorBase:
        raise NotImplementedError
