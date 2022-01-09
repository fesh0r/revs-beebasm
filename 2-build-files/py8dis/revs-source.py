from commands import *
from trace6502 import *
import acorn


load(0x1200, "Revs.bin", "0a0da117451375a1df0eab317892725b")
set_output_filename("Revs-out.bin")

acorn.bbc()

# Code from &1500-&15DA that ends up at &7000-70DA
move(0x7000, 0x1500, 0x15da - 0x1500 + 1)
label(0x7000, "movedFrom1500To7000")

# Code from &1300-&14FF that ends up at &0B00-&0CFF
move(0x0b00, 0x1300, 0x14ff - 0x1300 + 1)
label(0x0b00, "movedFrom1300To0b00")

# Code from &120E-&12FFthat ends up at &790E-&79FF
move(0x790e, 0x120e, 0xff - 0xe + 1)
label(0x790e, "movedFrom120eTo790e")

# Code from &5300-&5949 that ends up at &70DB-&7724
move(0x70db, 0x5300, 0x7724 - 0x70db + 1)
label(0x70db, "movedFrom5300To709db")

# Code from &5A80-&645B that ends up at &0D00-&16DB
move(0x0d00, 0x5a80, 0x645b - 0x5a80 + 1) # <--- This produces BeebAsm code that fails
label(0x0d00, "movedFrom5a80To0d00")

# Code from &64D0-&6BFF that ends up at &5FD0-&63FF
move(0x5fd0, 0x64d0, 0x6bff - 0x64d0 + 1) # <--- This produces BeebAsm code that fails
label(0x5fd0, "movedFrom64d0")

go()
