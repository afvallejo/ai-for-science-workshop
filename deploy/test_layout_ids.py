"""Run after prepare_workshop.py; no server or new dependencies required."""
import io
import sys
import unittest
from pathlib import Path
from zipfile import ZipFile
from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'website'))
from room_decks import merge_decks, P, A


class MergeLayoutTests(unittest.TestCase):
    def test_repeated_template_keeps_unique_layouts_and_editable_text(self):
        template = (ROOT / 'website/public/room/template.pptx').read_bytes()
        for count in (2, 15):
            with self.subTest(slides=count), ZipFile(io.BytesIO(merge_decks([template] * count))) as z:
                self.assertIsNone(z.testzip())
                presentation = etree.fromstring(z.read('ppt/presentation.xml'))
                self.assertEqual(len(presentation.findall('.//{%s}sldId' % P)), count)
                layout_ids = []
                slide_texts = []
                for name in z.namelist():
                    if name.endswith('.xml') and '/slideMasters/' in name:
                        layout_ids += etree.fromstring(z.read(name)).xpath('//*[local-name()="sldLayoutId"]/@id')
                    if name.endswith('.xml') and '/slides/slide' in name:
                        slide_texts.append(etree.fromstring(z.read(name)).findall('.//{%s}t' % A))
                self.assertTrue(layout_ids)
                self.assertEqual(len(layout_ids), len(set(layout_ids)))
                self.assertEqual(len(slide_texts), count)
                self.assertTrue(all(len(texts) == 11 for texts in slide_texts))


if __name__ == '__main__':
    unittest.main()
