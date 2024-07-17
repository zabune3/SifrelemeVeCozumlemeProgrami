from cx_Freeze import setup, Executable

setup(
    name="ŞifrelemeProgramı",
    version="1.0",
    description="4 çeşit şifreleme türünü destekleyen şifreleme aracı",
    executables=[Executable("main.py")]
)


