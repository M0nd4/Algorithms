(TeX-add-style-hook "equations"
 (lambda ()
    (LaTeX-add-labels
     "Natural Log")
    (TeX-run-style-hooks
     "mathtools"
     "graphicx"
     "latex2e"
     "art10"
     "article")))

