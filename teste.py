import sqlite3
import tkinter as tk


# --- BANCO DE DADOS (SQLite) ---
def inicializar_banco():
    # Conecta ao arquivo rpg.db (cria se não existir)
    conexao = sqlite3.connect("rpg.db")
    cursor = conexao.cursor()

    # Cria a tabela de histórico de batalhas caso ela ainda não exista
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vencedor TEXT,
            perdedor TEXT,
            vida_restante INTEGER
        )
    """
    )

    conexao.commit()
    conexao.close()


def salvar_resultado(vencedor, perdedor, vida_restante):
    conexao = sqlite3.connect("rpg.db")
    cursor = conexao.cursor()

    # Insere uma nova linha na tabela historico
    cursor.execute(
        """
        INSERT INTO historico (vencedor, perdedor, vida_restante)
        VALUES (?, ?, ?)
    """,
        (vencedor, perdedor, vida_restante),
    )

    conexao.commit()
    conexao.close()
    print(f"Batalha salva no banco de dados! Vencedor: {vencedor}")


# Inicializa o banco ao abrir o programa
inicializar_banco()


# 1. Sua classe original intacta
class Personagem:

  def __init__(self, nome: str, ataque: int, defesa: int, vida: int):
    self.nome = nome
    self.ataque = ataque
    self.defesa = defesa
    self.vida = vida

  def sobreviveu(self, dano):
    dano_real = dano - self.defesa
    if dano_real < 0:
      dano_real = 0
    self.vida = self.vida - dano_real
    if self.vida > 0:
      return True
    else:
      self.vida = 0
      return False

  def atacar(self, alvo):
    print(f"{self.nome} atacou {alvo.nome}!")
    alvo.sobreviveu(self.ataque)


# 2. Objetos do jogo
heroi = Personagem("Guerreiro", 20, 5, 100)
monstro = Personagem("Goblin", 10, 2, 50)


# 3. Função de Ação do Botão
def acao_atacar():
  if heroi.vida > 0 and monstro.vida > 0:
    heroi.atacar(monstro)

    if monstro.vida > 0:
      monstro.atacar(heroi)

    label_vida_heroi.config(text=f"Vida: {heroi.vida} HP")
    label_vida_monstro.config(text=f"Vida: {monstro.vida} HP")

    # Quando a luta termina:
    if heroi.vida <= 0 or monstro.vida <= 0:
      botao_atacar.config(state=tk.DISABLED)

      if heroi.vida <= 0:
        label_status.config(text="Derrota! O Herói caiu...", fg="red")
        # Salva o monstro como vencedor
        salvar_resultado(
            vencedor=monstro.nome, perdedor=heroi.nome, vida_restante=monstro.vida
        )
      else:
        label_status.config(text="Vitória! O Monstro foi derrotado!", fg="green")
        # Salva o herói como vencedor
        salvar_resultado(
            vencedor=heroi.nome, perdedor=monstro.nome, vida_restante=heroi.vida
        )


# 4. Interface Gráfica
janela = tk.Tk()
janela.title("Mini RPG - Duelo com Banco de Dados")
janela.geometry("450x380")

titulo = tk.Label(janela, text="⚔️ ARENA DE COMBATE ⚔️", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

frame_combate = tk.Frame(janela)
frame_combate.pack(pady=10)

# PAINEL DO HERÓI
frame_heroi = tk.LabelFrame(
    frame_combate, text=" Herói ", font=("Arial", 11, "bold"), padx=15, pady=10
)
frame_heroi.pack(side=tk.LEFT, padx=15)

label_nome_heroi = tk.Label(
    frame_heroi, text=heroi.nome, font=("Arial", 12, "bold"), fg="blue"
)
label_nome_heroi.pack()

label_vida_heroi = tk.Label(
    frame_heroi, text=f"Vida: {heroi.vida} HP", font=("Arial", 10)
)
label_vida_heroi.pack()

label_stats_heroi = tk.Label(
    frame_heroi,
    text=f"Ataque: {heroi.ataque} | Defesa: {heroi.defesa}",
    font=("Arial", 8),
    fg="gray",
)
label_stats_heroi.pack(pady=5)

# PAINEL DO MONSTRO
frame_monstro = tk.LabelFrame(
    frame_combate, text=" Monstro ", font=("Arial", 11, "bold"), padx=15, pady=10
)
frame_monstro.pack(side=tk.RIGHT, padx=15)

label_nome_monstro = tk.Label(
    frame_monstro, text=monstro.nome, font=("Arial", 12, "bold"), fg="red"
)
label_nome_monstro.pack()

label_vida_monstro = tk.Label(
    frame_monstro, text=f"Vida: {monstro.vida} HP", font=("Arial", 10)
)
label_vida_monstro.pack()

label_stats_monstro = tk.Label(
    frame_monstro,
    text=f"Ataque: {monstro.ataque} | Defesa: {monstro.defesa}",
    font=("Arial", 8),
    fg="gray",
)
label_stats_monstro.pack(pady=5)

# BOTÃO E STATUS
botao_atacar = tk.Button(
    janela,
    text="⚔️ Atacar Turno",
    font=("Arial", 11, "bold"),
    bg="orange",
    fg="black",
    command=acao_atacar,
)
botao_atacar.pack(pady=15)

label_status = tk.Label(
    janela, text="Clique no botão para iniciar a batalha!", font=("Arial", 10)
)
label_status.pack(pady=5)

janela.mainloop()