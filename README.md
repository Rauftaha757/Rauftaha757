<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Taha Rauf — Flutter Developer</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Mono:wght@300;400;500&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet"/>
<style>
  *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

  :root {
    --ink: #0a0a0f;
    --paper: #f5f3ee;
    --gold: #c9a96e;
    --gold-light: #e8d5a3;
    --muted: #6b6860;
    --accent: #1a3a5c;
    --soft: #ede9e0;
    --line: rgba(201,169,110,0.25);
  }

  html { scroll-behavior: smooth; }

  body {
    background: var(--ink);
    color: var(--paper);
    font-family: 'DM Mono', monospace;
    min-height: 100vh;
    overflow-x: hidden;
    cursor: none;
  }

  /* CURSOR */
  .cursor {
    position: fixed;
    width: 8px; height: 8px;
    background: var(--gold);
    border-radius: 50%;
    pointer-events: none;
    z-index: 9999;
    transform: translate(-50%, -50%);
    transition: transform 0.1s ease, width 0.3s, height 0.3s, background 0.3s;
    mix-blend-mode: difference;
  }
  .cursor-ring {
    position: fixed;
    width: 36px; height: 36px;
    border: 1px solid rgba(201,169,110,0.5);
    border-radius: 50%;
    pointer-events: none;
    z-index: 9998;
    transform: translate(-50%, -50%);
    transition: transform 0.18s ease, width 0.3s, height 0.3s;
  }

  /* NOISE OVERLAY */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 1000;
    opacity: 0.35;
  }

  /* GRID LINES */
  body::after {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(201,169,110,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(201,169,110,0.03) 1px, transparent 1px);
    background-size: 80px 80px;
    pointer-events: none;
    z-index: 0;
  }

  /* LAYOUT */
  .page {
    position: relative;
    z-index: 1;
    max-width: 900px;
    margin: 0 auto;
    padding: 0 40px;
  }

  /* TOP BAR */
  .topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 32px 0 0;
    opacity: 0;
    animation: fadeUp 0.8s 0.1s forwards;
  }
  .topbar-left {
    font-size: 10px;
    letter-spacing: 0.25em;
    color: var(--gold);
    text-transform: uppercase;
  }
  .topbar-right {
    display: flex;
    gap: 24px;
    font-size: 10px;
    letter-spacing: 0.2em;
    color: var(--muted);
    text-transform: uppercase;
  }
  .topbar-right a {
    color: inherit;
    text-decoration: none;
    transition: color 0.3s;
  }
  .topbar-right a:hover { color: var(--gold); }

  /* DIVIDER */
  .rule {
    height: 1px;
    background: var(--line);
    margin: 24px 0;
    opacity: 0;
    animation: scaleIn 0.8s 0.3s forwards;
    transform-origin: left;
  }

  /* HERO */
  .hero {
    padding: 60px 0 80px;
  }
  .hero-eyebrow {
    font-size: 10px;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 28px;
    opacity: 0;
    animation: fadeUp 0.8s 0.4s forwards;
  }
  .hero-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(64px, 12vw, 120px);
    font-weight: 300;
    line-height: 0.9;
    letter-spacing: -0.02em;
    color: var(--paper);
    margin-bottom: 8px;
    opacity: 0;
    animation: fadeUp 1s 0.5s forwards;
  }
  .hero-name em {
    font-style: italic;
    color: var(--gold);
  }
  .hero-subtitle {
    font-family: 'Syne', sans-serif;
    font-size: 13px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--muted);
    margin-top: 24px;
    margin-bottom: 40px;
    opacity: 0;
    animation: fadeUp 0.8s 0.7s forwards;
  }
  .hero-quote {
    font-family: 'Cormorant Garamond', serif;
    font-size: 18px;
    font-style: italic;
    color: var(--muted);
    max-width: 480px;
    line-height: 1.6;
    border-left: 1px solid var(--gold);
    padding-left: 20px;
    opacity: 0;
    animation: fadeUp 0.8s 0.9s forwards;
  }

  /* STATUS ROW */
  .status-row {
    display: flex;
    gap: 40px;
    flex-wrap: wrap;
    padding: 40px 0;
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    opacity: 0;
    animation: fadeUp 0.8s 1.0s forwards;
  }
  .status-item {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }
  .status-label {
    font-size: 9px;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--gold);
  }
  .status-value {
    font-size: 12px;
    color: var(--paper);
    letter-spacing: 0.05em;
    opacity: 0.8;
  }

  /* SECTIONS */
  .section {
    padding: 80px 0;
    border-bottom: 1px solid var(--line);
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.8s ease, transform 0.8s ease;
  }
  .section.visible {
    opacity: 1;
    transform: translateY(0);
  }

  .section-header {
    display: flex;
    align-items: baseline;
    gap: 16px;
    margin-bottom: 52px;
  }
  .section-num {
    font-size: 10px;
    letter-spacing: 0.2em;
    color: var(--gold);
    font-family: 'DM Mono', monospace;
  }
  .section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 38px;
    font-weight: 300;
    letter-spacing: -0.01em;
    color: var(--paper);
  }
  .section-line {
    flex: 1;
    height: 1px;
    background: var(--line);
    margin-left: 16px;
  }

  /* ABOUT */
  .about-text {
    font-size: 14px;
    line-height: 1.9;
    color: rgba(245,243,238,0.7);
    max-width: 620px;
    letter-spacing: 0.03em;
  }
  .about-text strong {
    color: var(--gold);
    font-weight: 400;
  }

  /* TECH STACK */
  .tech-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
    gap: 1px;
    background: var(--line);
    border: 1px solid var(--line);
  }
  .tech-cell {
    background: var(--ink);
    padding: 28px 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    transition: background 0.3s;
    position: relative;
    overflow: hidden;
  }
  .tech-cell::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(201,169,110,0.06), transparent);
    opacity: 0;
    transition: opacity 0.3s;
  }
  .tech-cell:hover::before { opacity: 1; }
  .tech-cell:hover { background: #0f0f16; }
  .tech-icon {
    font-size: 22px;
    filter: grayscale(0.4);
  }
  .tech-name {
    font-size: 11px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--paper);
    opacity: 0.7;
  }
  .tech-type {
    font-size: 9px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--gold);
    opacity: 0.6;
  }

  /* CONNECT */
  .connect-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 2px;
    background: var(--line);
    border: 1px solid var(--line);
  }
  .connect-item {
    background: var(--ink);
    padding: 32px 24px;
    text-decoration: none;
    display: flex;
    align-items: flex-start;
    gap: 18px;
    transition: background 0.3s;
    position: relative;
    overflow: hidden;
    group: true;
  }
  .connect-item::after {
    content: '→';
    position: absolute;
    bottom: 20px;
    right: 24px;
    color: var(--gold);
    font-size: 16px;
    opacity: 0;
    transform: translateX(-8px);
    transition: opacity 0.3s, transform 0.3s;
  }
  .connect-item:hover { background: #0e0e14; }
  .connect-item:hover::after { opacity: 1; transform: translateX(0); }
  .connect-icon {
    font-size: 20px;
    margin-top: 2px;
  }
  .connect-label {
    font-size: 9px;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 6px;
  }
  .connect-value {
    font-size: 12px;
    color: var(--paper);
    opacity: 0.7;
    letter-spacing: 0.05em;
  }

  /* STATS */
  .stats-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1px;
    background: var(--line);
    border: 1px solid var(--line);
    margin-bottom: 2px;
  }
  .stat-cell {
    background: var(--ink);
    padding: 40px 32px;
    position: relative;
    overflow: hidden;
  }
  .stat-cell::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 2px;
    height: 0;
    background: var(--gold);
    transition: height 0.6s ease;
  }
  .stat-cell:hover::before { height: 100%; }
  .stat-number {
    font-family: 'Cormorant Garamond', serif;
    font-size: 52px;
    font-weight: 300;
    color: var(--gold-light);
    line-height: 1;
    letter-spacing: -0.02em;
  }
  .stat-label {
    font-size: 10px;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--muted);
    margin-top: 8px;
  }

  .github-card {
    border: 1px solid var(--line);
    padding: 32px;
    background: #08080d;
    position: relative;
    overflow: hidden;
  }
  .github-card::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(201,169,110,0.04), transparent 70%);
    pointer-events: none;
  }
  .github-card img {
    width: 100%;
    border-radius: 2px;
    opacity: 0.9;
    filter: contrast(1.05);
  }

  /* FOOTER */
  .footer {
    padding: 60px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    opacity: 0;
    animation: fadeUp 0.8s 1.2s forwards;
  }
  .footer-motto {
    font-family: 'Cormorant Garamond', serif;
    font-size: 22px;
    font-style: italic;
    color: var(--muted);
  }
  .footer-motto em { color: var(--gold); font-style: normal; }
  .footer-right {
    font-size: 9px;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--muted);
    opacity: 0.5;
  }

  /* FLOATING BADGE */
  .badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 9px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--gold);
    border: 1px solid var(--line);
    padding: 8px 16px;
    margin-right: 12px;
    margin-bottom: 12px;
  }
  .badge::before {
    content: '';
    width: 4px;
    height: 4px;
    background: var(--gold);
    border-radius: 50%;
    animation: pulse 2s infinite;
  }

  /* ANIMATIONS */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
  @keyframes scaleIn {
    from { opacity: 0; transform: scaleX(0); }
    to { opacity: 1; transform: scaleX(1); }
  }
  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
  }
  @keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }

  /* SCROLLBAR */
  ::-webkit-scrollbar { width: 3px; }
  ::-webkit-scrollbar-track { background: var(--ink); }
  ::-webkit-scrollbar-thumb { background: var(--gold); opacity: 0.5; }

  /* RESPONSIVE */
  @media (max-width: 600px) {
    .page { padding: 0 24px; }
    .stats-row { grid-template-columns: 1fr; }
    .topbar-right { display: none; }
    .footer { flex-direction: column; gap: 16px; text-align: center; }
  }
</style>
</head>
<body>

<div class="cursor" id="cursor"></div>
<div class="cursor-ring" id="cursorRing"></div>

<div class="page">

  <!-- TOP BAR -->
  <div class="topbar">
    <div class="topbar-left">Portfolio · 2025</div>
    <div class="topbar-right">
      <a href="mailto:rauftaha757@gmail.com">Email</a>
      <a href="https://linkedin.com/in/rauftaha757" target="_blank">LinkedIn</a>
      <a href="https://github.com/rauftaha757" target="_blank">GitHub</a>
      <a href="https://drive.google.com/file/d/1GyhDPpnKMCYqWWOsodRyCgmi7mvZAgXp/view" target="_blank">Résumé</a>
    </div>
  </div>

  <div class="rule"></div>

  <!-- HERO -->
  <div class="hero">
    <div class="hero-eyebrow">Flutter Developer · Full Stack Engineer · Problem Solver</div>
    <h1 class="hero-name">Taha <em>Rauf</em></h1>
    <div class="hero-subtitle">Bringing ideas to life through elegant code</div>
    <div class="hero-quote">
      "Bringing ideas to life through elegant code and seamless user experiences"
    </div>
  </div>

  <!-- STATUS ROW -->
  <div class="status-row">
    <div class="status-item">
      <span class="status-label">Currently</span>
      <span class="status-value">Cross-Platform Mobile Apps</span>
    </div>
    <div class="status-item">
      <span class="status-label">Exploring</span>
      <span class="status-value">Cloud · DevOps · Real-time</span>
    </div>
    <div class="status-item">
      <span class="status-label">Location</span>
      <span class="status-value">Pakistan 🇵🇰</span>
    </div>
    <div class="status-item">
      <span class="status-label">Status</span>
      <span class="status-value" style="color:var(--gold)">● Open to Work</span>
    </div>
  </div>

  <!-- ABOUT -->
  <div class="section" id="about">
    <div class="section-header">
      <span class="section-num">01</span>
      <h2 class="section-title">About</h2>
      <div class="section-line"></div>
    </div>
    <p class="about-text">
      I'm a <strong>Flutter Developer</strong> and <strong>Full Stack Engineer</strong> 
      passionate about crafting beautiful, high-performance mobile applications. 
      I specialise in building <strong>cross-platform experiences</strong> with Flutter 
      backed by robust <strong>Node.js services</strong>, real-time systems, and 
      thoughtfully designed APIs.<br><br>
      Clean architecture, purposeful UI/UX, and impactful technology — these are 
      the principles I build around. Whether it's a sleek mobile app or a scalable 
      backend, I bring the same obsessive attention to detail.
    </p>
    <div style="margin-top: 40px;">
      <span class="badge">Flutter</span>
      <span class="badge">Mobile-first</span>
      <span class="badge">Clean Code</span>
      <span class="badge">Real-time Systems</span>
    </div>
  </div>

  <!-- TECH STACK -->
  <div class="section" id="stack">
    <div class="section-header">
      <span class="section-num">02</span>
      <h2 class="section-title">Tech Stack</h2>
      <div class="section-line"></div>
    </div>
    <div class="tech-grid">
      <div class="tech-cell">
        <div class="tech-icon">🎯</div>
        <div class="tech-name">Dart</div>
        <div class="tech-type">Language</div>
      </div>
      <div class="tech-cell">
        <div class="tech-icon">📱</div>
        <div class="tech-name">Flutter</div>
        <div class="tech-type">Framework</div>
      </div>
      <div class="tech-cell">
        <div class="tech-icon">⚡</div>
        <div class="tech-name">Node.js</div>
        <div class="tech-type">Backend</div>
      </div>
      <div class="tech-cell">
        <div class="tech-icon">🚂</div>
        <div class="tech-name">Express</div>
        <div class="tech-type">Backend</div>
      </div>
      <div class="tech-cell">
        <div class="tech-icon">🍃</div>
        <div class="tech-name">MongoDB</div>
        <div class="tech-type">Database</div>
      </div>
      <div class="tech-cell">
        <div class="tech-icon">🔥</div>
        <div class="tech-name">Firebase</div>
        <div class="tech-type">Platform</div>
      </div>
      <div class="tech-cell">
        <div class="tech-icon">🔌</div>
        <div class="tech-name">Socket.IO</div>
        <div class="tech-type">Real-time</div>
      </div>
      <div class="tech-cell">
        <div class="tech-icon">🔒</div>
        <div class="tech-name">JWT</div>
        <div class="tech-type">Auth</div>
      </div>
      <div class="tech-cell">
        <div class="tech-icon">🐙</div>
        <div class="tech-name">Git</div>
        <div class="tech-type">Version Control</div>
      </div>
      <div class="tech-cell">
        <div class="tech-icon">🐧</div>
        <div class="tech-name">Linux</div>
        <div class="tech-type">Systems</div>
      </div>
    </div>
  </div>

  <!-- GITHUB STATS -->
  <div class="section" id="stats">
    <div class="section-header">
      <span class="section-num">03</span>
      <h2 class="section-title">GitHub Stats</h2>
      <div class="section-line"></div>
    </div>

    <div class="stats-row">
      <div class="stat-cell" id="stat-repos">
        <div class="stat-number" id="repos-count">—</div>
        <div class="stat-label">Repositories</div>
      </div>
      <div class="stat-cell" id="stat-stars">
        <div class="stat-number" id="stars-count">—</div>
        <div class="stat-label">Stars Earned</div>
      </div>
      <div class="stat-cell" id="stat-commits">
        <div class="stat-number" id="contrib-count">—</div>
        <div class="stat-label">Contributions</div>
      </div>
    </div>

    <div class="github-card" style="margin-top:2px;">
      <img src="https://github-readme-stats.vercel.app/api?username=rauftaha757&show_icons=true&theme=dark&bg_color=08080d&title_color=c9a96e&text_color=f5f3ee&icon_color=c9a96e&border_color=1a1a24&hide_border=false" alt="GitHub Stats"/>
    </div>
    <div class="github-card" style="margin-top:2px;">
      <img src="https://github-readme-streak-stats.herokuapp.com/?user=rauftaha757&theme=dark&background=08080d&ring=c9a96e&fire=e8d5a3&currStreakLabel=c9a96e&border=1a1a24" alt="GitHub Streak"/>
    </div>
    <div class="github-card" style="margin-top:2px;">
      <img src="https://github-readme-activity-graph.vercel.app/graph?username=rauftaha757&bg_color=08080d&color=c9a96e&line=c9a96e&point=e8d5a3&area=true&hide_border=true" alt="Contribution Graph"/>
    </div>
  </div>

  <!-- CONNECT -->
  <div class="section" id="connect">
    <div class="section-header">
      <span class="section-num">04</span>
      <h2 class="section-title">Connect</h2>
      <div class="section-line"></div>
    </div>
    <div class="connect-grid">
      <a class="connect-item" href="mailto:rauftaha757@gmail.com">
        <div class="connect-icon">✉️</div>
        <div>
          <div class="connect-label">Email</div>
          <div class="connect-value">rauftaha757@gmail.com</div>
        </div>
      </a>
      <a class="connect-item" href="https://linkedin.com/in/rauftaha757" target="_blank">
        <div class="connect-icon">💼</div>
        <div>
          <div class="connect-label">LinkedIn</div>
          <div class="connect-value">rauftaha757</div>
        </div>
      </a>
      <a class="connect-item" href="https://github.com/rauftaha757" target="_blank">
        <div class="connect-icon">🐙</div>
        <div>
          <div class="connect-label">GitHub</div>
          <div class="connect-value">rauftaha757</div>
        </div>
      </a>
      <a class="connect-item" href="https://drive.google.com/file/d/1GyhDPpnKMCYqWWOsodRyCgmi7mvZAgXp/view" target="_blank">
        <div class="connect-icon">📄</div>
        <div>
          <div class="connect-label">Résumé</div>
          <div class="connect-value">View Full CV</div>
        </div>
      </a>
    </div>
  </div>

  <!-- FOOTER -->
  <div class="footer">
    <div class="footer-motto">"Code. Create. <em>Repeat.</em>"</div>
    <div class="footer-right">Taha Rauf · 2025</div>
  </div>

</div><!-- end .page -->

<script>
  // CUSTOM CURSOR
  const cursor = document.getElementById('cursor');
  const ring = document.getElementById('cursorRing');
  let mx = 0, my = 0, rx = 0, ry = 0;
  document.addEventListener('mousemove', e => { mx = e.clientX; my = e.clientY; });
  function animCursor() {
    cursor.style.left = mx + 'px';
    cursor.style.top = my + 'px';
    rx += (mx - rx) * 0.15;
    ry += (my - ry) * 0.15;
    ring.style.left = rx + 'px';
    ring.style.top = ry + 'px';
    requestAnimationFrame(animCursor);
  }
  animCursor();
  document.querySelectorAll('a, button, .tech-cell').forEach(el => {
    el.addEventListener('mouseenter', () => {
      cursor.style.width = '14px';
      cursor.style.height = '14px';
      ring.style.width = '54px';
      ring.style.height = '54px';
    });
    el.addEventListener('mouseleave', () => {
      cursor.style.width = '8px';
      cursor.style.height = '8px';
      ring.style.width = '36px';
      ring.style.height = '36px';
    });
  });

  // SCROLL REVEAL
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.1 });
  document.querySelectorAll('.section').forEach(s => observer.observe(s));

  // GITHUB STATS
  async function loadGitHubStats() {
    try {
      const res = await fetch('https://api.github.com/users/rauftaha757');
      const data = await res.json();
      document.getElementById('repos-count').textContent = data.public_repos || '—';
      document.getElementById('contrib-count').textContent = '500+';

      // Count total stars
      const reposRes = await fetch('https://api.github.com/users/rauftaha757/repos?per_page=100');
      const repos = await reposRes.json();
      if (Array.isArray(repos)) {
        const stars = repos.reduce((sum, r) => sum + (r.stargazers_count || 0), 0);
        document.getElementById('stars-count').textContent = stars;
      }
    } catch(e) {
      document.getElementById('repos-count').textContent = '30+';
      document.getElementById('stars-count').textContent = '—';
      document.getElementById('contrib-count').textContent = '500+';
    }
  }
  loadGitHubStats();

  // COUNTER ANIMATION
  function animateCount(el, target) {
    let current = 0;
    const step = Math.max(1, Math.floor(target / 40));
    const interval = setInterval(() => {
      current = Math.min(current + step, target);
      el.textContent = current;
      if (current >= target) clearInterval(interval);
    }, 30);
  }
</script>
</body>
</html>
