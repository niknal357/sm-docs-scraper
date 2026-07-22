const themeButton = document.getElementById('theme-button');
const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
const updateThemeButton = () => {
  const dark = document.documentElement.dataset.theme === 'dark';
  const nextTheme = dark ? 'light' : 'dark';
  themeButton.setAttribute('aria-label', `Switch to ${nextTheme} mode`);
  themeButton.title = `Switch to ${nextTheme} mode`;
};
const applyTheme = (theme) => {
  document.documentElement.dataset.theme = theme;
  updateThemeButton();
};
const savedTheme = () => {
  try {
    const theme = localStorage.getItem('sm-docs-theme');
    return theme === 'light' || theme === 'dark' ? theme : null;
  } catch (_) {
    return null;
  }
};
updateThemeButton();
themeButton.addEventListener('click', () => {
  const theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
  applyTheme(theme);
  try {
    localStorage.setItem('sm-docs-theme', theme);
  } catch (_) {}
});
if ('addEventListener' in systemTheme) {
  systemTheme.addEventListener('change', (event) => {
    if (!savedTheme()) applyTheme(event.matches ? 'dark' : 'light');
  });
}

const menu = document.getElementById('menu-button');
const sidebar = document.getElementById('sidebar');
const mobileNavigation = window.matchMedia('(max-width: 996px)');
const mobileSearch = window.matchMedia('(max-width: 600px)');
const mobileSearchButton = document.getElementById('mobile-search-button');
const mobileSearchClose = document.getElementById('mobile-search-close');
const searchInput = document.getElementById('site-search-input');

const setSidebarOpen = (open) => {
  const shouldOpen = Boolean(open && mobileNavigation.matches);
  if (shouldOpen) setMobileSearchOpen(false);
  document.body.classList.toggle('sidebar-open', shouldOpen);
  menu.setAttribute('aria-expanded', String(shouldOpen));
  menu.setAttribute('aria-label', shouldOpen ? 'Close navigation' : 'Open navigation');
  if (mobileNavigation.matches && !shouldOpen) {
    sidebar.setAttribute('inert', '');
    sidebar.setAttribute('aria-hidden', 'true');
  } else {
    sidebar.removeAttribute('inert');
    sidebar.removeAttribute('aria-hidden');
  }
};

const setMobileSearchOpen = (open) => {
  const shouldOpen = Boolean(open && mobileSearch.matches);
  if (shouldOpen) setSidebarOpen(false);
  document.body.classList.toggle('mobile-search-open', shouldOpen);
  mobileSearchButton.setAttribute('aria-expanded', String(shouldOpen));
  if (shouldOpen) {
    requestAnimationFrame(() => searchInput.focus({ preventScroll: true }));
  } else {
    searchInput.blur();
  }
};

menu.addEventListener('click', () => {
  setSidebarOpen(!document.body.classList.contains('sidebar-open'));
});
mobileSearchButton.addEventListener('click', () => setMobileSearchOpen(true));
mobileSearchClose.addEventListener('click', () => {
  setMobileSearchOpen(false);
  mobileSearchButton.focus();
});
setSidebarOpen(false);
document.addEventListener('sm-docs:open-mobile-search', () => {
  setMobileSearchOpen(true);
});
document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  if (document.body.classList.contains('mobile-search-open')) {
    setMobileSearchOpen(false);
    mobileSearchButton.focus();
  } else if (document.body.classList.contains('sidebar-open')) {
    setSidebarOpen(false);
    menu.focus();
  }
});
if ('addEventListener' in mobileNavigation) {
  mobileNavigation.addEventListener('change', (event) => {
    if (!event.matches) setSidebarOpen(false);
  });
  mobileSearch.addEventListener('change', (event) => {
    if (!event.matches) setMobileSearchOpen(false);
  });
}

const statePrefix = 'sm-docs-sidebar:';
const groups = sidebar.querySelectorAll('details[data-sidebar-key]');
groups.forEach((group) => {
  const key = statePrefix + group.dataset.sidebarKey;
  try {
    const saved = sessionStorage.getItem(key);
    if (saved !== null) {
      group.open = saved === 'open';
    } else {
      sessionStorage.setItem(key, group.open ? 'open' : 'closed');
    }
  } catch (_) {}
  group.addEventListener('toggle', () => {
    try {
      sessionStorage.setItem(key, group.open ? 'open' : 'closed');
    } catch (_) {}
  });
});
const scrollAnchorKey = statePrefix + 'scroll-anchor';
sidebar.addEventListener('click', (event) => {
  const link = event.target.closest('a');
  if (!link || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
  const sidebarRect = sidebar.getBoundingClientRect();
  const linkRect = link.getBoundingClientRect();
  try {
    sessionStorage.setItem(scrollAnchorKey, JSON.stringify({
      href: link.href,
      top: linkRect.top - sidebarRect.top,
    }));
  } catch (_) {}
  setSidebarOpen(false);
});

const activeLink = sidebar.querySelector('a.active');
if (activeLink) {
  let parent = activeLink.parentElement;
  while (parent) {
    if (parent.tagName === 'DETAILS') parent.open = true;
    parent = parent.parentElement;
  }

  let restoredPosition = false;
  try {
    const savedAnchor = JSON.parse(sessionStorage.getItem(scrollAnchorKey));
    sessionStorage.removeItem(scrollAnchorKey);
    if (savedAnchor?.href === window.location.href && Number.isFinite(savedAnchor.top)) {
      const sidebarRect = sidebar.getBoundingClientRect();
      const activeRect = activeLink.getBoundingClientRect();
      sidebar.scrollTop += activeRect.top - sidebarRect.top - savedAnchor.top;
      restoredPosition = true;
    }
  } catch (_) {
    try {
      sessionStorage.removeItem(scrollAnchorKey);
    } catch (_) {}
  }
  if (!restoredPosition) activeLink.scrollIntoView({ block: 'nearest' });
}

const copyStatus = document.getElementById('copy-status');
const createSvgElement = (name, attributes = {}) => {
  const element = document.createElementNS('http://www.w3.org/2000/svg', name);
  Object.entries(attributes).forEach(([key, value]) => element.setAttribute(key, value));
  return element;
};
const setCopyIcon = (button, copied) => {
  const svg = createSvgElement('svg', {
    'aria-hidden': 'true',
    viewBox: '0 0 24 24',
  });
  if (copied) {
    svg.append(createSvgElement('path', { d: 'm4 12 5 5L20 6' }));
  } else {
    svg.append(
      createSvgElement('rect', { x: '9', y: '9', width: '11', height: '11' }),
      createSvgElement('path', { d: 'M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1' }),
    );
  }
  button.replaceChildren(svg);
};
const writeClipboard = async (text) => {
  if (navigator.clipboard?.writeText) {
    try {
      await navigator.clipboard.writeText(text);
      return;
    } catch (_) {}
  }
  const textarea = document.createElement('textarea');
  textarea.value = text;
  textarea.style.position = 'fixed';
  textarea.style.opacity = '0';
  document.body.append(textarea);
  textarea.select();
  const copied = document.execCommand('copy');
  textarea.remove();
  if (!copied) throw new Error('Clipboard access failed');
};
const createCopyButton = (text, label, className = '') => {
  const button = document.createElement('button');
  button.className = `copy-button${className ? ` ${className}` : ''}`;
  button.type = 'button';
  button.setAttribute('aria-label', label);
  button.title = label;
  setCopyIcon(button, false);

  let resetTimer;
  button.addEventListener('click', async () => {
    try {
      await writeClipboard(text);
      clearTimeout(resetTimer);
      setCopyIcon(button, true);
      const copiedLabel = label.replace(/^Copy/, 'Copied');
      button.setAttribute('aria-label', copiedLabel);
      copyStatus.textContent = `${copiedLabel}.`;
      resetTimer = setTimeout(() => {
        setCopyIcon(button, false);
        button.setAttribute('aria-label', label);
        copyStatus.textContent = '';
      }, 1500);
    } catch (error) {
      console.error(error);
      copyStatus.textContent = 'Could not copy to the clipboard.';
    }
  });
  return button;
};
window.SmDocsCopy = { createButton: createCopyButton };

document.querySelectorAll('.api-signature').forEach((signature) => {
  const code = signature.querySelector('code');
  if (!code) return;
  const copy = code.cloneNode(true);
  copy.querySelectorAll('.optional-marker').forEach((marker) => {
    marker.textContent = '?';
  });
  const text = copy.textContent.trim();
  if (!text) return;
  signature.append(createCopyButton(text, 'Copy signature', 'signature-copy'));
});
