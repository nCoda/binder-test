#(set-default-paper-size "letter" 'landscape)
#(set-global-staff-size 12)

\layout {
    \context {
        \Score
        \override BarLine.bar-extent = #'(0 . 0)
        \override Beam.breakable = ##t
        \override Glissando.breakable = ##t
        \override SpacingSpanner.strict-grace-spacing = ##t
        \override SpacingSpanner.strict-note-spacing = ##t
        \override SpacingSpanner.uniform-stretching = ##t
        \override TimeSignature.X-extent = ##f
        \override TimeSignature.Y-offset = 10
        \override TupletNumber.font-size = 1
        \override TupletNumber.text = #tuplet-number::calc-fraction-text
        autoBeaming = ##f
        proportionalNotationDuration = #(ly:make-moment 1 64)
    }
    indent = 0
}

\paper {
    left-margin = 1\in
    tagline = ##f
    top-margin = 1\in
}

