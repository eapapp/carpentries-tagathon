# Carpentries Tagathon

This is the Oslo carpentry Study group's contribution to the [October Tagathon](https://carpentries.org/blog/2019/10/carpentries-tagathon/). The original blog posts courtesy of [Data Carpentries](https://datacarpentry.org/blog/).

## What does it do so far?

* All data carpentries blog posts found [here](https://github.com/datacarpentry/datacarpentry.github.io/tree/master/_posts) are processed
* The yaml header is removed and `title` and `teaser` are added as H1, H2 headlines in markdown. 
* The markdown is then converted with Pandoc to plain text (`.txt`). Clean Markdown and plain text are stored in `clean/` folder.

## Roadmap

* text mine it and come up with automatic tags.

## Setup

* The cleaning script requires R and RStudio, `tidyverse`, and `knitr` packages
