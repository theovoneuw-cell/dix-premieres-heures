(function () {
  /* ---------- diagrammes d'accords ----------
     f : une case par corde, de mi grave à mi aigu. 'x' = étouffée, '0' = à vide.
     d : le doigt utilisé, '-' si aucun. (cases 1 à 9 seulement) */
  var CH = {
    Em:{f:'022000',d:'-23---',label:'Em'},      Am:{f:'x02210',d:'--231-',label:'Am'},
    D:{f:'xx0232',d:'---132',label:'D'},        G:{f:'320003',d:'21---3',label:'G'},
    C:{f:'x32010',d:'-32-1-',label:'C'},        Cadd9:{f:'x32033',d:'-21-34',label:'Cadd9'},
    A:{f:'x02220',d:'--123-',label:'A'},        A7:{f:'x02020',d:'--2-3-',label:'A7'},
    D7:{f:'xx0212',d:'---213',label:'D7'},      E7:{f:'020100',d:'-2-1--',label:'E7'},
    E:{f:'022100',d:'-231--',label:'E'},
    F4:{f:'xx3211',d:'--3211',label:'Fa (4 cordes)'},
    F:{f:'133211',d:'134211',label:'Fa barré',barre:{fret:1,from:0,to:5}},
    Bm:{f:'x24432',d:'-13421',label:'Bm',barre:{fret:2,from:1,to:5}},
    E7s9:{f:'x7678x',d:'-2134-',label:'E7♯9'},
    A6:{f:'xx767x',d:'--213-',label:'A6'},      G6:{f:'xx545x',d:'--213-',label:'G6'},
    D6:{f:'xxx777',d:'---111',label:'D6'},      C6:{f:'xxx555',d:'---111',label:'C6'},
    E6:{f:'xxx999',d:'---111',label:'E6'}
  };

  var L = 15, TOP = 22, GAP = 13.2, FH = 16.5, W = 96, NF = 5;
  function sx(i) { return L + i * GAP; }

  function svgFor(c) {
    var frettes = [], i;
    for (i = 0; i < 6; i++) {
      var ch = c.f[i];
      if (ch !== 'x' && ch !== '0') frettes.push(parseInt(ch, 10));
    }
    var mx = Math.max.apply(null, frettes.concat([1]));
    var mn = Math.min.apply(null, frettes.concat([99]));
    // position haute : on décale la fenêtre et on affiche le numéro de case
    var base = (mx <= NF) ? 0 : (mn - 1);
    function fy(n) { return TOP + FH * (n - base - 0.5); }

    var s = '<svg viewBox="0 0 ' + W + ' ' + (TOP + FH * NF + 6) + '" width="86" role="img" aria-label="Diagramme de ' + c.label + '">';
    if (base === 0) {
      s += '<rect x="' + (L - 0.5) + '" y="' + (TOP - 3.2) + '" width="' + (GAP * 5 + 1) + '" height="3.2" fill="currentColor"/>';
    } else {
      s += '<line x1="' + L + '" y1="' + TOP + '" x2="' + (L + GAP * 5) + '" y2="' + TOP + '" stroke="currentColor" stroke-width=".9" opacity=".55"/>';
      s += '<text x="' + (L - 5) + '" y="' + (TOP + FH * 0.72) + '" text-anchor="end" font-family="IBM Plex Mono, monospace" font-size="8" fill="currentColor" opacity=".7">' + (base + 1) + '</text>';
    }
    for (var n = 1; n <= NF; n++)
      s += '<line x1="' + L + '" y1="' + (TOP + FH * n) + '" x2="' + (L + GAP * 5) + '" y2="' + (TOP + FH * n) + '" stroke="currentColor" stroke-width=".7" opacity=".34"/>';
    for (i = 0; i < 6; i++)
      s += '<line x1="' + sx(i) + '" y1="' + TOP + '" x2="' + sx(i) + '" y2="' + (TOP + FH * NF) + '" stroke="currentColor" stroke-width=".7" opacity=".34"/>';

    if (c.barre) {
      var x1 = sx(c.barre.from), x2 = sx(c.barre.to), y = fy(c.barre.fret);
      s += '<rect x="' + (x1 - 4.4) + '" y="' + (y - 4.4) + '" width="' + (x2 - x1 + 8.8) + '" height="8.8" rx="4.4" fill="currentColor"/>';
    }
    for (i = 0; i < 6; i++) {
      var ch2 = c.f[i], fg = c.d[i], x = sx(i);
      if (ch2 === 'x') {
        s += '<path d="M' + (x - 2.7) + ' ' + (TOP - 8.6) + ' l5.4 5.4 M' + (x + 2.7) + ' ' + (TOP - 8.6) + ' l-5.4 5.4" stroke="currentColor" stroke-width="1.2" fill="none" opacity=".7"/>';
      } else if (ch2 === '0') {
        s += '<circle cx="' + x + '" cy="' + (TOP - 6) + '" r="2.7" fill="none" stroke="currentColor" stroke-width="1.2" opacity=".7"/>';
      } else {
        var nn = parseInt(ch2, 10);
        var barre = c.barre && c.barre.fret === nn && i >= c.barre.from && i <= c.barre.to;
        if (!barre) s += '<circle cx="' + x + '" cy="' + fy(nn) + '" r="4.9" fill="currentColor"/>';
        if (fg !== '-') s += '<text x="' + x + '" y="' + (fy(nn) + 2.7) + '" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="7" font-weight="600" fill="var(--sheet)">' + fg + '</text>';
      }
    }
    return s + '</svg>';
  }

  document.querySelectorAll('.accord').forEach(function (el) {
    var c = CH[el.dataset.chord];
    if (!c) return;
    el.innerHTML = svgFor(c) + '<div class="nm">' + c.label + '</div>';
  });

  /* ---------- rythmiques ---------- */
  var BEAT = ['1', '&', '2', '&', '3', '&', '4', '&'];
  document.querySelectorAll('.rythme').forEach(function (el) {
    var p = el.dataset.p || '', out = '';
    for (var i = 0; i < 8; i++) {
      var c = p[i] || '-', bas = (i % 2 === 0), g, cl;
      if (c === 'D') { g = '↓'; cl = 'on'; }
      else if (c === 'U') { g = '↑'; cl = 'on'; }
      else if (c === 'x' || c === 'X') { g = '×'; cl = 'mute'; }
      else { g = bas ? '↓' : '↑'; cl = 'off'; }
      out += '<div class="slot"><div class="ar ' + cl + '">' + g + '</div><div class="bt">' + BEAT[i] + '</div></div>';
    }
    el.innerHTML = out;
  });

  /* ---------- minutes où l'élève a l'instrument en main ---------- */
  document.querySelectorAll('.seance').forEach(function (sec) {
    var m = 0;
    sec.querySelectorAll('.etape').forEach(function (e) {
      var t = e.dataset.type;
      if (t === 'jeu' || t === 'morceau') m += (+e.dataset.dur || 0);
    });
    var slot = sec.querySelector('.m-val');
    if (slot) slot.textContent = m + ' min';
  });

  /* ---------- export PDF d'une seule feuille ---------- */
  var masques = [];
  function masquerAutour(el) {
    var node = el;
    while (node && node !== document.body) {
      var kids = node.parentNode.children;
      for (var i = 0; i < kids.length; i++) {
        if (kids[i] !== node) { kids[i].classList.add('print-hidden'); masques.push(kids[i]); }
      }
      node = node.parentNode;
    }
  }
  function restaurer() {
    for (var i = 0; i < masques.length; i++) masques[i].classList.remove('print-hidden');
    masques = [];
    document.documentElement.classList.remove('printing-sheet');
  }
  document.querySelectorAll('.f-print').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var feuille = btn.closest('.feuille');
      if (!feuille) return;
      restaurer();
      masquerAutour(feuille);
      document.documentElement.classList.add('printing-sheet');
      window.print();
    });
  });
  window.addEventListener('afterprint', restaurer);
  if (window.matchMedia) {
    var mq = window.matchMedia('print');
    var onChange = function (m) { if (!m.matches) restaurer(); };
    if (mq.addEventListener) mq.addEventListener('change', onChange);
    else if (mq.addListener) mq.addListener(onChange);
  }

  /* ---------- service worker ---------- */
  if ('serviceWorker' in navigator) {
    addEventListener('load', function () {
      navigator.serviceWorker.register('sw.js').catch(function () {});
    });
  }
})();
