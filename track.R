# Load libraries
library(tidyverse)

# Load data
data <- read.csv("facultydata.csv")

# Thinking about who earned tenure
people <- data %>%
  select(Last, First, College) %>%
  unique()

trackProf <- function(i){
  tmp <- merge(people[i,], data) %>%
    arrange(Year)
  finalDataYear <- data %>%
    filter(College == tmp$College[1]) %>%
    pull(Year) %>%
    max
  positions <- tmp %>%
    pull(Position)
  lowestRank <- head(positions,1)
  highestRank <- tail(positions,1)
  wasAssistant <- "assistant prof." %in% positions
  earnedTenure <- (wasAssistant == TRUE) & highestRank %in% c("associate prof.","professor")
  failedTenure <- (wasAssistant == TRUE) & highestRank == "assistant prof." & nrow(tmp) >= 6 & max(tmp$Year) != finalDataYear
  final <- data.frame(Last = tmp$Last[1], First = tmp$First[1], College = tmp$College[1], lowestRank = lowestRank, highestRank = highestRank, wasAssistant = wasAssistant, earnedTenure = earnedTenure, failedTenure = failedTenure)
  return(final)
}

trackedProfs <- lapply(1:100, trackProf) %>%
  bind_rows()