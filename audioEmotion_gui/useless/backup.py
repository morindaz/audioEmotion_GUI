# coding=utf-8

def stop_wave(self):
    global Flag
    Flag = False


def record_wave(self):
    global Flag, itemList
    # open the input of wave
    pa = PyAudio()
    stream = pa.open(format=paInt16, channels=1,
                     rate=framerate, input=True,
                     frames_per_buffer=NUM_SAMPLES)
    save_buffer = []
    count = 0

    while count < TIME * 4 and Flag:
        # read NUM_SAMPLES sampling data
        string_audio_data = stream.read(NUM_SAMPLES)
        save_buffer.append(string_audio_data)
        count += 1
        print '.'
        if Flag == False:  # 判断Stop是否被按下
            print("stream test start")

    filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".wav"
    self.save_wave_file(filename, save_buffer)
    save_buffer = []
    itemList.append(filename)
    print filename, "saved"
    print itemList
