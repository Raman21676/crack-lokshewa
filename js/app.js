// app.js — Crack Lokshewa | Bilingual Vanilla JS SPA | GitHub Pages Ready

// ── State ──────────────────────────────────────────────────────────────
var state = {
    lang: localStorage.getItem('cl_lang') || '',
    i18n: {},
    categories: [],
    currentTests: [],
    currentCategory: null,
    currentTest: null,
    testData: null,
    answers: {},
    marked: {},
    currentQuestionIndex: 0,
    timerInterval: null,
    secondsLeft: 0
};

// ── DOM ───────────────────────────────────────────────────────────────
var appContainer = document.getElementById('app-container');
var appHeader    = document.getElementById('app-header');
var appFooter    = document.getElementById('app-footer');
var langToggle   = document.getElementById('lang-toggle');

if (langToggle) {
    langToggle.onclick = function () {
        var newLang = state.lang === 'ne' ? 'en' : 'ne';
        setLanguage(newLang);
    };
}

var logoBtn = document.getElementById('logo-home');
if (logoBtn) { logoBtn.onclick = function () { window.location.hash = '#home'; }; }

// ── Theme System ──────────────────────────────────────────────────────
var currentTheme = localStorage.getItem('cl_theme') || 'ocean';
var currentMode  = localStorage.getItem('cl_mode')  || 'light';

var THEME_COLORS = {
    ocean:    '#2563eb',
    royal:    '#b91c1c',
    midnight: '#7c3aed',
    sunset:   '#ea580c',
    emerald:  '#059669'
};

function applyTheme(theme) {
    currentTheme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('cl_theme', theme);
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', THEME_COLORS[theme] || THEME_COLORS.ocean);
    var sel = document.getElementById('theme-select');
    if (sel) sel.value = theme;
}

function applyMode(mode) {
    currentMode = mode;
    document.documentElement.setAttribute('data-mode', mode);
    localStorage.setItem('cl_mode', mode);
    var btn = document.getElementById('mode-btn');
    if (btn) btn.textContent = mode === 'dark' ? '☀️' : '🌙';
}

function initTheme() {
    applyTheme(currentTheme);
    applyMode(currentMode);

    var sel = document.getElementById('theme-select');
    if (sel) {
        sel.value = currentTheme;
        sel.onchange = function () { applyTheme(this.value); };
    }

    var modeBtn = document.getElementById('mode-btn');
    if (modeBtn) {
        modeBtn.onclick = function () {
            applyMode(currentMode === 'dark' ? 'light' : 'dark');
        };
    }
}

// ── Helpers ───────────────────────────────────────────────────────────
function setLanguage(lang) {
    state.lang = lang;
    localStorage.setItem('cl_lang', lang);
    document.body.classList.toggle('lang-ne', lang === 'ne');
    if (langToggle) {
        langToggle.textContent = lang === 'ne' ? 'EN / ने' : 'EN / ने';
    }
    handleRoute();
}

function t(key, replacements) {
    var str = (state.i18n[key] && state.i18n[key][(state.lang || 'en')]) || key;
    if (replacements) {
        for (var k in replacements) {
            str = str.replace('{' + k + '}', replacements[k]);
        }
    }
    return str;
}

// Cache-busting version — increment this after every data/content update
var DATA_VERSION = 'v10';

function fetchJSON(url, callback) {
    var sep = url.indexOf('?') === -1 ? '?' : '&';
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url + sep + '_cb=' + DATA_VERSION, true);
    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 300) {
            try { callback(null, JSON.parse(xhr.responseText)); }
            catch (e) { callback('Invalid JSON in ' + url); }
        } else {
            callback('HTTP ' + xhr.status + ' for ' + url);
        }
    };
    xhr.onerror = function () { callback('Network error fetching ' + url); };
    xhr.send();
}

function setHTML(html) { appContainer.innerHTML = html; }

function escapeHTML(str) {
    if (str == null) return '';
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}

function showHeaderFooter(show) {
    if (appHeader) appHeader.style.display = show ? 'block' : 'none';
    if (appFooter) appFooter.style.display = show ? 'block' : 'none';
}

// ── Init i18n & boot ──────────────────────────────────────────────────
function initApp() {
    initTheme();
    fetchJSON('data/i18n.json', function (err, data) {
        if (data) state.i18n = data;
        if (!state.lang) {
            renderLanguageSelector();
        } else {
            document.body.classList.toggle('lang-ne', state.lang === 'ne');
            initRouter();
        }
    });
}

// ── Language Selector ─────────────────────────────────────────────────
function renderLanguageSelector() {
    showHeaderFooter(false);
    setHTML(
        '<div class="fade-in lang-selector">' +
            '<div class="logo-text">🇳🇵 Crack<span class="highlight">Lokshewa</span></div>' +
            '<p class="page-subtitle">Nepal Lok Sewa Mock Test Platform</p>' +
            '<h1 class="page-title" style="margin-bottom:2rem">' + t('select_language') + '</h1>' +
            '<div class="lang-options">' +
                '<div class="lang-card" tabindex="0" role="button" onclick="selectLang(\'en\')">' +
                    '<div class="lang-flag">🇬🇧</div>' +
                    '<div class="lang-name">English</div>' +
                '</div>' +
                '<div class="lang-card" tabindex="0" role="button" onclick="selectLang(\'ne\')">' +
                    '<div class="lang-flag">🇳🇵</div>' +
                    '<div class="lang-name">नेपाली</div>' +
                '</div>' +
            '</div>' +
        '</div>'
    );
}

window.selectLang = function (lang) {
    setLanguage(lang);
    window.location.hash = '#home';
    initRouter();
};

// ── Router ────────────────────────────────────────────────────────────
function initRouter() {
    window.addEventListener('hashchange', handleRoute);
    handleRoute();
}

function handleRoute() {
    stopTimer();
    var hash  = window.location.hash || '#home';
    var parts = hash.replace('#', '').split('/');
    var route = parts[0];

    if (!state.lang && route !== 'lang') {
        renderLanguageSelector();
        return;
    }

    switch (route) {
        case 'lang':     renderLanguageSelector(); break;
        case 'home':     renderHome();             break;
        case 'category': parts[1] ? renderCategory(parts[1]) : goHome(); break;
        case 'test':     parts[1] && parts[2] ? renderTest(parts[1], parts[2]) : goHome(); break;
        case 'results':  renderResults();          break;
        case 'about':    renderAbout();            break;
        default:         renderHome();
    }
}

function goHome() { window.location.hash = '#home'; }
window.goHome = goHome;

// ── HOME ──────────────────────────────────────────────────────────────
function renderHome() {
    showHeaderFooter(true);
    setHTML('<div class="loading-spinner"><div class="spinner"></div><p>Loading...</p></div>');

    function build() {
        var cards = state.categories.map(function (cat) {
            var style = 'background:' + cat.color + '18;color:' + cat.color + ';';
            var title = cat.title[state.lang] || cat.title.en;
            var desc  = cat.description[state.lang] || cat.description.en;
            return '<div class="card category-card" tabindex="0" role="button" ' +
                        'onclick="window.location.hash=\'#category/' + cat.id + '\'">' +
                    '<div class="card-icon" style="' + style + '">' + cat.icon + '</div>' +
                    '<h2 class="card-title">' + title + '</h2>' +
                    '<p class="card-desc">' + desc + '</p>' +
                    '<span class="card-action" style="color:' + cat.color + ';">' + t('view_tests') + ' →</span>' +
                   '</div>';
        }).join('');

        setHTML(
            '<div class="fade-in">' +
                '<div class="hero">' +
                    '<h1 class="page-title">' + t('home_title') + '</h1>' +
                    '<p class="page-subtitle">' + t('home_subtitle') + '</p>' +
                '</div>' +
                '<div class="grid-container">' + cards + '</div>' +
            '</div>'
        );
    }

    if (state.categories.length > 0) {
        build();
        return;
    }
    fetchJSON('data/categories.json', function (err, data) {
        if (err || !data) {
            setHTML('<div class="error-msg">⚠️ ' + t('load_error') + '</div>');
            return;
        }
        state.categories = data;
        build();
    });
}

// ── CATEGORY ──────────────────────────────────────────────────────────
function renderCategory(categoryId) {
    showHeaderFooter(true);
    setHTML('<div class="loading-spinner"><div class="spinner"></div><p>Loading...</p></div>');
    state.currentCategory = categoryId;

    function loadTests() {
        var cat      = state.categories.find(function (c) { return c.id === categoryId; });
        var catTitle = cat ? (cat.title[state.lang] || cat.title.en) : 'Mock Tests';
        var catColor = cat ? cat.color : '#2563eb';

        fetchJSON('data/' + state.lang + '/' + categoryId + '/tests.json', function (err, tests) {
            if (err || !tests || tests.length === 0) {
                setHTML(
                    '<div class="fade-in">' +
                        '<button class="btn btn-secondary mb-4" onclick="goHome()">← ' + t('back_home') + '</button>' +
                        '<div class="empty-state">' +
                            '<p>😕 ' + t('no_tests') + '</p>' +
                            '<p class="text-sm">' + t('adding_soon') + '</p>' +
                        '</div>' +
                    '</div>'
                );
                return;
            }

            state.currentTests = tests;

            var rows = tests.map(function (test, i) {
                var lockIcon = test.locked ? '🔒 ' : '';
                var btn = test.locked
                    ? '<span class="badge badge-locked">' + t('coming_soon') + '</span>'
                    : '<button class="btn btn-primary" onclick="window.location.hash=\'#test/' + categoryId + '/' + test.id + '\'">' + t('start_test') + ' →</button>';

                return '<div class="card test-card">' +
                            '<div class="test-card-num" style="background:' + catColor + '18;color:' + catColor + ';">' + (i + 1) + '</div>' +
                            '<div class="test-info">' +
                                '<h3 class="test-title">' + lockIcon + escapeHTML(test.title) + '</h3>' +
                                '<div class="test-meta">' +
                                    '<span class="meta-tag">📝 ' + test.questionCount + ' ' + t('questions') + '</span>' +
                                    '<span class="meta-tag">⏱ ' + test.timeLimit + ' ' + t('min') + '</span>' +
                                    '<span class="meta-tag difficulty-' + test.difficulty.toLowerCase() + '">' + test.difficulty + '</span>' +
                                '</div>' +
                            '</div>' +
                            btn +
                       '</div>';
            }).join('');

            setHTML(
                '<div class="fade-in">' +
                    '<button class="btn btn-secondary mb-4" onclick="goHome()">← ' + t('back_home') + '</button>' +
                    '<h1 class="page-title">' + catTitle + '</h1>' +
                    '<p class="page-subtitle">' + t('select_test') + '</p>' +
                    '<div class="tests-list">' + rows + '</div>' +
                '</div>'
            );
        });
    }

    if (state.categories.length === 0) {
        fetchJSON('data/categories.json', function (err, data) {
            if (data) state.categories = data;
            loadTests();
        });
    } else {
        loadTests();
    }
}

// ── TEST ENGINE ───────────────────────────────────────────────────────
function renderTest(categoryId, testId) {
    showHeaderFooter(true);
    setHTML('<div class="loading-spinner"><div class="spinner"></div><p>Loading...</p></div>');

    function fetchQuestions(timeLimit) {
        fetchJSON('data/' + state.lang + '/' + categoryId + '/' + testId + '.json', function (err, data) {
            if (err || !data || data.length === 0) {
                setHTML(
                    '<div class="fade-in">' +
                        '<button class="btn btn-secondary mb-4" onclick="window.location.hash=\'#category/' + categoryId + '\'">← ' + t('back') + '</button>' +
                        '<div class="error-msg">⚠️ ' + t('test_error') + '</div>' +
                    '</div>'
                );
                return;
            }
            state.testData             = data;
            state.answers              = {};
            state.marked               = {};
            state.currentQuestionIndex = 0;
            state.currentCategory      = categoryId;
            state.currentTest          = testId;
            state.secondsLeft          = timeLimit * 60;
            renderQuestionUI();
            startTimer();
        });
    }

    var cached = state.currentTests && state.currentTests.find(function (t) { return t.id === testId; });
    if (cached && cached.timeLimit && state.currentCategory === categoryId) {
        fetchQuestions(cached.timeLimit);
    } else {
        fetchJSON('data/' + state.lang + '/' + categoryId + '/tests.json', function (err, tests) {
            var timeLimit = 45;
            if (tests && Array.isArray(tests)) {
                state.currentTests = tests;
                var meta = tests.find(function (t) { return t.id === testId; });
                if (meta && meta.timeLimit) { timeLimit = meta.timeLimit; }
            }
            fetchQuestions(timeLimit);
        });
    }
}

// ── QUESTION UI ───────────────────────────────────────────────────────
function renderQuestionUI() {
    var q           = state.testData[state.currentQuestionIndex];
    var total       = state.testData.length;
    var progress    = Math.round(((state.currentQuestionIndex + 1) / total) * 100);
    var answered    = Object.keys(state.answers).length;
    var isLast      = state.currentQuestionIndex === total - 1;
    var selectedIdx = state.answers.hasOwnProperty(state.currentQuestionIndex)
                        ? state.answers[state.currentQuestionIndex]
                        : null;
    var isMarked    = state.marked[state.currentQuestionIndex];

    var optionsHTML = q.options.map(function (opt, idx) {
        var isSelected = selectedIdx === idx;
        return '<label class="option-label' + (isSelected ? ' selected' : '') +
                    '" onclick="selectOption(' + idx + ')">' +
                '<span class="option-letter">' + String.fromCharCode(65 + idx) + '</span>' +
                '<span class="option-text">' + escapeHTML(opt) + '</span>' +
               '</label>';
    }).join('');

    var markBtnText = isMarked ? t('unmark_review') : t('mark_review');
    var markBtnClass = isMarked ? 'btn-mark active' : 'btn-mark';

    var navBtn = isLast
        ? '<button class="btn btn-submit" onclick="confirmSubmit()">' + t('submit_test') + ' ✓</button>'
        : '<button class="btn btn-primary" onclick="nextQuestion()">' + t('next') + ' →</button>';

    // Palette
    var paletteHTML = '';
    for (var p = 0; p < total; p++) {
        var pAns = state.answers.hasOwnProperty(p);
        var pMark = state.marked[p];
        var pCls = 'palette-btn';
        if (p === state.currentQuestionIndex) pCls += ' current';
        if (pAns && pMark) pCls += ' answered marked';
        else if (pAns) pCls += ' answered';
        else if (pMark) pCls += ' marked';
        paletteHTML += '<button class="' + pCls + '" onclick="jumpToQuestion(' + p + ')">' + (p + 1) + '</button>';
    }

    setHTML(
        '<div class="fade-in test-container">' +
            '<div class="test-topbar">' +
                '<div class="test-info-row">' +
                    '<span class="q-counter">' + t('question') + ' <strong>' + (state.currentQuestionIndex + 1) + '</strong> ' + t('of') + ' ' + total + '</span>' +
                    '<span class="answered-count">' + answered + '/' + total + ' ' + t('answered') + '</span>' +
                    '<span class="timer" id="timer-display">⏱ ' + formatTime(state.secondsLeft) + '</span>' +
                    '<button class="btn btn-sm btn-danger" onclick="confirmExit()">' + t('exit') + '</button>' +
                '</div>' +
                '<div class="progress-bar-bg"><div class="progress-bar-fill" style="width:' + progress + '%"></div></div>' +
            '</div>' +

            '<div class="palette-section">' +
                '<div class="palette-title">' + t('palette') + '</div>' +
                '<div class="palette-grid">' + paletteHTML + '</div>' +
                '<div class="palette-legend">' +
                    '<span><span class="legend-dot" style="background:var(--border)"></span> ' + t('not_visited') + '</span>' +
                    '<span><span class="legend-dot" style="background:var(--success-light);border:1px solid var(--success)"></span> ' + t('answered_status') + '</span>' +
                    '<span><span class="legend-dot" style="background:var(--warning-light);border:1px solid var(--warning)"></span> ' + t('marked_review') + '</span>' +
                '</div>' +
            '</div>' +

            '<div class="question-card">' +
                '<p class="question-number">' + t('question') + ' ' + (state.currentQuestionIndex + 1) + ' ' + t('of') + ' ' + total + '</p>' +
                '<h2 class="question-text">' + escapeHTML(q.question) + '</h2>' +
                '<div class="options-list">' + optionsHTML + '</div>' +
            '</div>' +

            '<div class="test-navigation">' +
                '<button class="btn btn-secondary" onclick="prevQuestion()"' + (state.currentQuestionIndex === 0 ? ' disabled' : '') + '>← ' + t('previous') + '</button>' +
                '<div class="test-nav-center">' +
                    '<button class="' + markBtnClass + '" onclick="toggleMark()">' + markBtnText + '</button>' +
                '</div>' +
                navBtn +
            '</div>' +
        '</div>'
    );
}

// ── TIMER ─────────────────────────────────────────────────────────────
function startTimer() {
    stopTimer();
    state.timerInterval = setInterval(function () {
        state.secondsLeft--;
        var el = document.getElementById('timer-display');
        if (el) {
            el.textContent = '⏱ ' + formatTime(state.secondsLeft);
            if (state.secondsLeft <= 300) { el.classList.add('urgent'); }
        }
        if (state.secondsLeft <= 0) {
            stopTimer();
            alert(t('time_up'));
            submitTest();
        }
    }, 1000);
}

function stopTimer() {
    if (state.timerInterval) {
        clearInterval(state.timerInterval);
        state.timerInterval = null;
    }
}

function formatTime(seconds) {
    if (seconds < 0) { seconds = 0; }
    var m = Math.floor(seconds / 60);
    var s = seconds % 60;
    return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
}

// ── NAVIGATION HANDLERS ───────────────────────────────────────────────
window.selectOption = function (idx) {
    state.answers[state.currentQuestionIndex] = idx;
    renderQuestionUI();
};

window.nextQuestion = function () {
    if (state.currentQuestionIndex < state.testData.length - 1) {
        state.currentQuestionIndex++;
        renderQuestionUI();
    }
};

window.prevQuestion = function () {
    if (state.currentQuestionIndex > 0) {
        state.currentQuestionIndex--;
        renderQuestionUI();
    }
};

window.jumpToQuestion = function (idx) {
    if (idx >= 0 && idx < state.testData.length) {
        state.currentQuestionIndex = idx;
        renderQuestionUI();
    }
};

window.toggleMark = function () {
    var idx = state.currentQuestionIndex;
    if (state.marked[idx]) {
        delete state.marked[idx];
    } else {
        state.marked[idx] = true;
    }
    renderQuestionUI();
};

window.confirmExit = function () {
    if (confirm(t('confirm_exit'))) {
        stopTimer();
        window.location.hash = '#category/' + state.currentCategory;
    }
};

window.confirmSubmit = function () {
    var unanswered = state.testData.length - Object.keys(state.answers).length;
    var msg = unanswered > 0
        ? t('confirm_submit_unanswered', { n: unanswered })
        : t('confirm_submit');
    if (confirm(msg)) { submitTest(); }
};

function submitTest() {
    stopTimer();
    window.location.hash = '#results';
}
window.submitTest = submitTest;

// ── RESULTS ───────────────────────────────────────────────────────────
function renderResults() {
    showHeaderFooter(true);
    if (!state.testData || state.testData.length === 0) {
        goHome();
        return;
    }

    var correct = 0;
    var wrong   = 0;
    var skipped = 0;
    var total   = state.testData.length;
    var marks   = 0;
    var negMarks = 0;

    var subjectStats = {};

    var reviewHTML = state.testData.map(function (q, i) {
        var userAns   = state.answers.hasOwnProperty(i) ? state.answers[i] : null;
        var isSkipped = userAns === null;
        var isCorrect = userAns === q.correctIndex;
        var subj = q.subject || 'OTHER';

        if (!subjectStats[subj]) {
            subjectStats[subj] = { correct: 0, wrong: 0, skipped: 0, total: 0 };
        }
        subjectStats[subj].total++;

        if (isCorrect) {
            correct++;
            marks += 2;
            subjectStats[subj].correct++;
        } else if (isSkipped) {
            skipped++;
            subjectStats[subj].skipped++;
        } else {
            wrong++;
            negMarks += 0.4;
            subjectStats[subj].wrong++;
        }

        var opts = q.options.map(function (opt, oi) {
            var cls = '';
            if (oi === q.correctIndex) { cls = 'is-correct-answer'; }
            else if (oi === userAns)   { cls = 'is-wrong-answer'; }
            return '<div class="review-option ' + cls + '">' +
                        '<span class="option-letter">' + String.fromCharCode(65 + oi) + '</span>' +
                        '<span>' + escapeHTML(opt) + '</span>' +
                        (oi === q.correctIndex ? '<span class="tick">✓</span>' : '') +
                        (oi === userAns && oi !== q.correctIndex ? '<span class="cross">✗</span>' : '') +
                   '</div>';
        }).join('');

        var cardCls = isSkipped ? 'skipped' : (isCorrect ? 'correct' : 'incorrect');
        var badge   = isSkipped ? '— ' + t('skipped') : (isCorrect ? '✓ ' + t('correct') : '✗ ' + t('incorrect'));

        var explanationHTML = '';
        if (q.explanation) {
            explanationHTML = '<div class="explanation"><strong>💡 ' + t('explanation') + ':</strong> ' + escapeHTML(q.explanation) + '</div>';
        }

        return '<div class="review-card ' + cardCls + '">' +
                    '<div class="review-qheader">' +
                        '<h4 class="review-question">' + t('question') + ' ' + (i + 1) + '. ' + escapeHTML(q.question) + '</h4>' +
                        '<span class="review-badge">' + badge + '</span>' +
                    '</div>' +
                    '<div class="review-options">' + opts + '</div>' +
                    explanationHTML +
               '</div>';
    }).join('');

    var finalMarks = Math.max(0, marks - negMarks);
    var pct = Math.round((finalMarks / (total * 2)) * 100);
    var grade, gradeClass;
    if (pct >= 80)      { grade = t('excellent') + ' 🎉'; gradeClass = 'grade-excellent'; }
    else if (pct >= 60) { grade = t('good') + ' 👍';      gradeClass = 'grade-good'; }
    else if (pct >= 45) { grade = t('pass') + ' ✔';       gradeClass = 'grade-pass'; }
    else                { grade = t('needs_work') + ' 📚'; gradeClass = 'grade-fail'; }

    setHTML(
        '<div class="fade-in results-container">' +
            '<h1 class="page-title text-center">' + t('test_results') + '</h1>' +
            '<div class="score-card">' +
                '<div class="score-circle ' + gradeClass + '">' +
                    '<span class="score-number">' + finalMarks.toFixed(1) + '</span>' +
                    '<span class="score-denom">/ ' + (total * 2) + '</span>' +
                '</div>' +
                '<h2 class="score-percentage">' + pct + '% ' + t('score') + '</h2>' +
                '<p class="score-grade">' + grade + '</p>' +
                '<p class="score-note">' + t('passing_mark') + '</p>' +
                '<div class="score-breakdown">' +
                    '<div class="breakdown-item">' +
                        '<div class="breakdown-value" style="color:var(--success)">' + correct + '</div>' +
                        '<div class="breakdown-label">' + t('correct_count') + '</div>' +
                    '</div>' +
                    '<div class="breakdown-item">' +
                        '<div class="breakdown-value" style="color:var(--error)">' + wrong + '</div>' +
                        '<div class="breakdown-label">' + t('wrong_count') + '</div>' +
                    '</div>' +
                    '<div class="breakdown-item">' +
                        '<div class="breakdown-value" style="color:var(--text-3)">' + skipped + '</div>' +
                        '<div class="breakdown-label">' + t('skipped_count') + '</div>' +
                    '</div>' +
                    '<div class="breakdown-item">' +
                        '<div class="breakdown-value" style="color:var(--primary)">+' + marks + '</div>' +
                        '<div class="breakdown-label">' + t('marks_obtained') + '</div>' +
                    '</div>' +
                    '<div class="breakdown-item">' +
                        '<div class="breakdown-value" style="color:var(--error)">-' + negMarks.toFixed(1) + '</div>' +
                        '<div class="breakdown-label">' + t('negative_marks') + '</div>' +
                    '</div>' +
                '</div>' +
            '</div>' +
            renderSubjectAnalysis(subjectStats) +
            '<div class="results-actions">' +
                '<button class="btn btn-secondary" onclick="window.location.hash=\'#test/' + state.currentCategory + '/' + state.currentTest + '\'">🔄 ' + t('retry') + '</button>' +
                '<button class="btn btn-primary" onclick="window.location.hash=\'#category/' + state.currentCategory + '\'">' + t('more_tests') + '</button>' +
                '<button class="btn btn-secondary" onclick="goHome()">🏠 ' + t('home') + '</button>' +
            '</div>' +
            '<h3 class="section-title mt-8">📋 ' + t('detailed_review') + '</h3>' +
            '<div class="review-list">' + reviewHTML + '</div>' +
        '</div>'
    );
}

function renderSubjectAnalysis(stats) {
    var keys = Object.keys(stats);
    if (keys.length === 0) return '';

    var cards = keys.map(function (k) {
        var s = stats[k];
        var subjKey = 'subject_' + k.toLowerCase();
        var label = t(subjKey);
        if (label === subjKey) label = k;
        var pct = s.total > 0 ? Math.round((s.correct / s.total) * 100) : 0;
        var barColor = pct >= 70 ? 'var(--success)' : (pct >= 45 ? 'var(--warning)' : 'var(--error)');

        return '<div class="subject-card">' +
            '<div class="subject-header">' +
                '<span class="subject-name">' + label + '</span>' +
                '<span class="subject-pct" style="color:' + barColor + '">' + pct + '%</span>' +
            '</div>' +
            '<div class="subject-bar-bg"><div class="subject-bar-fill" style="width:' + pct + '%;background:' + barColor + '"></div></div>' +
            '<div class="subject-stats">' +
                '<span>✓ ' + s.correct + '</span>' +
                '<span>✗ ' + s.wrong + '</span>' +
                '<span>— ' + s.skipped + '</span>' +
                '<span class="subject-total">/ ' + s.total + '</span>' +
            '</div>' +
        '</div>';
    }).join('');

    return '<h3 class="section-title">📊 ' + t('subject_analysis') + '</h3>' +
        '<div class="subject-grid">' + cards + '</div>';
}

// ── ABOUT ─────────────────────────────────────────────────────────────
function renderAbout() {
    showHeaderFooter(true);
    setHTML(
        '<div class="fade-in about-container">' +
            '<h1 class="page-title">' + t('about_title') + '</h1>' +
            '<p class="page-subtitle">' + t('about_subtitle') + '</p>' +
            '<div class="about-card">' +
                '<h2>' + t('about_what') + '</h2>' +
                '<p>' + t('about_desc') + '</p>' +
                '<h2 style="margin-top:1.5rem">' + t('about_format') + '</h2>' +
                '<ul class="about-list">' +
                    '<li>📋 ' + t('about_format_1') + '</li>' +
                    '<li>⏱ ' + t('about_format_2') + '</li>' +
                    '<li>✅ ' + t('about_format_3') + '</li>' +
                    '<li>❌ ' + t('about_format_4') + '</li>' +
                    '<li>📚 ' + t('about_format_5') + '</li>' +
                '</ul>' +
                '<h2 style="margin-top:1.5rem">' + t('about_disclaimer') + '</h2>' +
                '<p>' + t('about_disclaimer_text') + '</p>' +
            '</div>' +
            '<button class="btn btn-primary mt-8" onclick="goHome()">← ' + t('home') + '</button>' +
        '</div>'
    );
}

// ── BOOT ──────────────────────────────────────────────────────────────
initApp();
