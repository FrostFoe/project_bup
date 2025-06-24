# Read the data
data <- read.csv(file.choose())
head(data)
# Rename columns
colnames(data) <- c("Year", "Trade_GDP", "GINI")
View(data)
# Descriptive statistics
summary(data[, c("Trade_GDP", "GINI")])
sd(data$Trade_GDP)
sd(data$GINI)
# Histogram
hist(data$Trade_GDP, main="Histogram of Trade (% of GDP)", xlab="Trade (% of GDP)", col="skyblue")
hist(data$GINI, main="Histogram of GINI Index", xlab="GINI Index", col="salmon")
# Scatter plot
plot(data$Trade_GDP, data$GINI,
     main = "Trade Openness vs GINI Index",
     xlab = "Trade (% of GDP)",
     ylab = "GINI Index",
     pch = 19,
     col = "blue")
abline(lm(GINI ~ Trade_GDP, data = data), col="red")
# Regression
model <- lm(GINI ~ Trade_GDP, data = data)
summary(model)
# Interpret p-value
pval <- summary(model)$coefficients[2, 4]
if(pval < 0.05){
  print("Reject the null hypothesis: Trade openness significantly affects inequality.")
} else {
  print("Fail to reject the null hypothesis: No significant effect.")
}
