# Automação com Ansible

Este diretório contém playbooks Ansible para automatizar o setup e o gerenciamento do ambiente de desenvolvimento deste projeto.

## Objetivo

O objetivo principal do Ansible aqui é orquestrar todo o ciclo de vida do desenvolvimento local com um **único comando**. Ele garante que qualquer desenvolvedor possa configurar pré-requisitos, construir a aplicação, implantá-la no cluster local e executar análises de código de forma automatizada, rápida e à prova de erros.

## Pré-requisitos

Antes de executar o playbook, você precisa ter o seguinte instalado na sua máquina:

1.  **Ansible:**
    ```bash
    # Exemplo de instalação em sistemas baseados em Debian/Ubuntu
    sudo apt update
    sudo apt install ansible -y
    ```

2.  **Coleções Ansible para Docker e Kubernetes:**
    ```bash
    ansible-galaxy collection install community.docker community.kubernetes
    ```

3.  **Ferramentas de Desenvolvimento:** `docker`, `docker-compose`, e `kind`.

4.  **Token de Acesso do SonarQube:**
    - Acesse o SonarQube em **http://localhost:9001** (usuário/senha: admin/admin).
    - Vá para **Meu Perfil (My Account) > Segurança (Security)**.
    - Gere um novo token (ex: `ansible-token`) e copie o valor.
    - Exporte o token como uma variável de ambiente no seu terminal. O playbook irá usá-la.
      ```bash
      export SONAR_TOKEN="seu_token_copiado_aqui"
      ```

## Como Usar

O playbook principal é o `setup.yml`. Ele é dividido em "tags" para que você possa executar o ciclo completo ou apenas partes dele.

### Executando o Ciclo Completo

Para executar todas as tarefas, desde a configuração do host até a análise do SonarQube, use o comando:

```bash
# Execute a partir do diretório raiz do projeto
ansible-playbook ansible/setup.yml
```

### Executando Partes do Ciclo

Você pode usar tags para executar apenas as tarefas que desejar:

-   **Apenas construir a imagem da API:**
    ```bash
    ansible-playbook ansible/setup.yml --tags build
    ```

-   **Apenas fazer o deploy no Kubernetes (pressupõe que a imagem já foi construída):**
    ```bash
    ansible-playbook ansible/setup.yml --tags deploy
    ```

-   **Apenas executar a análise do SonarQube:**
    ```bash
    ansible-playbook ansible/setup.yml --tags scan
    ```

-   **Construir e fazer o deploy, mas não escanear:**
    ```bash
    ansible-playbook ansible/setup.yml --tags build,deploy
    ```
