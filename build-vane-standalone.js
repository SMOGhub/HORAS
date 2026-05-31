const fs = require('fs'), path = require('path'), BASE = __dirname;

const scripts = [
  'three.min.js',
  'libjs/geometries/RoundedBoxGeometry.js',
];

const preamble = scripts.map(s =>
  `/* ===== ${s} ===== */\n${fs.readFileSync(path.join(BASE, s), 'utf8')}`
).join('\n\n');

let html = fs.readFileSync(path.join(BASE, 'daikin-vane.html'), 'utf8');
html = html.replace(/<script src="[^"]*"><\/script>\n?/g, '');
html = html.replace('<script>\n\'use strict\';', `<script>\n${preamble}\n\n'use strict';`);

fs.writeFileSync(path.join(BASE, 'daikin-stylish-vane.html'), html, 'utf8');
const size = (Buffer.byteLength(html,'utf8')/1024).toFixed(0);
console.log(`Built daikin-stylish-vane.html — ${size} KB`);
