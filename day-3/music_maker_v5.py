import abjad
import copy


class AttachmentMaker(object):
    """
    An attachment-making machine.
    """

    def __init__(self, attachment, selector):
        self.attachment = attachment
        self.selector = selector

    def __call__(self, music):
        for selection in self.selector(music):
            attachment = copy.copy(self.attachment)
            abjad.attach(attachment, selection)


class MusicMaker(object):
    """
    A music-making machine.
    """

    def __init__(
        self,
        counts,
        denominator,
        pitches,
        attachment_makers=None,
        ):
        self.counts = counts
        self.denominator = denominator
        self.pitches = pitches
        self.attachment_makers = attachment_makers or []

    def __call__(self, time_signature_pairs):
        music = self._make_basic_rhythm(
            time_signature_pairs,
            self.counts,
            self.denominator,
            )
        music = self._clean_up_rhythm(music, time_signature_pairs)
        music = self._add_pitches(music, self.pitches)
        music = self._add_attachments(music)
        return music

    def _make_basic_rhythm(self, time_signature_pairs, counts, denominator):
        """
        Make a basic rhythm using ``time_signature_pairs``, ``counts`` and
        ``denominator``.
        """
        total_duration = sum(
            abjad.Duration(pair) for pair in time_signature_pairs
            )
        talea = abjad.rhythmmakertools.Talea(
            counts=counts,
            denominator=denominator,
            )
        talea_index = 0
        all_leaves = []
        current_duration = abjad.Duration(0)
        while current_duration < total_duration:
            leaf_duration = talea[talea_index]
            if leaf_duration > 0:
                pitch = abjad.NamedPitch("c'")
            else:
                pitch = None
            leaf_duration = abs(leaf_duration)
            if (leaf_duration + current_duration) > total_duration:
                leaf_duration = total_duration - current_duration
            current_leaves = abjad.LeafMaker()([pitch], [leaf_duration])
            all_leaves.extend(current_leaves)
            current_duration += leaf_duration
            talea_index += 1
        music = abjad.Container(all_leaves)
        return music

    def _clean_up_rhythm(self, music, time_signature_pairs):
        """
        Clean up rhythms in ``music`` via ``time_signature_pairs``.
        """
        shards = abjad.mutate(music[:]).split(time_signature_pairs)
        for i, shard in enumerate(shards):
            time_signature_pair = time_signature_pairs[i]
            measure = abjad.Measure(time_signature_pair)
            assert shard.get_duration() == abjad.Duration(
                time_signature_pair)
            abjad.mutate(shard).wrap(measure)
        return music

    def _add_pitches(self, music, pitches):
        """
        Add ``pitches`` to music.
        """
        pitches = abjad.CyclicTuple(pitches)
        logical_ties = abjad.iterate(music).by_logical_tie(pitched=True)
        for i, logical_tie in enumerate(logical_ties):
            pitch = pitches[i]
            for note in logical_tie:
                note.written_pitch = pitch
        return music

    def _add_attachments(self, music):
        """
        Add attachments to ``music``.
        """
        for attachment_maker in self.attachment_makers:
            attachment_maker(music)
        return music


slur_attachment_maker = AttachmentMaker(
    attachment=abjad.Slur(),
    selector=abjad.select().by_leaf().by_run((abjad.Note, abjad.Chord))
    )


accent_attachment_maker = AttachmentMaker(
    attachment=abjad.Articulation('accent'),
    selector=abjad.select().by_leaf().by_run((abjad.Note, abjad.Chord))[0]
    )


fast_music_maker = MusicMaker(
    counts=[1, 1, 1, 1, 1, -1],
    denominator=16,
    pitches=[0, 1],
    attachment_makers=[
        slur_attachment_maker,
        accent_attachment_maker,
        ],
    )

music = fast_music_maker([(3, 4), (5, 8), (4, 4)] * 10)

staff = abjad.Staff([music])
score = abjad.Score([staff])
lilypond_file = abjad.LilyPondFile.new(
    music=score,
    includes=['stylesheet.ily'],
    )

abjad.show(lilypond_file)
