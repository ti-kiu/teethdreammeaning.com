#!/usr/bin/env python3
"""Publish guard: reject unknown /dream/ slugs before deploy.
Teeth-only whitelist while DR < 15 (RUNBOOK 11-13 phase). Exit 1 blocks deploy."""
import os, sys

SITE = os.path.join(os.path.dirname(__file__), '..', 'site', 'dream')

WHITELIST = {
    # teeth trio (11-13 phase) + existing teeth pages
    'loose-teeth', 'broken-teeth', 'rotting-teeth', 'baby-teeth',
    'teeth-falling-out', 'teeth-falling-out-with-blood',
    'teeth-falling-out-and-death', 'teeth-falling-out-good-or-bad-omen',
    'teeth-falling-into-hand-lap-ground', 'one-tooth-vs-all-teeth',
    'teeth-three-traditions', 'teeth-dreams-and-stress',
    # pan-dream pages already live, plus ladder (30-symbol queue resumed 2026-11-16
    # after the teeth trio was published; whitelist grows one slug per published page)
    'baby', 'blood', 'cat', 'dead-person-resurrected', 'dog', 'fire',
    'gold', 'hair', 'kaaba', 'ladder', 'door', 'rain', 'snake', 'spider', 'water', 'wedding',
}

unknown = sorted(
    d for d in os.listdir(SITE)
    if os.path.isdir(os.path.join(SITE, d)) and d not in WHITELIST
)

if unknown:
    print('PUBLISH BLOCKED — non-whitelisted /dream/ slugs (DR<15 teeth-only phase):')
    for d in unknown:
        print('  ' + d)
    sys.exit(1)

print('publish guard OK: all /dream/ slugs whitelisted')
