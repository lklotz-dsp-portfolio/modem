# Bell 103 Modem Decoder

This program reads an audio file and decodes it into a text message using 
the Bell 103 modem protocol.

The Bell 103 modem protocol uses two frequencies to represent binary data.
In this implementation, the frequencies are:
- 2025 Hz for a binary '0'
- 2225 Hz for a binary '1'

Program Structure:

1. initialize 4 different arrays:
    - sine and cosine for 2025 Hz, 160 samples long
    - sine and cosine for 2225 Hz, 160 samples long
2. Loop through the audio in blocks of 160 samples (which corresponds to one bit):
    - For each block, calculate the dot product
    - whichever dot prodoct is greater (2025 or 2225) determines if the bit is a '1' or '0'

3. Convert the binary string into ASCII characters:
    - Group the binary string into 10-bit segments
        - Each block has a starting but and an ending bit which are discarded
        - Convert the remaining 8 bits into an ASCII character
4. Print the resulting text message.

## Requirements

```
pip install numpy
```

## Running

Place your `message.wav` file in the same directory as `m.py`, then run:

**Windows**
```
python m.py
```

**Mac / Linux**
```
python3 m.py
```
