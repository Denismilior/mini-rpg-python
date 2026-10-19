⚔️ Mini RPG - Python Desktop (POO + Tkinter + SQLite)

Este é um miniprojeto de um jogo de RPG de turno desenvolvido em Python puro, focado na consolidação dos conceitos essenciais de Programação Orientada a Objetos (POO), Interfaces Gráficas (GUI com Tkinter) e Persistência de Dados (SQLite).

🚀 Tecnologias Utilizadas

Python 3: Linguagem base do projeto.

POO (Programação Orientada a Objetos): Estruturação dos combatentes através de classes, métodos e atributos encapsulados.

Tkinter: Biblioteca padrão do Python para criação da interface gráfica desktop interativa.

SQLite3: Banco de dados relacional leve e local para persistência e registro do histórico de batalhas.

🎯 Funcionalidades

Mecânica de Combate:

Sistema de cálculo de dano considerando o ataque do atacante e a defesa do defensor.

Alternância de turnos entre o Herói e o Monstro.

Interface Gráfica Interativa:

Painéis visuais separados (LabelFrame) para Herói e Monstro dispostos lado a lado na arena.

Atualização dos pontos de vida (HP) em tempo real a cada clique do jogador no botão de ataque.

Bloqueio automático da ação e exibição de mensagem de vitória/derrota ao término do combate.

Armazenamento de Dados:

Criação automática do banco de dados local (rpg.db) e tabela de histórico.

Registro de vitórias, derrotas e vida restante do vencedor ao final da luta.

🛠️ Como Executar o Projeto

Pré-requisitos:

Ter o Python 3 instalado na sua máquina.

Clonar o Repositório:

git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git


Navegar até a pasta do projeto:

cd SEU_REPOSITORIO


Executar o script principal:

python teste.py


(Substitua teste.py pelo nome do seu arquivo .py se for diferente)

🎓 Aprendizados

Este projeto foi construído passo a passo com o objetivo de fixar a base essencial do desenvolvimento em Python. Ele demonstra na prática como conectar a lógica de negócio interna (POO) a elementos visuais de tela (Tkinter) e persistir o estado do sistema em um banco de dados relacional (SQLite).