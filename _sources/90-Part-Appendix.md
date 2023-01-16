\cleardoublepage

```{r echo=FALSE, results='asis'}
# This is the first appendix
if(!knitr::is_latex_output()){
  cat("# (APPENDIX) Appendix {-}")
} else {
  cat("\\appendix")
}
```


```{r setup_appA, include=FALSE}
chap <- "A"
lc <- 0
rq <- 0
# **`r paste0("(LC", chap, ".", (lc <- lc + 1), ")")`**
# **`r paste0("(RQ", chap, ".", (rq <- rq + 1), ")")`**
knitr::opts_chunk$set(
  tidy = FALSE, 
  out.width = '\\textwidth', 
  fig.height = 4,
  warning = FALSE
)
```
