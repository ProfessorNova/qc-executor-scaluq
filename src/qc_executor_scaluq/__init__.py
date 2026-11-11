"""Scaluq plugin for the QC Executor framework."""

__version__ = "0.0.1"

try:
    from qc_executor.factory import Executor

    from .scaluq_circuit import ScaluqCircuit
    from .scaluq_executor import ScaluqExecutor
    from .scaluq_operator import ScaluqOperator

    Executor.register("scaluq")(ScaluqExecutor)

    __all__ = [
        "ScaluqCircuit",
        "ScaluqExecutor",
        "ScaluqOperator",
    ]

except ImportError as e:
    import warnings

    warnings.warn(
        f"Scaluq executor plugin not available: {e}. "
        "Install with: pip install qc-executor-scaluq",
        UserWarning,
    )
    raise
