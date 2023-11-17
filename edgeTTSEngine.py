import edge_tts
from tkinter import messagebox


async def engine(text, voice, filename) -> None:
    if not text == "":
        try:
            communicate = edge_tts.Communicate(text, voice)
            await communicate.save(f"{filename}.mp3")
            messagebox.showinfo("Success", f"The audio file {filename} was generated!")
        except Exception as e:
            messagebox.showerror("Error", f"{str(e)}")
    else:
        messagebox.showerror("Error", "Insert a valid text to generate the audio file.")
