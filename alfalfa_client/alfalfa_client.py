# :copyright (c) Alliance for Energy Innovation, LLC, and other contributors.
# See also https://github.com/NatLabRockies/alfalfa-client/blob/develop/LICENSE.txt

# Compatibility shim for the pre-rename `alfalfa_client.alfalfa_client` module.
# `AlfalfaClient` and `PacerClient` are the same class; see `pacer_client.pacer_client`.

from pacer_client.pacer_client import ModelID, PacerClient, RunID
from pacer_client.pacer_client import PacerClient as AlfalfaClient

__all__ = ["AlfalfaClient", "ModelID", "PacerClient", "RunID"]
