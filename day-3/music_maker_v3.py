import abjad

# THIS IS THE INPUT TO MY MUSICAL IDEA
time_signature_pairs = [(4, 4), (3, 4), (7, 16), (6, 8)]
counts = [1, 2, -3, 4]
denominator = 16
pitches = abjad.CyclicTuple([0, 3, 7, 12, 7, 3])



class MusicMaker(object):

    def __init__(self, counts, denominator, pitches):
        self.counts = counts
        self.denominator = denominator
        self.pitches = pitches

    def make_basic_rhythm(self, time_signature_pairs, counts, denominator):
        # THIS IS HOW WE MAKE THE BASIC RHYTHM
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


    def clean_up_rhythm(self, music, time_signature_pairs):
        # THIS IS HOW WE CLEAN UP THE RHYTHM
        shards = abjad.mutate(music[:]).split(time_signature_pairs)
        for i, shard in enumerate(shards):
            measure = abjad.Measure(time_signature_pairs[i])
            abjad.mutate(shard).wrap(measure)
        return music
            

    def add_pitches(self, music, pitches):
        # THIS IS HOW WE ADD PITCHES
        pitches = abjad.CyclicTuple(pitches)
        logical_ties = abjad.iterate(music).by_logical_tie(pitched=True)
        for i, logical_tie in enumerate(logical_ties):
            pitch = pitches[i]
            for note in logical_tie:
                note.written_pitch = pitch
        return music


    def add_attachments(self, music):
        # THIS IS HOW WE ADD DYNAMICS AND ACCENTS
        for run in abjad.select(music).by_leaf().by_run(
            (abjad.Note, abjad.Chord)):
            abjad.attach(abjad.Articulation('accent'), run[0])
            if 1 < len(run):
                abjad.attach(abjad.Hairpin('p < f'), run)
            else:
                abjad.attach(abjad.Dynamic('ppp'), run[0])
        return music


    def make_music(self, time_signature_pairs):
        music = self.make_basic_rhythm(
            time_signature_pairs,
            self.counts,
            self.denominator,
            )
        music = self.clean_up_rhythm(music, time_signature_pairs)
        music = self.add_pitches(music, self.pitches)
        music = self.add_attachments(music)
        return music
