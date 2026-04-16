# ============================================
# FARMTECH SOLUTIONS - ANALISE EM R
# ============================================

# Dados simulados de umidade do solo (%)
umidade <- c(35, 42, 38, 50, 47, 44)

# Dados simulados de pH do solo
ph <- c(6.2, 6.5, 6.1, 6.8, 6.4, 6.2)

# ============================================
# ANALISE DE UMIDADE
# ============================================
cat("=== Análise de Umidade ===\n")
cat("Média:", mean(umidade), "\n")
cat("Mediana:", median(umidade), "\n")
cat("Desvio Padrão:", sd(umidade), "\n\n")

# ============================================
# ANALISE DE pH
# ============================================
cat("=== Análise de pH ===\n")
cat("Média do pH:", mean(ph), "\n\n")

# ============================================
# CORRELAÇÃO ENTRE UMIDADE E pH
# ============================================
cat("=== Correlação Umidade x pH ===\n")
cat("Correlação:", cor(umidade, ph), "\n\n")

# ============================================
# DECISAO DE IRRIGACAO
# ============================================
cat("=== Decisão de Irrigação ===\n")
media_umidade <- mean(umidade)

if (media_umidade < 60) {
  cat("Solo seco -> LIGAR irrigação\n")
} else {
  cat("Solo úmido -> NÃO ligar irrigação\n")
}

# ============================================
# GRAFICOS
# ============================================
png("grafico_irrigacao.png", width = 1000, height = 500)

par(mfrow = c(1, 2))

barplot(
  umidade,
  main = "Umidade do Solo",
  xlab = "Leituras",
  ylab = "Umidade (%)",
  col = "lightblue"
)

barplot(
  ph,
  main = "pH do Solo",
  xlab = "Leituras",
  ylab = "pH",
  col = "lightgreen"
)

dev.off()