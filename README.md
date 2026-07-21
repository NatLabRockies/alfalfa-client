# Pacer Client

The purpose of this repository is to provide a standalone client for use with the Alfalfa application. It additionally includes a Historian to quickly/easily enable saving of results from Alfalfa simulations.

## Usage

This repo is packaged and hosted on [PyPI here](https://pypi.org/project/pacer-client/).

```bash
pip install pacer-client
```

```python
from pacer_client.pacer_client import PacerClient

client = PacerClient("http://localhost")
```

Additional documentation for the functions of `pacer-client` can be found [here](https://natlabrockies.github.io/alfalfa-client/).

## Development

Prerequisites:

- [poetry](https://python-poetry.org/docs/#installation) for managing environment

Cloning and Installing:

```bash
git clone https://github.com/NatLabRockies/alfalfa-client.git
cd alfalfa-client
poetry install
```

Running Tests:
All `pacer-client` tests currently require a running instance of [Alfalfa](https://github.com/NREL/alfalfa) with at least 2 workers.

```bash
poetry run pytest -m integration
```

## Releasing

Every PR must carry at least one categorization label (`breaking`, `enhancement`, `bug`, `dependencies`,
`github_actions`, `python`, `documentation`, `add test`, or `do not publish` to exclude it) — this is enforced by
the `Verify Pull Request Labeling` CI check and is what allows GitHub to group the auto-generated release notes
correctly, per `.github/release.yml`.

1. Confirm all PRs intended for the release are merged into `develop`, are labeled correctly, and CI is passing.
1. Bump the version on `develop` (assume version is 0.1.2): `poetry version 0.1.2`, open a PR, and merge it once tests pass.
1. Fast-forward `main` to `develop` so both branches point at the same commit (do **not** create a merge commit):
   ```bash
   git checkout main
   git merge --ff-only develop
   git push origin main
   ```
   If `--ff-only` fails, `main` and `develop` have diverged (e.g. a hotfix landed only on `main`) — reconcile that first so the release doesn't leave the branches out of sync.
1. Draft a release on the GitHub repository targeting `main` (tag `v0.1.2`) and click **"Generate release notes"**
   (UI), or run `gh release create v0.1.2 --target main --generate-notes --draft` — do not publish yet.
1. Copy the generated "## What's Changed" notes into `CHANGELOG.MD` as a new `# pacer-client Version 0.1.2` entry
   at the top of the file (see existing entries for the format), cleaning up wording/spelling as needed. Commit
   this alongside the version bump PR, or as a quick follow-up commit on `main`.
1. Publish the drafted release. This triggers the `PyPIRelease` workflow (`.github/workflows/pypi_release.yml`),
   which builds the package and publishes it to PyPI via trusted publishing — no manual `poetry build`/`poetry
publish` needed.
1. Confirm the new version appears on [PyPI](https://pypi.org/project/pacer-client/) and that the release notes
   and `CHANGELOG.MD` match.
