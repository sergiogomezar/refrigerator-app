#!/usr/bin/env python3
"""Headless layout probe for the Freezai demo.

Walks every beat on both devices and reports any clipped view, overflowing rail or
horizontal scroll. Run it after touching layout, spacing or type:

    python3 tools/probe.py                 # the five rehearsal sizes
    python3 tools/probe.py 1600x950        # one size
    python3 tools/probe.py -f restaurantes.html   # another demo file

It works by writing a throwaway copy of index.html with a measuring script appended,
so everything runs in a single document. The older iframe harness (tools/probe.html)
cannot read the frame under file:// because Chrome treats each file as its own origin.

Caveat: headless and offline, the web fonts never load, so the measurements use
fallback metrics and are a close approximation, not the exact projector layout.
"""

import json, os, re, subprocess, sys, tempfile

CHROME = "/home/sergio/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome"
HERE = os.path.dirname(os.path.abspath(__file__))
DEMO = os.path.dirname(HERE)
SIZES = ["1920x1080", "1600x950", "1440x900", "1366x768", "1280x720"]

MEASURE = """
<script>
(async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const out = document.createElement('pre');
  out.id = 'probeout';
  out.style.cssText = 'position:fixed;left:-9999px';
  document.body.appendChild(out);
  try {
    let D = null;
    for (let t = 0; t < 200 && !D; t++){ D = window.Demo; if (!D) await sleep(50); }
    if (!D){ out.textContent = 'RESULT ' + JSON.stringify({error:'no Demo'}); return; }
    await sleep(250);
    const d = document, rows = [];
    for (const dev of ['mobile','tablet']){
      d.body.dataset.device = dev;
      window.dispatchEvent(new Event('resize'));
      await sleep(80);
      for (let i = 0; i < D.count; i++){
        D.goto(i); D.pause();
        await sleep(60);
        const view = d.querySelector('.view.is-on');
        const rail = d.querySelector('.rail');
        const cap = d.querySelector('.caption').getBoundingClientRect();
        const tra = d.querySelector('.transport').getBoundingClientRect();
        const wr  = d.getElementById('deviceWrap').getBoundingClientRect();
        const dv  = d.getElementById('device').getBoundingClientRect();
        rows.push({
          dev: dev, i: i, id: D.ids[i],
          view: view ? view.dataset.view : null,
          vOver: view ? view.scrollHeight - view.clientHeight : 0,
          rOver: rail.scrollHeight - rail.clientHeight,
          hOver: d.documentElement.scrollWidth - d.documentElement.clientWidth,
          bOver: d.body.scrollHeight - d.body.clientHeight,
          /* the caption sits next to the transport: any bleed means it ran under the buttons */
          cap: Math.round(cap.right - tra.left),
          capH: Math.round(cap.height),
          /* the phone must sit whole inside its wrapper, top and bottom */
          devClip: Math.round(Math.max(wr.top - dv.top, dv.bottom - wr.bottom))
        });
      }
    }
    out.textContent = 'RESULT ' + JSON.stringify(rows);
  } catch (e) {
    out.textContent = 'RESULT ' + JSON.stringify({error:String(e && e.stack || e)});
  }
})();
</script>
"""

UNESCAPE = [("&quot;", '"'), ("&#39;", "'"), ("&lt;", "<"), ("&gt;", ">"), ("&amp;", "&")]


def build_runner(name="index.html"):
    with open(os.path.join(DEMO, name), encoding="utf-8") as fh:
        html = fh.read()
    assert "</body>" in html
    fd, path = tempfile.mkstemp(prefix="_probe-", suffix=".html", dir=DEMO)
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(html.replace("</body>", MEASURE + "</body>", 1))
    return path


def run(path, size):
    w, h = size.split("x")
    dom = subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
         "--window-size=%s,%s" % (w, h), "--virtual-time-budget=90000", "--dump-dom",
         "file://" + path],
        capture_output=True, text=True, timeout=180).stdout
    m = re.search(r'<pre id="probeout"[^>]*>(.*?)</pre>', dom, re.S)
    if not m or not m.group(1).strip():
        return None
    raw = m.group(1).strip()
    for a, b in UNESCAPE:
        raw = raw.replace(a, b)
    return json.loads(raw[len("RESULT "):])


def main():
    argv = sys.argv[1:]
    name = "index.html"
    if "-f" in argv:
        k = argv.index("-f")
        name = argv[k + 1]
        argv = argv[:k] + argv[k + 2:]
    sizes = argv or SIZES
    path = build_runner(name)
    failed = False
    try:
        for size in sizes:
            rows = run(path, size)
            if rows is None:
                print("%-9s  sin salida" % size); failed = True; continue
            if isinstance(rows, dict):
                print("%-9s  error: %s" % (size, rows.get("error"))); failed = True; continue
            bad = [r for r in rows
                   if r["vOver"] > 0 or r["rOver"] > 0 or r["hOver"] > 0 or r["bOver"] > 0
                   or r["cap"] > 0 or r["devClip"] > 1]
            capH = max(r["capH"] for r in rows)
            print("%-9s  %d beats x 2 dispositivos  ·  %d desbordes  ·  pie max %dpx"
                  % (size, len(rows) // 2, len(bad), capH))
            for r in bad:
                failed = True
                print("    %-7s #%02d %-13s vista=%-3s vOver=%s rOver=%s hOver=%s bodyOver=%s capBleed=%s telClip=%s"
                      % (r["dev"], r["i"], r["id"], r["view"],
                         r["vOver"], r["rOver"], r["hOver"], r["bOver"], r["cap"], r["devClip"]))
    finally:
        os.unlink(path)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
