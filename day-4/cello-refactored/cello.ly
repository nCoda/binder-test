\version "2.18.2"
\language "english"

\include "stylesheet.ily"

\new Score \with {
    } <<
    \new PianoStaff \with {
        \override StaffGrouper.staff-staff-spacing.minimum-distance = 18
        } <<
        % THIS IS MY RIGHT HAND STAFF
        \new Staff \with {
            \override Clef.stencil = ##f
            \override NoteHead.stencil = ##f
            \override StaffSymbol.line-positions = #'(0)
            instrumentName = \markup { \hcenter-in #6 RH }
            } <<
            % THIS IS A SPECIAL VOICE JUST FOR TIME SIGNATURES!
            \new Voice \with {
                \remove Forbid_line_break_engraver
                } {
                \time 9/16
                s1 * 9/16
                \time 7/16
                s1 * 7/16
            }
            % THIS IS A VOICE FOR THE RH *MUSIC* (instead of time signatures)
            \new Voice \with {
                \override Beam.positions = #'(-6 . -6)
                \override DynamicLineSpanner.staff-padding = 9
                \override Glissando.bound-details.left.padding = 0.25
                \override Glissando.bound-details.left.start-at-dot = ##f
                \override Glissando.bound-details.right.padding = 0
                \override Glissando.thickness = 6
                \override Stem.length = 10
                \remove Forbid_line_break_engraver
            } {
                b'8 [ \glissando \f \<
                b'8 \glissando
                b'16 \glissando
                b'16 ] \glissando
                b'8 [ \glissando
                b'8 \glissando
                b'16 \glissando
                b'16 ] \glissando
                \times 2/3 { 
                    b'4  \glissando \ff \>
                    b'8 \f
                }
            }
            >>
        % THIS IS MY LEFT HAND STAFF
        \new Staff \with {
            \remove Time_signature_engraver
            instrumentName = \markup { \hcenter-in #6 LH }
            } {
                % THIS IS THE VOICE FOR MUSIC IN THE LEFT HAND
                \new Voice \with {
                    \override Glissando.thickness = 3
                    \remove Forbid_line_break_engraver
                } {
                    \clef "bass"
                    \times 2/3 {
                        d'8 \glissando
                        cs'1 \glissando
                        ef'4 \glissando
                        d'8
                    }
                }
            }
        >>
>>
