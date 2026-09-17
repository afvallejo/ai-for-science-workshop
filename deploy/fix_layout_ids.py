"""Apply the verified v4 merger fix without modifying the original archive."""
from pathlib import Path


def apply(site: Path):
    path = site / 'room_decks.py'
    source = path.read_text()
    anchor = '    master_index = 0\n'
    insertion = """            else:
                ctype = overrides.get(name) or defaults.get(name.rsplit('.', 1)[-1])
"""
    replacement = """            else:
                # Layout identifiers must be unique across all source masters.
                # Reserve a separate range above all possible master identifiers.
                if '/slideMasters/' in name and name.endswith('.xml'):
                    root = xml(blob)
                    for layout in root.findall('.//{%s}sldLayoutId' % P):
                        layout.set('id', str(layout_index))
                        layout_index += 1
                    blob = serial(root)
                ctype = overrides.get(name) or defaults.get(name.rsplit('.', 1)[-1])
"""
    if source.count(anchor) != 1 or source.count(insertion) != 1:
        raise RuntimeError('Unexpected merger source: review the layout-ID fix.')
    source = source.replace(anchor, anchor + '    layout_index = 2147549184\n')
    source = source.replace(insertion, replacement)
    path.write_text(source)
