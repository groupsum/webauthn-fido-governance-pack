# webauthn-fido-governance-pack

Governance for WebAuthn relying parties, registration and authentication ceremonies, passkeys, attestation, extensions, CTAP adjacency, conformance, and audit evidence.

## Package identity

- Pack ID: `pack:webauthn-fido`
- PyPI distribution: `webauthn-fido-governance-pack`
- Python import: `webauthn_fido_governance_pack`
- Reservation owner: `extension-pack:webauthn-fido-governance-pack`

## Normative ownership

This package is the canonical owner of the governance surfaces represented by its packaged ADRs and SPECs. Adjacent governance packs reference these documents rather than restating their requirements.

## Install

```bash
uv add webauthn-fido-governance-pack
uv run ssot pack sync . webauthn_fido_governance_pack --all --trust --yes
uv run ssot validate .
```

## Authority sources

- https://www.w3.org/TR/webauthn-3/
- https://fidoalliance.org/specifications/
