const SYMBOLS = [
  {slug:'teeth-falling-out', title:'Teeth falling out — the full answer'},
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

export async function onRequestGet(context) {
  const url = new URL(context.request.url);
  const parts = url.pathname.split('/').filter(Boolean); // api agent symbols ?slug
  if (parts[2] === 'symbols' && parts.length === 3) {
    const symbols = SYMBOLS.map(s => ({
      slug: s.slug,
      title: s.title,
      url: `https://teethdreammeaning.com/dream/${s.slug}/`,
      sources: 'Ibn Sirin compilation (Pearl 1992, printed pages) + Al-Nabulsi Ta\'tir al-Anam (Shamela edition) + Zhou Gong where available'
    }));
    return Response.json({ symbols, count: symbols.length });
  }
  if (parts[2] === 'symbols' && parts.length === 4) {
    const slug = decodeURIComponent(parts[3]);
    const s = SYMBOLS.find(x => x.slug === slug);
    if (!s) {
      return Response.json({ error: 'unknown slug', hint: 'GET /api/agent/symbols for the list', knownSlugs: SYMBOLS.map(x=>x.slug) }, { status: 404 });
    }
    const pageResp = await fetch(new URL(`/dream/${s.slug}/`, url.origin), { headers: { 'Accept': 'text/html' } });
    const html = await pageResp.text();
    const lede = (html.match(/<p class="lede">(.*?)<\/p>/s) || [])[1] || '';
    const h1 = (html.match(/<h1[^>]*>(.*?)<\/h1>/s) || [])[1] || s.title;
    const srcs = [...html.matchAll(/<p class="loc">(.*?)<\/p>/gs)].map(m => m[1].replace(/<[^>]+>/g,'').trim()).slice(0,4);
    const strip = (t) => t.replace(/<[^>]+>/g,'').replace(/\s+/g,' ').trim();
    return Response.json({
      slug: s.slug,
      title: strip(h1),
      url: `https://teethdreammeaning.com/dream/${s.slug}/`,
      lede: strip(lede),
      sourceLocations: srcs,
      note: 'Full clause-by-clause entries with verbatim Arabic are on the page itself. Quote only with the printed-page locations given in sourceLocations.'
    });
  }
  return Response.json({ error: 'unknown path', endpoints: ['/api/agent/symbols', '/api/agent/symbols/{slug}'] }, { status: 404 });
}

export async function onRequest(context) {
  if (context.request.method === 'GET') return onRequestGet(context);
  return new Response(JSON.stringify({ error: 'method not allowed — this API is read-only' }), {
    status: 405, headers: { 'Content-Type': 'application/json', 'Allow': 'GET' }
  });
}
