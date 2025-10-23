# 🌍 Geopolítica Global

**Geopolítica Global** é uma publicação independente dedicada à análise das forças políticas, econômicas e culturais que moldam o mundo contemporâneo.  
O projeto foi desenvolvido para combinar **autonomia editorial**, **padronização visual** e **publicação automatizada**, unindo reflexão crítica e tecnologia.

---

## 🧭 Estrutura Geral do Projeto

geopolitica-global/
│
├── artigos/ ← artigos autorais
│
├── colaboracoes/ ← contribuições externas
│ ├── ensaios/ ← colaborações longas (ensaios)
│ └── comentarios/ ← comentários e respostas a artigos
│
├── textos/ ← originais em formato .txt
│ ├── artigos/
│ └── colaboracoes/
│ ├── ensaios/
│ └── comentarios/
│
├── includes/ ← header.html e footer.html
├── css/ ← estilos visuais (main, artigo, responsivo)
├── js/ ← scripts de navegação e menu
├── imagens/ ← imagens de capa e ícones
├── index.html ← página inicial do site
├── gerar_artigo.py ← script automatizador de artigos
└── README.md ← este arquivo


---

## 🧱 Filosofia do Projeto

O site foi pensado para unir **conteúdo analítico** e **ferramentas de automação editorial**.  
Cada artigo nasce de um arquivo `.txt` puro, que é convertido automaticamente em HTML padronizado pelo script `gerar_artigo.py`.

A estrutura modular com **includes (`header.html` e `footer.html`)** garante consistência visual em todas as páginas e facilita a manutenção.

---

## ⚙️ Fluxo Editorial Completo

### 1️⃣ Escrever o texto base

Crie um arquivo `.txt` simples, sem tags HTML.  
Os parágrafos devem ser separados por uma linha em branco.  
As citações podem ser indicadas com o símbolo `>` no início da linha.

**Exemplo:**

1. O Custo da Mentira

A verdade tornou-se cara demais.

Enquanto se discute moralidade, a economia segue guiada pela conveniência.


Salve o texto em:



/textos/artigos/


ou, no caso de colaborações:



/textos/colaboracoes/ensaios/


ou ainda:



/textos/colaboracoes/comentarios/


---

### 2️⃣ Gerar o HTML automaticamente

Execute o script Python na raiz do projeto:

```bash
python gerar_artigo.py


Responda às perguntas:

Tipo (artigo/colaboracao): artigo
Título: A Hipocrisia como Sistema
Subtítulo: Reflexão sobre a dissimulação na vida pública brasileira
Autor: Santana
Data (ex: 26 de outubro de 2025): 26 de outubro de 2025
Nome do arquivo (sem espaços, ex: hipocrisia): hipocrisia
Caminho do texto base (.txt): textos/artigos/hipocrisia.txt


O script fará automaticamente:

✅ Criar o arquivo HTML completo
✅ Copiar o .txt original para /textos/
✅ Inserir o novo artigo no index.html
✅ Evitar duplicações
✅ Preservar o padrão visual (incluindo header e footer)

3️⃣ Estrutura do HTML gerado

O artigo final segue o mesmo modelo dos originais:

<!--#include virtual="includes/header.html" -->
<script src="/js/ativo.js"></script>

<main class="duas-colunas">
  <article class="col-esquerda">
    <section class="artigo">
      <h2>[TÍTULO]</h2>
      <h3>[SUBTÍTULO]</h3>
      <p class="meta">Publicado em [DATA]</p>
      <hr>
      [CONTEÚDO FORMATADO]
    </section>
  </article>
  [ASIDE AUTOMÁTICO]
</main>

<!--#include virtual="includes/footer.html" -->
<script src="/js/ativo.js"></script>
<script src="/js/menu.js"></script>

4️⃣ Teste local

Para testar o site localmente (sem Netlify), use:

python -m http.server


e acesse:

http://localhost:8000/


⚠️ Observação: os includes (<!--#include virtual=... -->) funcionam apenas em servidores reais (como Netlify ou Apache com SSI habilitado).
No ambiente local, o conteúdo principal aparecerá sem cabeçalho e rodapé.

✉️ Envio de Colaborações

Leitores e colaboradores podem enviar textos por e-mail seguindo o padrão abaixo:

Enviar um arquivo .txt com o texto completo.

No corpo do e-mail, incluir:

Tipo de texto: artigo, ensaio ou comentário

Título

Subtítulo (1 linha)

Autor (nome completo, profissão e cidade, se desejar)

Data de redação

Enviar para: seunome@proton.me

Os textos passam por revisão editorial e são publicados nas seções adequadas:

/colaboracoes/ensaios/

/colaboracoes/comentarios/

🧩 Organização das Colaborações
Tipo	Destino	Exemplo
Artigos autorais	/artigos/	apartheid-financeiro.html
Ensaios de leitores	/colaboracoes/ensaios/	renato-lima-desigualdade.html
Comentários	/colaboracoes/comentarios/	ana-paula-educacao.html
🧠 Filosofia Editorial

“O conhecimento coletivo nasce da pluralidade de vozes.”

O Geopolítica Global propõe um espaço de pensamento autônomo, livre de alinhamentos partidários e aberto à crítica construtiva.
O objetivo é restaurar a densidade do debate público, articulando economia, cultura e sociedade sob uma ótica civilizatória.

🧩 Licenciamento

Este projeto e seus textos estão sob licença de uso autoral.
A reprodução integral ou parcial é permitida mediante citação da fonte e sem uso comercial.

💻 Tecnologias Utilizadas

HTML5 / CSS3 / JavaScript — estrutura e interface

Python 3 — automação editorial

Server Side Includes (SSI) — modularização de cabeçalho e rodapé

Netlify — hospedagem e deploy contínuo

✨ Autor e Curadoria

Santana — ensaísta e analista político.
Escreve sobre economia, poder, cultura e os dilemas civilizatórios do século XXI.

📬 Contato

📧 seunome@proton.me

📰 Substack — Santana

🌐 Geopolítica Global (Netlify)


---

## ✅ O que esse README cobre

✔ Estrutura do projeto  
✔ Fluxo completo de publicação  
✔ Instruções de colaboração  
✔ Tecnologias usadas  
✔ Contexto editorial  
✔ Licença e contato  

---

Posso agora gerar uma **versão em HTML desse README** (no mesmo formato visual do site, com cabeçalho e rodapé), para que ele também possa ser acessado em `/readme.html` dentro do projeto — como uma “documentação interna” no próprio site?
