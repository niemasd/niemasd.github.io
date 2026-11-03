(() => {
  "use strict";

  const root = document.documentElement;
  const themeButtons = Array.from(document.querySelectorAll("[data-theme-toggle]"));
  const themeStorageKey = "academic-site-theme";

  function readStoredTheme() {
    try {
      const saved = window.localStorage.getItem(themeStorageKey);
      return saved === "light" || saved === "dark" ? saved : null;
    } catch (_error) {
      return null;
    }
  }

  function preferredTheme() {
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  function setTheme(theme, persist) {
    root.dataset.theme = theme;
    themeButtons.forEach((button) => {
      const nextTheme = theme === "dark" ? "light" : "dark";
      const label = nextTheme === "dark" ? "Switch to dark theme" : "Switch to light theme";
      button.setAttribute("aria-label", label);
      button.setAttribute("title", label);
      const text = button.querySelector(".theme-toggle-label");
      if (text) text.textContent = nextTheme === "dark" ? "Dark theme" : "Light theme";
      else button.textContent = nextTheme === "dark" ? "Dark theme" : "Light theme";
    });
    if (persist) {
      try {
        window.localStorage.setItem(themeStorageKey, theme);
      } catch (_error) {
        // Storage may be unavailable for local file URLs or restricted browsers.
      }
    }
  }

  setTheme(readStoredTheme() || preferredTheme(), false);
  themeButtons.forEach((button) => {
    button.addEventListener("click", () => {
      setTheme(root.dataset.theme === "dark" ? "light" : "dark", true);
    });
  });

  // Expand/collapse nested navigation and persist visitor choices when storage works.
  const navStorageKey = "academic-site-navigation";
  let navState = {};
  try {
    const parsedState = JSON.parse(window.localStorage.getItem(navStorageKey) || "{}");
    navState = parsedState && typeof parsedState === "object" && !Array.isArray(parsedState)
      ? parsedState
      : {};
  } catch (_error) {
    navState = {};
  }

  function setNavigationState(button, open, save) {
    const list = document.getElementById(button.getAttribute("aria-controls"));
    if (!list) return;
    const requiredOpen = button.dataset.requiredOpen === "true" || button.disabled;
    const expanded = requiredOpen || open;
    button.setAttribute("aria-expanded", String(expanded));
    const label = button.dataset.navLabel || "section";
    button.setAttribute("aria-label", `${expanded ? "Collapse" : "Expand"} ${label}`);
    list.hidden = !expanded;
    if (save) {
      navState[button.dataset.navId] = expanded;
      try {
        window.localStorage.setItem(navStorageKey, JSON.stringify(navState));
      } catch (_error) {
        // Navigation still works when local storage is unavailable.
      }
    }
  }

  document.querySelectorAll("[data-nav-toggle]").forEach((button) => {
    const requiredOpen = button.dataset.requiredOpen === "true" || button.disabled;
    const saved = Object.prototype.hasOwnProperty.call(navState, button.dataset.navId)
      ? Boolean(navState[button.dataset.navId])
      : false;
    setNavigationState(button, requiredOpen || saved, requiredOpen);
    button.addEventListener("click", () => {
      if (button.disabled) return;
      const currentlyOpen = button.getAttribute("aria-expanded") === "true";
      setNavigationState(button, !currentlyOpen, true);
    });
  });

  // External links can come from Markdown, trusted HTML, or custom builders.
  // Apply the new-tab/security policy consistently to all HTTP(S) links.
  document.querySelectorAll("a[href]").forEach((link) => {
    const href = link.getAttribute("href").trim();
    if (/^(https?:)?\/\//i.test(href)) {
      link.setAttribute("target", "_blank");
      const relTokens = new Set((link.getAttribute("rel") || "").split(/\s+/).filter(Boolean));
      relTokens.add("noopener");
      relTokens.add("noreferrer");
      link.setAttribute("rel", Array.from(relTokens).join(" "));
    }
  });

  // Mobile navigation drawer.
  const sidebar = document.getElementById("site-sidebar");
  const menuButton = document.getElementById("mobile-menu-button");
  const closeButton = document.getElementById("sidebar-close");
  const backdrop = document.getElementById("sidebar-backdrop");

  function openSidebar() {
    if (!sidebar || !menuButton || !backdrop) return;
    sidebar.classList.add("is-open");
    backdrop.classList.add("is-visible");
    menuButton.setAttribute("aria-expanded", "true");
    menuButton.setAttribute("aria-label", "Close navigation");
    if (closeButton) closeButton.focus();
  }

  function closeSidebar(returnFocus) {
    if (!sidebar || !menuButton || !backdrop) return;
    sidebar.classList.remove("is-open");
    backdrop.classList.remove("is-visible");
    menuButton.setAttribute("aria-expanded", "false");
    menuButton.setAttribute("aria-label", "Open navigation");
    if (returnFocus) menuButton.focus();
  }

  if (menuButton) menuButton.addEventListener("click", openSidebar);
  if (closeButton) closeButton.addEventListener("click", () => closeSidebar(true));
  if (backdrop) backdrop.addEventListener("click", () => closeSidebar(true));

  document.querySelectorAll(".site-sidebar a[href]").forEach((link) => {
    link.addEventListener("click", () => {
      if (window.matchMedia("(max-width: 850px)").matches) closeSidebar(false);
    });
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && sidebar && sidebar.classList.contains("is-open")) {
      closeSidebar(true);
    }
  });
})();
