import array
import math
import time
import pyaudio

VOLUME = 0.5
p = pyaudio.PyAudio()


def generate_tone(duration, frequency, sample_rate):

    num_samples = int(sample_rate * duration)
    samples = []

    for k in range(0, num_samples):
        this_sample = VOLUME * math.sin(
            2 * math.pi * k * frequency / sample_rate)
        samples.append(this_sample)

    output_bytes = array.array("f", samples).tobytes()

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True,                    
                    output_device_index=1
    )

    start_time = time.time()
    stream.write(output_bytes)
    print("Played sound for {:.2f} seconds".format(time.time() - start_time))

    stream.stop_stream()
    stream.close()


if __name__ == "__main__":
    
    ## your answers here
    p.terminate()
