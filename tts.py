import pyttsx3 as tts


def main():
    engine = tts.init()
    # engine.setProperty('rate', 250)
    print(engine.getProperty("voice"))
    fp = open("essay.txt", 'r')
    for line in fp:
        print(line)
        engine.say(line)

    engine.runAndWait()
    fp.close()


if __name__ == "__main__":
    main()