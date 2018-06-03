\layout {
    \context {
        \Score
        \override SpacingSpanner.uniform-stretching = ##t
        autoBeaming = ##f
        proportionalNotationDuration = #(ly:make-moment 1 32)
    }
}

\paper {
    indent = 20\mm
    short-indent = 15\mm
    bottom-margin = 10\mm
    left-margin = 10\mm
    right-margin = 10\mm
    top-margin = 10\mm
    oddHeaderMarkup = \markup {}
    evenHeaderMarkup = \markup {}
    page-breaking = #ly:optimal-breaking
    ragged-bottom = ##f
    ragged-last-bottom = ##t
}
