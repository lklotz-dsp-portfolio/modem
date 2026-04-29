import wave
import numpy as np

with wave.open("message.wav", "rb") as f:
    raw = f.readframes(f.getnframes())

samples = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0

print(len(samples))

#precompute 4 reference arrays 
#sin, cos 2025hz
#sin, cos 2225hz
#each 160 samples long

s2025 = np.sin(2 * np.pi * 2025 * np.arange(160) / 48000)
c2025 = np.cos(2 * np.pi * 2025 * np.arange(160) / 48000)
s2225 = np.sin(2 * np.pi * 2225 * np.arange(160) / 48000)
c2225 = np.cos(2 * np.pi * 2225 * np.arange(160) / 48000)

#loop through audio in blocks of 160 samples
bits = []
for i in range(0, len(samples), 160):
    block = samples[i:i+160]
    if len(block) < 160:
        break
    
    #compute power at each frequency using dot products
    power2025 = np.dot(block, s2025)**2 + np.dot(block, c2025)**2
    power2225 = np.dot(block, s2225)**2 + np.dot(block, c2225)**2
    
    #emit 0 or 1 depending on which power is larger
    bits.append(1 if power2225 > power2025 else 0)

#group bits into groups of 10, discard start/stop, reassemble bytes LSB-first
bytes = []
for i in range(0, len(bits), 10):
    byte_bits = bits[i:i+10]
    if len(byte_bits) < 10:
        break
    #discard start/stop bits
    data_bits = byte_bits[1:9]
    #reassemble byte LSB-first
    byte = sum(bit << j for j, bit in enumerate(data_bits))
    print(f"Byte: {chr(byte)} ({byte})")
    bytes.append(byte)

#convert bytes to characters and print
message = ''.join(chr(byte) for byte in bytes)
print(message)
