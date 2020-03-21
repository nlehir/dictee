# Use the sounddevice module
# http://python-sounddevice.readthedocs.io/en/0.3.10/

import numpy as np
import sounddevice as sd
import time

rate = 44100       # sampling rate, Hz, must be integer


def one_note_array(frequency, note_duration):
    nb_samples = int(rate*note_duration)
    samples = (np.sin(2*np.pi*np.arange(nb_samples)
                      * frequency/rate)).astype(np.float32)
    window = build_window(nb_samples)
    samples = samples * window
    return samples


def build_window(nb_samples):
    window = np.array([], dtype="float32")
    nb_rising = int(nb_samples*5/100)
    rising = np.linspace(0, 1, nb_rising)
    window = np.concatenate((window, rising))

    nb_top = int(nb_samples*90/100)
    top = np.ones(nb_top)
    window = np.concatenate((window, top))

    nb_decreasing = nb_samples-nb_rising - nb_top
    decreasing = np.linspace(1, 0, nb_decreasing)
    window = np.concatenate((window, decreasing))

    return window


def build_array(nb_notes_per_second, notes_sequence):
    note_duration = 1.0/nb_notes_per_second   # in seconds, may be float

    samples = np.array([])
    for frequency in notes_sequence:
        one_array = one_note_array(frequency, note_duration)
        samples = np.concatenate((samples, one_array))
    return samples


def play_sequence(frequencies_sequence, nb_notes_per_second):
    nb_notes = len(frequencies_sequence)
    waveform = build_array(nb_notes_per_second, frequencies_sequence)

    period = 1/nb_notes_per_second
    duration_s = period*nb_notes*1.2

    # Attenuation so the sound is reasonable
    atten = 0.3
    waveform_quiet = waveform * atten

    # Play the waveform out the speakers
    sd.play(waveform_quiet, rate)
    time.sleep(duration_s)
    sd.stop()


if __name__ == '__main__':
    play_sequence([220, 880, 990, 1100], 5)
