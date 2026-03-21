# 🧠 MicroPassos

![Demonstração do MicroPassos](demo.gif)

![Versão](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Status](https://img.shields.io/badge/status-concluído-brightgreen.svg)

## 🎯 O Problema (Dor Real)
Pessoas neurodivergentes (como pessoas com TDAH ou Autismo) e estudantes com dificuldades de rotina frequentemente sentem-se sobrecarregados ("paralisia de análise") ao enfrentar grandes tarefas. Aplicações de produtividade tradicionais são muitas vezes complexas e geram ansiedade. A dor real é a dificuldade em iniciar tarefas devido à falta de quebra de objetivos em etapas visíveis e digeríveis.

## 💡 A Solução Proposta
O **MicroPassos** é uma aplicação simples de interface em Linha de Comando (CLI) focada no "agora". Permite que o utilizador registe uma grande tarefa e a divida em micro-passos minúsculos. O sistema foca-se na conclusão individual de cada passo, calculando o progresso e proporcionando reforço positivo, diminuindo a carga mental.

## 👥 Público-Alvo
- Estudantes com TDAH ou dificuldade de concentração;
- Pessoas neurodivergentes que necessitam de rotinas estruturadas;
- Qualquer indivíduo que sofra de procrastinação por sobrecarga de tarefas.

## ⚙️ Funcionalidades Principais
- Adicionar tarefas divididas em micro-passos;
- Visualizar o progresso em percentagem (%);
- Concluir micro-passos individualmente;
- Armazenamento local leve via ficheiro JSON.

## 🛠️ Tecnologias Utilizadas
- **Python 3** (Linguagem base)
- **JSON** (Armazenamento de dados nativo)
- **Pytest** (Testes automatizados)
- **Flake8** (Linting / Análise estática)
- **GitHub Actions** (Integração Contínua - CI)

---

## 🚀 Como Instalar e Executar

1. **Clone o repositório:**
   ```bash
   git clone git@github.com:joycejdm/micropassos.git
   ```

2. **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    # No Windows:
    venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate
   ```

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
    ```bash
    python main.py
   ```

## 🧪 Como Correr os Testes e o Linter

Este projeto utiliza ferramentas de qualidade de código. Para as executar, garanta que o ambiente virtual está ativo.

1. **Para correr os testes automatizados (Pytest):**
   ```bash
   pytest tests/
   ```

2. **Para correr a análise estática (Flake8):**
    ```bash
    flake8 src/ main.py tests/
   ```

## 📦 Versionamento

Este projeto utiliza [Versionamento Semântico](https://semver.org/).

Versão atual: 1.1.0 