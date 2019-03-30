src_diff_p_value = vector(mode="numeric", length=100)
test_diff_p_value = vector(mode="numeric", length=100)
status_p_value = vector(mode="numeric", length=100)
date_diff_p_value = vector(mode="numeric", length=100)
assert_p_value = vector(mode="numeric", length=100)
core_p_value = vector(mode="numeric", length=100)
test_failed_p_value = vector(mode="numeric", length=100)

for (sample in 0:99){
  input_filename = paste0("D://CMPUT501/project/project-saragholami/sample/sample", sample, ".csv")
  data = read.csv(input_filename)
  
  src_diff_model = lm(git_diff_src_churn / gh_sloc ~ gh_team_size, data = data)
  src_diff_p_value[sample] = summary(src_diff_model)$coefficients[2,4]
  
  test_diff_model = lm(git_diff_test_churn / gh_sloc ~ gh_team_size, data = data)
  test_diff_p_value[sample] = summary(test_diff_model)$coefficients[2,4]
  
  status_model = glm(tr_status ~ gh_team_size, data = data)
  status_p_value[sample] = summary(status_model)$coefficients[2,4]
  
  date_diff_model = lm(date_diff ~ gh_team_size, data = data)
  date_diff_p_value[sample] = summary(date_diff_model)$coefficients[2,4]
  
  assert_model = lm(gh_asserts_cases_per_kloc ~ gh_team_size, data = data)
  assert_p_value[sample] = summary(assert_model)$coefficients[2,4]
  
  core_model = glm(gh_by_core_team_member ~ gh_team_size, data = data)
  core_p_value[sample] = summary(core_model)$coefficients[2,4]
  
  test_failed_model = lm(tr_log_num_tests_failed ~ gh_team_size, data = data)
  test_failed_p_value[sample] = summary(test_failed_model)$coefficients[2,4]
}

write.table(src_diff_p_value, "D://CMPUT501/project/project-saragholami/models/src_code_diff.txt", append = FALSE, sep = " ", dec = ".")




















test_diff_model = lm(git_diff_test_churn / gh_sloc ~ gh_team_size, data = data)
summary(test_diff_model)

status_model = glm(tr_status ~ gh_team_size, data = data)
summary(status_model)

date_diff_model = lm(date_diff ~ gh_team_size, data = data)
summary(date_diff_model)

assert_model = lm(gh_asserts_cases_per_kloc ~ gh_team_size, data = data)
summary(assert_model)

core_model = glm(gh_by_core_team_member ~ gh_team_size, data = data)
summary(core_model)

test_failed_model = lm(tr_log_num_tests_failed ~ gh_team_size, data = data)
summary(test_failed_model)

out = capture.output(summary(codeDiffModel))
cat("codeDiffModel", out, file="source_code_diff_reg.txt", sep="n", append=TRUE)