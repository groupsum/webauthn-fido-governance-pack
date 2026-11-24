"""Find a specification and its downstream path in the installed manifest."""

from webauthn_fido_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:webauthn-relying-party-configuration-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2000-webauthn-relying-party-configuration-contract.yaml"
