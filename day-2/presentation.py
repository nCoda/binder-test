import abjad


def make_sketch_lilypond_file(component):
    for voice in abjad.iterate(component).by_class(abjad.Voice):
        voice.remove_commands.append('Forbid_line_break_engraver')
    abjad.override(component).bar_line.stencil = False
    abjad.override(component).bar_number.stencil = False
    abjad.override(component).beam.positions = abjad.schemetools.SchemePair((4, 4))
    abjad.override(component).spacing_spanner.strict_grace_spacing = True
    abjad.override(component).spacing_spanner.strict_note_spacing = True
    abjad.override(component).spacing_spanner.uniform_stretching = True
    abjad.override(component).stem.length = 8.25
    abjad.override(component).text_script.outside_staff_padding = 1
    abjad.override(component).time_signature.stencil = False
    abjad.override(component).tuplet_bracket.bracket_visibility = True
    abjad.override(component).tuplet_bracket.minimum_length = 3
    abjad.override(component).tuplet_bracket.outside_staff_padding = 1.5
    abjad.override(component).tuplet_bracket.padding = 1.5
    abjad.override(component).tuplet_bracket.springs_and_rods = \
        abjad.schemetools.Scheme('ly:spanner::set-spacing-rods', verbatim=True)
    abjad.override(component).tuplet_bracket.staff_padding = 2.25
    abjad.override(component).tuplet_number.text = \
        abjad.schemetools.Scheme('tuplet-number::calc-fraction-text', verbatim=True)
    abjad.setting(component).proportional_notation_duration = \
        abjad.schemetools.SchemeMoment((1, 24))
    abjad.setting(component).tuplet_full_length = True
    lilypond_file = abjad.lilypondfiletools.LilyPondFile.new(component)
    lilypond_file.layout_block.indent = 0
    return lilypond_file


def make_sketch(rhythm_maker, divisions):
    # rhythmic creation
    selections = rhythm_maker(divisions)
    voice = abjad.Voice(selections)
    staff = abjad.Staff([voice], context_name='RhythmicStaff')
    score = abjad.Score([staff])
    lilypond_file = make_sketch_lilypond_file(score)
    return lilypond_file


__all__ = [
    'make_sketch',
    'make_sketch_lilypond_file',
    ]