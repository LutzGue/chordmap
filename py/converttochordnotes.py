"""
## Manual pre-process
The first step is a manual pre-process that can be done in two ways: The first way is to import an MP3 or WAV audio file into a DAW, determine the tempo, and create a chord track. In this track, chords are inserted at the corresponding position in the song. This chord track is then inserted into a MIDI track as individual notes (using drag and drop). Finally, this MIDI track can be exported as a MIDI file. 
The second way is to transfer the printed chord progressions from a book into a TXT file.

## Project 1: converttochordnotes
In step 2, the MIDI file created using option A (creating chord-track in a DAW) or the TXT file created with option B (adapting chords from a book) is used as input for the conversion module "converttochordnotes". This generates an output file in JSON format with individual chord notes in machine-readable format.
"""