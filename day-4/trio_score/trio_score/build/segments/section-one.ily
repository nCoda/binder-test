    \context Score = "Trio Score" <<
        \context StaffGroup = "Trio Staff Group" <<
            \tag #'violin
            \context ViolinStaff = "Violin Staff" \with {
                midiInstrument = #"violin"
            } {
                \clef "treble"
                \set Staff.instrumentName = \markup { Violin }
                \set Staff.shortInstrumentName = \markup { Vn. }
                \context Voice = "Violin Voice" {
                    {
                        \time 4/4
                        {
                            c'16 [
                            d'16
                            c'8
                            d'8. ]
                            r16
                            c'4
                            d'16 [
                            c'16
                            d'8 ~ ]
                        }
                    }
                    {
                        \time 3/4
                        {
                            d'16 [
                            c'16
                            d'8
                            c'8. ]
                            r16
                            d'4
                        }
                    }
                    {
                        \time 5/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 20/21 {
                            c'16 [
                            d'16
                            c'8
                            d'16
                            c'16
                            d'8
                            c'8. ]
                            r16
                            d'4
                            c'16 [
                            d'16
                            c'8
                            d'16 ~ ]
                        }
                    }
                    {
                        \time 4/4
                        {
                            d'16 [
                            c'8
                            d'8. ]
                            r16
                            c'4
                            d'16 [
                            c'16
                            d'8
                            c'16 ]
                        }
                    }
                    {
                        \time 3/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 12/13 {
                            d'16 [
                            c'8
                            d'8. ]
                            r16
                            c'4
                            d'16 [
                            c'16 ~ ]
                        }
                    }
                    {
                        \time 5/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 10/11 {
                            c'8 [
                            d'16
                            c'16
                            d'8
                            c'8. ]
                            r16
                            d'4
                            c'16 [
                            d'16
                            c'8
                            d'16
                            c'16
                            d'8 ]
                            \bar "||"
                        }
                    }
                }
            }
            \tag #'viola
            \context ViolaStaff = "Viola Staff" \with {
                midiInstrument = #"viola"
            } {
                \clef "alto"
                \set Staff.instrumentName = \markup { Viola }
                \set Staff.shortInstrumentName = \markup { Va. }
                \context Voice = "Viola Voice" {
                    {
                        \time 4/4
                        {
                            c'4
                            d'4
                            c'4
                            d'4 ~
                        }
                    }
                    {
                        \time 3/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 6/7 {
                            d'8 [
                            c'8
                            d'8
                            c'8
                            d'8
                            c'8
                            d'8 ~ ]
                        }
                    }
                    {
                        \time 5/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 5/4 {
                            d'2
                            c'2 ~
                        }
                    }
                    {
                        \time 4/4
                        \times 4/5 {
                            c'4
                            d'4
                            c'4
                            d'4
                            c'4 ~
                        }
                    }
                    {
                        \time 3/4
                        {
                            c'8 [
                            d'8
                            c'8
                            d'8
                            c'8
                            d'8 ~ ]
                        }
                    }
                    {
                        \time 5/4
                        \tweak text #tuplet-number::calc-fraction-text
                        \times 5/6 {
                            d'2
                            c'2
                            d'2
                            \bar "||"
                        }
                    }
                }
            }
            \tag #'cello
            \context CelloStaff = "Cello Staff" \with {
                midiInstrument = #"cello"
            } {
                \clef "bass"
                \set Staff.instrumentName = \markup { Cello }
                \set Staff.shortInstrumentName = \markup { Vc. }
                \context Voice = "Cello Voice" {
                    {
                        \time 4/4
                        c'1 ~
                    }
                    {
                        \time 3/4
                        c'2.
                    }
                    {
                        \time 5/4
                        d'1 ~
                        d'4 ~
                    }
                    {
                        \time 4/4
                        d'1
                    }
                    {
                        \time 3/4
                        ef'2. ~
                    }
                    {
                        \time 5/4
                        ef'1 ~
                        ef'4
                        \bar "||"
                    }
                }
            }
        >>
    >>
