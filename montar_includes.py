import os

# Caminhos dos includes
header_path = "includes/header.html"
footer_path = "includes/footer.html"

# Lê o conteúdo do cabeçalho e rodapé
with open(header_path, "r", encoding="utf-8") as f:
    header = f.read()

with open(footer_path, "r", encoding="utf-8") as f:
    footer = f.read()

# Função para inserir header e footer
def montar_html(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Remove cabeçalho e rodapé antigos se existirem
    if "<!-- HEADER-START -->" in conteudo and "<!-- FOOTER-END -->" in conteudo:
        conteudo = conteudo.split("<!-- HEADER-START -->")[1]
        conteudo = conteudo.split("<!-- FOOTER-END -->")[0]

    # Monta o novo HTML
    novo_conteudo = f"{header}\n<!-- HEADER-START -->\n{conteudo}\n<!-- FOOTER-END -->\n{footer}"

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(novo_conteudo)

    print(f"✔️ Atualizado: {caminho_arquivo}")

# Percorre o projeto e atualiza todos os .html
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html") and "includes" not in root:
            caminho = os.path.join(root, file)
            montar_html(caminho)
