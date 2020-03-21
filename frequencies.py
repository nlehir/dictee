import random


def generate_one_frequency(center_offset_to_a4, ambitus):
    """
        ambitus is in semi tones
        n_note is in semitones
    """
    if ambitus % 2 == 0:
        p = ambitus // 2
        offset_to_center = random.randint(-p, p)
    else:
        p = (ambitus - 1) // 2
        offset_to_center = random.randint(-p, p+1)
    n_note = center_offset_to_a4 + offset_to_center
    frequency = pow(2, n_note/12)*440
    return frequency


def build_frequencies_sequence(center_offset_to_a4, nb_notes, ambitus):
    """
        center_offset_to_a4: int
        nb_notes: int
        ambitus: int (tons)
    """
    freq_sequence = list()
    center_frequency = pow(2, center_offset_to_a4/12)*440
    freq_sequence.append(center_frequency)
    for note_index in range(0, nb_notes-1):
        frequency = generate_one_frequency(center_offset_to_a4, ambitus)
        freq_sequence.append(frequency)
    return freq_sequence
