library(tidyverse)
subs <- c(seq(302,304), seq(328,339), 350, seq(352,355), seq(377,381))

expDir <- '/Users/maddie/Library/CloudStorage/Box-Box/LEAP/version3/'

for (s in subs){
  data <- read.csv(paste0(expDir, 'data/',s, '_leap3.csv')) %>% 
  mutate(procedure = if_else(!is.na(pracBlocks.thisN), 'LDTpractice', 
                           if_else(!is.na(LDT_block.thisN), 'experimental', NA))) %>% 
  mutate(block = if_else(procedure == 'LDTpractice', pracTrial.thisN+1, 
                         if_else(procedure == 'experimental', LDT_block.thisN+1, NA))) %>% 
  mutate(trial = if_else(procedure == 'LDTpractice', pracBlocks.thisN+1, 
                           if_else(procedure == 'experimental', LDT_trial.thisN+1, NA))) %>% 
  mutate(response = if_else(procedure == 'LDTpractice', LDTpracKey.keys, 
                              if_else(procedure == 'experimental', LDTResp.keys, NA))) %>%
  mutate(correct = if_else(procedure == 'LDTpractice', LDTpracKey.corr, 
                             if_else(procedure == 'experimental', LDTResp.corr, NA))) %>%
  mutate(reaction_time = if_else(procedure == 'LDTpractice', LDTpracKey.rt, 
                                   if_else(procedure == 'experimental',  LDTResp.rt, NA))) %>%
  mutate(PMdemand = if_else(block_desc == 'LoDemNoTar', 'ld',
                            if_else(block_desc == 'HiDemTar', 'hd',
                                    if_else(block_desc == 'HiDemNoTar', 'hd',
                                            if_else(block_desc == 'LoDemTar', 'ld', NA))))) %>% 
 rename(context = stim_location, correct_key = corr_key) 
        # pressedQ_blank = blankQResp.keys, pressedQ_fix = lateQResp.keys)
  
  if ('pressedQ' %in% colnames(data) == F){
    data$pressedQ <- c(rep(NA, nrow(data)))
  } 
  if ('pressedQ_blank' %in% colnames(data) == F){
    data$pressedQ_blank <- c(rep(NA, nrow(data)))
  } 
  if('pressedQ_late' %in% colnames(data) == F){
    data$pressedQ_late <- c(rep(NA, nrow(data)))
  }
  
  data <- data %>% rename(pressedQ_fix = pressedQ_late)
  
  data <- data %>%
    select(c('procedure','block','trial','PMdemand','context','stim', 'role',
             'word_type', 'correct_key','response', 'correct','reaction_time','pressedQ','pressedQ_blank','pressedQ_fix')) %>% 
    subset(!is.na(block)) %>% 
    subset(!is.na(trial))

  write.csv(data,
            file = paste0(expDir, 'data/cleaned_data/',s, '_leap3_cleaned.csv'),
            row.names = F)
}