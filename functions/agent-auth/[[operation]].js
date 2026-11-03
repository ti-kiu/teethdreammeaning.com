export async function onRequest(context) {
  const { request, params } = context;
  const headers = { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' };
  if (request.method !== 'GET' && request.method !== 'POST') {
    return new Response(JSON.stringify({ status: 'under_construction', available: false, error: 'temporarily_unavailable' }), { status: 405, headers: { ...headers, 'Allow': 'GET, POST' } });
  }
  let op = 'This authentication operation';
  try {
    const p = params && params.operation;
    if (p) {
      const parts = Array.isArray(p) ? p : String(p).split('/').filter(Boolean);
      if (parts.length && parts[0]) op = `Authentication operation "${parts[0]}"`;
    }
  } catch (e) { /* keep default label */ }
  return new Response(JSON.stringify({
    status: 'under_construction',
    available: false,
    error: 'temporarily_unavailable',
    error_description: `Coming soon. ${op} is not available yet. All public lookup endpoints remain open without authentication — use GET /api/agent/symbols or GET /api/agent/symbols/{slug}.`,
    launch_date: null
  }), { status: 503, headers });
}
