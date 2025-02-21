import subprocess


def convert_audio(input_file, output_file):
    try:
        # Command to convert .m4a to .mp3 using ffmpeg
        command = [
            "ffmpeg",
            "-i", input_file,  # Input file
            output_file        # Output file
        ]

        # Run the command
        subprocess.run(command, check=True)
        print(f"Conversion successful: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except FileNotFoundError:
        print("ffmpeg not found. Please install ffmpeg and ensure it's in your PATH.")


if __name__ == "__main__":
    input_file = "sounds/test 2/Michael.m4a"
    output_file = input_file.replace(".m4a", ".mp3")
    convert_audio(input_file, output_file)
