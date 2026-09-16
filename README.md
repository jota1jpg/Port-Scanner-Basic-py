# Python Port Scanner Básico

Scanner de portas TCP desenvolvido em Python para estudo de redes de computadores e conceitos fundamentais de cibersegurança.

---

## Objetivo

Este projeto foi construído com fins exclusivamente educacionais para compreender o funcionamento de conexões de rede via Sockets, a pilha de protocolos TCP/IP e os mecanismos básicos de varredura (*scanning*) utilizados em etapas de reconhecimento de infraestrutura.

---

## Funcionalidades

* **Tratamento de entrada:** Sanitização automatizada para aceitar URLs, endereços com protocolo (HTTP/HTTPS) ou endereços IP diretos.
* **Varredura parametrizada:** Teste de portas de rede através da definição de intervalos (`range()`).
* **Controle de timeout:** Configuração de tempo limite por tentativa para otimizar o tempo total de resposta da execução.
* **Retorno estruturado:** Exibição clara no terminal sobre o status de cada porta analisada (ABERTA ou FECHADA).

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Biblioteca:** `socket` (módulo nativo da linguagem)

---

## Como Executar

### Pré-requisitos
* Python 3.x instalado no sistema.

### Instruções

1. Clone o repositório:
   ```bash
   git clone [https://github.com/jota1jpg/Port-Scanner-Basic-py.git](https://github.com/jota1jpg/Port-Scanner-Basic-py.git)
