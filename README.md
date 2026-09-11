# Paz da Morte

Site acadêmico de uma funerária fictícia, voltado à apresentação de serviços e ao acolhimento de famílias. Mini-projeto 1 da Semana 6 de Programação para Internet.

## Tecnologias

- Python 3.9+ e Flask 3.1
- Jinja2: herança de templates, `for` e `if`
- Bootstrap 5.3.8: navbar, grid responsivo e cards
- HTML, CSS e Git/GitHub

Bootstrap está incluído em `static/vendor/`: o site não depende de CDN durante a apresentação.

## Como executar no Windows

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe app.py
```

Abra http://127.0.0.1:5000. Para encerrar, pressione Ctrl+C. Não é necessário ativar o ambiente virtual.

No Linux/macOS, use `python3 -m venv venv` e substitua `.\venv\Scripts\python.exe` por `venv/bin/python`.

## Páginas

| Rota | Conteúdo |
| --- | --- |
| / | Apresentação e serviços em destaque |
| /servicos | Catálogo dinâmico com seis serviços |
| /sobre | Propósito e valores |
| /contato | Informações de contato e identificação da demonstração |

Todas as páginas, incluindo o erro 404, herdam `templates/base.html`. O menu indica a página atual e se recolhe no celular.

## Dados e teste do item novo

A lista `servicos` fica em `app.py`. Cada dicionário contém `id`, `nome`, `categoria`, `descricao` e `destaque`.

O arquivo `templates/_cards.html` usa `for` para criar os cards e `if` para exibir o badge. O `else` do laço trata a lista vazia. A página inicial filtra os destaques.

Para demonstrar o item novo, acrescente um dicionário à lista, reinicie o servidor e atualize o catálogo: o novo card aparece sem alterar o HTML.

## Verificação

```powershell
.\venv\Scripts\python.exe -m unittest discover -s tests -v
```

Testes verificam rotas, navegação, item novo, destaques, lista vazia, erro 404 e arquivos estáticos. Para a conferência visual, abra as quatro páginas em 375px e 1280px no DevTools, teste o menu móvel e a navegação por teclado.

## Estrutura

- `app.py`: rotas e dados.
- `templates/`: base, páginas e cards.
- `static/css/style.css`: identidade visual.
- `static/vendor/`: Bootstrap CSS e JavaScript, com licença.
- `tests/test_app.py`: testes de comportamento.
- `docs/planejamento.md`: requisitos e planejamento.
- `docs/apresentacao.md`: roteiro de um minuto.

## Escopo e publicação

Empresa fictícia, sem telefone, endereço ou e-mail reais. Não há formulário, banco de dados ou coleta de mensagens. Dados reais de contato dependem de definição do responsável.

O servidor embutido é destinado ao desenvolvimento local. GitHub armazena o código; GitHub Pages não executa Flask. A hospedagem pública da aplicação exige um serviço compatível com Python.

Faça commits ao concluir etapas reais, com mensagens claras, e publique no repositório após revisar. Não inclua o ambiente virtual: ele já está no `.gitignore`. A aprovação do professor, a apresentação ao vivo e o histórico distribuído ao longo da aula são etapas do aluno.

## Referências

- [Flask: guia rápido](https://flask.palletsprojects.com/en/stable/quickstart/)
- [Bootstrap: documentação oficial](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
