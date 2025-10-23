// === MENU RESPONSIVO ===
document.addEventListener("DOMContentLoaded", function () {
  const toggle = document.querySelector(".menu-toggle");
  const links = document.querySelector(".menu-links");

  toggle.addEventListener("click", function () {
    links.classList.toggle("mostrar");
    toggle.textContent = links.classList.contains("mostrar") ? "✕" : "☰";
  });
});
// === EFEITO AO ROLAR (menu transparente) ===
window.addEventListener("scroll", () => {
  const menu = document.querySelector(".menu-site");
  if (window.scrollY > 10) {
    menu.classList.add("scrolled");
  } else {
    menu.classList.remove("scrolled");
  }
});
