(function() {
  'use strict';
  var mc = (typeof document !== 'undefined' && document.modelContext) ||
           (typeof navigator !== 'undefined' && navigator.modelContext);
  if (!mc || typeof mc.registerTool !== 'function') return;
  var controller = new AbortController();

  var SYMBOLS = [
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

  mc.registerTool({
    name: 'list_dream_symbols',
    description: 'List all published dream-symbol pages on Teeth Dream Meaning with slugs and titles',
    inputSchema: { type: 'object', properties: {} },
    execute: async function() {
      return { symbols: SYMBOLS.map(function(s){ return { slug: s.slug, title: s.title, url: 'https://teethdreammeaning.com/dream/' + s.slug + '/' }; }), count: SYMBOLS.length };
    },
    signal: controller.signal
  });

  mc.registerTool({
    name: 'get_dream_symbol',
    description: 'Read one dream-symbol page summary: headline reading, lede paragraph and source citations (printed pages + library locations) from the Ibn Sirin compilation and Al-Nabulsi',
    inputSchema: {
      type: 'object',
      properties: { slug: { type: 'string', description: 'Symbol slug, e.g. snake, gold, wedding, teeth-falling-out' } },
      required: ['slug']
    },
    execute: async function(params) {
      var slug = String(params && params.slug || '').trim();
      var s = SYMBOLS.find(function(x){ return x.slug === slug; });
      if (!s) return { error: 'unknown slug', knownSlugs: SYMBOLS.map(function(x){ return x.slug; }) };
      var resp = await fetch('/dream/' + slug + '/', { headers: { 'Accept': 'text/html' }, signal: controller.signal });
      var html = await resp.text();
      var strip = function(t){ return t.replace(/<[^>]+>/g,'').replace(/\s+/g,' ').trim(); };
      var ledeM = html.match(/<p class="lede">(.*?)<\/p>/s);
      var h1M = html.match(/<h1[^>]*>(.*?)<\/h1>/s);
      var srcs = [];
      var re = /<p class="loc">(.*?)<\/p>/gs, m;
      while ((m = re.exec(html)) && srcs.length < 4) srcs.push(strip(m[1]));
      return {
        slug: slug,
        title: h1M ? strip(h1M[1]) : s.title,
        url: 'https://teethdreammeaning.com/dream/' + slug + '/',
        lede: ledeM ? strip(ledeM[1]) : '',
        sourceLocations: srcs
      };
    },
    signal: controller.signal
  });
})();
