import os
import shutil

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


def inserir_no_index(tipo, titulo, subtitulo, nome_arquivo, autor):
    """Insere automaticamente o novo artigo ou colaboração no index.html."""
    index_path = "index.html"
    if not os.path.exists(index_path):
        print("⚠️ index.html não encontrado na raiz. Item não inserido automaticamente.")
        return

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    if tipo == "artigo":
        bloco = f"""
    <article class="card-artigo">
      <h3><a href="/artigos/{nome_arquivo}.html">{titulo}</a></h3>
      <p>{subtitulo}</p>
    </article>"""
        marcador = "<!-- COLABORAÇÕES -->"  # ponto de referência seguro (caso queira usar)
        if "<aside" in html:
            pos = html.find("<aside")
        else:
            pos = len(html)
    else:
        bloco = f"""
      <article class="card-artigo">
        <h3><a href="/colaboracoes/{nome_arquivo}.html">{autor} — {titulo}</a></h3>
        <p>{subtitulo}</p>
      </article>"""
        # Procura a seção "Colaborações dos Leitores"
        marcador = "Colaborações dos Leitores"
        pos = html.find("</section>", html.find(marcador))

    if pos == -1:
        print("⚠️ Posição de inserção não encontrada. Verifique a estrutura do index.html.")
        return

    # Inserir o novo bloco antes do fechamento da seção correspondente
    novo_html = html[:pos] + bloco + "\n" + html[pos:]

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(novo_html)

    print(f"✅ {titulo} adicionado automaticamente ao index.html.")


# ====== Entrada de dados ======

tipo = input("Tipo (artigo/colaboracao): ").strip().lower()
titulo = input("Título: ").strip()
subtitulo = input("Subtítulo: ").strip()
autor = input("Autor: ").strip()
data_publicacao = input("Data (ex: 22 de outubro de 2025): ").strip()
nome_arquivo = input("Nome do arquivo (sem espaços, ex: apartheid-financeiro): ").strip()
texto_base = input("Caminho do texto base (.txt): ").strip()

# ====== Verificação do texto base ======

if not os.path.exists(texto_base):
    print(f"❌ Arquivo {texto_base} não encontrado.")
    exit(1)

if not os.path.exists("textos"):
    os.makedirs("textos")

destino_texto = os.path.join("textos", os.path.basename(texto_base))
if not os.path.exists(destino_texto):
    shutil.copy2(texto_base, destino_texto)
    print(f"📄 Texto original copiado para {destino_texto}")

with open(texto_base, "r", encoding="utf-8") as f:
    conteudo_txt = f.read()

conteudo_html = formatar_paragrafos(conteudo_txt)

# ====== Caminho de destino ======

if tipo == "artigo":
    pasta_destino = "artigos"
elif tipo == "colaboracao":
    pasta_destino = "colaboracoes"
else:
    print("❌ Tipo inválido. Use 'artigo' ou 'colaboracao'.")
    exit(1)

os.makedirs(pasta_destino, exist_ok=True)
caminho_saida = os.path.join(pasta_destino, f"{nome_arquivo}.html")

# ====== Aside específico ======

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

# ====== Template HTML ======

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

# ====== Grava o HTML ======

with open(caminho_saida, "w", encoding="utf-8") as f:
    f.write(html_final)

print(f"✅ Arquivo gerado com sucesso: {caminho_saida}")

# ====== Atualiza o index.html ======
inserir_no_index(tipo, titulo, subtitulo, nome_arquivo, autor)
