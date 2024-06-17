# Boas vindas ao exercício de Raspagem de Dados com Python 🚀

<details>
  <summary><strong>👨‍💻 O que deverá ser desenvolvido</strong></summary><br />
  
  Nesse exercício você implementará uma função em Python para resolver um teste técnico similar ao que já foi aplicado pelo Facebook e outras big techs! Tente desenvolver uma solução otimizada e escolha bem qual estrutura de dados será utilizada em termos de complexidade de tempo e espaço! Essa escolha tende a ser um diferencial em um processo seletivo desse tipo.

</details>

<details>
  <summary><strong>🚵 Habilidades a serem trabalhadas:</strong></summary><br />
  
  <ul>
    <li>Raspagem de Dados.</li>
    <li>Requisições na Web com Python.</li>
  </ul>

</details>

# Orientações
<details>
  <summary><strong>⚠ Antes de começar a desenvolver</strong></summary><br />

  1. Crie o ambiente virtual para o exercício

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

# Exercício

## Baseando-se em uma página contendo detalhes sobre um livro (http://books.toscrape.com/catalogue/the-grand-design_405/index.html), faça a extração dos campos título, preço, descrição e url contendo a imagem de capa do livro dentro da função `scrape` que recebe uma URL como parâmetro

> ⚠️ O preço deve vir somente valores numéricos e ponto. Ex: `Â£13.76` -> `13.76`. ⚠️ A descrição de ter o sufixo “more…” removido quando existir. ⚠️ Os campos extraídos devem ser apresentados separados por vírgula. Ex: `título,preço,descrição,capa`.

Exemplo:

```bash
The Grand Design,13.76,THE FIRST MAJOR WORK IN NEARLY A DECADE...,http://books.toscrape.com/catalogue/../../media/cache/9b/69/9b696c2064d6ee387774b6121bb4be91.jpg
```

> **Implemente em:** `src/scrape.py`
> De olho na dica 👀: no retorno do caminho da imagem lembre-se de apresentar também a constante URL_BASE que aponta para a página inicial do site.
