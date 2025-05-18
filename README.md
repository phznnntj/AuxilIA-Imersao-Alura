# 🤖 AuxilIA - Chat com Agentes para Empreendedores


O **AuxilIA** é um sistema de chat inovador que utiliza agentes de inteligência artificial (baseados no modelo Gemini do Google) para auxiliar pequenos empreendedores no Brasil. O objetivo principal é fornecer informações relevantes e práticas em diversas áreas cruciais para o sucesso de um negócio, como finanças, operações/regulamentações e marketing/vendas.

Este projeto visa democratizar o acesso a informações especializadas, permitindo que empreendedores obtenham insights valiosos e direcionamento estratégico de forma rápida e acessível, diretamente através de uma interface de chat intuitiva construída com Streamlit.

## ✨ Funcionalidades Principais

* **Agentes Especializados:**
    * **Consultor Financeiro:** Oferece orientações sobre financiamento, planejamento financeiro, regimes tributários e gestão financeira.
    * **Especialista em Operações e Regulamentações:** Informa sobre requisitos legais, burocracia, compliance e otimização de processos.
    * **Especialista em Marketing e Vendas:** Sugere estratégias de marketing digital, atração de clientes, análise da concorrência e diferenciação.
    * **Revisor e Integrador:** Sintetiza as análises dos agentes especializados em um plano de ação coeso e prático para o empreendedor.
* **Interface de Chat Interativa:** Construída com Streamlit, proporcionando uma experiência de conversação fluida e amigável.
* **Baseado no Modelo Gemini:** Utiliza o poder do modelo Gemini do Google para gerar respostas relevantes e contextuais.
* **Foco em Pequenos Empreendedores no Brasil:** As informações e conselhos são adaptados à realidade e ao contexto do mercado brasileiro.
* **Tema Dark:** Interface com tema escuro para uma experiência visual agradável e moderna.

## 🚀 Como Utilizar

1.  **Acesse o Aplicativo Online:** Você pode testar o AuxilIA através do link do Streamlit Cloud:
    [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://auxilia-seu-link-do-streamlit.app) 2.  **Interaja com os Agentes:** Na interface de chat, digite sua pergunta ou consulta relacionada ao seu negócio. O sistema encaminhará sua pergunta aos agentes especializados relevantes e apresentará uma resposta integrada.
3.  **Obtenha Insights:** Receba informações e sugestões práticas para te ajudar a tomar decisões informadas e impulsionar o seu empreendimento.

## ⚙️ Configuração para Desenvolvimento Local (Opcional)

Se você deseja executar o projeto localmente para desenvolvimento ou contribuição, siga estas etapas:

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio-auxilia.git](https://github.com/seu-usuario/seu-repositorio-auxilia.git)
    cd seu-repositorio-auxilia
    ```
2.  **Crie um Ambiente Virtual (Recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    venv\Scripts\activate  # No Windows
    ```
3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure a API Key do Google Gemini:**
    * **Opção 1 (Não recomendado para produção):** Edite diretamente a variável `GOOGLE_API_KEY_PLACEHOLDER` no arquivo `AuxilIA.py` com a sua chave da API do Google Gemini. **Tenha cuidado ao compartilhar este código publicamente com sua chave inserida diretamente.**
    * **Opção 2 (Recomendado):** Configure uma variável de ambiente chamada `GOOGLE_API_KEY` com a sua chave.
        * **No Linux/macOS (Terminal):**
            ```bash
            export GOOGLE_API_KEY="SUA_API_KEY_AQUI"
            ```
        * **No Windows (PowerShell):**
            ```powershell
            $env:GOOGLE_API_KEY="SUA_API_KEY_AQUI"
            ```
        * Para persistência, adicione esta linha ao seu arquivo de configuração do shell (e.g., `.bashrc`, `.zshrc`) ou às configurações de ambiente do Windows.
5.  **Execute o Aplicativo Streamlit:**
    ```bash
    streamlit run app_streamlit.py
    ```
6.  **Acesse no Navegador:** O aplicativo será aberto automaticamente no seu navegador (geralmente em `http://localhost:8501`).

![Vídeo do WhatsApp de 2025-05-17 à(s) 20 52 23_ffcdb472](https://github.com/user-attachments/assets/4977e786-14b6-49ff-9876-c365772a2c54)

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Google Generative AI (Gemini):** Modelo de linguagem grande para os agentes de IA.
* **Streamlit:** Framework Python para construir interfaces web interativas.
* **GitHub:** Plataforma para controle de versão e colaboração.

## 🤝 Contribuição

Contribuições são bem-vindas\! Se você tiver ideias para melhorar o sistema, adicionar novos agentes, otimizar o código ou corrigir bugs, siga estas etapas:

1.  Faça um fork do repositório.
2.  Crie uma branch para sua feature (`git checkout -b feature/sua-feature`).
3.  Faça o commit das suas mudanças (`git commit -am 'Add some feature'`).
4.  Faça o push para a branch (`git push origin feature/sua-feature`).
5.  Abra um Pull Request no GitHub.

## 📧 Contato

Raphael Henriques - raphael.sl.henriques@gmail.com