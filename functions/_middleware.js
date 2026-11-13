// Root middleware: runs for every route before route-level functions.
// Canonical host is the apex (non-www). 301 www -> apex, path+query preserved, single hop.
export async function onRequest(context) {
  const url = new URL(context.request.url);
  if (url.hostname === 'www.teethdreammeaning.com') {
    const target = 'https://teethdreammeaning.com' + url.pathname + url.search;
    return Response.redirect(target, 301);
  }
  return context.next();
}
