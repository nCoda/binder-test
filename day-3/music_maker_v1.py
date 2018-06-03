import abjad


#time_signature_pairs = [(4, 4), (3, 8), (3, 4), (7, 16), (2, 4)] * 100
#time_signature_pairs = [(6, 8)] * 100
time_signature_pairs = [(4, 4), (3, 4), (7, 16), (6, 8)]

total_duration = sum(abjad.Duration(pair) for pair in time_signature_pairs)

counts = [1, 2, -3, 4]
#counts = [1]
denominator = 16
talea = abjad.rhythmmakertools.Talea(counts=counts, denominator=denominator)
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


shards = abjad.mutate(music[:]).split(time_signature_pairs)
for i, shard in enumerate(shards):
    measure = abjad.Measure(time_signature_pairs[i])
    abjad.mutate(shard).wrap(measure)
    

#pitches = abjad.CyclicTuple(["d'", "a''", "gs'", "fs'"])
#pitches = abjad.CyclicTuple(["c'", "c''"])
#pitches = abjad.CyclicTuple([0, 2, 4, 5, 7, 9, 11, 12])
pitches = abjad.CyclicTuple([0, 3, 7, 12, 7, 3])


logical_ties = abjad.iterate(music).by_logical_tie(pitched=True)
for i, logical_tie in enumerate(logical_ties):
    pitch = pitches[i]
    for note in logical_tie:
        note.written_pitch = pitch

for run in abjad.select(music).by_leaf().by_run((abjad.Note, abjad.Chord)):
    abjad.attach(abjad.Articulation('accent'), run[0])
    if 1 < len(run):
        abjad.attach(abjad.Hairpin('p < f'), run)
    else:
        abjad.attach(abjad.Dynamic('ppp'), run[0])
