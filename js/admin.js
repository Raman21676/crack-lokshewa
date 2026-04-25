/* admin.js — Crack Lokshewa Admin Panel
 * Credentials are verified via SHA-256 hashes ONLY.
 * No plaintext passwords are stored or transmitted.
 */
(function() {
    'use strict';

    // ── Credential hashes (SHA-256) — NEVER the plaintext ──
    var USER_HASH = 'dca5b7df09a6178b75f23d657374496ece61449d7e322d9fef8c98bd4a641dfe';
    var PASS_HASH = 'b287a582ecae5662b3ba57ab46b8726469214774ed4b6306b5ec5b009549d077';
    var NS = 'lokshewa.online';

    async function sha256(text) {
        var buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
        return Array.from(new Uint8Array(buf)).map(function(b) {
            return b.toString(16).padStart(2, '0');
        }).join('');
    }

    function $(id) { return document.getElementById(id); }

    // ── Login ──
    window.doLogin = async function() {
        var u = $('a-user').value.trim();
        var p = $('a-pass').value;
        var uh = await sha256(u);
        var ph = await sha256(p);

        if (uh === USER_HASH && ph === PASS_HASH) {
            sessionStorage.setItem('cl_adm', '1');
            showDash();
        } else {
            $('a-err').textContent = 'Invalid username or password.';
            $('a-pass').value = '';
        }
    };

    window.doLogout = function() {
        sessionStorage.removeItem('cl_adm');
        $('login-wrap').style.display = 'flex';
        $('dash-wrap').style.display = 'none';
        $('a-user').value = '';
        $('a-pass').value = '';
        $('a-err').textContent = '';
    };

    // ── Dashboard ──
    function showDash() {
        $('login-wrap').style.display = 'none';
        $('dash-wrap').style.display = 'block';
        loadStats();
    }

    async function loadStats() {
        var pages = ['total','homepage','adhikrit','constitution','driving','gk','iq','it','kharidar','livestock','nursing','police','subbha'];
        var counts = {};

        // Fetch CountAPI stats
        await Promise.all(pages.map(function(p) {
            return fetch('https://api.countapi.xyz/get/' + NS + '/' + p)
                .then(function(r) { return r.json(); })
                .then(function(j) { counts[p] = j.value || 0; })
                .catch(function() { counts[p] = 0; });
        }));

        // Total
        $('stat-total').textContent = (counts.total || 0).toLocaleString();

        // Per-category breakdown
        var tbody = $('cat-table');
        tbody.innerHTML = '';
        var catNames = {
            adhikrit:'Adhikrit', constitution:'Constitution', driving:'Driving',
            gk:'GK', iq:'IQ', it:'IT', kharidar:'Kharidar', livestock:'Livestock',
            nursing:'Nursing', police:'Police', subbha:'Subbha'
        };
        Object.keys(catNames).forEach(function(key) {
            var tr = document.createElement('tr');
            tr.innerHTML = '<td>' + catNames[key] + '</td><td>' + (counts[key] || 0).toLocaleString() + '</td>';
            tbody.appendChild(tr);
        });

        // Session detail (this browser)
        var sess = JSON.parse(sessionStorage.getItem('cl_track') || '{"pages":[]}');
        $('stat-sess').textContent = sess.pages.length;

        // Today's hits (localStorage)
        var today = new Date().toISOString().slice(0,10);
        var hist  = JSON.parse(localStorage.getItem('cl_hist') || '{}');
        $('stat-today').textContent = (hist[today] || 0).toLocaleString();

        // Recent activity table
        var recent = sess.pages.slice(-20).reverse();
        var rbody = $('recent-table');
        rbody.innerHTML = '';
        recent.forEach(function(row) {
            var tr = document.createElement('tr');
            var d = new Date(row.time);
            tr.innerHTML = '<td>' + (row.page || '-') + '</td>' +
                '<td>' + (row.cat || '-') + '</td>' +
                '<td>' + d.toLocaleTimeString() + '</td>';
            rbody.appendChild(tr);
        });
    }

    // ── Init ──
    if (sessionStorage.getItem('cl_adm') === '1') {
        showDash();
    }
})();
