# O repositório central começa vazio
REGISTRO_DE_ACOES = {}

# O decorador que vai adicionar as funções ao dicionário automaticamente
def registrar_acao(nome_comando):
    def decorador(funcao_original):
        REGISTRO_DE_ACOES[nome_comando] = funcao_original
        return funcao_original
    return decorador

# Agora, basta colocar o decorador em cima de qualquer função!
@registrar_acao("enviar_email")
def acao_email(dados):
    return f"Enviando e-mail para {dados['destino']}"

@registrar_acao("gerar_pdf")
def acao_pdf(dados):
    return f"Gerando PDF do relatório {dados['id']}"

# Testando o resultado: o dicionário foi preenchido sozinho!
print(REGISTRO_DE_ACOES.keys()) 
# Output: dict_keys(['enviar_email', 'gerar_pdf'])

# Executando dinamicamente
comando = "gerar_pdf"
print(REGISTRO_DE_ACOES[comando]({"id": 404})) 
# Output: Gerando PDF do relatório 404