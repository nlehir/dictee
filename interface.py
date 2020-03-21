# coding: utf-8
import player
import sys
import frequencies
from PIL import ImageFont
import random
import center_note
if sys.version_info < (3, 0):
    import Tkinter as tk
else:
    import tkinter as tk


font_choice_1 = "./Bebas-Regular.ttf"
font_choice_2 = "./Roboto-Condensed.ttf"
font_choice_3 = "./BebasNeue-Regular.ttf"
font = ImageFont.truetype(font_choice_2, 15)
colors = ["#68baa8",
          "#7ac4b4",
          "#84d1c0",
          "#6bbfad",
          "#56b39f",
          "#35b095",
          "#2fc4a4",
          "#3bd4b3",
          "#36b59a",
          "#23c2a0"]


positions = ["RP", "R1", "R2", "R3"]

config_text = (
    "     Enter : nouvelles notes "
    "| a : augmenter ambitus     "
    "| A : diminuer ambitus     \n"
    "| v : augmenter vitesse (notes par seconde)    "
    "| V : diminuer vitesse     "
    "| p : rejouer"
)


class Interface(tk.Frame):
    def __init__(self, fenetre):
        tk.Frame.__init__(self, fenetre)
        # self.grid_propagate(0)
        self.pack(fill=tk.BOTH)
        self.note_sequence = list()
        self.nb_notes = 4
        self.ambitus = 4
        self.speed = 2
        fontsize = 50
        width = 10

        # --------------
        # pans
        # --------------
        self.pan_1 = tk.Label(self)
        self.pan_1.pack(fill=tk.BOTH)

        self.nb_notes_pan = tk.Label(
            self.pan_1,
            width=width,
            height=3,
            bg=random.choice(colors),
            font=(font, fontsize),
            text="Nb notes\n{}".format(self.nb_notes))
        self.nb_notes_pan.pack(side="left")

        self.ambitus_pan = tk.Label(
            self.pan_1,
            width=width,
            height=3,
            bg=random.choice(colors),
            font=(font, fontsize),
            text="Ambitus\n{} tons".format(self.ambitus))
        self.ambitus_pan.pack(side="left")

        self.center_pan = tk.Label(
            self.pan_1,
            width=width,
            height=3,
            bg=random.choice(colors),
            font=(font, fontsize),
            text="Appuyer\nsur\nEntrée")
        self.center_pan.pack(side="left")

        self.speed_pan = tk.Label(
            self.pan_1,
            width=width,
            height=3,
            bg=random.choice(colors),
            font=(font, fontsize),
            text="Vitesse\n{} nps".format(self.speed))
        self.speed_pan.pack(side="left")

        self.options = tk.Label(self, bg="#73abf5", width="60")
        self.options.pack(fill="both")

        self.config = tk.Label(
            self.options,
            width=70,
            height=3,
            bg="#73abf5",
            font=(font, 25),
            text=config_text)
        self.config.pack(side="left", fill="both")
        # --------------
        # --------------

    def play_note_sequence(self):
        player.play_sequence(self.frequencices_sequence, self.speed)

    def next_note_sequence(self):
        """
            center is offset compared to A4
        """
        self.center_offset_to_a4 = random.randint(-9, 3)
        self.frequencices_sequence = frequencies.build_frequencies_sequence(
            self.center_offset_to_a4,
            self.nb_notes,
            self.ambitus)

    def increase_ambitus(self):
        if self.ambitus < 20:
            self.ambitus += 1
            self.ambitus_pan["text"] = "Ambitus\n{} tons".format(self.ambitus)

    def decrease_ambitus(self):
        if self.ambitus > 1:
            self.ambitus -= 1
            self.ambitus_pan["text"] = "Ambitus\n{} tons".format(self.ambitus)

    def increase_nb_notes(self):
        if self.nb_notes < 20:
            self.nb_notes += 1
            self.nb_notes_pan["text"] = "Nb notes\n{}".format(self.nb_notes)

    def update_first_note(self):
        first_note = center_note.get_center_note(self.center_offset_to_a4)
        self.center_pan["text"] = first_note

    def decrease_nb_notes(self):
        if self.nb_notes > 2:
            self.nb_notes -= 1
            self.nb_notes_pan["text"] = "Nb notes\n{}".format(self.nb_notes)

    def increase_speed(self):
        if self.speed < 8:
            self.speed += 1
            self.speed_pan["text"] = "Vitesse\n{} nps".format(self.speed)

    def decrease_speed(self):
        if self.speed > 1:
            self.speed -= 1
            self.speed_pan["text"] = "Vitesse\n{} nps".format(self.speed)

    def string_from_integer(self, note_int):
        return self.all_notes[note_int]

    def integer_from_string(self, note_string):
        return self.all_notes.index(note_string)


def increase_ambitus(event):
    interface.increase_ambitus()


def decrease_ambitus(event):
    interface.decrease_ambitus()


def increase_nb_notes(event):
    interface.increase_nb_notes()


def decrease_nb_notes(event):
    interface.decrease_nb_notes()


def increase_speed(event):
    interface.increase_speed()


def decrease_speed(event):
    interface.decrease_speed()


def play_note(event):
    interface.play_note()


def next_note_sequence(event):
    interface.next_note_sequence()


def next_all(event):
    interface.next_note_sequence()
    interface.update_first_note()
    interface.play_note_sequence()


def play_sequence(event):
    interface.play_note_sequence()


def quit_ex(event):
    interface.quit()


fenetre = tk.Tk()
interface = Interface(fenetre)
fenetre.bind('<Return>', next_all)
fenetre.bind('<p>', play_sequence)
fenetre.bind('<a>', increase_ambitus)
fenetre.bind('<A>', decrease_ambitus)
fenetre.bind('<n>', increase_nb_notes)
fenetre.bind('<N>', decrease_nb_notes)
fenetre.bind('<v>', increase_speed)
fenetre.bind('<V>', decrease_speed)
fenetre.bind('<q>', quit_ex)
interface.mainloop()
