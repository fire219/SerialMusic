# SerialMusic
### Simple and easy to use serial-controlled Arduino music synthesizer

----------

Ever wanted an easy way to play fun little melodies and songs on an Arduino, without the need to hardcode the notes? Well, here you are! 

**SerialMusic just takes a few steps to use:**
1. Flash the Arduino with the sketch.
2. Connect a speaker to Arduino **digital pin 3** and **ground**.
3. Run the provided Python script "Note Server"!

SerialMusic comes with a built in demo ("Your Reality" from *Doki Doki Literature Club!*) accessible from the Note Server's **demo** command, but also comes with a few example external note files. And with a few minutes work, you can make your own note files due to the *extremely simple* syntax:

```
140   - BPM (beats per minute)
C4 8  - <note+octave> <note length in sixteenths> Therefore, this is middle C as a half (8/16) note
CS4 8 - This is how you indicate a sharp note. SerialMusic does not use flats for simplicity.
D5 1  - D5 sixteenth note
E5 1  - any content on a line after the note length will be ignored.
```

SerialMusic makes use of Connor Nishijima's excellent GPLv3-licensed [Volume3 library](https://github.com/connornishijima/arduino-volume3). Volume3 is available through the Arduino IDE's Library Manager as well as its Github page, but for convenience it has been included here. If needed, merge the included **libraries** directory with your existing Arduino libraries.


## License
SerialMusic was created by Matthew Petry (fire219/fireTwoOneNine) and is licensed under the GPLv3 license -- see LICENSE file for more information.