# ChordMap
ChordMap is a visual way of representing the chord progressions of songs using a circular diagram. They are based on the concept of Roman numeral analysis, which assigns a number to each chord in a key according to its scale degree. For example, in the key of C major, the chord C is I, the chord Dm is ii, the chord Em is iii, and so on. ChordMaps show these Roman numerals along with the chord type (major, minor, diminished, etc.) in a circle that corresponds to the 12 possible keys. By rotating the circle, one can easily transpose a song to a different key or compare songs in different keys. ChordMaps also show the common patterns and relationships among chords, such as the circle of fifths, the diatonic chords, and the secondary dominants. ChordMaps are a useful tool for songwriters, performers, and music students who want to learn and understand the music theory of songs.

# Process
Here is a description about the process that involves converting chord names to chord notes, then to Roman numerals, and finally to a chord map. 

## Manual pre-process
The first step is a manual pre-process that can be done in two ways: The first way is to import an MP3 or WAV audio file into a DAW, determine the tempo, and create a chord track. In this track, chords are inserted at the corresponding position in the song. This chord track is then inserted into a MIDI track as individual notes (using drag and drop). Finally, this MIDI track can be exported as a MIDI file. 
The second way is to transfer the printed chord progressions from a book into a TXT file.

## Project 1: converttochordnotes
In step 2, the MIDI file created using option A (creating chord-track in a DAW) or the TXT file created with option B (adapting chords from a book) is used as input for the conversion module "converttochordnotes". This generates an output file in JSON format with individual chord notes in machine-readable format.

## Project 2: chordnotestoromannumeral
In project 2, the output JSON file generated in project 1 is read. In the first analysis step, the key of each section is determined. Then, each chord note is assigned to Roman numerals in the corresponding keys. The chord names and notes are converted enharmonically correctly into the key. An output JSON file containing the analysis results is generated.

## Project 3: romannumeraltochordmap
In project 3, the analysis JSON generated in project 2 is used for chord mapping. The goal of chord mapping is to map Roman numerals in keys for the GUI so that they can be positioned in a circle.