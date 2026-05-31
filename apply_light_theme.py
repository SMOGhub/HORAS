#!/usr/bin/env python3
"""Applies light theme CSS transformations and assembles final HTML."""

SRC = '/root/.claude/uploads/0714768b-e82a-4c35-afbb-647f498bff72/a8c453ba-RCoPilot.html'
OUT = '/home/user/HORAS/RCoPilot_redesigned.html'
HEAD_LINES = 19  # already written to OUT

with open(SRC, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# CSS is lines 18-1110 (0-indexed 17-1109), wrapped by <style> (line 17) and </style> (line 1110)
css = ''.join(lines[17:1110])  # includes <style> opening

# --- :root variables ---
css = css.replace(
    '--bg: #0C0C0F;',
    '--bg: #F4F5F9;'
)
css = css.replace(
    '--surface: #14141B;',
    '--surface: #FFFFFF;'
)
css = css.replace(
    '--card: #1C1C27;',
    '--card: #FFFFFF;'
)
css = css.replace(
    '--card2: #22222F;',
    '--card2: #EEF0F7;'
)
css = css.replace(
    '--border: #2C2C3E;',
    '--border: rgba(0,0,0,.08);'
)
css = css.replace(
    '--text: #EEEEF5;',
    '--text: #111827;'
)
css = css.replace(
    '--muted: #72728A;',
    '--muted: #6B7280;'
)
css = css.replace(
    '--subtle: #32324A;',
    '--subtle: #E5E7EB;'
)
css = css.replace(
    '--nav-h: 68px;',
    '--nav-h: 72px;'
)

# --- Font: add Plus Jakarta Sans ---
css = css.replace(
    "font-family:'DM Sans',system-ui,sans-serif",
    "font-family:'Plus Jakarta Sans','DM Sans',system-ui,sans-serif"
)
css = css.replace(
    "font-family:'DM Sans',sans-serif",
    "font-family:'Plus Jakarta Sans','DM Sans',sans-serif"
)

# --- nav: add subtle shadow ---
css = css.replace(
    "nav{height:calc(var(--nav-h) + var(--safe));padding-bottom:var(--safe);background:var(--surface);border-top:.5px solid var(--border);display:flex;align-items:center;flex-shrink:0;position:fixed;bottom:0;left:0;right:0;max-width:480px;margin:0 auto;z-index:150}",
    "nav{height:calc(var(--nav-h) + var(--safe));padding-bottom:var(--safe);background:var(--surface);border-top:.5px solid var(--border);display:flex;align-items:center;flex-shrink:0;position:fixed;bottom:0;left:0;right:0;max-width:480px;margin:0 auto;z-index:150;box-shadow:0 -4px 20px rgba(0,0,0,.06)}"
)

# --- card: add shadow ---
css = css.replace(
    ".card{background:var(--card);border:.5px solid var(--border);border-radius:18px;padding:16px;margin:0 16px 12px}",
    ".card{background:var(--card);border:.5px solid var(--border);border-radius:18px;padding:16px;margin:0 16px 12px;box-shadow:0 2px 8px rgba(0,0,0,.05)}"
)

# --- stat-card: add shadow ---
css = css.replace(
    ".stat-card{background:var(--card);border:.5px solid var(--border);border-radius:16px;padding:14px 12px;display:flex;flex-direction:column-reverse;justify-content:flex-end}",
    ".stat-card{background:var(--card);border:.5px solid var(--border);border-radius:16px;padding:14px 12px;display:flex;flex-direction:column-reverse;justify-content:flex-end;box-shadow:0 1px 6px rgba(0,0,0,.04)}"
)

# --- total-hero: change dark gradient to light ---
css = css.replace(
    ".total-hero{margin:0 16px 12px;padding:20px;border-radius:18px;background:linear-gradient(135deg,#1C1C27,#22222F);border:.5px solid var(--border)}",
    ".total-hero{margin:0 16px 12px;padding:20px;border-radius:18px;background:linear-gradient(135deg,#EEF0F7,#E4E7EF);border:.5px solid var(--border);box-shadow:0 2px 12px rgba(0,0,0,.06)}"
)

# --- total-hero text colors: was white on dark, now dark on light ---
css = css.replace(
    ".total-big{font-family:'Syne',sans-serif;font-size:28px;font-weight:800;color:#fff;line-height:1}",
    ".total-big{font-family:'Syne',sans-serif;font-size:28px;font-weight:800;color:var(--text);line-height:1}"
)
css = css.replace(
    "#all-h,#all-e-val{font-family:'DM Sans',sans-serif;font-size:24px;font-weight:700;color:#fff;line-height:1}",
    "#all-h,#all-e-val{font-family:'Plus Jakarta Sans','DM Sans',sans-serif;font-size:24px;font-weight:700;color:var(--text);line-height:1}"
)
css = css.replace(
    ".total-big span{font-size:11px;color:rgba(255,255,255,.55);font-weight:400;display:block;margin-bottom:5px;font-family:'DM Sans',sans-serif;text-transform:uppercase;letter-spacing:.06em}",
    ".total-big span{font-size:11px;color:var(--muted);font-weight:400;display:block;margin-bottom:5px;font-family:'Plus Jakarta Sans','DM Sans',sans-serif;text-transform:uppercase;letter-spacing:.06em}"
)
css = css.replace(
    ".total-earn-big{font-family:'Syne',sans-serif;font-size:28px;font-weight:800;color:#fff;text-align:right;line-height:1}",
    ".total-earn-big{font-family:'Syne',sans-serif;font-size:28px;font-weight:800;color:var(--text);text-align:right;line-height:1}"
)
css = css.replace(
    ".total-earn-big span{font-size:11px;color:rgba(255,255,255,.55);font-weight:400;display:block;margin-bottom:5px;font-family:'DM Sans',sans-serif;text-transform:uppercase;letter-spacing:.06em;text-align:right}",
    ".total-earn-big span{font-size:11px;color:var(--muted);font-weight:400;display:block;margin-bottom:5px;font-family:'Plus Jakarta Sans','DM Sans',sans-serif;text-transform:uppercase;letter-spacing:.06em;text-align:right}"
)

# --- week hist items: white text → dark ---
css = css.replace(
    ".whi-h{font-family:'Syne',sans-serif;font-size:15px;font-weight:800;color:#fff;flex-shrink:0;text-align:right}",
    ".whi-h{font-family:'Syne',sans-serif;font-size:15px;font-weight:800;color:var(--text);flex-shrink:0;text-align:right}"
)

# --- month history ---
css = css.replace(
    ".month-total-h{font-family:'Syne',sans-serif;font-size:14px;font-weight:800;color:#fff}",
    ".month-total-h{font-family:'Syne',sans-serif;font-size:14px;font-weight:800;color:var(--text)}"
)
css = css.replace(
    ".mwi-h{font-family:'Syne',sans-serif;font-size:13px;font-weight:800;color:#fff;text-align:right}",
    ".mwi-h{font-family:'Syne',sans-serif;font-size:13px;font-weight:800;color:var(--text);text-align:right}"
)

# --- numpad sep color ---
css = css.replace(
    ".numpad-display-time .sep{color:#fff;background:none}",
    ".numpad-display-time .sep{color:var(--text);background:none}"
)

# --- note done text decoration ---
css = css.replace(
    "text-decoration-color:rgba(255,255,255,.4)",
    "text-decoration-color:rgba(0,0,0,.3)"
)

# --- lighten dark overlays/shadows outside A4 section ---
# Toast shadow
css = css.replace(
    "#toast{position:fixed;bottom:calc(var(--nav-h) + var(--safe) + 20px);left:50%;transform:translateX(-50%) translateY(16px);background:var(--card2);border:.5px solid var(--border);border-radius:12px;padding:10px 20px;font-size:13px;white-space:nowrap;opacity:0;transition:all .28s;pointer-events:none;z-index:999;box-shadow:0 8px 32px rgba(0,0,0,.4)}",
    "#toast{position:fixed;bottom:calc(var(--nav-h) + var(--safe) + 20px);left:50%;transform:translateX(-50%) translateY(16px);background:var(--card2);border:.5px solid var(--border);border-radius:12px;padding:10px 20px;font-size:13px;white-space:nowrap;opacity:0;transition:all .28s;pointer-events:none;z-index:999;box-shadow:0 4px 16px rgba(0,0,0,.10)}"
)

# Week dropdown shadow
css = css.replace(
    "box-shadow:0 12px 40px rgba(0,0,0,.5);",
    "box-shadow:0 8px 24px rgba(0,0,0,.12);"
)

# Duration menu shadow
css = css.replace(
    "box-shadow:0 8px 24px rgba(0,0,0,.35);",
    "box-shadow:0 6px 20px rgba(0,0,0,.10);"
)

# Card dim overlay
css = css.replace(
    ".card-dim-overlay.dimmed{background:rgba(0,0,0,.45)}",
    ".card-dim-overlay.dimmed{background:rgba(0,0,0,.18)}"
)

# numpad key ok shadow
css = css.replace(
    ".numpad-key.ok{background:linear-gradient(135deg,var(--orange),var(--red));color:#fff;box-shadow:0 4px 16px rgba(255,98,0,.35)}",
    ".numpad-key.ok{background:linear-gradient(135deg,var(--orange),var(--red));color:#fff;box-shadow:0 4px 16px rgba(240,90,0,.3)}"
)

# --- Modal sheet background update for report modal ---
css = css.replace(
    ".modal-sheet{background:var(--bg);border:.5px solid var(--border);border-radius:24px 24px 18px 18px;width:100%;max-width:520px;max-height:88vh;overflow-y:auto;padding:24px 20px 32px}",
    ".modal-sheet{background:var(--surface);border:.5px solid var(--border);border-radius:24px 24px 18px 18px;width:100%;max-width:520px;max-height:88vh;overflow-y:auto;padding:24px 20px 32px;box-shadow:0 -8px 40px rgba(0,0,0,.08)}"
)

# Notes modal sheet
css = css.replace(
    ".modal-sheet{width:100%;max-width:480px;background:var(--surface);border-radius:20px 20px 0 0;padding:20px 20px calc(20px + var(--safe));max-height:90vh;overflow-y:auto}",
    ".modal-sheet{width:100%;max-width:480px;background:var(--surface);border-radius:20px 20px 0 0;padding:20px 20px calc(20px + var(--safe));max-height:90vh;overflow-y:auto;box-shadow:0 -4px 24px rgba(0,0,0,.08)}"
)

# Perm sheet
css = css.replace(
    ".perm-sheet{background:var(--card);border-radius:28px 28px 0 0;padding:28px 24px 40px;width:100%;max-width:480px;transform:translateY(100%);transition:transform .35s cubic-bezier(.32,0,.67,0)}",
    ".perm-sheet{background:var(--card);border-radius:28px 28px 0 0;padding:28px 24px 40px;width:100%;max-width:480px;transform:translateY(100%);transition:transform .35s cubic-bezier(.32,0,.67,0);box-shadow:0 -4px 24px rgba(0,0,0,.08)}"
)

# New folder sheet
css = css.replace(
    ".new-folder-sheet{background:var(--card);border-radius:24px 24px 0 0;width:100%;padding:24px 20px 40px;transition:transform .25s cubic-bezier(.4,0,.2,1)}",
    ".new-folder-sheet{background:var(--card);border-radius:24px 24px 0 0;width:100%;padding:24px 20px 40px;transition:transform .25s cubic-bezier(.4,0,.2,1);box-shadow:0 -4px 24px rgba(0,0,0,.08)}"
)

# Numpad sheet
css = css.replace(
    ".numpad-sheet{background:var(--card);border:.5px solid var(--border);border-radius:24px 24px 0 0;width:100%;max-width:480px;padding:20px 20px 36px;touch-action:none;overscroll-behavior:contain}",
    ".numpad-sheet{background:var(--card);border:.5px solid var(--border);border-radius:24px 24px 0 0;width:100%;max-width:480px;padding:20px 20px 36px;touch-action:none;overscroll-behavior:contain;box-shadow:0 -4px 24px rgba(0,0,0,.08)}"
)

# --- Improve page header for light theme ---
css = css.replace(
    ".page-header{padding:48px 20px 16px;position:sticky;top:0;z-index:20;background:linear-gradient(180deg,var(--bg) 75%,transparent);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}",
    ".page-header{padding:48px 20px 16px;position:sticky;top:0;z-index:20;background:linear-gradient(180deg,var(--bg) 80%,rgba(244,245,249,0));backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}"
)

# --- Logo shadow: reduce for light ---
css = css.replace(
    ".header-logo{width:54px;height:54px;object-fit:contain;filter:drop-shadow(0 2px 8px rgba(0,0,0,.4));flex-shrink:0}",
    ".header-logo{width:54px;height:54px;object-fit:contain;filter:drop-shadow(0 1px 4px rgba(0,0,0,.15));flex-shrink:0}"
)

# --- Planning shadows ---
css = css.replace(
    ".pl-task{position:absolute;border-radius:8px;padding:0;color:#fff;cursor:pointer;overflow:hidden;border:.5px solid rgba(255,255,255,.18);box-shadow:0 2px 8px rgba(0,0,0,.4),inset 0 1px 0 rgba(255,255,255,.12);text-shadow:0 1px 2px rgba(0,0,0,.35);-webkit-user-select:none;user-select:none;transition:box-shadow .12s,filter .12s;min-height:24px}",
    ".pl-task{position:absolute;border-radius:8px;padding:0;color:#fff;cursor:pointer;overflow:hidden;border:.5px solid rgba(255,255,255,.25);box-shadow:0 2px 8px rgba(0,0,0,.18),inset 0 1px 0 rgba(255,255,255,.15);text-shadow:0 1px 2px rgba(0,0,0,.25);-webkit-user-select:none;user-select:none;transition:box-shadow .12s,filter .12s;min-height:24px}"
)

# --- Note FAB shadow: softer ---
css = css.replace(
    ".note-fab{position:fixed;bottom:calc(var(--nav-h) + var(--safe) + 80px);left:50%;transform:translateX(-50%);width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,var(--orange),var(--red));border:none;color:#fff;font-size:26px;display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 4px 20px rgba(255,98,0,.5);z-index:50;transition:transform .15s,opacity .15s}",
    ".note-fab{position:fixed;bottom:calc(var(--nav-h) + var(--safe) + 80px);left:50%;transform:translateX(-50%);width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,var(--orange),var(--red));border:none;color:#fff;font-size:26px;display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 4px 16px rgba(240,90,0,.35);z-index:50;transition:transform .15s,opacity .15s}"
)

# --- btn-generate shadow ---
css = css.replace(
    ".btn-generate{width:calc(100% - 32px);margin:8px 16px 0;padding:17px;border-radius:16px;background:linear-gradient(135deg,var(--orange),var(--red));border:none;color:#fff;font-family:'Syne',sans-serif;font-size:16px;font-weight:800;cursor:pointer;box-shadow:0 6px 24px rgba(255,98,0,.4);letter-spacing:.01em;transition:opacity .18s,transform .15s}",
    ".btn-generate{width:calc(100% - 32px);margin:8px 16px 0;padding:17px;border-radius:16px;background:linear-gradient(135deg,var(--orange),var(--red));border:none;color:#fff;font-family:'Syne',sans-serif;font-size:16px;font-weight:800;cursor:pointer;box-shadow:0 4px 16px rgba(240,90,0,.3);letter-spacing:.01em;transition:opacity .18s,transform .15s}"
)

# --- equipe fab shadow ---
css = css.replace(
    ".equipe-membres-fab{width:46px;height:46px;border-radius:50%;background:linear-gradient(135deg,var(--orange),var(--red));border:none;color:#fff;font-size:26px;line-height:1;display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 4px 18px rgba(255,98,0,.5);transition:transform .15s,opacity .15s}",
    ".equipe-membres-fab{width:46px;height:46px;border-radius:50%;background:linear-gradient(135deg,var(--orange),var(--red));border:none;color:#fff;font-size:26px;line-height:1;display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 4px 14px rgba(240,90,0,.3);transition:transform .15s,opacity .15s}"
)

# --- theme-light override: update to our new light values ---
css = css.replace(
    """/* ── THÈME CLAIR ── */
body.theme-light {
  --bg:#F2F2F7;--surface:#FFFFFF;--card:#FFFFFF;--card2:#FFFFFF;--border:rgba(0,0,0,.1);
  --text:#1C1C1E;--muted:#8E8E93;--subtle:#E5E5EA;--input:#F2F2F7;
  --nav-bg:rgba(242,242,247,.92);
}
body.theme-light .week-pill{background:#FFFFFF;color:#1C1C1E}
body.theme-light .week-pill-arrow{background:#F2F2F7;color:#1C1C1E}
body.theme-light .page-title,body.theme-light .nav-btn{color:#1C1C1E}
body.theme-light .set-input,body.theme-light .modal-textarea,body.theme-light .modal-author-input{color:#1C1C1E;background:#F2F2F7}
body.theme-light .menu-back-btn{color:#1C1C1E}
body.theme-light .menu-subscreen{background:#F2F2F7}
body.theme-light .menu-subscreen-header{border-color:rgba(0,0,0,.1)}""",
    """/* ── THÈME CLAIR (défaut) ── */
body.theme-light {
  --bg:#F4F5F9;--surface:#FFFFFF;--card:#FFFFFF;--card2:#EEF0F7;--border:rgba(0,0,0,.08);
  --text:#111827;--muted:#6B7280;--subtle:#E5E7EB;
}"""
)

# --- dark theme override: if app sets dark explicitly ---
# Add dark theme override after the theme-light block
css = css.replace(
    "/* ── THEME SELECTOR ── */",
    """/* ── THÈME SOMBRE (override) ── */
body.theme-dark {
  --bg:#0C0C0F;--surface:#14141B;--card:#1C1C27;--card2:#22222F;--border:#2C2C3E;
  --text:#EEEEF5;--muted:#72728A;--subtle:#32324A;
}
/* ── THEME SELECTOR ── */"""
)

# Now write: append <style> + modified css (already has <style> tag from position 17)
# Actually the css variable starts with '<style>\n', ends just before '</style>'
# Write it to the output file after the head section

with open(OUT, 'r', encoding='utf-8') as f:
    head = f.read()

# Assemble: head (19 lines already) + css (with <style> tag) + </style> + rest of original
rest = ''.join(lines[1110:])  # from </style> onwards (line 1111 = index 1110)

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(head)
    f.write(css)
    f.write(rest)

print(f"Done. Output: {OUT}")
with open(OUT, 'r', encoding='utf-8') as f:
    total = sum(1 for _ in f)
print(f"Total lines: {total}")
