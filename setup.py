from cx_Freeze import setup, Executable

setup(
    name = "Randomizer",
    version = "0.1",
    description = "Randomly assigns players to positions",
    executables = [Executable("Position Randomizer.py")]
)