library(tidyverse)
subs <- c(seq(302,304), seq(328,339), 350, seq(352,355), seq(377,381))
df <- as.data.frame(matrix(nrow = 0, ncol = 133))

for (s in subs){
  # read in data for this participant and get columns of interest
  data <- read.csv(paste0('/Users/maddie/Library/CloudStorage/Box-Box/LEAP/version3/data/',s,'_leap3.csv')) %>%
    mutate(procedure = if_else(!is.na(LDT_block.thisN), 'LDT',
                               if_else(!is.na(pracBlocks.thisN), 'LDTpractice',''))) %>%
    mutate(context = if_else((block_desc == 'HiDemTar'| block_desc == 'HiDemNoTar'),'hd',
                             if_else((block_desc == 'LoDemTar'| block_desc == 'LoDemNoTar'),'ld', block_desc)))

  if ('pressedQ' %in% colnames(data) == F){
    data$pressedQ <- c(rep(NA, nrow(data)))
  }
  if ('pressedQ_blank' %in% colnames(data) == F){
    data$pressedQ_blank <- c(rep(NA, nrow(data)))
  }
  if ('pressedQ_late' %in% colnames(data) == F){
    data$pressedQ_late <- c(rep(NA, nrow(data)))
  }
  
  # Calculate practice accuracy and RT
  pracAcc <- mean(data$LDTpracKey.corr[which(data$procedure == 'LDTpractice')], na.rm = T)
  pracRT <- mean(data$LDTpracKey.rt[which(data$procedure == 'LDTpractice')], na.rm = T)
  
  # Calculate overall PM accuracy
  corrPM_trials <- c()
  for (tarRow in which(data$role == 'target')){
      if (data$LDTResp.keys[tarRow] == 'q'){
        corrPM_trials <- append(corrPM_trials, 1)
      } else if (!is.na(data$pressedQ_blank[tarRow])){
        corrPM_trials <- append(corrPM_trials, 1)
      } else if (!is.na(data$pressedQ_late[tarRow+1])){
        corrPM_trials <- append(corrPM_trials, 1)
      } else if(data$LDTResp.keys[tarRow+1] == 'q'){
        corrPM_trials <- append(corrPM_trials, 1)
      } else if(!is.na(data$pressedQ_blank[tarRow+1])){
        corrPM_trials <- append(corrPM_trials, 1)
      } else if (!is.na(data$pressedQ_late[tarRow+2])){
        corrPM_trials <- append(corrPM_trials, 1)
      } else if (data$LDTResp.keys[tarRow+2] == 'q'){
        corrPM_trials <- append(corrPM_trials, 1)
      } else if (!is.na(data$pressedQ_blank[tarRow+2])){
        corrPM_trials <- append(corrPM_trials, 1)
      } else{
        corrPM_trials <- append(corrPM_trials, 0)
      }
  }

  PM_overall <- mean(corrPM_trials)

  pmContext <- c()
  for (i in which(data$role == 'target')){
    pmContext <- append(pmContext, data$context[i])
  }
  

  PM_HD <- sum(corrPM_trials[which(pmContext == 'hd')])/length(which(pmContext == 'hd'))
  PM_LD <- sum(corrPM_trials[which(pmContext == 'ld')])/length(which(pmContext == 'ld'))
  
  # Trim trials where RT more greater than +- 2/5 standard deviations from mean of that block
  rowsToTrim <- c()
  for (b in c(na.omit(unique(data$LDT_block.thisN)))){
    RTblockM <- mean(data$LDTResp.rt[which(data$LDT_block.thisN == b)], na.rm = T)
    RTblockSD <- sd(data$LDTResp.rt[which(data$LDT_block.thisN == b)], na.rm = T)
    rows <- which(data$LDT_block.thisN == b & (data$LDTResp.rt > (RTblockM + 2.5*RTblockSD))|
                           data$LDT_block.thisN == b & (data$LDTResp.rt < (RTblockM - 2.5*RTblockSD)))
    rowsToTrim <- append(rowsToTrim, rows)
  }
  tarTrials <- which(data$role == 'target' | data$role == 'aftertar1' | data$role == 'aftertar2')
  data <- data[-c(rowsToTrim, tarTrials),]
  
  # Calculate overall RT for HD and LD trials
  HDrt_overall <- mean(data$LDTResp.rt[which(data$procedure == 'LDT' & data$context == 'hd')], na.rm = T)
  HDrt_var <- sd(data$LDTResp.rt[which(data$procedure == 'LDT' & data$context == 'hd')], na.rm = T)
  LDrt_overall <- mean(data$LDTResp.rt[which(data$procedure == 'LDT' & data$context == 'ld')], na.rm = T)
  LDrt_var <- sd(data$LDTResp.rt[which(data$procedure == 'LDT' & data$context == 'ld')], na.rm = T)
  
  HDacc_overall <- mean(data$LDTResp.corr[which(data$procedure == 'LDT' & data$context == 'hd')], na.rm = T)
  LDacc_overall <- mean(data$LDTResp.corr[which(data$procedure == 'LDT' & data$context == 'ld')], na.rm = T)
  HD <- c(seq(1,length(na.omit(unique(data$LDT_block.thisN)))))
  LD <- c(seq(1,length(na.omit(unique(data$LDT_block.thisN)))))
  # Calculate block RT for HD and LD trials 
  for (r in c(na.omit(unique(data$LDT_block.thisN)))){
    if(data$context[which(data$LDT_block.thisN == r)[1]] == 'hd'){
      thisRun <- HD[1]
      if (thisRun < 10){block_str <- 'b0'}else{block_str <- 'b'}
      assign(paste0('HDrt_',block_str,thisRun), mean(data$LDTResp.rt[which(data$LDT_block.thisN == r & data$context == 'hd')], na.rm = T))
      assign(paste0('HDrt_var_',block_str,thisRun), sd(data$LDTResp.rt[which(data$LDT_block.thisN == r & data$context == 'hd')], na.rm = T))
      assign(paste0('HDaccu_',block_str,thisRun), mean(data$LDTResp.corr[which(data$LDT_block.thisN == r & data$context == 'hd')], na.rm = T))
      HD <- HD[2:length(HD)]
    } else{
      thisRun <- LD[1]
      if (thisRun < 10){block_str <- 'b0'}else{block_str <- 'b'}
      assign(paste0('LDrt_',block_str,thisRun), mean(data$LDTResp.rt[which(data$LDT_block.thisN == r & data$context == 'ld')], na.rm = T))
      assign(paste0('LDrt_var_',block_str,thisRun), sd(data$LDTResp.rt[which(data$LDT_block.thisN == r & data$context == 'ld')], na.rm = T))
      assign(paste0('LDaccu_',block_str,thisRun), mean(data$LDTResp.corr[which(data$LDT_block.thisN == r & data$context == 'ld')], na.rm = T))
      LD <- LD[2:length(LD)]
    }
  }
  df[nrow(df)+1, ] <- c(s, PM_overall, PM_HD, PM_LD,
                        HDrt_overall, LDrt_overall, HDrt_var, LDrt_var,
                        HDacc_overall, LDacc_overall,
                        c(mget(ls(pattern = 'HDrt_b')), mget(ls(pattern = 'LDrt_b')), 
                          mget(ls(pattern = 'HDrt_var_b')), mget(ls(pattern = 'LDrt_var_b')),
                          mget(ls(pattern = 'HDaccu_b')),mget(ls(pattern = 'LDaccu_b'))),
                        length(rowsToTrim),pracAcc, pracRT)
}
colnames(df) <- c('sub', 'PM_overall', 'PM_HD', 'PM_LD',
                  'HDrt_overall', 'LDrt_overall', 'HDrt_var', 'LDrt_var',
                  'HDacc_overall', 'LDacc_overall',
                  c((ls(pattern = 'HDrt_b')), (ls(pattern = 'LDrt_b')),
                    (ls(pattern = 'HDrt_var_b')), (ls(pattern = 'LDrt_var_b')),
                    (ls(pattern = 'HDaccu_b')),(ls(pattern = 'LDaccu_b'))),
                  'rowsToTrim','pracAcc', 'pracRT')
write.csv(df,
          file = '/Users/maddie/Library/CloudStorage/Box-Box/LEAP/version3/analyses/leap3_compiled.csv',
          row.names = F)


