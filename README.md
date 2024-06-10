## HEIC to PNG Converter

This Python script converts HEIC (High-Efficiency Image Format) files to PNG format using the Pillow library. It scans the current directory for HEIC files, converts them to PNG, and moves them to a designated folder.

### Requirements
- Python 3
- Pillow library (`pillow-heif` extension)
- Ensure you have the necessary HEIC support installed for Pillow (`pillow-heif`).

### Installation Steps

1. **Install Python 3**: If you haven't already installed Python 3, download and install it from the official [Python website](https://www.python.org/).

2. **Install Pillow Library**: Run the following command in your terminal or command prompt to install the Pillow library with HEIC support:

    ```
    pip install pillow
    pip install pillow-heif
    ```

### Usage

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Navigate to the Directory**: Open a terminal or command prompt, navigate to the directory where the script is located.

3. **Run the Script**: Execute the script by running the following command:

    ```
    python heic_converter.py
    ```

4. **Output**: Converted PNG files will be generated and moved to a new folder named `png`.

### Example

Suppose you have HEIC files in your current directory:

```
photo1.HEIC
photo2.HEIC
```

After running the script, PNG versions of these files will be created in the `png` folder:

```
png/
    photo1.png
    photo2.png
```

---

Feel free to customize the script or report as needed for your project!



### But Why Use Python When You Can Bash It Up?

Honestly, the task can be accomplished using the shell script provided below. However, I'm currently engaged in developing an open-source command-line tool tailored for web engineers. I figured I'd share this snippet on GitHub just in case it piques someone's interest.

```bash
for file in *.png; do cwebp "$file" -o "${file%.png}.webp"; done
```

And hey, if Fish is more your style, check out this one-liner:

```fish
for file in *.png; cwebp "$file" -o (basename "$file" .png).webp; end
```

