# Creates mine-able plain text files from Jekyll blog post md.

library(tidyverse)
library(knitr)


clean_md <- function(fn) {
  # removes the header from the md file `fn` and prepends title 
  # and teaser as H1, H2 
  
  text       <- read_file(fn)
  
  text_split <- str_split(text, '[\n\r]---[\n\r]', simplify = T)
  head       <- text_split[1]
  body       <- text_split[2]
  title      <- str_match(head, "(title:)[\\s]*([^\\n]*)")[3]
  teaser     <- str_match(head, '(teaser:)[\\s]*\"([^\\n]*)')[3]
  
  str_c(
    paste0("# ", title), 
    paste0("## ", teaser), 
    body, 
    sep = "\n"
  )
}


dir_in   <- "_posts/"
dir_out  <- "clean/"
files_in <- list.files(path = dir_in, pattern = "*.md")

# (re)create empty output dir
unlink(dir_out, recursive = TRUE)
dir.create(dir_out)


for (fn in files_in) {
  fn_in  <- paste0(dir_in, fn)
  fn_out <- paste0(dir_out, str_replace(fn, ".md$", "_clean.md"))
  
  # store as "clean" markdown and plain text
  write_file(clean_md(fn_in), fn_out)
  knitr::pandoc(fn_out, format = 'plain', ext = "txt")
}


