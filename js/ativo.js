// =============================================
// ativo.js — versão simplificada e precisa
// =============================================

document.addEventListener("DOMContentLoaded", () => {
  // obtém o caminho atual, sem query nem hash
  let path = window.location.pathname;

  // normaliza caminho removendo barras finais
  if (path.endsWith("/")) path = path.slice(0, -1);
  if (path === "") path = "/";

  // obtém todos os links do menu
  const links = document.querySelectorAll(".menu a, .menu-site a");

  // limpa estados anteriores
  links.forEach(link => link.classList.remove("ativo"));

  // percorre cada link
  links.forEach(link => {
    let href = link.getAttribute("href");

    // ignora query ou hash no href
    if (href.includes("?")) href = href.split("?")[0];
    if (href.includes("#")) href = href.split("#")[0];

    // normaliza o href
    if (href.endsWith("/")) href = href.slice(0, -1);
    if (href === "") href = "/";

    // comparação exata para a página atual
    if (href === path) {
      link.classList.add("ativo");
    }
    // regra extra: se estivermos em subpasta de artigos, ativa o link principal
    else if (path.startsWith("/artigos") && href === "/artigos") {
      link.classList.add("ativo");
    }
  });
});
