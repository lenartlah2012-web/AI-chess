import io
import zstandard


PATH = "data/"
FILE_NAME =  "lichess_db_standard_rated_2025-12.pgn.zst"
LINES_TO_PRINT = 30


print("Opening the compressed file...")

with open(PATH + FILE_NAME, "rb") as compressed_file:
    decompressor = zstandard.ZstdDecompressor()

    with decompressor.stream_reader(compressed_file) as binary_stream:
        with io.TextIOWrapper(
            binary_stream,
            encoding="utf-8",
        ) as text_stream:

            print("File opened successfully!")
            print()
            print("First lines in the file:")
            print("------------------------")

            for line_number, line in enumerate(
                text_stream,
                start=1,
            ):
                # Remove the newline already contained in line.
                clean_line = line.rstrip()

                print(f"{line_number:2}: {clean_line}")

                if line_number >= LINES_TO_PRINT:
                    break


print("------------------------")
print("Finished!")