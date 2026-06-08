# --- Identificação ---
NOME_MISSAO = "Nova Horizonte Delta"
NOME_EQUIPE  = "Equipe Vega"

dados_missao = [
    [22, 95, 91, 98, 93], [26, 83, 75, 95, 87], [32, 61, 54, 90, 68],
    [37, 40, 35, 85, 52], [41, 25, 17, 76, 33], [35, 52, 30, 83, 48],
    [30, 68, 45, 88, 62], [27, 77, 60, 92, 74]
]

# Configuração dos sensores: [Nome, Unidade, Ação, (Limite_Atenção, Limite_Crítico, Direção_Inversa)]
# Direção_Inversa = True quando valores ABAIXO do limite são ruins (ex: bateria, oxigênio, comunicação, estabilidade)
CONFIG_SENSORES = {
    "Temperatura":  ["Temperatura interna", "°C", "verificar o controle térmico da missão", (30, 35, False), "Temperatura abaixo do ideal", "Temperatura estável", "Temperatura elevada", "Risco de superaquecimento"],
    "Comunicação":  ["Comunicação com a base", "%", "tentar restabelecer contato com a base", (60, 30, True), "Comunicação com a base em nível crítico", "Comunicação instável", "Comunicação estável"],
    "Bateria":      ["Sistema de energia", "%", "ativar modo de economia de energia", (50, 20, True), "Bateria em nível crítico", "Bateria abaixo do recomendado", "Energia estável"],
    "Oxigênio":     ["Suporte de oxigênio", "%", "acionar protocolo de suporte à vida", (90, 80, True), "Oxigênio em nível crítico", "Oxigênio abaixo do ideal", "Oxigênio adequado"],
    "Estabilidade": ["Estabilidade operacional", "%", "reduzir operações não essenciais", (70, 40, True), "Estabilidade operacional crítica", "Estabilidade operacional reduzida", "Estabilidade operacional adequada"]
}

CHAVES_SENSORES = list(CONFIG_SENSORES.keys())

def analisar_sensor(tipo, valor):
    cfg = CONFIG_SENSORES[tipo]
    lim_atencao, lim_critico, inversa = cfg[3]
    
    if inversa:
        if valor < lim_critico: return "CRÍTICO", 2, cfg[4]
        if valor < lim_atencao: return "ATENÇÃO", 1, cfg[5]
        return "NORMAL", 0, cfg[6]
    else:
        if valor < 18: return "ATENÇÃO", 1, cfg[4]
        if valor <= lim_atencao: return "NORMAL", 0, cfg[5]
        if valor <= lim_critico: return "ATENÇÃO", 1, cfg[6]
        return "CRÍTICO", 2, cfg[7]

def classificar_ciclo(pontuacao):
    if pontuacao <= 2: return "MISSÃO ESTÁVEL"
    return "MISSÃO EM ATENÇÃO" if pontuacao <= 5 else "MISSÃO CRÍTICA"

def gerar_recomendacao(resultados):
    criticos = [CHAVES_SENSORES[i] for i, (st, _, _) in enumerate(resultados) if st == "CRÍTICO"]
    atencoes = [CHAVES_SENSORES[i] for i, (st, _, _) in enumerate(resultados) if st == "ATENÇÃO"]

    if not criticos and not atencoes: return "Manter operação normal e continuar monitoramento."
    if len(criticos) >= 3: return "Ativar modo de segurança máxima e priorizar suporte à vida, energia e comunicação."

    partes = [CONFIG_SENSORES[s][2].capitalize() for s in criticos] + [f"monitorar {s.lower()} com atenção" for s in atencoes]
    return "; ".join(partes) + "."

def gerar_relatorio_final(riscos_ciclos, resultados_ciclos, classificacoes):
    n_ciclos = len(dados_missao)
    risco_medio = sum(riscos_ciclos) / n_ciclos
    pontos_por_area = [sum(res[i][1] for res in resultados_ciclos) for i in range(5)]
    area_mais_afetada_idx = pontos_por_area.index(max(pontos_por_area))
    classificacao_final = classificar_ciclo(round(risco_medio))

    print("\n" + "=" * 60 + "\nRELATÓRIO FINAL DA MISSÃO\n" + "=" * 60)
    print(f"Missão : {NOME_MISSAO}\nEquipe : {NOME_EQUIPE}\nQuantidade de ciclos analisados: {n_ciclos}\n")
    
    for i, s in enumerate(CHAVES_SENSORES):
        media = sum(dados_missao[r][i] for r in range(n_ciclos)) / n_ciclos
        print(f"Média de {s.lower():<13}: {media:.2f}{CONFIG_SENSORES[s][1]}")

    print(f"\nCiclo mais crítico      : Ciclo {riscos_ciclos.index(max(riscos_ciclos)) + 1}")
    print(f"Maior pontuação de risco: {max(riscos_ciclos)}\nRisco médio da missão   : {risco_medio:.2f}")
    print(f"Ciclos críticos         : {classificacoes.count('MISSÃO CRÍTICA')}\n")
    print(f"Tendência da missão:\n  A missão apresentou tendência de {'PIORA' if riscos_ciclos[-1] > riscos_ciclos[0] else 'MELHORA' if riscos_ciclos[-1] < riscos_ciclos[0] else 'ESTÁVEL em relação ao início'}.\n")
    
    print("Pontuação acumulada por área:")
    for i, s in enumerate(CHAVES_SENSORES):
        print(f"  {CONFIG_SENSORES[s][0]}: {pontos_por_area[i]} pontos")
        
    print(f"\nÁrea mais afetada:\n  {CONFIG_SENSORES[CHAVES_SENSORES[area_mais_afetada_idx]][0]}")
    print(f"\nClassificação final da missão:\n  {classificacao_final}\n\nConclusão:")
    
    conclusoes = {
        "MISSÃO ESTÁVEL": "A missão transcorreu dentro dos parâmetros esperados. Todos os sistemas operaram de forma satisfatória.",
        "MISSÃO EM ATENÇÃO": "A missão apresentou instabilidades relevantes durante a operação. A equipe deve manter monitoramento contínuo e o plano de contingência ativo.",
        "MISSÃO CRÍTICA": "A missão atingiu níveis críticos em múltiplos sistemas. É necessária intervenção imediata e revisão completa dos protocolos de segurança."
    }
    print(f"  {conclusoes[classificacao_final]}\n" + "=" * 60)

def main():
    print("=" * 60 + "\n                  MISSION CONTROL AI\n" + "=" * 60)
    print(f"Missão : {NOME_MISSAO}\nEquipe : {NOME_EQUIPE}\nQuantidade de ciclos analisados: {len(dados_missao)}\n" + "=" * 60)

    riscos_ciclos, resultados_ciclos, classificacoes = [], [], []

    for num_ciclo, ciclo in enumerate(dados_missao, start=1):
        print(f"\nCICLO {num_ciclo}\n" + "-" * 60)
        resultados = []
        
        for i, valor in enumerate(ciclo):
            tipo = CHAVES_SENSORES[i]
            status, pontos, desc = analisar_sensor(tipo, valor)
            resultados.append((status, pontos, desc))
            print(f"{tipo}: {valor}{CONFIG_SENSORES[tipo][1]} | {status} | {desc}")

        risco_ciclo = sum(r[1] for r in resultados)
        classif = classificar_ciclo(risco_ciclo)
        print(f"\nPontuação de risco do ciclo: {risco_ciclo}\nClassificação do ciclo     : {classif}\nRecomendação               : {gerar_recomendacao(resultados)}")

        riscos_ciclos.append(risco_ciclo)
        resultados_ciclos.append(resultados)
        classificacoes.append(classif)

    gerar_relatorio_final(riscos_ciclos, resultados_ciclos, classificacoes)

if __name__ == "__main__":
    main()