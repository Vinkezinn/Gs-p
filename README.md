
# 🚀 Mission Control AI

**GS2026.1 — Pensamento Computacional e Automação com Python**

Sistema inteligente de monitoramento de missão espacial desenvolvido em Python puro.

---

## 📋 Descrição

O **Mission Control AI** simula o acompanhamento de uma missão espacial experimental por meio de ciclos de monitoramento. A cada ciclo, cinco sensores são analisados automaticamente; o sistema gera alertas, calcula pontuações de risco, classifica a situação da missão e exibe um relatório final completo no terminal.

---

## 📁 Estrutura do repositório

```
mission-control-ai/
├── README.md
└── mission_control.py
```

---

## ▶️ Como executar

Nenhuma biblioteca externa é necessária. Basta ter o Python 3 instalado.

```bash
python mission_control.py
```

---

## 🛰️ Dados da missão

| Campo        | Valor                  |
|--------------|------------------------|
| Nome da missão | Nova Horizonte Delta |
| Nome da equipe | Equipe Vega          |
| Ciclos monitorados | 8                |

### Matriz `dados_missao`

Cada linha representa um ciclo: `[temperatura(°C), comunicacao(%), bateria(%), oxigenio(%), estabilidade(%)]`

| Ciclo | Temperatura | Comunicação | Bateria | Oxigênio | Estabilidade | Descrição |
|-------|-------------|-------------|---------|----------|--------------|-----------|
| 1 | 22 °C | 95% | 91% | 98% | 93% | Início da missão |
| 2 | 26 °C | 83% | 75% | 95% | 87% | Estabilização dos sistemas |
| 3 | 32 °C | 61% | 54% | 90% | 68% | Queda parcial de comunicação |
| 4 | 37 °C | 40% | 35% | 85% | 52% | Alerta de energia |
| 5 | 41 °C | 25% | 17% | 76% | 33% | Risco operacional |
| 6 | 35 °C | 52% | 30% | 83% | 48% | Tentativa de recuperação |
| 7 | 30 °C | 68% | 45% | 88% | 62% | Recuperação parcial |
| 8 | 27 °C | 77% | 60% | 92% | 74% | Estabilização progressiva |

---

## 📐 Regras de alerta

### Temperatura (°C)
| Condição | Classificação |
|----------|--------------|
| < 18 °C | ATENÇÃO |
| 18 – 30 °C | NORMAL |
| 31 – 35 °C | ATENÇÃO |
| > 35 °C | CRÍTICO |

### Comunicação (%)
| Condição | Classificação |
|----------|--------------|
| < 30% | CRÍTICO |
| 30 – 59% | ATENÇÃO |
| ≥ 60% | NORMAL |

### Bateria (%)
| Condição | Classificação |
|----------|--------------|
| < 20% | CRÍTICO |
| 20 – 49% | ATENÇÃO |
| ≥ 50% | NORMAL |

### Oxigênio (%)
| Condição | Classificação |
|----------|--------------|
| < 80% | CRÍTICO |
| 80 – 89% | ATENÇÃO |
| ≥ 90% | NORMAL |

### Estabilidade (%)
| Condição | Classificação |
|----------|--------------|
| < 40% | CRÍTICO |
| 40 – 69% | ATENÇÃO |
| ≥ 70% | NORMAL |

---

## 🔢 Pontuação de risco

| Classificação | Pontos |
|---------------|--------|
| NORMAL | 0 |
| ATENÇÃO | 1 |
| CRÍTICO | 2 |

Pontuação máxima por ciclo: **10 pontos** (5 sensores × 2 pontos).

---

## 🏷️ Classificação do ciclo

| Pontuação total | Classificação |
|-----------------|--------------|
| 0 – 2 | MISSÃO ESTÁVEL |
| 3 – 5 | MISSÃO EM ATENÇÃO |
| 6 – 10 | MISSÃO CRÍTICA |

---

## ⚙️ Funções implementadas

| Função | Descrição |
|--------|-----------|
| `analisar_temperatura()` | Classifica a temperatura do módulo |
| `analisar_comunicacao()` | Classifica o sinal de comunicação |
| `analisar_bateria()` | Classifica o nível de bateria |
| `analisar_oxigenio()` | Classifica o nível de oxigênio |
| `analisar_estabilidade()` | Classifica a estabilidade operacional |
| `classificar_ciclo()` | Determina a classificação geral do ciclo |
| `gerar_recomendacao()` | Gera recomendações automáticas com base nos alertas |
| `analisar_tendencia()` | Compara o primeiro e último ciclo para indicar tendência |
| `identificar_area_mais_afetada()` | Soma pontos por área e identifica a mais crítica |
| `gerar_relatorio_final()` | Exibe o relatório consolidado no terminal |

---

