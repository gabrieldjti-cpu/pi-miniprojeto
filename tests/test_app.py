import unittest
from app import app, servicos


class SiteTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_paginas_e_navegacao(self):
        for rota in ["/", "/servicos", "/sobre", "/contato"]:
            with self.subTest(rota=rota):
                response = self.client.get(rota)
                self.assertEqual(response.status_code, 200)
                html = response.get_data(as_text=True)
                self.assertIn('lang="pt-BR"', html)
                self.assertIn('aria-current="page"', html)
                for destino in ["/servicos", "/sobre", "/contato"]:
                    self.assertIn('href="' + destino + '"', html)

    def test_item_novo_aparece_sem_alterar_template(self):
        novo = {"id": 7, "nome": "Homenagem de teste", "categoria": "Teste", "descricao": "Descrição de teste", "destaque": True}
        servicos.append(novo)
        try:
            self.assertIn(novo["nome"], self.client.get("/servicos").get_data(as_text=True))
            self.assertIn(novo["nome"], self.client.get("/").get_data(as_text=True))
        finally:
            servicos.remove(novo)

    def test_lista_vazia(self):
        originais = servicos[:]
        servicos.clear()
        try:
            self.assertIn("Nenhum serviço disponível", self.client.get("/servicos").get_data(as_text=True))
        finally:
            servicos.extend(originais)

    def test_destaques(self):
        html = self.client.get("/").get_data(as_text=True)
        for servico in servicos:
            if servico["destaque"]:
                self.assertIn(servico["nome"], html)
            else:
                self.assertNotIn(servico["nome"], html)

    def test_404(self):
        response = self.client.get("/nao-existe")
        self.assertEqual(response.status_code, 404)
        self.assertIn("Voltar ao início", response.get_data(as_text=True))

    def test_assets_locais(self):
        for caminho in ["css/style.css", "vendor/bootstrap.min.css", "vendor/bootstrap.bundle.min.js"]:
            with self.client.get("/static/" + caminho) as response:
                self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
