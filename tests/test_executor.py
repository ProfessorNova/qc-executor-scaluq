"""Tests for ScaluqExecutor.

Methods that are not implemented yet are asserted to raise
``NotImplementedError``.
"""

from __future__ import annotations

import pytest
from qc_executor.factory import Executor

from qc_executor_scaluq import ScaluqExecutor


def test_remote_property_is_local(scaluq_executor) -> None:
    """Scaluq runs locally, so the executor is not remote."""
    assert scaluq_executor.remote is False


def test_get_accepted_backend_types(scaluq_executor) -> None:
    """No backend object types are registered for auto-detection."""
    assert scaluq_executor.get_accepted_backend_types() == []


def test_get_accepted_backend_aliases(scaluq_executor) -> None:
    """No backend aliases are registered."""
    assert scaluq_executor.get_accepted_backend_aliases() == []


def test_factory_forwards_configuration() -> None:
    """The factory should pass constructor kwargs straight through to the plugin."""
    executor = Executor.create("scaluq", shots=1024, seed=42)
    assert isinstance(executor, ScaluqExecutor)
    config = executor.get_config()
    assert config["shots"] == 1024
    assert config["seed"] == 42


def test_switch_backend_preserves_configuration() -> None:
    """``switch_backend`` round-trips this plugin's configuration."""
    executor = Executor.create("scaluq", shots=1024, seed=42)
    switched = executor.switch_backend("scaluq", shots=2048)
    assert isinstance(switched, ScaluqExecutor)
    assert switched.get_config()["shots"] == 2048
    assert switched.get_config()["seed"] == 42


def test_expectation_value_stub(scaluq_executor) -> None:
    """``expectation_value`` is not implemented yet."""
    with pytest.raises(NotImplementedError):
        scaluq_executor.expectation_value(circuit=None, observable=None)


def test_expectation_value_derivatives_stub(scaluq_executor) -> None:
    """``expectation_value_derivatives`` is not implemented yet."""
    with pytest.raises(NotImplementedError):
        scaluq_executor.expectation_value_derivatives(circuit=None, observable=None)


def test_sample_stub(scaluq_executor) -> None:
    """``sample`` is not implemented yet."""
    with pytest.raises(NotImplementedError):
        scaluq_executor.sample(circuit=None)


def test_statevector_stub(scaluq_executor) -> None:
    """``statevector`` is not implemented yet."""
    with pytest.raises(NotImplementedError):
        scaluq_executor.statevector(circuit=None)


def test_transpile_circuit_stub(scaluq_executor) -> None:
    """``transpile_circuit`` is not implemented yet."""
    with pytest.raises(NotImplementedError):
        scaluq_executor.transpile_circuit(circuit=None)


def test_transpile_operator_stub(scaluq_executor) -> None:
    """``transpile_operator`` is not implemented yet."""
    with pytest.raises(NotImplementedError):
        scaluq_executor.transpile_operator(operator=None)
