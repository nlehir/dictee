def get_center_note(center_offset_to_a4):
    """
        get the first note
    """
    if center_offset_to_a4 == 0:
        return "A4"
    elif center_offset_to_a4 == 1:
        return "Bb4"
    elif center_offset_to_a4 == 2:
        return "B4"
    elif center_offset_to_a4 == 3:
        return "C5"
    elif center_offset_to_a4 == -1:
        return "Ab4"
    elif center_offset_to_a4 == -2:
        return "G4"
    elif center_offset_to_a4 == -3:
        return "Gb4"
    elif center_offset_to_a4 == -4:
        return "F4"
    elif center_offset_to_a4 == -5:
        return "E4"
    elif center_offset_to_a4 == -6:
        return "Eb4"
    elif center_offset_to_a4 == -7:
        return "D4"
    elif center_offset_to_a4 == -8:
        return "Db4"
    elif center_offset_to_a4 == -9:
        return "C4"
    else:
        return "error"
