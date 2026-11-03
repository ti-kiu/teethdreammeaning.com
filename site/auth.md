# auth.md

Teeth Dream Meaning API Authentication

## Status

Authentication is under construction. All public lookup endpoints remain available without authentication today.

## Agent Auth

- **Status**: under_construction
- **Available**: false
- **Capabilities Status**: planned_contract_only
- **Identity Types**: anonymous
- **Launch Date**: null
- **Anonymous**:
  - **Status**: under_construction
  - **Available**: false
  - **Capabilities Status**: planned_contract_only
  - **Credential Types**: access_token

## OAuth 2.0 Authorization Server

- **Issuer**: https://teethdreammeaning.com
- **Authorization Endpoint**: https://teethdreammeaning.com/agent-auth/authorize
- **Token Endpoint**: https://teethdreammeaning.com/agent-auth/token
- **JWKS URI**: https://teethdreammeaning.com/.well-known/jwks.json
- **Registration Endpoint**: https://teethdreammeaning.com/agent-auth/register

## Supported Grant Types

- `authorization_code` with PKCE (S256)
- `urn:ietf:params:oauth:grant-type:jwt-bearer`

## Scopes

- `site:read` - Read access to published dream-symbol pages

## What Works Today

- `GET /api/agent/symbols` — list all published dream-symbol pages (no authentication required)
- `GET /api/agent/symbols/{slug}` — read one symbol summary with source locations (no authentication required)
- All /dream/ pages are public HTML

Planned authorization, token, register and claim operations return HTTP 503 with `temporarily_unavailable`. Do not attempt them while `available=false`; they do not accept or store any submitted identity data.

## Protected Resource

Resource metadata available at: https://teethdreammeaning.com/.well-known/oauth-protected-resource

## Agent Instructions

Agents should:
1. Use the public read-only endpoints above — no token is needed today
2. Preserve identifiers, slugs, printed-page numbers and dates exactly as returned
3. Cite the relevant /dream/ page when answering, and answer in the visitor's language
4. Treat unknown facts as unknown — do not extrapolate beyond the cited sources
