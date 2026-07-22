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

> **Renaming from `alfalfa-client`:** this project was renamed from `alfalfa-client`/`AlfalfaClient` to
> `pacer-client`/`PacerClient`. During the transition, both names keep working: `AlfalfaClient` is an alias of
> `PacerClient`, and the `alfalfa_client` package/`pip install alfalfa-client` continue to be published with
> identical functionality (see `alfalfa_client/__init__.py`). `import alfalfa_client` (in any form) emits a
> `DeprecationWarning` pointing you to `pacer_client`; the `alfalfa-client` name and imports will eventually be
> removed, so new code should prefer `pacer_client`/`PacerClient`.

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
All `pacer-client` tests currently require a running instance of [Alfalfa](https://github.com/NatLabRockies/alfalfa) with at least 2 workers.

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
1. Copy the generated "## What's Changed" notes into `CHANGELOG.md` under the `# Unreleased` section, then (as part of the release) rename that header to `# pacer-client Version 0.1.2` and add the `**Full Changelog**` line.
1. Commit this alongside the version bump PR, or as a quick follow-up commit on `main`.
1. Publish the drafted release. This triggers the `PyPIRelease` workflow (`.github/workflows/pypi_release.yml`),
   which builds the package **twice** (once as `pacer-client`, once with the name swapped to `alfalfa-client`) and
   publishes both to PyPI via trusted publishing — no manual `poetry build`/`poetry publish` needed. Both
   distributions have identical contents; this keeps `pip install alfalfa-client` working during the rename
   transition (see the note in the README's Usage section). Publishing to `alfalfa-client` requires a Trusted
   Publisher to be configured on that PyPI project pointing at the `pypi_release_alfalfa` environment — set this
   up once on [pypi.org](https://pypi.org/manage/project/alfalfa-client/settings/publishing/) before the first
   release after this change.
1. Confirm the new version appears on both [pacer-client](https://pypi.org/project/pacer-client/) and
   [alfalfa-client](https://pypi.org/project/alfalfa-client/) on PyPI, and that the release notes and
   `CHANGELOG.md` match.
