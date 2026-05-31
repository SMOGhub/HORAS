const fs = require('fs');
const path = require('path');

const BASE = __dirname;

// Ordered list of external script sources
const scripts = [
  'three.min.js',
  'libjs/shaders/CopyShader.js',
  'libjs/shaders/LuminosityHighPassShader.js',
  'libjs/postprocessing/Pass.js',
  'libjs/postprocessing/ShaderPass.js',
  'libjs/postprocessing/MaskPass.js',
  'libjs/postprocessing/EffectComposer.js',
  'libjs/postprocessing/RenderPass.js',
  'libjs/postprocessing/UnrealBloomPass.js',
  'libjs/geometries/RoundedBoxGeometry.js',
];

// Build a concatenated preamble of all external scripts
const preamble = scripts.map(s => {
  const src = fs.readFileSync(path.join(BASE, s), 'utf8');
  return `/* ===== ${s} ===== */\n${src}`;
}).join('\n\n');

// Read source HTML, strip all <script src="..."> tags and
// inject everything as one inline block before the main script
let html = fs.readFileSync(path.join(BASE, 'daikin-exploded.html'), 'utf8');

// Remove all <script src="..."></script> tags
html = html.replace(/<script src="[^"]*"><\/script>\n?/g, '');

// Insert the preamble right before the inline <script>
html = html.replace('<script>\n\'use strict\';', `<script>\n${preamble}\n\n'use strict';`);

fs.writeFileSync(path.join(BASE, 'daikin-stylish-3d.html'), html, 'utf8');

const size = (Buffer.byteLength(html, 'utf8') / 1024).toFixed(0);
console.log(`Built daikin-stylish-3d.html — ${size} KB`);
