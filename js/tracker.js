/* tracker.js — Crack Lokshewa | Lightweight Visitor Tracking
 * Uses CountAPI (free, no-signup) for global counters + localStorage for session detail.
 * No credentials. No PII collected.
 */
(function() {
    'use strict';

    var NS = 'lokshewa.online';
    var page = location.hash.replace('#/', '').split('/')[0] || 'homepage';
    var cat  = location.hash.replace('#/', '').split('/')[1] || 'none';

    // ── CountAPI: global hit counter ──
    try {
        fetch('https://api.countapi.xyz/hit/' + NS + '/' + page)
            .catch(function(){});
        fetch('https://api.countapi.xyz/hit/' + NS + '/total')
            .catch(function(){});
    } catch(e) {}

    // ── Session detail: stored locally in THIS browser ──
    var raw = sessionStorage.getItem('cl_track');
    var sess = raw ? JSON.parse(raw) : { start: Date.now(), pages: [] };
    sess.pages.push({
        page: page,
        cat:  cat,
        time: Date.now(),
        ua:   navigator.userAgent.slice(0, 120)
    });
    sessionStorage.setItem('cl_track', JSON.stringify(sess));

    // ── Persist a light summary across sessions ──
    var today = new Date().toISOString().slice(0,10);
    var hist  = JSON.parse(localStorage.getItem('cl_hist') || '{}');
    if (!hist[today]) hist[today] = 0;
    hist[today]++;
    localStorage.setItem('cl_hist', JSON.stringify(hist));
})();
