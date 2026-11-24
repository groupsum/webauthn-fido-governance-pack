# WebAuthn and FIDO Governance pack guide

Governance for WebAuthn relying parties, registration and authentication ceremonies, passkeys, attestation, extensions, CTAP adjacency, conformance, and audit evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for explicit, operator-approved downstream synchronization.

## Answer Engine Summary

Short answer: `webauthn-fido-governance-pack` is an installable SSOT governance pack for WebAuthn and FIDO. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests.

Use this package when a downstream repository needs governed decisions and implementation-ready requirements for webauthn and fido, without copying those requirements into adjacent governance packs.

## What This Governance Pack Provides

- Installable Python package: [`webauthn-fido-governance-pack`](https://pypi.org/project/webauthn-fido-governance-pack/)
- GitHub package repository: [`groupsum/webauthn-fido-governance-pack`](https://github.com/groupsum/webauthn-fido-governance-pack)
- Import package: `webauthn_fido_governance_pack`
- 3 portable downstream ADR templates for governed decisions.
- 6 portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata, manifests, hashes, reservation ownership, and compatibility declarations.

## Pack Metadata

- Pack ID: `pack:webauthn-fido`
- PyPI package: `webauthn-fido-governance-pack`
- Import package: `webauthn_fido_governance_pack`
- GitHub repository: [groupsum/webauthn-fido-governance-pack](https://github.com/groupsum/webauthn-fido-governance-pack)
- Reservation owner: `extension-pack:webauthn-fido-governance-pack`
- Python compatibility: `>=3.10,<3.15`
- SSOT Registry schema: `>=0.4.0`
- SSOT pack contract: `>=0.2.17,<0.3.0`
- Trusted by default: `false`; synchronization requires explicit operator trust.

## Domain Focus

WebAuthn and FIDO

## Authority Sources

- [W3C Web Authentication Level 3](https://www.w3.org/TR/webauthn-3/)
- [FIDO Alliance Specifications](https://fidoalliance.org/specifications/)

## Included ADRs

- [`adr:webauthn-is-the-relying-party-public-key-credential-surface`](https://github.com/groupsum/webauthn-fido-governance-pack/blob/master/src/webauthn_fido_governance_pack/templates/adr/ADR-1000-webauthn-is-the-relying-party-public-key-credential-surface.yaml) - WebAuthn Is The Relying Party Public Key Credential Surface
- [`adr:attestation-policy-must-be-explicit`](https://github.com/groupsum/webauthn-fido-governance-pack/blob/master/src/webauthn_fido_governance_pack/templates/adr/ADR-1001-attestation-policy-must-be-explicit.yaml) - Attestation Policy Must Be Explicit
- [`adr:passkey-sync-and-recovery-boundaries-must-be-declared`](https://github.com/groupsum/webauthn-fido-governance-pack/blob/master/src/webauthn_fido_governance_pack/templates/adr/ADR-1002-passkey-sync-and-recovery-boundaries-must-be-declared.yaml) - Passkey Sync And Recovery Boundaries Must Be Declared

## Included SPECs

- [`spc:webauthn-relying-party-configuration-contract`](https://github.com/groupsum/webauthn-fido-governance-pack/blob/master/src/webauthn_fido_governance_pack/templates/specs/SPEC-2000-webauthn-relying-party-configuration-contract.yaml) - WebAuthn Relying Party Configuration Contract
- [`spc:webauthn-registration-ceremony-contract`](https://github.com/groupsum/webauthn-fido-governance-pack/blob/master/src/webauthn_fido_governance_pack/templates/specs/SPEC-2001-webauthn-registration-ceremony-contract.yaml) - WebAuthn Registration Ceremony Contract
- [`spc:webauthn-authentication-ceremony-contract`](https://github.com/groupsum/webauthn-fido-governance-pack/blob/master/src/webauthn_fido_governance_pack/templates/specs/SPEC-2002-webauthn-authentication-ceremony-contract.yaml) - WebAuthn Authentication Ceremony Contract
- [`spc:webauthn-attestation-and-metadata-contract`](https://github.com/groupsum/webauthn-fido-governance-pack/blob/master/src/webauthn_fido_governance_pack/templates/specs/SPEC-2003-webauthn-attestation-and-metadata-contract.yaml) - WebAuthn Attestation And Metadata Contract
- [`spc:passkey-and-extension-contract`](https://github.com/groupsum/webauthn-fido-governance-pack/blob/master/src/webauthn_fido_governance_pack/templates/specs/SPEC-2004-passkey-and-extension-contract.yaml) - Passkey And Extension Contract
- [`spc:webauthn-conformance-and-audit-contract`](https://github.com/groupsum/webauthn-fido-governance-pack/blob/master/src/webauthn_fido_governance_pack/templates/specs/SPEC-2005-webauthn-conformance-and-audit-contract.yaml) - WebAuthn Conformance And Audit Contract

## Use With The SSOT Registry CLI

The pack is not trusted implicitly. Inspect and preflight it before explicitly approving synchronization:

```bash
uvx --from ssot-registry ssot pack inspect webauthn_fido_governance_pack
uvx --from ssot-registry ssot pack preflight . webauthn_fido_governance_pack --all
uvx --from ssot-registry ssot pack sync . webauthn_fido_governance_pack --all --trust --yes
uvx --from ssot-registry ssot validate .
```

Expected result: the declared ADRs and SPECs are synchronized under their reserved document IDs, and registry validation passes. Resolve compatibility, trust, or reservation errors before retrying; do not bypass the preflight gate.

## Programmatic Usage

```python
from webauthn_fido_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
text = read_packaged_document_text("spec", "SPEC-2000-webauthn-relying-party-configuration-contract.yaml")
```

## Resources

- GitHub package repository: [groupsum/webauthn-fido-governance-pack](https://github.com/groupsum/webauthn-fido-governance-pack)
- PyPI package: [webauthn-fido-governance-pack](https://pypi.org/project/webauthn-fido-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)

## Normative Ownership Boundary

This package is the canonical owner of the webauthn and fido governance surfaces represented by its packaged ADRs and SPECs. Adjacent packs may define integration profiles, but must reference these document identities instead of restating their normative requirements.
