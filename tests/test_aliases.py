# :copyright (c) Alliance for Energy Innovation, LLC, and other contributors.
# See also https://github.com/NatLabRockies/alfalfa-client/blob/develop/LICENSE.txt

"""Guards the `alfalfa_client` / `AlfalfaClient` backwards-compatibility aliases.

`alfalfa-client` is being renamed to `pacer-client`; these names are kept working during
the transition period. If any of these assertions ever fail, the alias has drifted out
of sync with `pacer_client` and needs to be fixed before release.
"""

import importlib
import sys

import pytest

import pacer_client
from pacer_client.lib import AlfalfaAPIException, AlfalfaClientException, AlfalfaException, AlfalfaWorkerException
from pacer_client.pacer_client import PacerClient


def test_pacer_client_exposes_alfalfa_client_alias():
    assert pacer_client.AlfalfaClient is PacerClient


def test_alfalfa_client_import_emits_deprecation_warning():
    # Force a fresh import so the module-level warning fires again, regardless of
    # whether an earlier test already imported (and cached) `alfalfa_client`.
    for name in list(sys.modules):
        if name == "alfalfa_client" or name.startswith("alfalfa_client."):
            del sys.modules[name]

    with pytest.warns(DeprecationWarning, match="pacer-client"):
        importlib.import_module("alfalfa_client")


def test_alfalfa_client_package_alias():
    import alfalfa_client

    assert alfalfa_client.AlfalfaClient is PacerClient


def test_alfalfa_client_module_alias():
    from alfalfa_client.alfalfa_client import AlfalfaClient
    from alfalfa_client.alfalfa_client import PacerClient as ShimPacerClient

    assert AlfalfaClient is PacerClient
    assert ShimPacerClient is PacerClient


def test_alfalfa_client_lib_alias():
    from alfalfa_client.lib import (
        AlfalfaAPIException as ShimAPIException,
    )
    from alfalfa_client.lib import (
        AlfalfaClientException as ShimClientException,
    )
    from alfalfa_client.lib import (
        AlfalfaException as ShimException,
    )
    from alfalfa_client.lib import (
        AlfalfaWorkerException as ShimWorkerException,
    )

    assert ShimException is AlfalfaException
    assert ShimAPIException is AlfalfaAPIException
    assert ShimClientException is AlfalfaClientException
    assert ShimWorkerException is AlfalfaWorkerException
