import os
from datetime import date

# ====== Funções utilitárias ======

def formatar_paragrafos(texto):
    """Converte texto simples em HTML <p> e <blockquote> mantendo estrutura."""
    linhas = texto.strip().split("\n")
    html = []
    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue
        if linha.startswith(">"):
            html.append(f"<blockquote>{linha[1:].strip()}</blockquote>")
        else:
            html.append(f"<p>{linha}</p>")
    return "\n        ".join(html)


# ====== Entrada de dados ======

tipo = input("Tipo (artigo/colaboracao): ").strip().lower()
titulo = input("Título: ").strip()
subtitulo = input("Subtítulo: ").strip()
autor = input("Autor: ").strip()
data_publicacao = input("Data (ex: 22 de outubro de 2025): ").strip()
nome_arquivo = input("Nome do arquivo (sem espaços, ex: apartheid-financeiro): ").strip()
texto_base = input("Caminho do texto base (.txt): ").strip()

# ====== Leitura do texto ======

if not os.path.exists(texto_base):
    print(f"❌ Arquivo {texto_base} não encontrado.")
    exit(1)

with open(texto_base, "r", encoding="utf-8") as f:
    conteudo_txt = f.read()

conteudo_html = formatar_paragrafos(conteudo_txt)

# ====== Definição de destino ======

if tipo == "artigo":
    pasta_destino = "artigos"
elif tipo == "colaboracao":
    pasta_destino = "colaboracoes"
else:
    print("❌ Tipo inválido. Use 'artigo' ou 'colaboracao'.")
    exit(1)

os.makedirs(pasta_destino, exist_ok=True)
caminho_saida = os.path.join(pasta_destino, f"{nome_arquivo}.html")

# ====== Modelos HTML ======

if tipo == "artigo":
    aside_html = f"""
    <aside class="col-direita">
      <div class="box">
        <h3>Sobre o Autor</h3>
        <p><strong>{autor}</strong> é ensaísta e analista político. Escreve sobre economia, poder e os dilemas estruturais da sociedade brasileira.</p>
      </div>

      <div class="box">
        <h3>Artigos Relacionados</h3>
        <ul class="lista-link">
          <li><a href="direita-reacionaria.html">A Direita Reacionária e o Perigo da Normalização</a></li>
          <li><a href="entre-o-fracasso-e-a-farsa.html">Entre o Fracasso e a Farsa</a></li>
          <li><a href="torre-de-babel.html">A Torre de Babel Ideológica</a></li>
        </ul>
      </div>
    </aside>"""
else:
    aside_html = f"""
    <aside class="col-direita">
      <div class="box">
        <h3>Sobre o Autor</h3>
        <p><strong>{autor}</strong> é colaborador do projeto Geopolítica Global. Contribui com análises e reflexões sobre temas contemporâneos.</p>
      </div>

      <div class="box">
        <h3>Envie sua Colaboração</h3>
        <p>Deseja publicar um texto ou comentário? Envie sua colaboração para <a href="mailto:seunome@proton.me">seunome@proton.me</a>.</p>
      </div>
    </aside>"""

# ====== Template principal ======

html_final = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{titulo} — Geopolítica Global</title>
  <link rel="stylesheet" href="../css/main.css" />
  <link rel="stylesheet" href="../css/artigo.css" />
  <link rel="stylesheet" href="../css/responsivo.css" />
</head>
<body>

  <!-- Cabeçalho fixo -->
  <!--#include virtual="includes/header.html" -->
  <script src="/js/ativo.js"></script>

  <!-- Corpo principal -->
  <main class="duas-colunas">
    <article class="col-esquerda">
      <section class="artigo">
        <h2>{titulo}</h2>
        <h3>{subtitulo}</h3>
        <p class="meta">Publicado em {data_publicacao}</p>
        <hr>

        {conteudo_html}

      </section>
    </article>
{aside_html}
  </main>

  <!-- Rodapé fixo -->
  <!--#include virtual="includes/footer.html" -->
  <script src="/js/ativo.js"></script>
  <script src="../js/menu.js"></script>
</body>
</html>"""

# ====== Gravação ======

with open(caminho_saida, "w", encoding="utf-8") as f:
    f.write(html_final)

print(f"✅ Arquivo gerado com sucesso: {caminho_saida}")
