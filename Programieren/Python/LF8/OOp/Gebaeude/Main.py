from gebaeude import Gebaeude
from lagerhalle import Lagerhalle
from wohnhaus import Wohnhaus

wohnung = Wohnhaus("Musterstrasse 1", 10000, 2019, 10)
print(wohnung.get_daten())