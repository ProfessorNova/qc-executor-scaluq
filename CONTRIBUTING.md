# Contributing to qc-executor-scaluq

Thank you for your interest in contributing! This document covers everything you
need to get started.

## Development Setup

Prerequisites: [uv](https://docs.astral.sh/uv/getting-started/installation/) installed.

```bash
git clone https://github.com/ProfessorNova/qc-executor-scaluq.git
cd qc-executor-scaluq
uv sync --group dev
```

Run the test suite:

```bash
uv run pytest tests/
```

## Branching Strategy

- `main` – stable, released code
- Feature branches: `feat/<short-description>`
- Bug fixes: `fix/<short-description>`
- Infrastructure / CI: `chore/<short-description>`

Open a PR against `main`. For significant features, open an issue first to
discuss the design.

## Code Style

This project uses [Black](https://black.readthedocs.io/) with a line length of 99.

```bash
uv run black -l 99 src tests
```

Linting via [Pylint](https://pylint.readthedocs.io/):

```bash
uv run pylint src/qc_executor_scaluq
```

Both are checked automatically in CI on every PR.

### Docstrings

Use Google-style Python docstrings across the project.

- Use section headers like `Args:`, `Returns:`, and `Raises:`.
- Do not use NumPy-style headers like `Parameters`/`Returns` with dashed
  underlines.
- Keep argument and return types aligned with function signatures.

## Executor Contract

The plugin contract is defined by the
[QC Executor framework](https://github.com/flaqship/qc-executor) (this plugin
targets v0.1.0). `ScaluqExecutor` implements the abstract methods declared on
[`ExecutorBase`](https://github.com/flaqship/qc-executor/blob/main/src/qc_executor/base/executor_base.py):

| Method | What it does |
| ------ | ------------ |
| `_expectation_value` | Return the expectation value of an observable on a circuit. |
| `_expectation_value_derivatives` | Return analytic gradients of the expectation value. |
| `_sample` | Return measurement-shot counts. |
| `_statevector` | Return the full statevector. |
| `_transpile_circuit` | Convert a generic circuit into a Scaluq-native circuit. |
| `_transpile_operator` | Convert a generic operator into a Scaluq-native operator. |
| `get_accepted_backend_types` | List native backend/device classes for auto-detection. |
| `get_accepted_backend_aliases` | List string aliases the factory routes here. |

The executor is registered with the factory through the `qc_executor.backends`
entry point in `pyproject.toml`:

```toml
[project.entry-points."qc_executor.backends"]
scaluq = "qc_executor_scaluq:ScaluqExecutor"
```

## Changelog

Every PR that changes user-facing behaviour should add an entry to
[CHANGELOG.md](CHANGELOG.md) under the `[Unreleased]` section.

## Releasing (Maintainers)

1. Update the version in `src/qc_executor_scaluq/__init__.py`
2. Move the `[Unreleased]` section in `CHANGELOG.md` to a new versioned section
3. Commit: `git commit -m "chore: release vX.Y.Z"`
4. Tag: `git tag vX.Y.Z && git push --tags`
5. Create a GitHub Release – the `publish.yml` workflow builds and uploads the
   package to PyPI automatically via
   [trusted publishing](https://docs.pypi.org/trusted-publishers/).
