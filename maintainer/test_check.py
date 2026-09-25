"""Check that the maintainer guard catches representative publication defects."""
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("guard",ROOT/"maintainer/check.py")
guard=importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


class PublicationGuard(unittest.TestCase):
    def test_real_defects_are_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)
            for name in guard.public_files(ROOT):
                target=dest/name
                target.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(ROOT/name,target)
            self.assertEqual(guard.check(dest),[])
            readme=dest/"README.md"
            original=readme.read_text()
            readme.write_text(original+"\n[broken](missing.md)\n")
            self.assertTrue(any("broken/local" in e for e in guard.check(dest)))
            readme.write_text(original+"\n[broken anchor](README.md#missing-heading)\n")
            self.assertTrue(any("broken anchor" in e for e in guard.check(dest)))
            readme.write_text(original+"\n"+"http:"+"/"*2+"fixture"+"."+"home/private\n")
            self.assertTrue(any("private reference" in e for e in guard.check(dest)))
            readme.write_text(original)
            core=dest/"releases/2.3.0/core.md"
            core.write_text(core.read_text().replace("# ADAC core 2.3.0","# ADAC core 9.9.9",1))
            self.assertTrue(any("version mismatch" in e for e in guard.check(dest)))


if __name__=="__main__":
    unittest.main()
