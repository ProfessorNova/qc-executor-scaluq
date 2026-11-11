"""Tests that the plugin registers correctly with the QC Executor factory.

These are the tests that should keep passing after every change you make to
the plugin — if registration breaks, no other test will be meaningful.
"""

from importlib.metadata import entry_points

from qc_executor.factory import Executor

# Importing the plugin package runs Executor.register() as a side effect.
from qc_executor_scaluq import ScaluqExecutor


def test_backend_appears_in_available_backends() -> None:
    """Importing the plugin should expose ``scaluq`` to the factory."""
    assert "scaluq" in Executor.available_backends()


def test_factory_create_returns_scaluq_executor() -> None:
    """``Executor.create("scaluq")`` should return our executor."""
    instance = Executor.create("scaluq")
    assert isinstance(instance, ScaluqExecutor)


def test_entry_point_declared_in_pyproject_toml() -> None:
    """The ``qc_executor.backends`` entry point should be discoverable.

    This test passes once the package is installed (e.g. ``uv sync``);
    it confirms that ``pyproject.toml`` advertises the plugin to other
    code that never imports ``qc_executor_scaluq`` explicitly.
    """
    eps = entry_points(group="qc_executor.backends")
    names = {ep.name for ep in eps}
    assert "scaluq" in names, (
        "The 'qc_executor.backends' entry point group does not contain 'scaluq'. "
        "Reinstall the package with `uv sync` after changes to pyproject.toml."
    )
