data = read.csv("D://CMPUT501/project/project-saragholami/sample/travis_torrent_refined.csv", header = TRUE, sep = ",")


########################## gh_sloc ###################################
cor(data$gh_sloc, data$gh_team_size, method="pearson") 

sloc_model = lm(gh_sloc ~ gh_team_size, data = data)
summary(sloc_model)

sloc_p_value = vector(mode = "numeric", length = 100)
for (sample in 0:99) {
  input_filename = paste0("D://CMPUT501/project/project-saragholami/sample/sample", sample, ".csv")
  data = read.csv(input_filename, header = TRUE, sep = ",")
  sloc_p_value[sample] = cor(data$gh_sloc, data$gh_team_size, method="pearson")
}
mean(sloc_p_value)

########################## tr_status ###################################
cor(data$tr_status, data$gh_team_size, method="pearson") 

status_model = lm(tr_status ~ gh_team_size, data = data)
summary(status_model)

status_p_value = vector(mode = "numeric", length = 100)
for (sample in 0:99) {
  input_filename = paste0("D://CMPUT501/project/project-saragholami/sample/sample", sample, ".csv")
  data = read.csv(input_filename, header = TRUE, sep = ",")
  status_p_value[sample] = cor(data$tr_status, data$gh_team_size, method="pearson")
}
mean(status_p_value)

library(ltm)
biserial.cor(data$gh_team_size, data$tr_status, use = c("complete.obs"), level=1)


