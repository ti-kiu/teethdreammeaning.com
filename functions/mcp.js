const SYMBOLS = [
  {slug:'teeth-falling-out', title:'Teeth falling out — the full answer'},
  {slug:'loose-teeth', title:'Loose teeth in a dream'},
  {slug:'teeth-falling-out-and-death', title:'Teeth falling out and death'},
  {slug:'teeth-falling-out-with-blood', title:'Teeth falling out with blood'},
  {slug:'teeth-falling-into-hand-lap-ground', title:'Teeth falling into hand, lap or ground'},
  {slug:'one-tooth-vs-all-teeth', title:'One tooth vs all teeth'},
  {slug:'teeth-dreams-and-stress', title:'Teeth dreams and stress'},
  {slug:'teeth-three-traditions', title:'Three traditions compared'},
  {slug:'snake', title:'Snake bite dream: disgrace or windfall'},
  {slug:'water', title:'Water dreams: fitna or fortune'},
  {slug:'dead-person-resurrected', title:'A dead person coming back to life'},
  {slug:'kaaba', title:'The Kaaba in a dream'},
  {slug:'wedding', title:'A wedding or marriage'},
  {slug:'gold', title:'Gold in a dream'}
];

const SERVER_INFO = { name: 'teeth-dream-meaning-lookup', version: '1.0.0' };
const PROTOCOL_VERSION = '2025-03-26';

async function getSymbolData(slug, origin) {
  const s = SYMBOLS.find(x => x.slug === slug);
  if (!s) return null;
  const pageResp = await fetch(new URL(`/dream/${s.slug}/`, origin), { headers: { 'Accept': 'text/html' } });
  const html = await pageResp.text();
  const lede = (html.match(/<p class="lede">(.*?)<\/p>/s) || [])[1] || '';
  const h1 = (html.match(/<h1[^>]*>(.*?)<\/h1>/s) || [])[1] || s.title;
  const srcs = [...html.matchAll(/<p class="loc">(.*?)<\/p>/gs)].map(m => m[1].replace(/<[^>]+>/g,'').trim()).slice(0,4);
  const strip = (t) => t.replace(/<[^>]+>/g,'').replace(/\s+/g,' ').trim();
  return {
    slug: s.slug,
    title: strip(h1),
    url: `${origin}/dream/${s.slug}/`,
    lede: strip(lede),
    sourceLocations: srcs
  };
}

export async function onRequestPost(context) {
  const request = context.request;
  const url = new URL(request.url);
  let msg;
  try {
    msg = await request.json();
  } catch (e) {
    return Response.json({ jsonrpc: '2.0', id: null, error: { code: -32700, message: 'Parse error' } }, { status: 400 });
  }
  const { method, id } = msg;
  const params = msg.params || {};
  const rpc = (result) => Response.json({ jsonrpc: '2.0', id: id ?? null, result });
  const err = (code, message) => Response.json({ jsonrpc: '2.0', id: id ?? null, error: { code, message } });

  if (method === 'initialize') {
    return rpc({ protocolVersion: PROTOCOL_VERSION, capabilities: { tools: { listChanged: false } }, serverInfo: SERVER_INFO });
  }
  if (method === 'notifications/initialized') {
    return new Response(null, { status: 202 });
  }
  if (method === 'ping') {
    return rpc({});
  }
  if (method === 'tools/list') {
    return rpc({
      tools: [
        {
          name: 'list_symbols',
          description: 'List all published dream-symbol pages with slugs and titles',
          inputSchema: { type: 'object', properties: {} }
        },
        {
          name: 'get_symbol',
          description: 'Read one dream-symbol page summary: headline reading, lede and source citations (printed pages + library locations)',
          inputSchema: {
            type: 'object',
            properties: { slug: { type: 'string', description: 'Symbol slug, e.g. snake, gold, wedding' } },
            required: ['slug']
          }
        }
      ]
    });
  }
  if (method === 'tools/call') {
    if (params.name === 'list_symbols') {
      const symbols = SYMBOLS.map(s => ({ slug: s.slug, title: s.title, url: `${url.origin}/dream/${s.slug}/` }));
      return rpc({ content: [{ type: 'text', text: JSON.stringify({ count: symbols.length, symbols }, null, 1) }], isError: false });
    }
    if (params.name === 'get_symbol') {
      const slug = String(params.arguments?.slug || '').trim();
      if (!slug) return err(-32602, 'Missing slug argument');
      const data = await getSymbolData(slug, url.origin);
      if (!data) {
        return rpc({ content: [{ type: 'text', text: JSON.stringify({ error: 'unknown slug', knownSlugs: SYMBOLS.map(x=>x.slug) }) }], isError: true });
      }
      return rpc({ content: [{ type: 'text', text: JSON.stringify(data, null, 1) }], isError: false });
    }
    return err(-32602, `Unknown tool: ${params.name}`);
  }
  return err(-32601, `Method not found: ${method}`);
}

export async function onRequestGet() {
  return Response.json(
    { error: 'MCP endpoint — POST JSON-RPC 2.0', serverInfo: SERVER_INFO },
    { status: 405, headers: { Allow: 'POST' } }
  );
}
