(() => {
  'use strict';

  const content = document.querySelector('.doc-content[data-link-preview-index]');
  if (!content) return;

  const previewIndexUrl = new URL(content.dataset.linkPreviewIndex, window.location.href);
  const siteRoot = new URL('../', previewIndexUrl);
  const hoverAvailable = window.matchMedia('(hover: hover)');
  const showDelay = 300;
  const hideDelay = 100;

  const preview = document.createElement('aside');
  preview.className = 'link-preview';
  preview.id = 'link-preview';
  preview.setAttribute('role', 'tooltip');
  preview.hidden = true;
  document.body.append(preview);

  let recordsPromise;
  let hoverLink = null;
  let focusLink = null;
  let previewHovered = false;
  let visibleLink = null;
  let showTimer;
  let hideTimer;
  let requestVersion = 0;

  const targetUrl = (link) => {
    try {
      const url = new URL(link.href, window.location.href);
      const rootPath = siteRoot.pathname.endsWith('/')
        ? siteRoot.pathname
        : `${siteRoot.pathname}/`;
      if (url.origin !== siteRoot.origin || !url.pathname.startsWith(rootPath)) return null;
      if (!url.pathname.endsWith('.html')) return null;
      return url;
    } catch (_) {
      return null;
    }
  };

  const previewLink = (target) => {
    const link = target.closest('a[href]');
    return link && content.contains(link) && targetUrl(link) ? link : null;
  };

  const loadRecords = () => {
    if (!recordsPromise) {
      recordsPromise = fetch(previewIndexUrl)
        .then((response) => {
          if (!response.ok) throw new Error(`Link preview index returned ${response.status}`);
          return response.json();
        })
        .then((payload) => {
          if (payload.version !== 1 || !Array.isArray(payload.records)) {
            throw new Error('Unsupported link preview index');
          }
          return new Map(payload.records.map((record) => [
            new URL(record.url.replace(/^\/+/, ''), siteRoot).href,
            record,
          ]));
        });
    }
    return recordsPromise;
  };

  const renderPreview = (record) => {
    const heading = document.createElement('strong');
    heading.className = 'link-preview-title';
    heading.textContent = record.title;

    const hierarchy = document.createElement('div');
    hierarchy.className = 'link-preview-hierarchy';
    hierarchy.textContent = record.hierarchy;

    const elements = [heading];
    if (record.hierarchy) elements.push(hierarchy);

    if (record.signature) {
      const signature = document.createElement('code');
      signature.className = 'link-preview-signature';
      signature.textContent = record.signature;
      elements.push(signature);
    }
    if (record.summary) {
      const summary = document.createElement('p');
      summary.className = 'link-preview-summary';
      summary.textContent = record.summary;
      elements.push(summary);
    }
    preview.replaceChildren(...elements);
  };

  const positionPreview = (link) => {
    const gap = 10;
    const margin = 12;
    const linkRect = link.getBoundingClientRect();
    const previewRect = preview.getBoundingClientRect();
    let left = linkRect.left + (linkRect.width - previewRect.width) / 2;
    left = Math.max(margin, Math.min(left, window.innerWidth - previewRect.width - margin));

    let top = linkRect.bottom + gap;
    if (top + previewRect.height > window.innerHeight - margin) {
      top = linkRect.top - previewRect.height - gap;
    }
    top = Math.max(margin, Math.min(top, window.innerHeight - previewRect.height - margin));
    preview.style.left = `${Math.round(left)}px`;
    preview.style.top = `${Math.round(top)}px`;
  };

  const hidePreview = () => {
    clearTimeout(showTimer);
    clearTimeout(hideTimer);
    requestVersion += 1;
    if (visibleLink) visibleLink.removeAttribute('aria-describedby');
    previewHovered = false;
    visibleLink = null;
    preview.hidden = true;
  };

  const showPreview = async (link) => {
    const url = targetUrl(link);
    if (!url) return;
    const version = ++requestVersion;
    try {
      const records = await loadRecords();
      if (version !== requestVersion || link !== (focusLink || hoverLink)) return;
      const record = records.get(url.href);
      if (!record) return;

      if (visibleLink && visibleLink !== link) {
        visibleLink.removeAttribute('aria-describedby');
      }
      renderPreview(record);
      visibleLink = link;
      link.setAttribute('aria-describedby', preview.id);
      preview.hidden = false;
      positionPreview(link);
    } catch (error) {
      console.error('Link previews could not be loaded', error);
    }
  };

  const scheduleShow = (link, delay) => {
    clearTimeout(showTimer);
    clearTimeout(hideTimer);
    if (visibleLink === link) return;
    const version = ++requestVersion;
    showTimer = setTimeout(() => {
      if (version === requestVersion && link === (focusLink || hoverLink)) {
        showPreview(link);
      }
    }, delay);
  };

  const scheduleHide = () => {
    clearTimeout(showTimer);
    clearTimeout(hideTimer);
    const version = ++requestVersion;
    hideTimer = setTimeout(() => {
      if (version === requestVersion && !focusLink && !hoverLink && !previewHovered) {
        hidePreview();
      }
    }, hideDelay);
  };

  preview.addEventListener('mouseenter', () => {
    if (!hoverAvailable.matches) return;
    previewHovered = true;
    clearTimeout(hideTimer);
  });

  preview.addEventListener('mouseleave', () => {
    previewHovered = false;
    if (!focusLink && !hoverLink) scheduleHide();
  });

  content.addEventListener('mouseover', (event) => {
    if (!hoverAvailable.matches) return;
    const link = previewLink(event.target);
    if (!link || link.contains(event.relatedTarget)) return;
    hoverLink = link;
    scheduleShow(link, showDelay);
  });

  content.addEventListener('mouseout', (event) => {
    if (!hoverAvailable.matches) return;
    const link = previewLink(event.target);
    if (!link || link.contains(event.relatedTarget)) return;
    if (hoverLink === link) hoverLink = null;
    if (!focusLink) scheduleHide();
  });

  content.addEventListener('focusin', (event) => {
    const link = previewLink(event.target);
    if (!link) return;
    focusLink = link;
    scheduleShow(link, 0);
  });

  content.addEventListener('focusout', (event) => {
    const link = previewLink(event.target);
    if (!link || link.contains(event.relatedTarget)) return;
    if (focusLink === link) focusLink = null;
    if (hoverLink) scheduleShow(hoverLink, showDelay);
    else scheduleHide();
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && !preview.hidden) hidePreview();
  });
  window.addEventListener('scroll', hidePreview, { passive: true });
  window.addEventListener('resize', () => {
    if (visibleLink) positionPreview(visibleLink);
  });
})();
