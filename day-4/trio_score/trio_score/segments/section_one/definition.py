# -*- encoding: utf-8 -*-
import os
import abjad
from trio_score import materials
from trio_score.tools import SegmentMaker


segment_maker = SegmentMaker(
    time_signatures=[(4, 4), (3, 4), (5, 4)] * 2,
    cello_pitches=[0, 2, 3, 4],
    cello_rhythm_maker=materials.my_droning_rhythm_maker,
    viola_pitches=[0, 2],
    viola_rhythm_maker=materials.my_slow_rhythm_maker,
    violin_pitches=[0, 2],
    violin_rhythm_maker=materials.my_fast_rhythm_maker,
    )


if __name__ == '__main__':
    lilypond_file, _ = segment_maker()
    illustration_path = os.path.join(
        os.path.dirname(__file__),
        'illustration.pdf',
        )
    abjad.persist(lilypond_file).as_pdf(illustration_path)
    abjad.systemtools.IOManager.open_file(illustration_path)
