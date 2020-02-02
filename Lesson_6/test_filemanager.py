import filemanager as fm
import main as m

def test_filenames():
    assert len(fm.filenames()) == 6

def test_separator():
    assert m.separator(5) == '*****'

def test_is_correct_choice_0():
    assert m.is_correct_choice('3')

def test_is_correct_choice_0():
    assert m.is_correct_choice('11') is False