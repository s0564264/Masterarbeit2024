library(ggplot2)
library(readxl)
library(dplyr)
library(RColorBrewer)
library(writexl)

# Daten aus der Excel-Datei laden
file_path <- "AUSGANGSDATEI.xlsx"
df <- read_excel(file_path, sheet = "common_voice")

# Daten für die drei ASR-Systeme filtern
df_filtered <- df %>%
  filter(`ASR-System` %in% c('Amazon', 'Google', 'Microsoft')) %>%
  filter(is.finite(Distance) & !is.na(Distance))  # Entfernt NA und unendliche Werte

# ---- WER Boxplots ----
# Boxplot für WER nach Akzent und ASR-System plotten
ggplot(df_filtered, aes(x = Akzent, y = WER, fill = `ASR-System`)) +
  geom_boxplot() +
  scale_fill_brewer(palette = "Set3", direction = -1) +
  labs(title = "Verteilung von WER nach Akzent und ASR-System",
       x = "Akzent", y = "WER", fill = "ASR-System") +
  ylim(0, 1) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),
        plot.title = element_text(hjust = 0.5))

# Boxplot für WER nach Alter und ASR-System plotten
ggplot(df_filtered, aes(x = as.factor(Alter), y = WER, fill = `ASR-System`)) +
  geom_boxplot() +
  scale_fill_brewer(palette = "Set3", direction = -1) +
  labs(title = "Verteilung von WER nach Alter und ASR-System",
       x = "Alter", y = "WER", fill = "ASR-System") +
  ylim(0, 1) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),
        plot.title = element_text(hjust = 0.5))

# Boxplot für WER nach Geschlecht und ASR-System plotten
ggplot(df_filtered, aes(x = Geschlecht, y = WER, fill = `ASR-System`)) +
  geom_boxplot() +
  scale_fill_brewer(palette = "Set3", direction = -1) +
  labs(title = "Verteilung von WER nach Geschlecht und ASR-System",
       x = "Geschlecht", y = "WER", fill = "ASR-System") +
  ylim(0, 1) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),
        plot.title = element_text(hjust = 0.5))

# ---- Semantic Distance Boxplots ----
# Boxplot für Semantic Distance nach Akzent und ASR-System plotten
ggplot(df_filtered, aes(x = Akzent, y = Distance, fill = `ASR-System`)) +
  geom_boxplot() +
  scale_fill_brewer(palette = "Set3", direction = -1) +
  labs(title = "Verteilung von Semantic Distance nach Akzent und ASR-System",
       x = "Akzent", y = "Semantic Distance", fill = "ASR-System") +
  ylim(0, 1) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),
        plot.title = element_text(hjust = 0.5))

# Boxplot für Semantic Distance nach Alter und ASR-System plotten
ggplot(df_filtered, aes(x = as.factor(Alter), y = Distance, fill = `ASR-System`)) +
  geom_boxplot() +
  scale_fill_brewer(palette = "Set3", direction = -1) +
  labs(title = "Verteilung von Semantic Distance nach Alter und ASR-System",
       x = "Alter", y = "Semantic Distance", fill = "ASR-System") +
  ylim(0, 1) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),
        plot.title = element_text(hjust = 0.5))

# Boxplot für Semantic Distance nach Geschlecht und ASR-System plotten
ggplot(df_filtered, aes(x = Geschlecht, y = Distance, fill = `ASR-System`)) +
  geom_boxplot() +
  scale_fill_brewer(palette = "Set3", direction = -1) +
  labs(title = "Verteilung von Semantic Distance nach Geschlecht und ASR-System",
       x = "Geschlecht", y = "Semantic Distance", fill = "ASR-System") +
  ylim(0, 1) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),
        plot.title = element_text(hjust = 0.5))

# ---- Werte berechnen und im Excel-Format speichern ----
# WER nach Akzent und ASR-System
wer_akzent_asr <- df_filtered %>%
  group_by(Akzent, `ASR-System`) %>%
  summarize(
    Q1 = quantile(WER, 0.25, na.rm = TRUE),
    Median = median(WER, na.rm = TRUE),
    Q3 = quantile(WER, 0.75, na.rm = TRUE),
    Max = max(WER, na.rm = TRUE)
  )

# Semantic Distance nach Akzent und ASR-System
dist_akzent_asr <- df_filtered %>%
  group_by(Akzent, `ASR-System`) %>%
  summarize(
    Q1 = quantile(Distance, 0.25, na.rm = TRUE),
    Median = median(Distance, na.rm = TRUE),
    Q3 = quantile(Distance, 0.75, na.rm = TRUE),
    Max = max(Distance, na.rm = TRUE)
  )

# WER nach Alter und ASR-System
wer_alter_asr <- df_filtered %>%
  group_by(Alter, `ASR-System`) %>%
  summarize(
    Q1 = quantile(WER, 0.25, na.rm = TRUE),
    Median = median(WER, na.rm = TRUE),
    Q3 = quantile(WER, 0.75, na.rm = TRUE),
    Max = max(WER, na.rm = TRUE)
  )

# Semantic Distance nach Alter und ASR-System
dist_alter_asr <- df_filtered %>%
  group_by(Alter, `ASR-System`) %>%
  summarize(
    Q1 = quantile(Distance, 0.25, na.rm = TRUE),
    Median = median(Distance, na.rm = TRUE),
    Q3 = quantile(Distance, 0.75, na.rm = TRUE),
    Max = max(Distance, na.rm = TRUE)
  )

# WER nach Geschlecht und ASR-System
wer_geschlecht_asr <- df_filtered %>%
  group_by(Geschlecht, `ASR-System`) %>%
  summarize(
    Q1 = quantile(WER, 0.25, na.rm = TRUE),
    Median = median(WER, na.rm = TRUE),
    Q3 = quantile(WER, 0.75, na.rm = TRUE),
    Max = max(WER, na.rm = TRUE)
  )

# Semantic Distance nach Geschlecht und ASR-System
dist_geschlecht_asr <- df_filtered %>%
  group_by(Geschlecht, `ASR-System`) %>%
  summarize(
    Q1 = quantile(Distance, 0.25, na.rm = TRUE),
    Median = median(Distance, na.rm = TRUE),
    Q3 = quantile(Distance, 0.75, na.rm = TRUE),
    Max = max(Distance, na.rm = TRUE)
  )

# Ergebnisse in Excel-Dateien speichern
output_file_path_wer_akzent <- "AUSGABEDATEI_WER_AKZENT.xlsx"
write_xlsx(wer_akzent_asr, output_file_path_wer_akzent)

output_file_path_dist_akzent <- "AUSGABEDATEI_SEMANTICDISTANCE_AKZENT.xlsx"
write_xlsx(dist_akzent_asr, output_file_path_dist_akzent)

output_file_path_wer_alter <- "AUSGABEDATEI_WER_ALTER.xlsx"
write_xlsx(wer_alter_asr, output_file_path_wer_alter)

output_file_path_dist_alter <- "AUSGABEDATEI_SEMANTICDISTANCE_ALTER.xlsx"
write_xlsx(dist_alter_asr, output_file_path_dist_alter)

output_file_path_wer_geschlecht <- "AUSGABEDATEI_WER_GESCHLECHT.xlsx"
write_xlsx(wer_geschlecht_asr, output_file_path_wer_geschlecht)

output_file_path_dist_geschlecht <- "AUSGABEDATEI_SEMANTICDISTANCE_GESCHLECHT.xlsx"
write_xlsx(dist_geschlecht_asr, output_file_path_dist_geschlecht)

print("Boxplots erstellt und WER- sowie Semantic Distance-Werte wurden erfolgreich in Excel-Dateien gespeichert.")
