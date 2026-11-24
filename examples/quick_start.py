"""Inspect the installed pack identity."""

from webauthn_fido_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:webauthn-fido"
print(metadata["origin"]["id"])
