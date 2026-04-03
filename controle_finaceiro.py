from categoria import Categoria
from despesa import Despesa
from fpdf import FPDF
from datetime import datetime
import json
import os

class ControleFinanceiro:
    def __init__(self, arquivo_dado="daods_financeiros.json"):
        self.arquivo_dado = arquivo_dado
        self.categorias = {}
        self.carregar_dado()

    def registrar_despesa(self, valor, nome_cat, data, desc):
        if nome_cat not in self.categorias:
            self.categorias[nome_cat] = Categoria(nome_cat)
        
        nova_despesa = Despesa(valor, nome_cat, data, desc)
        self.categorias[nome_cat].adicionar_despesa(nova_despesa)
        self.salvar_dados()

    def salvar_dados(self):
        dados_para_salvar = {}
        for nome, cat in self.categorias.items():
            dados_para_salvar[nome] = {
                "limite": cat.limite,
                "despesas": [d.to_dict() for d in cat.despesas]
            }
        with open(self.arquivo_dado, 'w', encoding='utf-8') as f:
            json.dump(dados_para_salvar, f, indent=4, ensure_ascii=False)

    def carregar_dado(self):
        if os.path.exists(self.arquivo_dado):
            with open(self.arquivo_dado, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                for nome_cat, info in dados.items():
                    cat = Categoria(nome_cat, info['limite'])
                    for d in info['despesas']:
                        cat.despesas.append(Despesa(d['valor'], d['categoria'], d['data'], d['descricao']))
                    self.categorias[nome_cat] = cat

    def gerar_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, txt="Relatorio Financeiro Residencial", ln=True, align='C')
        
        total_geral = 0
        for nome, cat in self.categorias.items():
            pdf.set_font("Arial", "B", 12)
            pdf.ln(5)
            pdf.cell(0, 10, txt=f"Categoria: {nome} | Gasto: R${cat.total_gasto():.2f}", ln=True)
            pdf.set_font("Arial", size=10)
            for d in cat.despesas:
                pdf.cell(0, 7, txt=f" {d.data} - R${d.valor:.2f} ({d.descricao})", ln=True)
            total_geral += cat.total_gasto()
        
        pdf.ln(10)
        pdf.cell(0, 10, txt=f"TOTAL GERAL: R${total_geral:.2f}", ln=True)
        nome_pdf = f"Relatorio_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
        pdf.output(nome_pdf)
        return nome_pdf