\version "2.18.2"
\language "english"

\header {
    composer = "Best Composer"
    title = "My Great Piece"
    subtitle = "A Very Fine Gigue"
}

\header {
    title = "My Adequate Piece"
}

\header {
    subtitle = "Visions of a Somber World"
}

\layout {
    \context {
        \Staff
        \override NoteHead.color = #red
    }
}

\layout {
    \context {
        \Staff
        \override NoteHead.color = #blue
    }
}

\layout {
    \context {
        \Staff
        \override NoteHead.color = #green
    }
}

\new Staff {
    c'1
}
