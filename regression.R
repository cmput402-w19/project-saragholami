src_diff_p_value = vector(mode = "numeric", length = 100)
test_diff_p_value = vector(mode = "numeric", length = 100)
status_p_value = vector(mode = "numeric", length = 100)
date_diff_p_value = vector(mode = "numeric", length = 100)
assert_p_value = vector(mode = "numeric", length = 100)
core_p_value = vector(mode = "numeric", length = 100)
test_failed_p_value = vector(mode = "numeric", length = 100)
num_commits_p_value = vector(mode = "numeric", length = 100)
test_ok_p_value = vector(mode = "numeric", length = 100)
test_run_p_value = vector(mode = "numeric", length = 100)
failed_ratio_p_value = vector(mode = "numeric", length = 100)
ok_ratio_p_value = vector(mode = "numeric", length = 100)
touched_p_value = vector(mode = "numeric", length = 100)
test_line_p_value = vector(mode = "numeric", length = 100)
test_cases_p_value = vector(mode = "numeric", length = 100)
code_date_p_value = vector(mode = "numeric", length = 100)
sloc_p_value = vector(mode = "numeric", length = 100)

for (sample in 0:99) {
  input_filename = paste0("D://CMPUT501/project/project-saragholami/sample/sample", sample, ".csv")
  data = read.csv(input_filename, header = TRUE, sep = ",")
  
  # code_date_model = lm(src_date ~ gh_team_size, data = data, na.action=na.exclude)
  # code_date_p_value[sample] = summary(code_date_model)$coefficients[2,4]
  
  sloc_model = lm(gh_sloc ~ gh_team_size, data = data)
  sloc_p_value[sample] = summary(sloc_model)$coefficients[2,4]

}

#################################### Saving ##################################################

write.table(
  sloc_p_value,
  "D://CMPUT501/project/project-saragholami/models/sloc.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  code_date_p_value,
  "D://CMPUT501/project/project-saragholami/models/code_date.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  src_diff_p_value,
  "D://CMPUT501/project/project-saragholami/models/src_code_diff.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  test_diff_p_value,
  "D://CMPUT501/project/project-saragholami/models/test_code_diff.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  status_p_value,
  "D://CMPUT501/project/project-saragholami/models/status.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  date_diff_p_value,
  "D://CMPUT501/project/project-saragholami/models/date_diff.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  assert_p_value,
  "D://CMPUT501/project/project-saragholami/models/assert.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  core_p_value,
  "D://CMPUT501/project/project-saragholami/models/core.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  test_failed_p_value,
  "D://CMPUT501/project/project-saragholami/models/test_failed.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  num_commits_p_value,
  "D://CMPUT501/project/project-saragholami/models/num_commits.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  test_ok_p_value,
  "D://CMPUT501/project/project-saragholami/models/test_ok.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  test_run_p_value,
  "D://CMPUT501/project/project-saragholami/models/test_run.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  failed_ratio_p_value,
  "D://CMPUT501/project/project-saragholami/models/failed_ratio.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  ok_ratio_p_value,
  "D://CMPUT501/project/project-saragholami/models/ok_ratio.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  touched_p_value,
  "D://CMPUT501/project/project-saragholami/models/touched.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  test_line_p_value,
  "D://CMPUT501/project/project-saragholami/models/test_line.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)
write.table(
  test_cases_p_value,
  "D://CMPUT501/project/project-saragholami/models/test_case.txt",
  append = FALSE,
  sep = " ",
  dec = "."
)

#################################### Creating Models ##################################################

# test_line_model = lm(gh_test_lines_per_kloc ~ gh_team_size, data = data)
# test_line_p_value[sample] = summary(test_line_model)$coefficients[2, 4]
# 
# test_cases_model = lm(gh_test_cases_per_kloc ~ gh_team_size, data = data)
# test_cases_p_value[sample] = summary(test_cases_model)$coefficients[2, 4]
#
# touched_model = lm(gh_num_commits_on_files_touched ~ gh_team_size, data = data)
# touched_p_value[sample] = summary(touched_model)$coefficients[2,4]
#
# src_diff_model = lm(git_diff_src_churn / gh_sloc ~ gh_team_size, data = data)
# src_diff_p_value[sample] = summary(src_diff_model)$coefficients[2,4]
#
# test_diff_model = lm(git_diff_test_churn / gh_sloc ~ gh_team_size, data = data)
# test_diff_p_value[sample] = summary(test_diff_model)$coefficients[2,4]
#
# status_model = glm(tr_status ~ gh_team_size, data = data)
# status_p_value[sample] = summary(status_model)$coefficients[2,4]
#
# date_diff_model = lm(date_diff ~ gh_team_size, data = data)
# date_diff_p_value[sample] = summary(date_diff_model)$coefficients[2,4]
#
# assert_model = lm(gh_asserts_cases_per_kloc ~ gh_team_size, data = data)
# assert_p_value[sample] = summary(assert_model)$coefficients[2,4]
#
# core_model = glm(gh_by_core_team_member ~ gh_team_size, data = data)
# core_p_value[sample] = summary(core_model)$coefficients[2,4]
#
# test_failed_model = lm(tr_log_num_tests_failed ~ gh_team_size, data = data)
# test_failed_p_value[sample] = summary(test_failed_model)$coefficients[2,4]
#
# num_commits_model = lm(gh_num_commits_in_push ~ gh_team_size, data = data)
# num_commits_p_value[sample] = summary(num_commits_model)$coefficients[2,4]
#
# test_ok_model = lm(tr_log_num_tests_ok ~ gh_team_size, data = data)
# test_ok_p_value[sample] = summary(test_ok_model)$coefficients[2,4]
#
# test_run_model = lm(tr_log_num_tests_run ~ gh_team_size, data = data)
# test_run_p_value[sample] = summary(test_run_model)$coefficients[2,4]
#
# failed_ratio_model = lm(tr_log_num_tests_failed / tr_log_num_tests_run ~ gh_team_size, data = data)
# failed_ratio_p_value[sample] = summary(failed_ratio_model)$coefficients[2,4]
#
# ok_ratio_model = lm(tr_log_num_tests_ok / tr_log_num_tests_run ~ gh_team_size, data = data)
# ok_ratio_p_value[sample] = summary(ok_ratio_model)$coefficients[2,4]

##############################################################################################

# test_diff_model = lm(git_diff_test_churn / gh_sloc ~ gh_team_size, data = data)
# summary(test_diff_model)
#
# status_model = glm(tr_status ~ gh_team_size, data = data)
# summary(status_model)
#
# date_diff_model = lm(date_diff ~ gh_team_size, data = data)
# summary(date_diff_model)
#
# assert_model = lm(gh_asserts_cases_per_kloc ~ gh_team_size, data = data)
# summary(assert_model)
#
# core_model = glm(gh_by_core_team_member ~ gh_team_size, data = data)
# summary(core_model)
#
# test_failed_model = lm(tr_log_num_tests_failed ~ gh_team_size, data = data)
# summary(test_failed_model)
#
# out = capture.output(summary(codeDiffModel))
# cat("codeDiffModel", out, file="source_code_diff_reg.txt", sep="n", append=TRUE)