from pathlib import Path
from mutagen import File

music_folder = Path(input("Enter your music folder: "))

for file in music_folder.rglob("*"):
    if not file.is_file(): # This ignores folders... obviously. if not file is file, if file is not file basically. Backwards english. But forwards.
        continue

    audio = File(file)

    if audio is None:
        continue

    tags = audio.tags or {}

    title = tags.get("title", [file.stem])
    artist = tags.get("artist", ["Unknown Artist"])

    if hasattr(title, "text"):
        title = title.text

    if hasattr(artist, "text"):
        artist = artist.text

    print(f"{artist} - {title}")
