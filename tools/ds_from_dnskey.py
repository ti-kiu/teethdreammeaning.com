#!/usr/bin/env python3
"""Compute the authoritative DS record for teethdreammeaning.com from live DNSKEY (RFC 4034).

Run after enabling DNSSEC in Cloudflare. Verifies the Cloudflare-displayed DS
against the live zone — catches truncated/registrar paste errors for free.
"""
import urllib.request, json, hashlib, base64, re

def doh(name, rtype):
    url = f"https://cloudflare-dns.com/dns-query?name={name}&type={rtype}"
    req = urllib.request.Request(url, headers={'accept': 'application/dns-json'})
    return json.load(urllib.request.urlopen(req, timeout=20))

d = doh('teethdreammeaning.com', 'DNSKEY')
keys = d.get('Answer', [])
print(f"DNSKEY records found: {len(keys)}")
for a in keys:
    data = a['data'].replace(' ', '')
    # DoH may strip spaces: flags(4) proto(2) alg(2) are fixed-width hex-in-b64 layout.
    # Robust parse: DNSKEY rdata = flags u16, proto u8, alg u8, then base64 pubkey.
    # When spaces are stripped, decode via wire layout: total b64 decodes to 4+N bytes.
    raw = base64.b64decode(data + '=' * (-len(data) % 4))
    # Some DoH responses concatenate 'flags proto alg b64' without spaces; Cloudflare's
    # actual DNSKEY b64 starts with the 4-byte header inside the b64 blob itself.
    # If b64 starts with a plausible numeric prefix, parse textually first.
    m = re.match(r'^(\d{1,5})\s+(\d{1,3})\s+(\d{1,3})\s+([A-Za-z0-9+/=]+)$', a['data'].strip())
    if m:
        flags, proto, alg = int(m.group(1)), int(m.group(2)), int(m.group(3))
        pubkey_b64 = m.group(4)
        pubkey = base64.b64decode(pubkey_b64)
    else:
        raw = base64.b64decode(data + '=' * (-len(data) % 4))
        flags = int.from_bytes(raw[0:2], 'big')
        proto = raw[2]
        alg = raw[3]
        pubkey = raw[4:]
        pubkey_b64 = base64.b64encode(pubkey).decode()
    rdata = flags.to_bytes(2, 'big') + proto.to_bytes(1, 'big') + alg.to_bytes(1, 'big') + pubkey
    # key tag, RFC 4034 Appendix B
    ac = 0
    for i, b in enumerate(rdata):
        ac += (b << 8) if i % 2 == 0 else b
    ac += (ac >> 16) & 0xFFFF
    keytag = ac & 0xFFFF
    # SHA-256 digest: canonical owner name + rdata
    owner = 'teethdreammeaning.com'
    wire_name = b''.join(bytes([len(l)]) + l.encode() for l in owner.split('.')) + b'\x00'
    digest = hashlib.sha256(wire_name + rdata).hexdigest().upper()
    sep = 'KSK' if flags & 1 else 'ZSK'
    print(f"\nflags={flags} ({sep})  alg={alg}  keytag={keytag}")
    print(f"  pubkey b64 : {pubkey_b64}")
    print(f"  DS SHA256  : {keytag} 13 2 {digest}")
