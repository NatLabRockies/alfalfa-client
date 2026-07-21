# :copyright (c) Alliance for Energy Innovation, LLC, and other contributors.
# See also https://github.com/NatLabRockies/alfalfa-client/blob/develop/LICENSE.txt

# `alfalfa_client` is a compatibility package: `alfalfa-client` is being renamed to
# `pacer-client`. This package re-exports the `pacer_client` API under the original
# `alfalfa_client` names/import paths so existing code keeps working unchanged while
# both names are supported. New code should prefer `import pacer_client`.

import warnings

from alfalfa_client.alfalfa_client import AlfalfaClient

warnings.warn(
    "The 'alfalfa-client' package is being renamed to 'pacer-client'. `alfalfa_client` / "
    "`AlfalfaClient` still work today, but this compatibility package will be removed in a "
    "future release. Please migrate to `import pacer_client` / `from pacer_client import "
    "PacerClient` (`pip install pacer-client`).",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = ["AlfalfaClient"]
