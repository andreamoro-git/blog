---
layout: post
tags: tips
---


# LaTeX commands I keep forgetting

... and that I use a lot!

## Simplify page and margin size

      \usepackage[margin=1.25in]{geometry}

## 1.5 or double spacing

      \usepackage[onehalfspacing]{setspace}
           %\doublespacing

## Tabular cell vertical spacing

          \renewcommand{\arraystretch}{1.25}

## Change list item separation

           \itemsep 1ex      

## Change spacing around equations

          \setlength{\abovedisplayskip}{4pt}
          \setlength{\belowdisplayskip}{4pt}

## Spacing between bibliography items

          \setlength{\bibsep}{0pt}  

## Nice customizable bibliography style by Shiro Takeda

        \usepackage[authoryear]{natbib}
        \bibliographystyle{econ}

## Quick columns environment snippet

        \begin{columns}[t]
          \column{.5\textwidth}
            blah
          \column{.5\textwidth}
            bleh
        \end{columns}
        

## [Formatting beamer slides tips from Paul Goldsmith-Pinkham](https://github.com/paulgp/beamer-tips)

## [Generate a list of table and figures with corresponding latex file line number for replication packages](https://twitter.com/andreamoro/status/1400892405679902724?s=20) 
