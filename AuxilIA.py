# -*- coding: utf-8 -*-
"""
Sistema_Agentes_IA_Pequenos_Empreendedores_com_Gemini_VSCode.py

Para rodar este script no VS Code:
1. Certifique-se de ter Python instalado.
2. Instale a biblioteca do Google Generative AI:
   pip install google-generativeai
3. Insira sua GOOGLE_API_KEY na variável indicada abaixo.
"""

import google.generativeai as genai
import os
import time

# ==============================================================================
#  INSTRUÇÃO IMPORTANTE: INSIRA SUA API KEY DO GOOGLE GEMINI ABAIXO
# ==============================================================================
# SUBSTITUA "SUA_API_KEY_AQUI" PELA SUA CHAVE REAL.
# Exemplo: GOOGLE_API_KEY = "AIzaSyB... (sua chave completa)"
#
# Alternativa mais segura (RECOMENDADO para projetos maiores ou compartilhados):
# Configure uma variável de ambiente chamada GOOGLE_API_KEY com sua chave.
# O código abaixo tentará ler da variável de ambiente primeiro.
# Para configurar uma variável de ambiente (exemplo no Linux/macOS no terminal):
# export GOOGLE_API_KEY="SUA_API_KEY_AQUI"
# No Windows (PowerShell):
# $env:GOOGLE_API_KEY="SUA_API_KEY_AQUI"
# (Para persistência, adicione ao seu .bashrc, .zshrc, ou configurações de ambiente do Windows)
# ==============================================================================
GOOGLE_API_KEY_PLACEHOLDER = "AIzaSyBWP3v463FTvLE3aiFWlGAIanNmsKuTDik" # <<-- COLOQUE SUA CHAVE AQUI!

# Tenta carregar a API Key da variável de ambiente primeiro
api_key_to_use = os.environ.get("GOOGLE_API_KEY")

api_key_to_use = GOOGLE_API_KEY_PLACEHOLDER
print("API Key do Google Gemini configurada FORÇADAMENTE a partir da variável no código.")

#if not api_key_to_use:
 #   if GOOGLE_API_KEY_PLACEHOLDER == "SUA_API_KEY_AQUI" or not GOOGLE_API_KEY_PLACEHOLDER:
  #      print("ERRO: API Key do Google Gemini não configurada.")
   #     print("Por favor, insira sua API Key na variável 'GOOGLE_API_KEY_PLACEHOLDER' no código")
    #    print("OU configure a variável de ambiente 'GOOGLE_API_KEY'.")
      #  exit() # Encerra o script se a chave não for fornecida
    #api_key_to_use = GOOGLE_API_KEY_PLACEHOLDER
    #print("API Key do Google Gemini configurada a partir da variável no código.")
#else:
#    print("API Key do Google Gemini configurada a partir da variável de ambiente.")

try:
    genai.configure(api_key=api_key_to_use)
except Exception as e:
    print(f"Erro ao configurar a API Key do Google Gemini: {e}")
    print("Verifique se a API Key é válida.")
    exit()

# Configuração do modelo
MODEL_ID = "gemini-1.5-flash-latest"

# Configurações de geração para o modelo Gemini
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings=[
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

# Criar o modelo generativo
gemini_model = None # Inicializa como None
try:
    gemini_model = genai.GenerativeModel(
        model_name=MODEL_ID,
        safety_settings=safety_settings,
        generation_config=generation_config
    )
    print(f"Modelo Gemini '{MODEL_ID}' carregado com sucesso.")
except Exception as e:
    print(f"Erro ao carregar o modelo Gemini '{MODEL_ID}': {e}")
    print("Verifique se o nome do modelo está correto e se você tem acesso a ele e se a API Key é válida.")
    # Não vamos sair aqui, o sistema verificará se o modelo foi carregado antes de usar


class Agente:
    """Classe base para todos os agentes."""
    def __init__(self, nome, model):
        self.nome = nome
        self.model = model

    def _gerar_resposta_com_gemini(self, prompt):
        if not self.model:
            print(f"[{self.nome}] ERRO: Modelo Gemini não inicializado ou não pôde ser carregado.")
            return f"[{self.nome}] ERRO: Modelo Gemini não disponível."
        print(f"[{self.nome}] Enviando prompt para o Gemini...")
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"[{self.nome}] Erro ao chamar a API Gemini: {e}")
            if hasattr(e, 'response') and e.response:
                 print(f"Detalhes do erro da API: {e.response}")
            return f"[{self.nome}] Desculpe, não consegui processar sua solicitação no momento devido a um erro na API."

    def processar_consulta(self, consulta):
        print(f"\n[{self.nome}] Processando consulta: '{consulta}'")
        prompt = self._construir_prompt_especifico(consulta)
        return self._gerar_resposta_com_gemini(prompt)

    def _construir_prompt_especifico(self, consulta):
        raise NotImplementedError("Cada agente deve implementar a construção do seu prompt específico.")

class ConsultorFinanceiro(Agente):
    def __init__(self, model):
        super().__init__("Consultor Financeiro", model)

    def _construir_prompt_especifico(self, consulta):
        prompt = f"""
        Você é um Consultor Financeiro especialista em auxiliar pequenos empreendedores no Brasil.
        Seu objetivo é fornecer conselhos práticos e acionáveis.
        Analise a seguinte consulta de um empreendedor: "{consulta}"

        Com base na consulta, forneça informações sobre os seguintes tópicos, se relevantes:
        1.  **Oportunidades de Financiamento:** Identifique linhas de crédito (como BNDES, bancos comerciais para MEI/PMEs), fundos governamentais e outras oportunidades de financiamento relevantes para o contexto da consulta. Seja específico se possível.
        2.  **Planejamento e Projeções Financeiras:** Dê orientações sobre como realizar projeções financeiras básicas e análises de viabilidade. Mencione a importância de um plano de negócios.
        3.  **Regimes Tributários:** Sugira regimes tributários (Simples Nacional, Lucro Presumido, etc.) que podem ser vantajosos, explicando brevemente o porquê, considerando o tipo de negócio implícito na consulta.
        4.  **Gestão Financeira:** Ofereça dicas breves sobre gestão financeira básica para pequenos negócios.

        Seja claro, conciso e direto ao ponto. Evite jargões excessivos.
        Se a consulta for muito vaga, peça mais detalhes, mas tente fornecer alguma orientação geral.
        Foque em soluções aplicáveis à realidade de pequenos empreendedores no Brasil.
        """
        return prompt

class EspecialistaOperacoes(Agente):
    def __init__(self, model):
        super().__init__("Especialista em Operações e Regulamentações", model)

    def _construir_prompt_especifico(self, consulta):
        prompt = f"""
        Você é um Especialista em Operações e Regulamentações focado em pequenos empreendedores no Brasil.
        Seu objetivo é orientar sobre burocracia, conformidade regulatória e otimização de processos.
        Analise a seguinte consulta de um empreendedor: "{consulta}"

        Com base na consulta, forneça informações sobre os seguintes tópicos, se relevantes:
        1.  **Requisitos Legais e Burocracia:** Forneça um guia detalhado sobre os requisitos legais para a situação descrita (ex: obtenção de CNPJ, tipos de licenças necessárias como alvará de funcionamento, vigilância sanitária, corpo de bombeiros).
        2.  **Compliance:** Alerte sobre prazos importantes e documentos necessários para manter a conformidade legal do negócio.
        3.  **Otimização de Processos:** Proponha melhorias em processos operacionais que possam aumentar a eficiência do pequeno negócio (ex: gestão de estoque, atendimento, logística simplificada).
        4.  **Ferramentas (Conceitual):** Mencione tipos de ferramentas que podem ajudar (ex: sistemas ERP simplificados, planilhas de controle).

        Seja prático e forneça checklists ou passos claros sempre que possível.
        Adapte suas respostas ao contexto brasileiro.
        Se a consulta for muito vaga, peça mais detalhes, mas tente fornecer alguma orientação geral.
        """
        return prompt

class EspecialistaMarketing(Agente):
    def __init__(self, model):
        super().__init__("Especialista em Marketing e Vendas", model)

    def _construir_prompt_especifico(self, consulta):
        prompt = f"""
        Você é um Especialista em Marketing e Vendas com foco em ajudar pequenos empreendedores no Brasil a atrair clientes e aumentar a receita.
        Analise a seguinte consulta de um empreendedor: "{consulta}"

        Com base na consulta, desenvolva e sugira o seguinte, se relevante:
        1.  **Análise de Mercado e Consumidor:** Breves insights sobre tendências de mercado e comportamento do consumidor que podem ser relevantes para o negócio em questão.
        2.  **Estratégias de Marketing Digital:** Proponha campanhas de marketing personalizadas, com foco em mídias digitais (ex: Instagram, Facebook, Google Meu Negócio, WhatsApp Business). Sugira tipos de conteúdo e abordagens.
        3.  **Atração de Clientes:** Dê dicas práticas para atrair os primeiros clientes ou aumentar a base existente.
        4.  **Concorrência e Diferenciação:** Forneça insights sobre como analisar concorrentes e encontrar oportunidades de diferenciação.
        5.  **Ferramentas (Conceitual):** Mencione tipos de ferramentas úteis (ex: ferramentas de análise de redes sociais, CRM simples).

        Suas sugestões devem ser criativas, de baixo custo e alto impacto, adequadas para pequenos orçamentos.
        Seja específico e prático.
        Se a consulta for muito vaga, peça mais detalhes, mas tente fornecer alguma orientação geral.
        """
        return prompt

class RevisorIntegrador(Agente):
    def __init__(self, model):
        super().__init__("Revisor e Integrador", model)

    def _construir_prompt_especifico(self, consulta_original, analises_especialistas):
        analise_financeira = analises_especialistas.get("Consultor Financeiro", "Nenhuma análise financeira disponível.")
        analise_operacional = analises_especialistas.get("Especialista em Operações e Regulamentações", "Nenhuma análise operacional disponível.")
        analise_marketing = analises_especialistas.get("Especialista em Marketing e Vendas", "Nenhuma análise de marketing disponível.")

        prompt = f"""
        Você é um Revisor e Integrador Sênior de um sistema de IA para pequenos empreendedores no Brasil.
        Sua função é receber, revisar e integrar as informações dos agentes especializados para fornecer uma solução finalizada e coesa.

        A consulta original do empreendedor foi: "{consulta_original}"

        Você recebeu as seguintes análises dos agentes especializados:

        --- ANÁLISE DO CONSULTOR FINANCEIRO ---
        {analise_financeira}
        --- FIM DA ANÁLISE FINANCEIRA ---

        --- ANÁLISE DO ESPECIALISTA EM OPERAÇÕES E REGULAMENTAÇÕES ---
        {analise_operacional}
        --- FIM DA ANÁLISE OPERACIONAL ---

        --- ANÁLISE DO ESPECIALISTA EM MARKETING E VENDAS ---
        {analise_marketing}
        --- FIM DA ANÁLISE DE MARKETING ---

        Suas tarefas são:
        1.  **Sintetizar:** Combine as informações mais relevantes de cada análise em um texto fluido e coeso. Evite redundâncias.
        2.  **Avaliar Aplicabilidade:** Avalie criticamente se as soluções propostas são realmente aplicáveis e úteis ao contexto da consulta original do empreendedor. Se houver conflitos ou pontos que precisam de mais atenção, mencione-os.
        3.  **Gerar Plano de Ação Consolidado:** Crie um relatório ou plano de ação consolidado. Este plano deve ser claro, organizado (talvez com tópicos ou próximos passos) e fácil para o empreendedor entender e agir. Destaque as prioridades.
        4.  **Tom de Voz:** Mantenha um tom encorajador, prático e profissional.

        O resultado final deve ser um guia completo e integrado para o empreendedor.
        Se alguma análise especializada parecer fraca ou incompleta, tente complementar com seu conhecimento geral sobre empreendedorismo no Brasil, mas indique que é uma complementação.
        """
        return prompt

    def integrar_analises(self, consulta_original, analises_especialistas):
        print(f"\n[{self.nome}] Integrando análises para a consulta: '{consulta_original}'")
        prompt = self._construir_prompt_especifico(consulta_original, analises_especialistas)
        return self._gerar_resposta_com_gemini(prompt)


class SistemaAgentesIA:
    def __init__(self, model):
        if not model:
            print("ALERTA: Modelo Gemini não foi carregado. Os agentes não funcionarão corretamente.")
            # Considerar não instanciar os agentes se o modelo não estiver disponível
            # ou ter um modo de fallback (que não temos implementado aqui)
        self.consultor_financeiro = ConsultorFinanceiro(model)
        self.especialista_operacoes = EspecialistaOperacoes(model)
        self.especialista_marketing = EspecialistaMarketing(model)
        self.revisor_integrador = RevisorIntegrador(model)
        print("\nSistema de Agentes de IA para Pequenos Empreendedores INICIADO (com Gemini API).")
        print(f"Usando modelo: {MODEL_ID if model else 'NENHUM MODELO CARREGADO'}")
        print("Agentes disponíveis: Financeiro, Operações, Marketing, Revisor/Integrador.")

    def executar_consulta(self, consulta_empreendedor):
        if not self.consultor_financeiro.model: # Checa se o modelo está disponível em um dos agentes
            print("ERRO: Modelo Gemini não está disponível. Não é possível processar a consulta.")
            return "Não foi possível processar sua consulta pois o modelo de IA não está configurado corretamente."

        print(f"\n>>> Nova Consulta Recebida: '{consulta_empreendedor}'")
        print("-" * 70)

        analises = {}
        print("\n--- Fase de Análise Especializada ---")
        start_time = time.time()

        analises[self.consultor_financeiro.nome] = self.consultor_financeiro.processar_consulta(consulta_empreendedor)
        analises[self.especialista_operacoes.nome] = self.especialista_operacoes.processar_consulta(consulta_empreendedor)
        analises[self.especialista_marketing.nome] = self.especialista_marketing.processar_consulta(consulta_empreendedor)

        end_time_analise = time.time()
        print(f"--- Fim da Fase de Análise Especializada (Tempo: {end_time_analise - start_time:.2f}s) ---")

        print("-" * 70)
        print("\n--- Fase de Integração e Revisão ---")
        start_time_integracao = time.time()
        plano_final = self.revisor_integrador.integrar_analises(
            consulta_empreendedor,
            analises
        )
        end_time_integracao = time.time()
        print(f"--- Fim da Fase de Integração (Tempo: {end_time_integracao - start_time_integracao:.2f}s) ---")
        print("-" * 70)
        total_time = time.time() - start_time
        print(f"Tempo total de processamento da consulta: {total_time:.2f}s")

        return plano_final

# --- Fluxo de Operação e Exemplo de Uso ---
if __name__ == "__main__":
    if gemini_model: # Verifica se o modelo foi carregado com sucesso
        sistema = SistemaAgentesIA(gemini_model)

        print("\n" + "="*70)
        print("Sistema de Agentes de IA para Pequenos Empreendedores")
        print("Você pode testar o sistema com sua própria consulta agora.")
        print("Exemplos de consulta:")
        print("- Como posso financiar meu novo negócio de cafeteria e quais licenças preciso?")
        print("- Quero abrir uma loja de roupas online, mas não sei como conseguir financiamento nem atrair clientes.")
        print("- Preciso de ajuda com marketing digital para minha loja online de artesanato.")
        print("- Quais os primeiros passos para legalizar minha empresa de serviços de TI e como consigo clientes?")
        print("="*70)

        while True:
            consulta_usuario = input("\nDigite sua consulta para o sistema de IA (ou 'sair' para terminar): \n> ")
            if consulta_usuario.lower() == 'sair':
                print("Sistema encerrado. Boa sorte com seu empreendimento!")
                break
            if not consulta_usuario.strip():
                print("Por favor, digite uma consulta válida.")
                continue

            plano_de_acao_usuario = sistema.executar_consulta(consulta_usuario)
            print("\n✨ RESULTADO FINAL PARA O EMPREENDEDOR: ✨")
            print(plano_de_acao_usuario)
            print("="*70)
    else:
        print("ERRO CRÍTICO: O modelo Gemini não pôde ser carregado. O sistema não pode iniciar.")
        print("Verifique a configuração da API Key e o nome do modelo no início do script.")