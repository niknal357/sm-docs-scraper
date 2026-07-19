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
menu.addEventListener('click', () => document.body.classList.toggle('sidebar-open'));
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
const activeLink = sidebar.querySelector('a.active');
if (activeLink) {
  let parent = activeLink.parentElement;
  while (parent) {
    if (parent.tagName === 'DETAILS') parent.open = true;
    parent = parent.parentElement;
  }
  const sidebarRect = sidebar.getBoundingClientRect();
  const activeRect = activeLink.getBoundingClientRect();
  sidebar.scrollTop += activeRect.top - sidebarRect.top - sidebarRect.height / 2;
}
const search = document.getElementById('doc-search');
search.addEventListener('input', () => {
  const query = search.value.trim().toLowerCase();
  document.querySelectorAll('.sidebar-page').forEach((item) => {
    const matches = !query || item.textContent.toLowerCase().includes(query);
    item.hidden = !matches;
    if (query && matches) {
      let parent = item.parentElement;
      while (parent) {
        if (parent.tagName === 'DETAILS') parent.open = true;
        parent = parent.parentElement;
      }
    }
  });
});
