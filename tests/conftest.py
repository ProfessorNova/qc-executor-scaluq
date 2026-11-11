"""Shared pytest fixtures for the Scaluq plugin tests."""

import pytest
from qc_executor.factory import Executor

# Importing the plugin package runs Executor.register(), so the factory below
# resolves "scaluq" without any extra wiring.
from qc_executor_scaluq import ScaluqExecutor


@pytest.fixture
def scaluq_executor() -> ScaluqExecutor:
    """Return a freshly-constructed ScaluqExecutor."""
    return Executor.create("scaluq")
