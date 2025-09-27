# Install and load required packages
packages <- c("quantmod", "dplyr", "zoo", "caret", "tidyverse", "pROC")
installed <- packages %in% rownames(installed.packages())
if (any(!installed)) install.packages(packages[!installed])

library(quantmod)
library(dplyr)
library(zoo)
library(caret)
library(tidyverse)
library(pROC)

# Step 1: Download company stock data
getSymbols("AAPL", src = "yahoo", from = "2020-01-01", to = "2024-12-31")

# Step 2: Convert to dataframe
stock_df <- data.frame(date = index(AAPL), coredata(AAPL))
colnames(stock_df) <- c("date","open","high","low","close","volume","adjusted")

# Step 3: Calculate daily return
stock_df <- stock_df %>%
  mutate(return = dailyReturn(Cl(AAPL)))

# Step 4: Add features: volatility and moving averages
stock_df <- stock_df %>%
  mutate(volatility = (high - low) / open,
         ma_short = zoo::rollmean(adjusted, k = 5, fill = NA, align = "right"),
         ma_long  = zoo::rollmean(adjusted, k = 20, fill = NA, align = "right"),
         ma_diff  = ma_short - ma_long)

# Step 5: Create lagged predictors (use yesterday’s info to predict today)
stock_df <- stock_df %>%
  mutate(return_lag1 = lag(return, 1),
         return_lag2 = lag(return, 2),
         volume_lag1 = lag(volume, 1),
         volatility_lag1 = lag(volatility, 1),
         ma_diff_lag1 = lag(ma_diff, 1))

# Step 6: Clean data (remove NA rows from lags and moving averages)
stock_df <- na.omit(stock_df)

# Step 7: Split into training and testing sets (70/30 split)
set.seed(123)
train_index <- createDataPartition(stock_df$return, p = 0.7, list = FALSE)
train <- stock_df[train_index, ]
test  <- stock_df[-train_index, ]

# Step 8: Train a linear regression model
model <- lm(return ~ return_lag1 + return_lag2 + volume_lag1 + volatility_lag1 + ma_diff_lag1, 
            data = train)
summary(model) # check coefficients

# Step 9: Predict on the test set
test$predicted_return <- predict(model, newdata = test)

# Step 10: Simple trading strategy
# If predicted return > 0, buy and hold for that day; else, stay in cash
test <- test %>%
  mutate(strategy_return = ifelse(predicted_return > 0, return, 0))

# Step 11: Compare cumulative returns
test <- test %>%
  mutate(cum_strategy = cumsum(strategy_return),
         cum_buyhold  = cumsum(return))

# Step 12: Plot results
plot(test$date, test$cum_buyhold, type = "l", ylim = c(min(test$cum_strategy), max(test$cum_strategy)*1.2), col = "blue", lwd = 2,
     main = "Cumulative Returns: Strategy vs Buy & Hold (Your Name)",
     xlab = "Date", ylab = "Cumulative Return")
lines(test$date, test$cum_strategy, col = "red", lwd = 2)
legend("topleft", legend = c("Buy & Hold", "Strategy"),
       col = c("blue", "red"), lty = 1, lwd = 2)







