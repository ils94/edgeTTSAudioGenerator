import asyncio
import edge_tts


async def tts_engine(text) -> None:
    voice = "en-AU-NatashaNeural"
    output_file = "test.mp3"

    if text:
        try:
            communicate = edge_tts.Communicate(text, voice)
            await communicate.save(output_file)
            print("Audio saved successfully as test.mp3")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    else:
        print("Please enter some text to generate audio.")


def generate_audio(text):
    asyncio.run(tts_engine(text))


generate_audio("Get ready!")