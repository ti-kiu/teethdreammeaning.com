export async function onRequest(context) {
  const request = context.request;
  const url = new URL(request.url);
  if (request.method !== 'GET') return context.next();
  const accept = request.headers.get('Accept') || '';
  const path = url.pathname;
  // Homepage only — auth.md, .well-known/*, /api/* must serve their own content
  if (accept.includes('text/markdown') && (path === '/' || path === '')) {
    const llmsResp = await fetch(new URL('/llms.txt', url.origin));
    if (llmsResp.ok) {
      const content = await llmsResp.text();
      const tokens = Math.ceil(content.split(/\s+/).filter(Boolean).length * 1.3);
      return new Response(content, {
        headers: {
          'Content-Type': 'text/markdown; charset=utf-8',
          'x-markdown-tokens': String(tokens),
          'Vary': 'Accept',
          'Cache-Control': 'public, max-age=3600'
        }
      });
    }
  }
  return context.next();
}
